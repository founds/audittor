#!/usr/bin/env python
# -*- coding: utf-8 -*-

from manager import AddonManager


class Audittor():

    def __init__(self):

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
        AddonManager().list_addons()


if __name__ == '__main__':
    Audittor()
