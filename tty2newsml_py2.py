#!/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import serial
import sys
import IPTCMessage

class _main(object):
    def __init__(self, port='/dev/tty706'):
        self.openPort(port)
        while True:
            msg = self.waitForStart()
            msg += self.readUntilEOM()
            print("This is the message: %s" % repr(msg))

    def openPort(self, port):
        self.port = serial.Serial(port=port, baudrate=4800, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=None)
        print("%s opened with %i baud. Timeout is %s seconds." % (self.port.name, self.port.baudrate, self.port.timeout))

    def waitForStart(self):
        print("Waiting for start indicator (%i): " % self.port.inWaiting(), end='')
        sys.stdout.flush()
        while True:
            byte = self.port.read()
            print(".", end='')
            sys.stdout.flush()
            if byte == b'\x01':
                print("Found.")
                return byte

    def readUntilEOM(self):
        print("Reading data until EOM.", end='')
        sys.stdout.flush()
        msg = b''
        ctr = 0
        while True:
            print("%i>" % self.port.inWaiting(), end='')
            sys.stdout.flush()
            byte = self.port.read()
            ctr+=1
#            if ctr % 10 is 0:
            print(".", end='')
            sys.stdout.flush()
            if byte == b'\x01':
                print("PROBLEM: Got start indicator, but message not yet finished.")
                break
            msg += byte
            if byte == b'\x04':
                break
        print("Got %i bytes." % len(msg))
        return msg

    def readLine(self):
        rcv = self.port.readline()
        print("Got: %s" % repr(rcv))

if __name__=='__main__':
    _main()
