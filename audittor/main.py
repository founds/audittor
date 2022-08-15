#!/usr/bin/env python
# -*- coding: utf-8 -*-

from manager import AddonManager
import os
import sys
from datetime import datetime


VERSION = "v0.3"


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

        #AddonManager()

    def generate_log(self):
        with open(self.path + "/log.txt", 'w') as sys.stdout:
            print("Audittor %s" % VERSION )
            print("Fecha de analisis: %s    Hora de analisis: %s" % (datetime.today().strftime('%Y/%m/%d'),
                  datetime.today().strftime('%H:%M:%S')))
            print("\n")


if __name__ == '__main__':
    Audittor()
