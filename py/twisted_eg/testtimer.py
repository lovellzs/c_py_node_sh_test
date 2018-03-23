#!/usr/bin/python
# -*- coding: UTF-8 -*-

from twisted.internet import reactor

import time

def print_i(i):
    print i

def run():
    def long():
        print '''    ...taking a while '''

    def handle():
        if not long_dc.called:
            long_dc.cancel()
            print "handle"
        print "ok!"

    long_dc = reactor.callLater(5, long)

    reactor.callLater(1, print_i ,1 )
    reactor.callLater(2, print_i, 2)
    reactor.callLater(3, print_i, 3)
    reactor.callLater(4, handle)

reactor.callLater( 0 , run )
reactor.run()








