#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pystache
import re

class IPTCMessage(object):
    def __init__(self, raw):
        self.raw = raw
        self.length = len(self.raw)
        if self.raw[0:1] != b'\x01' or self.raw[-1:] != b'\x04':
            raise Exception("Not a valid IPTC message!")
        (self.fullheader, leftover) = self.raw[1:-1].split(b'\x02', 2)
        (self.text, self.posttext) = leftover.split(b'\x03', 2)
        self.parseHeader()
        self.parseText()
        self.parsePostText()
        print("Header: " + repr(self.header))
        print("Main text: " + self.text)
        print("Post-text: " + repr(self.posttext))
        print("Post-data: " + repr(self.postdata))
#        print("Message: %s" % repr(self.raw))

    def parseHeader(self):
        fullheader = self.fullheader.decode("latin1")
        parts = re.fullmatch('^([a-zA-Z]{1,3})([0-9]{3,4}) ([1-6]) ([a-zA-Z]{1,3}) ([0-9]{1,4}) (.{0,50})\r\n+(.{0,69})\r\n$', fullheader, re.MULTILINE | re.DOTALL)
        if parts is None:
            raise Exception("Header not conforming to IPTC structure.")
        self.header = {
            "source_id": parts.group(1),
            "message_no": parts.group(2),
            "priority": parts.group(3),
            "category": parts.group(4),
            "word_count": parts.group(5),
            "optional": parts.group(6),
            "keywords": parts.group(7)
        }

    def parseText(self):
        self.text = self.text.decode("latin1")
        pass

    def parsePostText(self):
        posttext = self.posttext.decode("latin1")
#        posttext = "191552 MEZ sep 14blafasel"   # test string according to spec
        parts = re.fullmatch('^([0-9]{6})( ([a-zA-Z]{3})(?= [a-zA-Z]))?( ([a-zA-Z]{3}) ([0-9]{2}))?(.{1,32})?$', posttext, re.MULTILINE | re.DOTALL)
        if parts is None:
            raise Exception("PostText not conforming to IPTC structure.")
        self.postdata = {
            "datetime": parts.group(1),
            "timezone": parts.group(3),  # skip one b/c "whole"-match
            "month": parts.group(5),  # skip one b/c "whole"-match
            "year": parts.group(6),
            "msg_separation": parts.group(7)
        }

    def getIPTC(self):
        return self.raw

    def getNewsML(self):
        renderer = pystache.Renderer()
        tpl = renderer.load_template('newsml')
        xml = renderer.render(tpl, self)
        return xml

if __name__=='__main__':
    print("Testmode!")
