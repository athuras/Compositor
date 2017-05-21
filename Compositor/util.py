from PIL import Image
import urllib.request, urllib.parse, urllib.error
import io


def get_image_from_url(url):
    '''Reads image from a (trusted) url to an image file readable by PIL.
    Note: only works properly if the image has a standard file-extension.'''
    f = io.StringIO(urllib.request.urlopen(url).read())
    img = Image.open(f)
    return img
