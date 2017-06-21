#!/usr/bin/env python3
# This is free and unencumbered software released into the public domain.

"""Installation script for the Conreality SDK for Python."""

from codecs import open
from os import path
from setuptools import setup
from shutil import copyfile

def readfile(*filepath):
  with open(path.join(*filepath), encoding='utf-8') as f:
    return f.read()

PWD = path.abspath(path.dirname(__file__))

VERSION          = readfile(PWD, 'VERSION').rstrip()
LONG_DESCRIPTION = readfile(PWD, 'README')

setup(
  name='conreality',
  version=VERSION,
  description="Conreality Software Development Kit (SDK) for Python",
  long_description=LONG_DESCRIPTION,
  url='https://sdk.conreality.org/python/',
  author='Conreality.org',
  author_email='conreality@googlegroups.com',
  license='Public Domain',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Science/Research',
    'License :: Public Domain',
    'Natural Language :: English',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Games/Entertainment :: Simulation',
    'Topic :: Scientific/Engineering :: Human Machine Interfaces',
    'Topic :: Software Development :: Embedded Systems',
    'Topic :: System :: Hardware :: Hardware Drivers',
  ],
  keywords='conreality sdk driver robotics',
  packages=['conreality', 'conreality.sdk'],
  install_requires=[
    'asyncpg>=0.11',
    'lupa>=1.4',
    'numpy>=1.13',
  ],
  extras_require={
    'test': ['pytest'],
  },
)
