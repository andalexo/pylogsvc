"""logsvc

Helper module to set up a logging service with some predefined defaults.
For usage:
>>> from logsvc import set_logging
>>> help(set_logging)
"""

__version_info__ = (0, 1, 0)
__version__ = ".".join(map(str, __version_info__))
__name__ = 'logsvc'

from .logging import set_logging
