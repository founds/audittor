#!/usr/bin/env python
# -*- coding: utf-8 -*-

from manager import AddonManager
import os
import sys
import argparse
from colorama import Fore


VERSION = "v0.3"
RED = Fore.RED
RESET = Fore.RESET

class Audittor():

    def __init__(self):

        print("#################################################################")
        print("#################################################################")
        print("####                                                         ####")
        print("####                       Audittor " + VERSION + "                     ####")
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

        self.parser = argparse.ArgumentParser(description="Opciones de Audittor", argument_default=argparse.SUPPRESS)

        self.parser.add_argument("-L", "--list_addons", help="Muestra todos los addons.")
        self.parser.add_argument("-e", "--enabled_addons", help="Activar addon.",
                                 type=str, )
        self.parser.add_argument("-d", "--disabled_addons", help="Desactivar addon.",
                                 type=str, )

    def audittor_cli(self):
        args = self.parser.parse_args()

        if len(sys.argv) < 2:
            print(f"{RED}No se ha especificado ningún argumento. Se inicia la audición por defecto.{RESET}\n")
            exec_addons = AddonManager().load_addons()

            print("\n - Ejecutando la auditación del sistema")

            for exec_addon in exec_addons:
                status = AddonManager().exec_addon(exec_addon)

            sys.exit(1)

        if args.list_addons:
            AddonManager().read_addons()

        if args.enabled_addons:
            print("Activando addon: %s" % args.enabled_addons)
            status = AddonManager().enable_addon(args.enabled_addons)

            if status == True:
                print("Addon %s activado", args.enabled_addons)
            else:
                print(f"{RED} - %s {RESET}" % status)

        if args.disabled_addons:
            print("Desactivando addon: %s" % args.disabled_addons)
            status = AddonManager().disable_addon(args.disabled_addons)
            if status == True:
                print("Addon %s desactivado" % args.disabled_addons)
            else:
                print(f"{RED} - %s {RESET}" % status)


    def generate_log(self, data):
        '''with open(, 'w') as sys.stdout:
            print("Audittor %s" % VERSION)

            print("\n")
'''



if __name__ == '__main__':
    Audittor().audittor_cli()
