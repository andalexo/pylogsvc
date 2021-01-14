"""Logging configuration

Single and simple function with nice defaults.
"""

import logging
from logging.handlers import RotatingFileHandler
from os import makedirs
from os.path import exists, join, expanduser
from copy import copy
from sys import version_info

# COLORS | BLACK | RED   | GREEN | YELLOW| BLUE  |MAGENTA| CYAN  | WHITE
# -------|---------------------------------------------------------------
# FG     | 30    | 31    | 32    | 33    | 34    | 35    | 36    | 37 
# BG     | 40    | 41    | 42    | 43    | 44    | 45    | 46    | 47
COLOR_SEQ = "\033[1;%dm"
COLOR = {
    'DEBUG': "{}{}".format(COLOR_SEQ % 40, COLOR_SEQ % 34),
    'INFO': "{}{}".format(COLOR_SEQ % 40, COLOR_SEQ % 37),
    'WARNING': "{}{}".format(COLOR_SEQ % 40, COLOR_SEQ % 33),
    'ERROR': "{}{}".format(COLOR_SEQ % 40, COLOR_SEQ % 31),
    'CRITICAL': "{}{}".format(COLOR_SEQ % 41, COLOR_SEQ % 37),
}
BOLD_SEQ = "\033[1m"
RESET_SEQ = "\033[0m"

MSG_FMT = "[%(asctime)s][%(levelname)-8s]\
[%(filename)s, %(lineno)d][%(name)s]  %(message)s"
DT_FMT = "%m-%d %H:%M:%S"
LOG_DIR = join(expanduser('~'),  '.local', 'logs')
MAX_BYTES = 50e6


def set_logging(vcount, 
                msg_fmt=MSG_FMT, dt_fmt=DT_FMT,
                logdir=LOG_DIR, flog=''):
    """Sets the logging configuration.

    vcount  : (int) logging level in the form of v-counts
    msg_fmt : (str) logger message format
    dt_fmt  : (str) datetime format
    logdir  : (path) log files directory
    flog    : (str) log to file
    """

    if vcount is None or vcount == 0:
        v = logging.ERROR
    elif vcount == 1:
        v = logging.WARNING
    elif vcount == 2:
        v = logging.INFO
    else:
        v = logging.DEBUG

    stream_formatter = StreamFormatter(fmt=msg_fmt, datefmt=dt_fmt)
    file_formatter = logging.Formatter(fmt=msg_fmt, datefmt=dt_fmt)

    handlers = []
    shandler = logging.StreamHandler()
    shandler.setFormatter(stream_formatter)
    handlers.append(shandler)
    if flog:
        if not exists(logdir):
            makedirs(logdir)

        fhandler = RotatingFileHandler(
            join(logdir, flog),
            mode='w',
            backupCount=1,
            maxBytes=MAX_BYTES
        )
        fhandler.setFormatter(file_formatter)
        handlers.append(fhandler)

    logging.basicConfig(level=v, handlers=handlers)


class StreamFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        if 'datefmt' in kwargs:
            kwargs['datefmt'] = BOLD_SEQ + kwargs['datefmt'] + RESET_SEQ
        super(StreamFormatter, self).__init__(*args, **kwargs)

    def format(self, record: logging.LogRecord) -> str:
        flevelname = "{}{:8s}{}".format(COLOR[record.levelname],
                                        record.levelname,
                                        RESET_SEQ)
        frecord = copy(record)
        frecord.levelname = flevelname

        return super().format(frecord)
