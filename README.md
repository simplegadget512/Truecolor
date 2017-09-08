# Truecolor

A True color terminal library for Python &#8212; similar in function to the [termcolor library](https://pypi.python.org/pypi/termcolor/1.1.0). It allows one to output color text in supported terminals using escape codes.

## Available functions
* **bold** - Return a bolder version of a color tuple.
* **dim** - Return a dimmer version of a color tuple.
* **hex_to_rgb** - Return a tuple of (red, green, blue) for a color given as #rrggbb.
* **rgb_to_hex** - Return color as #rrggbb for the given color tuple or component values.
* **fore_text** - Return text string with foreground only set.
* **color_text** - Return text string with foreground and background set.
* **fore_print** - Print text string with foreground only set.
* **color_print** - Print text string with foreground and background set.

## Example
The following is how I use the library in my .pythonrc file.

```python
#!/usr/bin/env python

import truecolor

# set up the prompts
sys.ps1 = truecolor.fore_text('>>>', truecolor.COLORS['green'])
sys.ps2 = truecolor.fore_text('...', truecolor.COLORS['green'])

```