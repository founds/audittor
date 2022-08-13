#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
from configobj import ConfigObj
from functools import partial
from colorama import Fore
from pluginbase import PluginBase

from priority import checkpriority

RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET


class AddonManager:

    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(sys.argv[0]))

        if not os.path.exists(self.path + "/addons.cfg"):
            self.newconfigfiles()

        self.load_addons()

    # Crear archivo de addons base
    def newconfigfiles(self):

        # Ver los addons disponibles
        addonslist = self.read_addons()

        config = ConfigObj()
        config.filename = self.path + "/addons.cfg"

        for addon_module in addonslist.values():
            description = addon_module.DESCRIPTION.encode('ascii', 'ignore').decode('ascii')
            config[addon_module.NAME] = {
                "Name": addon_module.NAME,
                "Version": addon_module.VERSION,
                "Status": False,
                "Description": description
            }

        config.write()

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
            print(f"{GREEN}   - " + plugin_dict[plugin_name].NAME + " " + plugin_dict[plugin_name].VERSION + f"{RESET}")

        return plugin_dict

    def load_addons(self):

        print(" - Leyendo archivos de addons de funciones")

        addons_dict = self.read_addons()
        addonsloads = dict()
        addon_name = []

        config = ConfigObj(self.path + "/addons.cfg")

        print("\n - Cargando archivos de addons de funciones")

        for plugin_module in addons_dict.values():
            addonsloads[plugin_module.NAME] = plugin_module.is_addon
            addon = config[plugin_module.NAME]

            if addon['Status'] == "True":
                print(f"{GREEN}   - " + plugin_module.NAME + " " + plugin_module.VERSION + f"{RESET}")
                addon_name.append(plugin_module.NAME)
            else:
                print(f"{RED}   - %s: Addons presentes pero no activo.{RESET}" % plugin_module.NAME)
                continue

        print("\n - Ejecutando la auditación del sistema")

        for exec_addon in addon_name:
            print(f"\n{GREEN}   - Auditando: %s {RESET}" % exec_addon)

            try:
                if addonsloads[exec_addon](self) == True:
                    print(f"\n{GREEN}     - %s: OK {RESET}" % exec_addon)

            except KeyError:
                print(f"{RED}     - Addon no encontrado pero registrado: " + plugin_module.NAME + f"{RESET}")



        if len(addonsloads) == 0:
            print(f"{RED}   - No se han encontrado addons de funciones.{RESET}")
            exit()