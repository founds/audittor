#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from colorama import Fore

RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET

ID = 'addon_ssh'
NAME = 'check_ssh'
VERSION = '0.3.1'
CATEGORY = 'services'
DESCRIPTION = 'Analisis servicio SSH'

def is_addon(self):
    check_ssh()

def check_ssh():
    status = os.system('systemctl is-active --quiet sshd')

    if status == 0:
        print("Se ha encontrado servicio SSH activo.")  # will return 0 for active else inactive.

        # Comprobar que exista el archivo de configuración
        if os.path.exists("/etc/ssh/sshd_config"):
            with open("/etc/ssh/sshd_config") as file:
                datafile = file.readlines()

            checks(datafile)

    else:
        print(f"{GREEN}     - No se ha encontrado servicio SSH activo.{RESET}")
        return True

def checks(datas):

    if "Port 22" in datas:
        print(f"{RED}   - Se está usando el puerto 22, este es un puerto por defecto.{RESET}")

    if "PermitRootLogin yes" or "#PermitRootLogin no" in datas:
        print(f"{RED}   - Se permite el acceso al usuario root.{RESET}")

    if "#StrictModes yes" or "StrictModes no" in datas:
        print(f"{RED}   - El modo estricto no esta activo.{RESET}")



