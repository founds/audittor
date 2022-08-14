#!/usr/bin/env python
# -*- coding: utf-8 -*-

from colorama import Fore
import logging
from manager import AddonManager

RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET


class Audittor():

    def __init__(self):
        self.log = logging.getLogger('audittor')

        print("############################################")
        print("############################################")
        print("###                                      ###")
        print("###              Audittor                ###")
        print("###                                      ###")
        print("###      Simple auditor de sistema       ###")
        print("###                                      ###")
        print("############################################")
        print("############################################\n")

        AddonManager()

        '''for addon in addons_exec:
            status = AddonManager().exec_addon(addon)
            print(status)'''


if __name__ == '__main__':
    Audittor()
