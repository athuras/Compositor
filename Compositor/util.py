from PIL import Image
import urllib
import cStringIO


def get_image_from_url(url):
    '''Reads image from a (trusted) url to an image file readable by PIL'''
    f = cStringIO.StringIO(urllib.urlopen(url).read())
    img = Image.open(f)
    return img
