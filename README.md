# yaplog: Yet Another Python Logging module

A simple helper module to set up logging in your project focusing on what is important !

## Usage

Single setup point the `set_logging` function. Import it from your project's 
main and set it with your preferred arguments.

```
>>> from yaplog import set_logging
>>> help(set_logging)
Sets the logging configuration.

    vcount  : (int) logging level in the form of v-counts
    msg_fmt : (str) logger message format
    dt_fmt  : (str) datetime format
    logdir  : (path) log files directory
    flog    : (str) log to file
