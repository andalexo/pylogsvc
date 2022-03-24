"""CLI interface for logging service module.

Some more info
"""

from socket import socket, AF_INET, SOCK_STREAM, timeout
from argparse import (ArgumentParser, ArgumentDefaultsHelpFormatter,
                      RawTextHelpFormatter)

LOG_LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
EXAMPLES_CMDS = """\n
Examples:

logsvc -h
logsvc loglevel -h
logsvc loglevel
logsvc loglevel --set DEBUG
"""


class RawDefaultsFormatter(ArgumentDefaultsHelpFormatter,
                           RawTextHelpFormatter):
    pass


class LogSvcCli:
    def __init__(self):
        kw_dict = {'description': __doc__, 'epilog': EXAMPLES_CMDS,
                   'formatter_class': RawDefaultsFormatter}
        self.parser = ArgumentParser(**kw_dict)

        netparser = self.set_network_parser()
        
        cmd_parser = self.parser.add_subparsers(dest='cmds')

        # LOG LEVEL COMMAND
        loglevel_parser = cmd_parser.add_parser('loglevel', parents=[netparser],
                                                formatter_class=RawDefaultsFormatter,
                                                help=self.loglevel.__doc__)
        loglevel_parser.add_argument('--set', dest='level', choices=LOG_LEVELS, required=False,
                                     type=str, help='the log level to set')
        loglevel_parser.set_defaults(func=self.loglevel)

        self.args = self.parser.parse_args()
        self.args.func()
    
    @staticmethod
    def set_network_parser():
        parser = ArgumentParser(add_help=False)
        parser.add_argument('--host', default='localhost', type=str,
                            help='The host to connect to.')
        parser.add_argument('--port', default=9030, type=int,
                            help='The port to connect to.')
        
        return parser

    def loglevel(self):
        """Management of the logging level"""

        msg = self.args.level if self.args.level else 'get' 
        try:
            with socket(AF_INET, SOCK_STREAM) as s:
                s.settimeout(3.)
                s.connect((self.args.host, self.args.port))
                s.sendall(msg.encode('utf-8'))
                print(s.recv(1024).decode('utf-8'))
        except (ConnectionRefusedError, timeout) as e:
            print('{} {}:{}'.format(e, self.args.host, self.args.port))
        except KeyboardInterrupt:
            pass


def main():
    LogSvcCli()


if __name__ == '__main__':
    main()
