
# coding: utf-8

# In[1]:

get_ipython().magic('pylab --no-import-all inline')
import numpy as np
import scipy as sp
import scipy.ndimage as ndimg
import scipy.ndimage.interpolation
import matplotlib
import matplotlib.pyplot as plt
from PIL import ImageFont, ImageDraw, Image, ImageFilter, ImageEnhance
import PIL
from fractions import gcd

import urllib.request, urllib.parse, urllib.error
import io




# ## To extract the .ttf fonts from .dfont object, we'll use "fondu"
# \$ brew install fondu;
#
# \$ (cd /path/to/compositor/fonts && fondu /System/Library/Fonts/Helvetica.dfont)

# In[2]:

monaco = ImageFont.truetype("./fonts/Monaco.ttf", 24)


# In[3]:

def show(img, cmap="Greys_r"): plt.imshow(np.asarray(img), cmap=cmap)


# In[4]:

def renderGlyph(glyph, font, size, fill=(255,255,255,0)):
    '''Render black glyph of the font on a white (filled) background'''
    background = Image.new("RGBA", size, fill)
    context = ImageDraw.Draw(background)
    context.text((0, 0), glyph, font=font, fill=(0, 0, 0, 255))
    return background

def genGlyph(char, bbox_size=(15, 30), font=monaco):
    '''Render a single bitmap array of the given character'''
    # truncates descending characters, not ideal, but easy. TODO: fix this
    image = np.asarray(renderGlyph(char, font=font, size=bbox_size))
    if char != " ":
        return image
    else:
        return np.zeros_like(image) + 255

def gen_mask_table(palette, font):
    assert len(palette) > 0
    x, y = font.getmetrics()
    z = x + y
    bbox = (z / 2, z)
    stripped = palette.strip() # whitespace isn't handled well by the font renderer
    glyphs = [genGlyph(x, bbox_size=bbox, font=font)[:,:,0] for x in stripped]
    if " " in palette:
        glyphs.append(np.zeros_like(glyphs[0]) + 255)

    return np.dstack(glyphs)


# In[23]:

alphabet = "abcdefghijklmnop1234567890"
symbols = """~`,.<>/?;:'"[]{}\|-_=+()*&^%$#@!"""
palette = alphabet + alphabet.upper() + symbols + " " + "¡™£¢∞§¶•ªº–œ∑´®†¥¨ˆøπåß©˙∆˚¬Ω≈˜µ≤ç√"


# In[6]:

monaco.getmetrics()


# In[7]:

masks = [genGlyph(x)[:,:,0] for x in palette]


# In[8]:

f, axes = plt.subplots(4, 21, figsize=(20, 8))
for c, ax in zip(masks, axes.flat):
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.imshow(c, cmap="Greys")


# In[55]:

# 1. Take an image, blow it up to high res
# 2. then break it into glyph-sized blocks.
# 3. with each block, find the 'best' matching glyph.


# In[9]:

def get_image_from_url(url):
    f = io.StringIO(urllib.request.urlopen(url).read())
    img = Image.open(f)
    return img


# In[14]:

test = get_image_from_url("http://www.vanseodesign.com/blog/wp-content/uploads/2010/03/model.jpg")


# In[53]:

def crop_image(big_img, base_shape):
    def remult(a, b): return (a / b) * b
    x, y = big_img.shape
    s1, s2 = base_shape
    x2 = remult(x, s1)
    y2 = remult(y, s2)
    return big_img[:x2, :y2]

def ordered_indexer(big_image, block_shape):
    '''Returns an iterator of index-points'''
    n, m = big_image.shape
    dx, dy = block_shape
    return ((i * dx, j * dy) for i in range(n / dx)
                             for j in range(m / dy))

def step_through(big_image, block_shape):
    '''Returns an iterator of block_size sub-images within big_image'''
    dx, dy = block_shape
    return (big_image[i:i+dx, j:j+dy]
            for i, j in ordered_indexer(big_image, block_shape))

def deep_rms(image, mask_table):
    '''Evaluate the rms for each depth-stacked matrix
    return vector of rms-values'''
    z = np.abs(image[..., None] - mask_table)
    return (z * z).sum(axis=0).sum(axis=0)

def deep_error(image, mask_table):
    z = np.abs(image[..., None] - mask_table)
    return z.sum(axis=0).sum(axis=0)

def find_best_fit(image, masks, obj=deep_error):
    '''Select the best mask from masks using a vectorized objective function'''
    assert image.shape == masks.shape[:2] # The masks must be the same shape.
    return np.argmin(obj(image, masks))

def reconstruct_render(big_image, labels, mask_table):
    '''Return the reconstructed image given the labelling and mask_table'''
    block_shape = mask_table.shape[:2]
    dx, dy = block_shape
    canvas = np.empty_like(big_image)
    indexer = ordered_indexer(big_image, block_shape)
    for ((i, j), l) in zip(indexer, labels):
        canvas[i:i + dx, j:j + dy] = mask_table[:,:,l]
    return canvas

def reconstruct_from_masks(orig, mask_table):
    mask_shape = mask_table.shape[:2]
    cropped = crop_image(orig, mask_shape)
    segments = step_through(cropped, mask_shape)

    # Fit each segment to a mask
    labels = [find_best_fit(s, mask_table) for s in segments]
    result = reconstruct_render(cropped, labels, mask_table)
    return result

def glyph_render(orig, palette, size=12, negative=False):
    ''' Renders with monaco '''
    font = ImageFont.truetype("./fonts/Monaco.ttf", size)
    mask_table = gen_mask_table(palette, font)
    if negative:
        mask_table = 255 - mask_table
    return reconstruct_from_masks(orig, mask_table)


# In[ ]:




# In[38]:

# Resize larger
img = test.convert("L")
enhancer = ImageEnhance.Brightness(img)
img = enhancer.enhance(1.6)

big = ndimg.interpolation.zoom(np.asarray(img), 1.5)
ascii = glyph_render(big, palette, size=18)


# In[39]:

f, (a1, a2) = plt.subplots(1, 2, figsize=(20, 10), sharey=True)
a1.imshow(big, cmap="Greys_r")
a2.imshow(ascii, cmap="Greys_r")


# In[70]:

# Resize larger
test = Image.open("./images/self.jpg")

low_fi = test.convert("L")
enhancer = ImageEnhance.Brightness(low_fi)
blurred = enhancer.enhance(2.88)

test2 = ndimg.interpolation.zoom(blurred, 1.8)
ascii2 = glyph_render(test2, palette + " ¬˚∆˙©πøˆ¨¥†…“«÷≥≤ œ∑´®†¥¨ˆß=26©˙∆˚≈˜µ≤ç√", size=18, negative=False)

f, (a1, a2) = plt.subplots(1, 2, figsize=(24, 10), sharey=True)
a1.imshow(test2, cmap="Greys_r")
a2.imshow(ascii2, cmap="Greys_r")


# In[71]:

f, ax = plt.subplots(1, 1, figsize=(20, 20))
ax.imshow(ascii2, cmap="Greys_r")
ax.axis("off")


# In[72]:

f.savefig("/Users/ahuras/Desktop/self.png")


# In[ ]:



