#!/usr/bin/env python

import socket
from colorama import Fore

RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET

NAME = 'Analisis de red'
VERSION = '0.1'

def is_addon(self):
    # Escanear puertos
    for port in range(1, 5000):
        sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = sck.connect_ex(("127.0.0.1", port))

        if result == 0:
            print(f"{RED}     - Puerto {port} abierto{RESET} ".format(port))
        sck.close()