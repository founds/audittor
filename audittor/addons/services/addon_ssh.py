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
        print(f"{RED}       - Port: Se está usando el puerto 22, este es un puerto por defecto.{RESET}")
        print("         No se recomienda usar el puerto por defecto.\n")
        nerrors += 1

    if "PermitRootLogin yes" or "#PermitRootLogin no" in data:
        print(f"{RED}       - PermitRootLogin: Se permite el acceso al usuario root.{RESET}")
        print("         .\n")
        nerrors += 1

    if "#PermitRootLogin no" in data:
        print(f"{RED}       - PermitRootLogin: Se permite el acceso al usuario root.{RESET}")
        print("         .\n")
        nerrors += 1

    if "PermitRootLogin" not in data:
        print(f"{RED}       - PermitRootLogin: Se permite el acceso al usuario root.{RESET}")
        print("         .\n")
        nerrors += 1

    if "#StrictModes yes" in data:
        print(f"{RED}       - StrictModes: El modo estricto no esta activo.{RESET}")
        print("         .\n")
        nerrors += 1

    if "StrictModes no" in data:
        print(f"{RED}       - StrictModes: El modo estricto no esta activo.{RESET}")
        print("         .\n")
        nerrors += 1

    if "StrictModes" not in data:
        print(f"{RED}       - StrictModes: El modo estricto no esta activo.{RESET}")
        print("         .\n")
        nerrors += 1

    if "#Bantime" in data:
        print(f"{RED}       - Bantime: No esta establecido el tiempo de baneo.{RESET}")
        print("         .\n")
        nerrors += 1

    if "Bantime" not in data:
        print(f"{RED}       - Bantime: No esta establecido el tiempo de baneo.{RESET}")
        print("         .\n")
        nerrors += 1

    if "#maxretry" in data:
        print(f"{RED}       - maxretry: No esta establecido el número de maximo de intentos.{RESET}")
        print("         Tiempo para la desconeción si el usuario no logra logarse.\n")
        nerrors += 1

    if "maxretry" not in data:
        print(f"{RED}       - maxretry: No esta establecido el número de maximo de intentos.{RESET}")
        print("         Tiempo para la desconeción si el usuario no logra logarse.\n")
        nerrors += 1

    if "#Protocol" in data:
        print(f"{RED}       - Protocol: No esta establecido el protocolo de conexión.{RESET}")
        print("         .\n")
        nerrors += 1

    if "Protocol" not in data:
        print(f"{RED}       - Protocol: No esta establecido el número de maximo de intentos.{RESET}")
        print("         Tiempo para la desconeción si el usuario no logra logarse.\n")
        nerrors += 1

    if "#LoginGraceTime" in data:
        print(f"{RED}       - LoginGraceTime: No esta establecido el tiempo maximo de loging.{RESET}")
        print("         Tiempo que tiene un usuario para loguearse en el sistema correctamente.\n")
        nerrors += 1

    if "LoginGraceTime" not in data:
        print(f"{RED}       - LoginGraceTime: No esta establecido el tiempo maximo de loging.{RESET}")
        print("         Tiempo que tiene un usuario para loguearse en el sistema correctamente.\n")
        nerrors += 1

    if "#UsePrivilegeSeparation" in data:
        print(f"{RED}       - UsePrivilegeSeparation: No esta establecido la separación de privilegios.{RESET}")
        print("         .\n")
        nerrors += 1

    if "UsePrivilegeSeparation" not in data:
        print(f"{RED}       - UsePrivilegeSeparation: No esta establecido la separación de privilegios.{RESET}")
        print("         .\n")
        nerrors += 1

    if "#MaxAuthTries" in data:
        print(f"{RED}       - MaxAuthTries: No esta especificado el número de intentos de autenticación permitidos "
              f"por conexión.{RESET}")
        print("         Número máximo de intentos de autenticación permitidos por conexión.\n")
        nerrors += 1

    if "MaxAuthTries" not in data:
        print(f"{RED}       - MaxAuthTries: No esta especificado el número de intentos de autenticación permitidos "
              f"por conexión.{RESET}")
        print("         Número máximo de intentos de autenticación permitidos por conexión.\n")
        nerrors += 1

    if "#MaxSessions" in data:
        print(f"{RED}       - MaxSessions: No esta especificado el número máximo de sessiones.{RESET}")
        print("         Permite especificar el número máximo de sesiones abiertas.\n")
        nerrors += 1

    if "MaxSessions" not in data:
        print(f"{RED}       - MaxSessions: No esta especificado el número máximo de sessiones.{RESET}")
        print("         Permite especificar el número máximo de sesiones abiertas.\n")
        nerrors += 1

    if "#PermitEmptyPasswords" in data:
        print(f"{RED}       - PermitEmptyPasswords: No esta especificado el valor para contraseñas vacias.{RESET}")
        print("         Permite especificar si el servidor aprobará (autorizará) el iniciar de sesión en cuentas de "
              "usuarios con cadenas de contraseña vacías.\n")
        nerrors += 1

    if "PermitEmptyPasswords" not in data:
        print(f"{RED}       - PermitEmptyPasswords: No esta especificado el valor para contraseñas vacias.{RESET}")
        print("         Permite especificar si el servidor aprobará (autorizará) el iniciar de sesión en cuentas de"
              " usuarios con cadenas de contraseña vacías.\n")
        nerrors += 1

    return nerrors




