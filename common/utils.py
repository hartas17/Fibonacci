import math

from PIL import Image


def resize_image(image, width=500, height=500):
    if image:
        size = width, height
        im = Image.open(image.path)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(image.path)


def get_fibonacci_value_recursive(number):
    """Recursive method fibonacci"""
    if number >= 2:
        return get_fibonacci_value_recursive(number-1) + get_fibonacci_value_recursive(number-2)
    return number


