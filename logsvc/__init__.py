"""logsvc

Helper module to set up a logging service with some predefined defaults.
For usage:
>>> from logsvc import set_logging
>>> help(set_logging)
"""

__version__ = '2.0.0'
__version_info__ = (2, 0, 0)
__name__ = 'logsvc'

from .logging import set_logging
