#!/bin/env python3
# -*- coding: utf-8 -*-

import serial
import IPTCMessage

class _main(object):
    def __init__(self, port='/dev/tty706'):
        ser = self.openPort(port)
        while True:
            msg = self.waitForStart(ser)
            msg += self.readUntilEOM(ser)
            iptc = IPTCMessage(msg)

    def openPort(self, port):
        ser = serial.Serial(port=port, baudrate=4800, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=None)
        print("%s opened with %i baud. Timeout is %s seconds." % (ser.name, ser.baudrate, ser.timeout))
        return ser

    def waitForStart(self, ser):
        print("Waiting for start indicator (%i): " % ser.inWaiting(), end='', flush=True)
        while True:
            byte = ser.read(size=1)
            print(".", end='', flush=True)
            if byte == b'\x01':
                print("Found.")
                return byte

    def readUntilEOM(self, ser):
        print("Reading data until EOM.", end='', flush=True)
        msg = b''
        ctr = 0
        while True:
            print("%i>" % ser.inWaiting(), end='', flush=True)
            byte = ser.read(size=1)
            ctr+=1
#            if ctr % 10 is 0:
            print(".", end='', flush=True)
            if byte == b'\x01':
                print("PROBLEM: Got start indicator, but message not yet finished.")
                break
            msg += byte
            if byte == b'\x04':
                break
        print("Got %i bytes." % len(msg))
        return msg

    def readLine(self, ser):
        rcv = ser.readline()
        print("Got: %s" % repr(rcv))

if __name__=='__main__':
    _main()
