# This is free and unencumbered software released into the public domain.

"""Conreality Software Development Kit (SDK) for Python."""

import sys

assert sys.version_info >= (3,7), \
    "Conreality SDK for Python requires Python 3.7+"

import drylib

from .asset   import *
from .binary  import *
from .camera  import *
from .client  import *
from .event   import *
from .message import *
from .object  import *
from .player  import *
from .session import *
from .theater import *

__all__ = [
    'Asset',
    'Binary',
    'Camera',
    'Client', 'AsyncClient',
    'Event',
    'Message',
    'Object',
    'Player',
    'Session',
    'Theater',
]
