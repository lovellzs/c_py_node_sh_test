#!/usr/bin/python
# -*- coding: UTF-8 -*-

from twisted.internet import reactor , defer

import time

def print_time():
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())



@defer.inlineCallbacks
def run():

    @defer.inlineCallbacks
    def handle():

        def long():
            print '''    ...taking a while '''

        def getData( callback =None ):
            time.sleep(3)
            if not callback is None :
                callback(1)

        def check():
            if not long_dc.called:
                long_dc.cancel()
                res =  "handle"
            else:
                res = "ok"

            return res

        long_dc = reactor.callLater(5, long)

        d1 = defer.Deferred()
        res = yield reactor.callInThread( getData , d1.callback )

        print res
        defer.returnValue(res)

    try:
        res = yield handle()
        print "========"

    except Exception , errMsg:
        print errMsg
    else :
        if res=="handle":
            reactor.callLater(0,reactor.stop)

reactor.callLater( 0 , run )
reactor.run()








