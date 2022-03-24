# pylogsvc

A simple helper module to set up logging in your project focusing on what is important !

## Usage

Single setup point the `set_logging` function. Import it from your project's 
main and set it with your preferred arguments.

The help message provides information on the input and the default values.

```
>>> from logsvc import set_logging
>>> help(set_logging)
Help on function set_logging in module logsvc.logging:

set_logging(name, level='DEBUG', vcount=None, msg_fmt='[%(asctime)s][%(levelname)-8s][%(filename)s, %(lineno)d][%(name)s]  %(message)s', dt_fmt='%Y-%m-%d %H:%M:%S', logdir='/home/$USER/.local/logs', flog='', monitor=False, listen=False)
    Sets the logging configuration.
    
    name    : (str) logger name
    level   : (str) the logging level ['debug', 'info', 'warning', 'error', 'critical']
    vcount  : (int) logging level in the form of v-counts. If set level is ignored.
    msg_fmt : (str) logger message format
    dt_fmt  : (str) datetime format
    logdir  : (path) log files directory
    flog    : (str) log to file
    monitor : (bool) starts the file monitor for log level
    listen  : (bool) starts the logging server for log commands
```

If the `listen` key is enabled then a TCP server is listening for connections that provide commands to the logging service.
An executable is provided to facilitate the interaction with the server.

```
$ logsvc -h
usage: logsvc [-h] {loglevel} ...

CLI interface for logging service module.

Some more info

positional arguments:
  {loglevel}
    loglevel  Management of the logging level

optional arguments:
  -h, --help  show this help message and exit

Examples:

logsvc -h
logsvc loglevel -h
logsvc loglevel
logsvc loglevel --set DEBUG
```


If the `monitor` key is enabled then the module stores the logging level to a file, which is then monitored for changes.
The level will be set based on the file content accordingly ('NOTSET', 'DEBUG' etc)
