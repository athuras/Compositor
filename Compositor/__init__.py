#!/usr/bin/env python
"""
Compositor: Morphologically Optimal ASCII-art

Usage:
    compositor text (-u IMAGE_URL | -f IMAGE_FILE ) [options]
    compositor image (-u IMAGE_URL | -f IMAGE_FILE ) OUTPUT_FILE [options]
    compositor (-h | --help | --version)

Options:
    -h, --help                         show this help message and exit
    --version                          show version and exit
    -u IMAGE_URL, --url IMAGE_URL      Read an image from a URL as imput.
    -f IMAGE_FILE        Read an image from a file as input.
    --sharpness=<float>  preprocessing sharpness value. [default: 1]
    --kmedian=<int>      preprocessing median filter value. [default: 1]
    --scale=<int>        preprocessing resolution modification. [default: 1]
    --brightness=<int>   preprocessing gamme correction. [default: 1]
    --font_size=<int>    font rendering size, at least 20 is recommended. [default: 24]
"""
from Compositor import Compositor
from FontRenderer import FontRenderer, monaco
from ImagePreprocessor import ImagePreprocessor
from docopt import docopt
from util import get_image_from_url
from PIL import Image
from Palettes import *


def main():
    '''Entry Point for CLI Compositor'''
    args = docopt(__doc__, version="1.0.0")
    preprocessor = ImagePreprocessor(sharpness = float(args['--sharpness']),
                                     brightness = float(args['--brightness']),
                                     scale = float(args['--scale']),
                                     kmedian = int(args['--kmedian']))
    fontRenderer = FontRenderer(font = monaco(int(args['--font_size'])))
    compositor = Compositor(preprocessor = preprocessor,
                            fontRenderer = fontRenderer)

    img = None
    if args['--url'] is not None:
        img = get_image_from_url(args['--url'])
    elif args['-f'] is not None:
        img = Image.open(args['-f'])
    else:
        print("Undefined state")

    palette = alpha_numeric

    if args['text']:
        gen_text(compositor, img, palette)
    elif args['image']:
        output_file = args['OUTPUT_FILE']
        gen_image(compositor, img, output_file, palette)


def gen_text(comp, img, palette):
    '''Write the composite to stdout'''
    s = ''.join(comp.render_text_composite(img, palette))
    print s

def gen_image(comp, img, output_file, palette):
    '''Generate image composite'''
    s = Image.fromarray(comp.render_composite(img, palette).T)
    s.save(output_file)

if __name__ == '__main__':
    main()
