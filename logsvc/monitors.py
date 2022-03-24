import logging
from os.path import join, expanduser
from time import sleep
from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM

LOG_DIR = join(expanduser('~'),  '.local', 'logs')


class FileLogLevelMonitor:
    def __init__(self, name, level, check_interval=5., logdir=LOG_DIR, **kwargs):
        self.level = level
        self.running = True
        self.name = name
        try:
            assert(check_interval >= 1)
        except AssertionError:
            raise ValueError('Check interval should be >= 1 sec')
        self.check_interval = check_interval

        self.fp = join(logdir, '.loglevel')

        with open(self.fp, 'w') as f:
            f.write(self.level)
    
    def stop(self):
        self.running = False
    
    def start(self):
        t = Thread(target=self.run, daemon=True)
        t.start()

    def run(self):
         while self.running:
            sleep(self.check_interval)

            with open(self.fp, 'r') as f:
                lvl = f.readline().rstrip()
                if lvl == self.level:
                    continue

                try:
                    logging.getLogger(self.name).setLevel(lvl)
                except ValueError as e:
                    logging.getLogger(self.name).error('%s: %s, ', type(self).__name__, e)


class SocketLogLevelMonitor():
    def __init__(self, name, host='localhost', port=9030):
        self.name = name
        self.host = host
        self.port = port
        self.running = True

    def stop(self):
        self.running = False
    
    def start(self):
        t = Thread(target=self.run, daemon=True)
        t.start()

    def run(self):
        with socket(AF_INET, SOCK_STREAM) as s:
            s.bind((self.host, self.port))

            while self.running:
                s.listen()
                conn, _ = s.accept()
                with conn:
                    data = conn.recv(1024).decode('utf-8')
                    if data == 'get':
                        loglvl = logging.getLevelName(logging.getLogger().getEffectiveLevel())
                        conn.sendall(loglvl.encode('utf-8'))    
                        continue
                    try:
                        logging.getLogger(self.name).setLevel(data)
                        loglvl = logging.getLevelName(logging.getLogger().getEffectiveLevel())
                        conn.sendall(loglvl.encode('utf-8'))  
                    except ValueError:
                        pass
