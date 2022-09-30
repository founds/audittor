#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from colorama import Fore

RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET

ID = 'addon_ssh'
NAME = 'check_ssh'
VERSION = '0.3.3'
CATEGORY = 'services'
DESCRIPTION = 'Analisis servicio SSH'

def is_addon(self):
    check_ssh()

def check_ssh():
    status = os.system('systemctl is-active --quiet sshd')

    if status == 0:
        print("     -> Se ha encontrado servicio SSH activo.\n")  # will return 0 for active else inactive.

        # Comprobar que exista el archivo de configuración
        if os.path.exists("/etc/ssh/sshd_config"):
            with open("/etc/ssh/sshd_config") as file:
                nerrors = checks(file.read())
    else:
        print(f"{GREEN}     -> No se ha encontrado servicio SSH activo.{RESET}\n")
        return True

    print(f"\n - Nº de errores encontrados: %s" % nerrors)

def checks(data):
    nerrors = 0

    if "Port 22" in data:
        print(f"{RED}       - Se está usando el puerto 22, este es un puerto por defecto.{RESET}")
        print("         No se recomienda usar el puerto por defecto.\n")
        nerrors += 1

    if "PermitRootLogin yes" or "#PermitRootLogin no" in data:
        print(f"{RED}       - Se permite el acceso al usuario root.{RESET}")
        print("         .\n")
        nerrors += 1

    if "#StrictModes yes" in data:
        print(f"{RED}       - El modo estricto no esta activo.{RESET}")
        print("         .\n")
        nerrors += 1

    if "StrictModes no" in data:
        print(f"{RED}       - El modo estricto no esta activo.{RESET}")
        print("         .\n")
        nerrors += 1

    if "#bantime" in data:
        print(f"{RED}       - No esta establecido el tiempo de baneo.{RESET}")
        print("         .\n")
        nerrors += 1

    if "#maxretry" in data:
        print(f"{RED}       - No esta establecido el número de maximo de intentos.{RESET}")
        print("         Tiempo para la desconeción si el usuario no logra logarse.\n")
        nerrors += 1

    if "#Protocol" in data:
        print(f"{RED}       - No esta establecido el número de maximo de intentos.{RESET}")
        print("         Tiempo para la desconeción si el usuario no logra logarse.\n")
        nerrors += 1

    if "Protocol" not in data:
        print(f"{RED}       - No esta establecido el número de maximo de intentos.{RESET}")
        print("         Tiempo para la desconeción si el usuario no logra logarse.\n")
        nerrors += 1

    if "#LoginGraceTime" in data:
        print(f"{RED}       - No esta establecido el tiempo maximo de loging.{RESET}")
        print("         Tiempo que tiene un usuario para loguearse en el sistema correctamente.\n")
        nerrors += 1

    if "#UsePrivilegeSeparation" in data:
        print(f"{RED}       - No esta establecido la separación de privilegios.{RESET}")
        print("         .\n")
        nerrors += 1

    if "#MaxAuthTries" in data:
        print(f"{RED}       - No esta especificado el número de intentos de autenticación permitidos por conexión.{RESET}")
        print("         Número máximo de intentos de autenticación permitidos por conexión.\n")
        nerrors += 1

    if "#MaxSessions" in data:
        print(f"{RED}       - No esta especificado el número máximo de sessiones.{RESET}")
        print("         Permite especificar el número máximo de sesiones abiertas.\n")
        nerrors += 1

    return nerrors




