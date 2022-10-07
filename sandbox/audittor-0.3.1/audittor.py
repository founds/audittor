#!/usr/bin/env python
# -*- coding: utf-8 -*-

from manager import AddonManager
import os
import sys
import argparse
from colorama import Fore


VERSION = "v0.3.1"
RED = Fore.RED
RESET = Fore.RESET

class Audittor():

    def __init__(self):

        print("#################################################################")
        print("#################################################################")
        print("####                                                         ####")
        print("####                       Audittor " + VERSION + "                    ####")
        print("####                                                         ####")
        print("####                Simple auditor de sistema                ####")
        print("####                                                         ####")
        print("####   Creado por Altsys                                     ####")
        print("####   EMAIL: info@altsys.es   WEB: https://www.altsys.es    ####")
        print("####                                                         ####")
        print("#################################################################")
        print("#################################################################\n")

        # Comprobar si existe el archivo de configuracion
        self.path = os.path.abspath(os.path.dirname(sys.argv[0]))


        if not os.path.exists(self.path + "/audittor.cfg"):
            pass

    def audittor_cli(self):

        if len(sys.argv) <= 1:
            print(f"{RED}No se ha especificado ningún argumento. Se inicia la audición por defecto.{RESET}\n")
            exec_addons = AddonManager().load_addons()

            print("\n - Ejecutando la auditación del sistema")

            for exec_addon in exec_addons:
                status = AddonManager().exec_addon(exec_addon)

            sys.exit(1)
        else:
            if sys.argv[1] == "-l":
                AddonManager().read_addons()
            elif sys.argv[1] == "-e":
                print("Activando addon: %s" % sys.argv[2])
                status = AddonManager().enable_addon(sys.argv[2])
                if status == True:
                    print("Addon %s activado" % sys.argv[2])
                else:
                    print(f"{RED} - %s {RESET}" % status)
            elif sys.argv[1] == "-d":
                if sys.argv[1]:
                    print("Desactivando addon: %s" % sys.argv[2])
                    status = AddonManager().disable_addon(sys.argv[2])
                    if status == True:
                        print("Addon %s desactivado" % sys.argv[2])
                    else:
                        print(f"{RED} - %s {RESET}" % status)


    def generate_log(self, data):
        '''with open(, 'w') as sys.stdout:
            print("Audittor %s" % VERSION)

            print("\n")
'''



if __name__ == '__main__':
    Audittor().audittor_cli()
