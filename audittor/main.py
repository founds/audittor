#!/usr/bin/env python
# -*- coding: utf-8 -*-

from colorama import Fore
import os
import logging
from functools import partial
from pluginbase import PluginBase
from priority import checkpriority

RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET

class audittor():

    def __init__(self):
        self.log = logging.getLogger('audittor')

        print("### Iniciando Audittor ###\n")

        audcheck = self.check_addon()

    def check_addon(self):

        print(" - Leyendo addons de funciones")

        plugin_dict = self.read_addons()
        self.addonsloads = dict()

        for plugin_module in plugin_dict.values():
            self.addonsloads[plugin_module.NAME] = plugin_module.is_addon
            print(f"{GREEN}   - " + plugin_module.NAME + " " + plugin_module.VERSION + f"{RESET}")

        if len( self.addonsloads) == 0:
            print(f"{RED}   - No se han encontrado addons de funciones.{RESET}")
            exit()

        # Check for prioritized ones first, then check those added externally
        checklist = checkpriority
        checklist += list(set( self.addonsloads.keys()) - set(checklist))
        detected = list()

        print("\n - Ejecutando la auditación del sistema")

        for audcheck in checklist:
            self.log.info('activando: %s' % audcheck)

            try:

                print(f"\n{GREEN}   - Auditando: %s {RESET}" % audcheck)

                if  self.addonsloads[audcheck](self) == True:
                    print(f"\n{GREEN}     - %s: OK {RESET}" % audcheck)
                    detected.append(audcheck)

            except KeyError:
                print(f"{RED}     - Addon no encontrado pero registrado: " + audcheck + f"{RESET}")
                pass

        return detected


    def read_addons(self):
        here = os.path.abspath(os.path.dirname(__file__))
        get_path = partial(os.path.join, here)
        plugin_dir = get_path('addons')

        plugin_base = PluginBase(
            package='addons', searchpath=[plugin_dir]
        )
        plugin_source = plugin_base.make_plugin_source(
            searchpath=[plugin_dir], persist=True
        )

        plugin_dict = {}
        for plugin_name in plugin_source.list_plugins():
            plugin_dict[plugin_name] = plugin_source.load_plugin(plugin_name)

        return plugin_dict


if __name__ == '__main__':
    audittor()