#!/bin/env python3
# -*- coding: utf-8 -*-

import iptcmessage
import unittest

class IPTCMessageTestCase(unittest.TestCase):

    def testMessageParsing(self):
        iptc = iptcmessage.IPTCMessage("")
        self.assertGreater(iptc.length, 0)

if __name__=='__main__':
    unittest.main()
