#!/usr/bin/env python3
# This is free and unencumbered software released into the public domain.

"""Installation script for the Conreality SDK for Python."""

from codecs import open
from os import path
from setuptools import setup, find_packages
from shutil import copyfile

def readfile(*filepath):
  with open(path.join(*filepath), encoding='utf-8') as f:
    return f.read()

PWD = path.abspath(path.dirname(__file__))

VERSION          = readfile(PWD, 'VERSION').rstrip()
LONG_DESCRIPTION = readfile(PWD, 'README.rst')

setup(
  name='conreality',
  version=VERSION,
  description="Conreality Software Development Kit (SDK) for Python",
  long_description=LONG_DESCRIPTION,
  long_description_content_type='text/x-rst',
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
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.7',
    'Topic :: Games/Entertainment :: Simulation',
    'Topic :: Scientific/Engineering :: Human Machine Interfaces',
    'Topic :: Software Development :: Embedded Systems',
    'Topic :: System :: Hardware :: Hardware Drivers',
  ],
  keywords='conreality sdk driver robotics',
  project_urls={
    'Source': 'https://github.com/conreality/conreality.py',
  },
  packages=find_packages(where='src'),
  package_dir={'': 'src'},
  install_requires=[
    'drylib',
    'grpcio>=1.15',
    'numpy>=1.15',
  ],
  python_requires='~=3.7',
  extras_require={
    'test': ['pytest'],
  },
)
