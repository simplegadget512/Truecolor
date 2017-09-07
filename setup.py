"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='truecolor',

    version='1.0b2',

    description='A Truecolor terminal library for Python',
    long_description=long_description,

    url='https://github.com/simplegadget512/Truecolor',

    author='Albert Freeman',
    author_email='simplegadget512@gmail.com',

    license='MIT',

    classifiers=[
        'Environment :: Console',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Terminals :: Terminal Emulators/X Terminals',
    ],

    keywords='ansi color console terminal',

    py_modules=["truecolor"],

    python_requires='>=2.7',

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'truecolor=truecolor:main',
        ],
    },
)
