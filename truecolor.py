#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

if os.getenv('COLORTERM') is None:
    raise RuntimeError('Not a truecolor terminal - use termcolor module instead')

PALETTE = {
    'white': (127, 127, 127),
    'grey': (64, 64, 64),
    'black': (0, 0, 0),

    'red': (127, 0, 0),
    'green': (0, 127, 0),
    'blue': (0, 0, 127),

    'yellow': (127, 127, 0),
    'brown': (127, 64, 0),

    'purple': (32, 0, 127)
}

Z_FORE = 38
Z_BACK = 48


def _e(red_component, green_component, blue_component, z_level=Z_FORE):
    """Return escaped color sequence"""
    return '\x01\x1b[{};2;{};{};{}m\x02'.format(
        z_level, red_component, green_component, blue_component)


def _f(red_component, green_component, blue_component):
    """Return escaped foreground color sequence"""
    return _e(red_component, green_component, blue_component, Z_FORE)


def _b(red_component, green_component, blue_component):
    """Return escaped background color sequence"""
    return _e(red_component, green_component, blue_component, Z_BACK)


def _r():
    """Return reset sequence"""
    return '\x01\x1b[0m\x02'


def _gamut(component):
    """keeps color components in the proper range"""
    return min(max(int(component), 0), 254)


def bold(color):
    """Return a bolder version of a color tuple."""
    return tuple(_gamut(i * 2) for i in color)


def dim(color):
    """Return a dimmer version of a color tuple."""
    return tuple(_gamut(i // 2) for i in color)


def hex_to_rgb(hex_string):
    """Return a tuple of red, green and blue components for the color
    given as #rrggbb.
    """
    return tuple(int(hex_string[i:i + 2], 16)
                 for i in range(1, len(hex_string), 2))


def rgb_to_hex(red_component=None, green_component=None, blue_component=None):
    """Return color as #rrggbb for the given color tuple or component
    values. Can be called as

    TUPLE VERSION:
        rgb_to_hex(COLORS['white']) or rgb_to_hex((128, 63, 96))

    COMPONENT VERSION
        rgb_to_hex(64, 183, 22)

    """
    if isinstance(red_component, tuple):
        red_component, green_component, blue_component = red_component
    return '#{:02X}{:02X}{:02X}'.format(
        red_component, green_component, blue_component)


def fore_text(txt, foreground=PALETTE['white']):
    """Return text string with foreground only set."""
    if isinstance(foreground, str) and foreground.startswith('#'):
        foreground = hex_to_rgb(foreground)
    return '{}{}{}'.format(_f(*foreground), txt, _r())


def color_text(txt, foreground=PALETTE['white'], background=PALETTE['black']):
    """Return text string with foreground and background set."""
    if isinstance(foreground, str) and foreground.startswith('#'):
        foreground = hex_to_rgb(foreground)
    if isinstance(background, str) and background.startswith('#'):
        background = hex_to_rgb(background)
    return '{}{}{}{}'.format(_f(*foreground), _b(*background), txt, _r())


def fore_print(txt, foreground=PALETTE['white']):
    """Print text string with foreground only set."""
    print(fore_text(txt, foreground))


def color_print(txt, foreground=PALETTE['white'], background=PALETTE['black']):
    """Print text string with foreground and background set."""
    print(color_text(txt, foreground, background))


if __name__ == "__main__":
    for color_name in PALETTE:
        color_print(
            '{} :: {} :: bright {} on dim {}'.format(
                rgb_to_hex(bold(PALETTE[color_name])),
                rgb_to_hex(dim(PALETTE[color_name])),
                color_name,
                color_name
            ).ljust(64, ' '),
            bold(PALETTE[color_name]),
            dim(PALETTE[color_name])
        )
