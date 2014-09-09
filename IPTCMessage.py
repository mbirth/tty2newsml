#!/bin/env python3
# -*- coding: utf-8 -*-

class IPTCMessage(object):
    def __init__(self, raw):
        self.raw = raw
        print("Message: %s" % repr(self.raw))

if __name__=='__main__':
    print("Testmode!")
