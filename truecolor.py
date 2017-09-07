#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


if os.getenv('COLORTERM') is None:
    raise RuntimeError('Not a true color terminal')


def _f(red, green, blue):
    """Return escaped foreground color sequence"""
    return '\x1b[38;2;{};{};{}m'.format(red, green, blue)


def _b(red, green, blue):
    """Return escaped background color sequence"""
    return '\x1b[48;2;{};{};{}m'.format(red, green, blue)


def _r():
    """Return reset sequence"""
    return '\x1b[0m'


def hex_to_rgb(hex_string):
    """Return a tuple of (red, green, blue) for the color given as #rrggbb."""
    hex_string = hex_string.lstrip('#')
    lv = len(hex_string)
    return tuple(int(hex_string[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def fore_text(txt, foreground=(255, 255, 255)):
    """Return text string with foreground only set."""
    return '{}{}{}'.format(_f(foreground[0], foreground[1], foreground[2]), txt, _r())


def color_text(txt, foreground=(255, 255, 255), background=(0, 0, 0)):
    """Return text string with foreground and background set."""
    return '{}{}{}{}'.format(_f(foreground[0], foreground[1], foreground[2]),
                             _b(background[0], background[1], background[2]),
                             txt,
                             _r())


def fore_print(txt, foreground=(255, 255, 255)):
    """Print text string with foreground only set."""
    print(fore_text(txt, foreground))


def color_print(txt, foreground=(255, 255, 255), background=(0, 0, 0)):
    """Print text string with foreground and background set."""
    print(color_text(txt, foreground, background))


if __name__ == "__main__":
    pass
