"""YAPLOG - Yet another python logger

Helper module to set up a logging service with some predefined defaults.
"""

import logging
from sys import version_info
from os import makedirs
from os.path import exists, join, expanduser


LOG_MSG_FMT = "[%(asctime)s][%(levelname)-8s]\
[%(filename)s, %(lineno)d][%(name)s]\t%(message)s"
LOG_DT_FMT = "\033[1m%m-%d %H:%M:%S\033[0m"
LOG_DIR = join(expanduser('~'),  '.local', 'logs')


def set_logging(vcount, msg_fmt=LOG_MSG_FMT, dt_fmt=LOG_DT_FMT, 
                logdir=LOG_DIR, flog=''):
    """Sets the logging configuration.

    vcount  : logging level in the form of v-counts
    mfg_fmt : logger message format
    dt_fmt  : date format
    flog    : log to file
    """

    logging.addLevelName(logging.DEBUG, "\033[1;34m%-8s\033[1;0m"
                         % logging.getLevelName(logging.DEBUG))
    logging.addLevelName(logging.INFO, "\033[1;37m%-8s\033[1;0m"
                         % logging.getLevelName(logging.INFO))
    logging.addLevelName(logging.WARNING, "\033[1;33m%-8s\033[1;0m"
                         % logging.getLevelName(logging.WARNING))
    logging.addLevelName(logging.ERROR, "\033[1;31m%-8s\033[1;0m"
                         % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.CRITICAL, "\033[1;41m%-8s\033[1;0m"
                         % logging.getLevelName(logging.CRITICAL))

    if vcount is None or vcount == 0:
        v = logging.WARNING
    elif vcount == 1:
        v = logging.INFO
    else:
        v = logging.DEBUG


    formatter = logging.Formatter(fmt=msg_fmt, datefmt=dt_fmt)

    handlers = []
    shandler = logging.StreamHandler()
    shandler.setFormatter(formatter)
    handlers.append(shandler)
    if flog:
        if not exists(logdir):
            makedirs(logdir)

        fhandler = logging.FileHandler(join(logdir, flog), mode='w')
        fhandler.setFormatter(formatter)
        handlers.append(fhandler)

        if version_info < (3, 3):
            # Python < 3.3 does not have the handlers keyword.
            # StramHandler will be added by default while the FileHandler
            # must be added manually.
            logging.getLogger('').addHandler(fhandler)

    logging.basicConfig(level=v, format=msg_fmt, datefmt=dt_fmt,
                        handlers=handlers)
