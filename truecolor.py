#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


if os.getenv('COLORTERM') is None:
    raise RuntimeError('Not a true color terminal')


COLORS = {
    'white':    (127, 127, 127),
    'grey':     (64, 64, 64),
    'black':    (0, 0, 0),

    'red':      (127, 0, 0),
    'green':    (0, 127, 0),
    'blue':     (0, 0, 127),

    'yellow':   (127, 127, 0),
    'brown':    (127, 64, 0),

    'purple':   (32, 0, 127)
}


def _f(red_component, green_component, blue_component):
    """Return escaped foreground color sequence"""
    return '\x01\x1b[38;2;{};{};{}m\x02'.format(red_component, green_component, blue_component)


def _b(red_component, green_component, blue_component):
    """Return escaped background color sequence"""
    return '\x01\x1b[48;2;{};{};{}m\x02'.format(red_component, green_component, blue_component)


def _r():
    """Return reset sequence"""
    return '\x01\x1b[0m\x02'


def _gamut(component):
    return int(component) if component < 255 else 254


def bold(color):
    """Return a bolder version of a color tuple."""
    return tuple(_gamut(i*2) for i in color)


def dim(color):
    """Return a dimmer version of a color tuple."""
    return tuple(int(i/2) for i in color)


def hex_to_rgb(hex_string):
    """Return a tuple of (red_component, green_component, blue_component) for the color given as #rrggbb."""
    hex_string = hex_string.lstrip('#')
    lv = len(hex_string)
    return tuple(int(hex_string[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_hex(red_component=None, green_component=None, blue_component=None):
    """Return color as #rrggbb for the given color tuple or component values."""
    if isinstance(red_component, tuple):
        red_component, green_component, blue_component = list(red_component)
    return '#{:02x}{:02x}{:02x}'.format(red_component, green_component, blue_component).upper()


def fore_text(txt, foreground=COLORS['white']):
    """Return text string with foreground only set."""
    if foreground[:1] == '#':
        foreground = hex_to_rgb(foreground)
    return '{}{}{}'.format(_f(foreground[0], foreground[1], foreground[2]), txt, _r())


def color_text(txt, foreground=COLORS['white'], background=COLORS['black']):
    """Return text string with foreground and background set."""
    return '{}{}{}{}'.format(_f(foreground[0], foreground[1], foreground[2]),
                             _b(background[0], background[1], background[2]),
                             txt,
                             _r())


def fore_print(txt, foreground=COLORS['white']):
    """Print text string with foreground only set."""
    print(fore_text(txt, foreground))


def color_print(txt, foreground=COLORS['white'], background=COLORS['black']):
    """Print text string with foreground and background set."""
    print(color_text(txt, foreground, background))


if __name__ == "__main__":
    for color_name in COLORS:
        color_print('{} :: {} :: bright {} on dim {}'.format(rgb_to_hex(bold(COLORS[color_name])),
                                                         rgb_to_hex(dim(COLORS[color_name])),
                                                         color_name,
                                                         color_name).ljust(64, ' '),
                    bold(COLORS[color_name]),
                    dim(COLORS[color_name]))
