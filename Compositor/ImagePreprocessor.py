from PIL import Image, ImageOps, ImageFilter, ImageEnhance
from functools import reduce

class ImagePreprocessor(object):
    """Class to encapsulate common image preprocessing tasks,
    image will be forced to greyscale"""
    def __init__(self, sharpness=1, brightness=1, scale=1, kmedian=1):
        """
        :sharpness: coefficient for default unsharp masking
        :brightness: correction factor for Brightnes. 1 is identity
        :scale: image resize factor. 1 is identity
        """
        self._sharpness = sharpness
        self._brightness = brightness
        self._scale = scale
        self._kmedian = kmedian

    def grayscale(self, img):
        return ImageOps.grayscale(img).convert('L')

    def sharpen(self, img):
        enhancer = ImageEnhance.Sharpness(img)
        return enhancer.enhance(self._sharpness)

    def brighten(self, img):
        enhancer = ImageEnhance.Brightness(img)
        return enhancer.enhance(self._brightness)

    def median_filter(self, img):
        return img.filter(ImageFilter.MedianFilter(self._kmedian))

    def scale(self, img, resample=Image.BICUBIC):
        x, y = [int(z * self._scale) for z in img.size]
        return img.resize(size=(x, y), resample=resample)

    def process(self, img):
        '''Apply each of the filters consecutively,
        returns the processed image
        :img: PIL.Image object.'''
        def right_apply(x, f): return f(x)
        operations = [self.grayscale,
                      self.median_filter,
                      self.brighten,
                      self.sharpen,
                      self.scale]
        return reduce(right_apply, operations, img)
