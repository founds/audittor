#!/usr/bin/env python
# -*- coding: utf-8 -*-

from colorama import Fore
import os
import logging
from manager import AddonManager


RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET

class audittor():

    def __init__(self):
        self.log = logging.getLogger('audittor')

        print("### Iniciando Audittor ###\n")

        AddonManager()

if __name__ == '__main__':
    audittor()