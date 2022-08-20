#!/usr/bin/env python

import socket
from colorama import Fore
import logging

RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET

ID = 'addon_network'
NAME = 'check_network'
CATEGORY = 'networks'
VERSION = '0.2'
DESCRIPTION = 'Analisis de red'


def is_addon(self):
    logging.basicConfig(filename=self.path + "/log.txt", level=logging.DEBUG)
    scan_ports()


def scan_ports():
    # Escanear puertos
    for port in range(1, 5000):
        sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = sck.connect_ex(("127.0.0.1", port))

        if result == 0:
            logging.debug("  - Puerto %s abierto" % port )
            print(f"{RED}     - Puerto {port} abierto{RESET} ".format(port))

        sck.close()



