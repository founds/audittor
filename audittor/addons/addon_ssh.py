#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from colorama import Fore

RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET

NAME = 'Analisis servicio SSH'
VERSION = '0.1'

def is_addon(self):
    check_ssh()

def check_ssh():
    status = os.system('systemctl is-active --quiet sshd')

    if status == 0:
        print("Se ha encontrado servicio SSH activo.")  # will return 0 for active else inactive.

        # Comprobar que exista el archivo de configuración
        if os.path.exists("/etc/ssh/sshd_config"):
            print("Existe")
    else:
        print(f"{GREEN}     - No se ha encontrado servicio SSH activo.{RESET}")
        return True





