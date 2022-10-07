#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from colorama import Fore
import platform
from psutil import virtual_memory, disk_io_counters
from psutil._common import bytes2human
import shutil
from blkinfo import BlkDiskInfo

RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET

ID = "addon_system"
NAME = "info_system"
VERSION = "0.2"
DESCRIPTION = "Recopilar información del sistema"

def is_addon(self):
    print("\n     - Sistema Operativo: " + platform.system())
    print("     - Versión: " + platform.version())
    print("     - Release: " + platform.release())
    print("     - Hostname: " + platform.node())

    hardware()

def hardware():

    # Memoria
    mem_usage = virtual_memory()
    total_in_human_format = bytes2human(mem_usage[0])
    used_in_human_format = bytes2human(virtual_memory().used)

    print("\n     - Hardware")
    print("       - Procesador: " + platform.processor())
    print("       - Nº de nucleos: " + str(os.cpu_count()))
    print("       - Memoria: " + str(total_in_human_format))
    print("       - Memoria en uso: " + str(used_in_human_format))

    print("\n     - Hardware - Discos")

    myblkd = BlkDiskInfo()
    all_my_disks = myblkd.get_disks()

    print("\n       - Nº de discos: %s" % len(all_my_disks))

    for item in all_my_disks:
        print("\n       - %s" % item["model"])
        print("         - Tipo: %s" % item["tran"])
        print("         - Serial: %s" % item["serial"])
        print("         - Label: %s" % item["label"])

        for subitem in item["children"]:
            print("\n           - Disco: %s" % subitem["name"])
            print("           - Label: %s" % subitem["label"])
            print("           - Formato: %s" % subitem["fstype"])
            print("           - P. Montaje: %s" % subitem["mountpoint"])
            print("           - Tipo: %s" % subitem["type"])

    total, used, free = shutil.disk_usage("/")
    print("\n       - Disco Principal")
    print("         - Tamaño: %s" % bytes2human(total))
    print("         - Usado: %s" % bytes2human(used))
    print("         - Libre: %s" % bytes2human(free))

    print("\n       - Actividad de disco")

    diskio = disk_io_counters(perdisk=False)

    print("         - Read Count: %s" % diskio[0])
    print("         - Write Count: %s" % diskio[1])
    print("         - Read Bytes: %s" % diskio[2])
    print("         - Write Bytes: %s" % diskio[3])
    print("         - Read Time: %s" % diskio[4])
    print("         - Write Time: %s" % diskio[5])
    print("         - Read Merge Count: %s" % diskio[6])
    print("         - Write Merge Count: %s" % diskio[7])
    print("         - Busy Time: %s" % diskio[8])