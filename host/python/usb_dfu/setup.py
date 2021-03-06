#!/usr/bin/env python
"""
dfu setup

Install script for dfu

Usage: python setup.py install

This file is part of project Ubertooth
Copyright 2012 Dominic Spill
"""

from distutils.core import setup

setup(
    name        = "dfu",
    version     = "0.svn",
    description = "A tool for reading and writing firmware to USB devices",
    author      = "Jared Boone, Michael Ossmann, Dominic Spill",
    url         = "https://sourceforge.net/projects/ubertooth/",
    license     = "GPL",
    packages    = ['dfu'],
    classifiers=[
        'Development Status :: 5 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
    ],
)
