import numpy as np
from PIL import ImageFont, ImageDraw

def monaco(size):
    return ImageFont.truetype("./fonts/Monaco.ttf", size)

def courier(size):
    return ImageFont.truetype("./fonts/Courier.ttf", size)

class FontRenderer(object):
    def __init__(self, font, ink=(0, 0, 0, 255), fill=(255, 255, 255, 0)):
        self._font = font
        self._ink = ink
        self._fill = fill

    def render(self, text):
        '''Render a bitmap array of the provided text,
        :text: should be unicode if you want good behaviour'''
        bbox = self.get_bbox(text)
        background = Image.new("RGBA", bbox, self._fill)
        context = ImageDraw.Draw(background)
        context.text((0, 0), text, font=self._font, fill=self._ink)
        return background

    def get_bbox(self, text):
        '''Find the bounding box for the text given the font properties,
        relies on font being monospace'''
        x, y = self._font.getmetrics()
        z = len(text) * (x + y)
        return (x + y) / 2, z
