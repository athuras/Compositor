import numpy as np
import FontRenderer
import ImagePreprocessor

alphabet = "abcdefghijklmnopqrstuvwxyz"
numeric = "1234567890"
symbols = """!@#$%^&*()_+-=[]{}\|;:'"/?.>,<`~"""
shenanigans1 = """¡™£¢∞§¶•ªº–≠œ∑®†øπ“‘«åß∂ƒ©˙∆˚¬…æΩ≈ç√∫˜˜µ≤≥÷"""
shenanigans2 = """⁄€‹›ﬁﬂ‡°·‚—±Œ„‰ˇÁ¨ˆØ∏”’»ÅÍÎÏ˝ÓÔÒÚÆ¸˛Ç◊ı˜Â¯˘¿"""
alpha_numeric = alphabet + alphabet.upper() + numeric + symbols

cacophony = alpha_numeric + shenanigans1 + shenanigans2

def truncate_image(big_img, base_shape):
    '''
    The largest sub-image in big_img so that base_shape can be tesselated evenly'''
    def remult(a, b): return (a / b) * b
    x, y = big_img.shape
    s1, s2 = base_shape
    x2, y2 = remult(x, s1), remult(y, s2)
    return big_img[:x2, :y2]


class ImageIndexer(object):
    '''Useful abstraction for iterating over sub-images,
    can also be used to mutate stuff ... if you're into that sort of thing'''
    def __init__(self, base_shape):
        self._base_shape = base_shape

    def shape(self, img):
        '''Returns the shape of the image in terms of the base shape'''
        n, m = img.shape
        dx, dy = self._base_shape
        return n / dx, m / dy

    def indices(self, img):
        '''Returns an iterator of index-points separated by base_shape'''
        n, m = self.shape(img)
        dx, dy = self._base_shape
        return ((i * dx, j * dy) for i in xrange(n)
                                 for j in xrange(m))
    def sub_images(self, img):
        '''Returns an iterator of sub-images of the
        truncated image. Same order as Indexer.indices'''
        dx, dy = self._base_shape
        return (img[i:i+dx, j:j+dy] for i, j in self.indices(img))


#  Vectorized error functions designed to broadcase along a tertiary axis.
def deep_rms(img, masks):
    z = np.abs(img[..., None] - masks)
    return np.sqrt((z * z)).sum(0).sum(0)

def deep_error(img, masks):
    z = np.abs(img[..., None] - masks)
    return z.sum(0).sum(0)


class Compositor(object):
    '''
    Composes a fontrender and preprocessor into one glorious pipeline
    '''
    def __init__(self, preprocessor, fontRenderer, cost_fn=deep_error):
        self._font = fontRenderer
        self._preprocessor = preprocessor
        self._cost_fn

    def gen_label_table(self, palette):
        '''useful for decoding the output'''
        return {i: k for i, k in enumerate(sorted(palette))}

    def gen_mask_table(self, palette):
        '''Render a set of glyphs, one for each string in the palette,
        :palette: iterable[String], i.e. "abcdef" or ["ab", "cd"]
            the length of each component must be identical.'''
        _render = self._fontRenderer.render
        return np.dstack([_render(s) for s in sorted(palette)])

    def base_shape(self, palette): return self._font.get_bbox(palette[0])

    def prepare_image(self, image, palette):
        '''applies preprocessing, and truncates so the palette fits evenly'''
        img = truncate_image(np.asarray(self._preprocessor.process(image)),
                             self.base_shape(palette))
        return img

    def composite(self, image, palette, preprocess=False):
        '''generates the labels for an ASCII/unicode glyph composition.
        :image:  PIL.Image,
        :palette: Iterable of strings
        :return an iterator of labels,
        :preprocess: will run Compositor.prepare_image if true'''
        masks = self.gen_mask_table(palette)
        base_shape = self.base_shape(palette)
        img = self.prepare_image(image, palette) if preprocess else image

        def argmin(sub_image):
            return np.argmin(self._cost_fn(sub_image, masks))

        indexer = ImageIndexer(base_shape)
        return (argmin(s) for s in indexer.sub_images(img))

    def render_text_composite(self, image, palette):
        '''renders the composite as a string'''
        base_shape = self.base_shape(palette)
        img = self.prepare_image(image, palette)
        labels = self.composite(img, palette, preprocess=False)
        chars = (self.gen_label_table(palette)[l] for l in labels)
        n, _ = ImageIndexer(base_shape).shape(img)
        rt = []
        for i, c in enumerate(chars):
            if i % n == 0:
                rt.append('\n')
            rt.append(c)
        return rt

    def render_composite(self, image, palette):
        '''Renders the bitmap 'text' analog to :image'''
        base_shape = self.base_shape(palette)
        indexer = ImageIndexer(base_shape)
        img = self.prepare_image(image, palette)
        masks = self.gen_mask_table(palette)
        labels = self.composite(img, palette, preprocess=False)

        canvas = np.empty_like(img)
        for subimage, l in izip(indexer.sub_images(canvas), labels):
            subimage = masks[:,:,l]
        return canvas  # hopefully non-empty...
