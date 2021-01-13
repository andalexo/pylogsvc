"""yaplog

Yet Another Python Logging module.
Helper module to set up a logging service with some predefined defaults.
For usage:
>>> from yaplog import set_logging
>>> help(set_logging)
"""

__version__ = '1.0'
__version_info__ = (1, 0, 0)
__name__ = 'yaplog'

from .logging import set_logging
