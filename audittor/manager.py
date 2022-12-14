#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from functools import partial
from colorama import Fore
from configobj import ConfigObj
from tabulate import tabulate
from pluginbase import PluginBase
import logging
from datetime import datetime


VERSION = "v0.3"
RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET


class AddonManager(object):

    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(sys.argv[0]))

        logging.basicConfig(filename=self.path + "/log.txt", level=logging.DEBUG)

        logging.debug("Audittor %s" % VERSION)

        logging.debug("Fecha de analisis: %s    Hora de analisis: %s" % (datetime.today().strftime('%Y/%m/%d'),
                                                                 datetime.today().strftime('%H:%M:%S')))

        if not os.path.exists(self.path + "/addons.cfg"):
            self.newconfigfiles()

        here = os.path.abspath(os.path.dirname(__file__))
        self.get_path = partial(os.path.join, here)

        self.plugin_dir = self.get_path(self.path + '/addons')

        self.plugin_base = PluginBase(
            package='addons', searchpath=[self.plugin_dir]
        )

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

        plugin_dict = {}

        here = os.path.abspath(os.path.dirname(__file__))
        get_path = partial(os.path.join, here)

        with os.scandir(get_path(self.path + '/addons')) as ficheros:
            subdirectorios = [fichero.name for fichero in ficheros if fichero.is_dir()]

        if "__pycache__" in subdirectorios:
            subdirectorios.remove("__pycache__")

        plugin_dir = get_path(self.path + '/addons')

        plugin_base = PluginBase(
            package='addons', searchpath=[plugin_dir]
        )

        for path_addon in subdirectorios:
            plugin_source = plugin_base.make_plugin_source(
                searchpath=[get_path(self.path + '/addons/%s') % path_addon], persist=True)

            for plugin_name in plugin_source.list_plugins():
                plugin_dict[plugin_name] = plugin_source.load_plugin(plugin_name)
                print(f"   - " + plugin_dict[plugin_name].NAME + " Versi??n: " +
                      plugin_dict[plugin_name].VERSION + "\n     Descripci??n: " +
                      plugin_dict[plugin_name].DESCRIPTION + "\n")

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
                addon_name.append([plugin_module.ID, plugin_module.CATEGORY])
            else:
                print(f"{RED}   - %s: Addons presentes pero no activo.{RESET}" % plugin_module.NAME)
                continue

        if len(addonsloads) == 0:
            print(f"{RED}   - No se han encontrado addons de funciones.{RESET}")
            exit()

        return addon_name

    def exec_addon(self, name):
        # Each application has a name
        self.name = name

        here = os.path.abspath(os.path.dirname(__file__))
        get_path = partial(os.path.join, here)

        plugin_base = PluginBase(package='audittor',
                                 searchpath=[get_path(self.path + '/addons')])

        if len(name) > 2:
            for addon in name:
                source = plugin_base.make_plugin_source(

                    searchpath=[get_path(self.path + '/addons/%s/') % addon[1]],
                    identifier=addon[0])

                print(f"\n{GREEN}   - Auditando: %s {RESET}\n" % addon[0])

        elif len(name) == 2:
            source = plugin_base.make_plugin_source(

                searchpath=[get_path(self.path + '/addons/%s/') % name[1]],
                identifier=name[0])

            print(f"\n{GREEN}   - Auditando: %s {RESET}\n" % name[0])

            for addon_name in source.list_plugins():
                addon = source.load_plugin(addon_name)

                try:
                    if addon.is_addon(self):
                        print(f"{GREEN}     - %s finalizado: OK {RESET}" % name[0])

                except KeyError:
                    print(f"{RED}     - Addon no encontrado pero registrado: " + name[0] + f"{RESET}")

        return True

    # Activar addon
    def enable_addon(self, id_addon):
        config = ConfigObj(self.path + "/addons.cfg")
        addon = config[id_addon]

        if addon["Status"] == "False":
            addon["Status"] = "True"
            config.write()
            return True
        elif addon["Status"] == "True":
            return "Este addon ya esta activado"



    # Desactivar addon
    def disable_addon(self, id_addon):
        config = ConfigObj(self.path + "/addons.cfg")
        addon = config[id_addon]

        if addon["Status"] == "True":
            addon["Status"] = "False"
            config.write()
            return True
        elif addon["Status"] == "False":
            return "Este addon ya esta desactivado"

    # Listar addons
    def list_addons(self):
        addon_dict = {}

        here = os.path.abspath(os.path.dirname(__file__))
        get_path = partial(os.path.join, here)

        with os.scandir(get_path(self.path + '/addons')) as ficheros:
            subdirectorios = [fichero.name for fichero in ficheros if fichero.is_dir()]

        subdirectorios.remove("__pycache__")

        plugin_dir = get_path(self.path + '/addons')

        plugin_base = PluginBase(
            package='addons', searchpath=[plugin_dir]
        )

        addons = []

        for path_addon in subdirectorios:
            plugin_source = plugin_base.make_plugin_source(
                searchpath=[get_path(self.path + '/addons/%s') % path_addon], persist=True)

            for plugin_name in plugin_source.list_plugins():
                addon_dict[plugin_name] = plugin_source.load_plugin(plugin_name)

            addons.append(
                [addon_dict[plugin_name].ID, addon_dict[plugin_name].NAME, addon_dict[plugin_name].VERSION,
                 addon_dict[plugin_name].DESCRIPTION, ]
            )

        print(tabulate(addons, headers=["ID", "NAME", "VERSION", "DESCRIPTION"], tablefmt='grid'))

        return addon_dict
