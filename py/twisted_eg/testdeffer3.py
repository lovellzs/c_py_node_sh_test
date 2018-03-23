#!/usr/bin/python
# -*- coding: UTF-8 -*-

from twisted.internet.defer import inlineCallbacks, Deferred, returnValue
from twisted.python.failure import Failure

from twisted.internet import reactor, defer


def loadRemoteData(callback):
    import time
    time.sleep(3)
    callback(1)


def loadRemoteData2(callback):
    import time
    time.sleep(3)
    callback(2)

@defer.inlineCallbacks
def getRemoteData():
    d1 = defer.Deferred()
    reactor.callInThread(loadRemoteData, d1.callback)
    # print "===r1===="
    # r1 = yield d1
    # print "===r1====" , r1

    d2 = defer.Deferred()
    reactor.callInThread(loadRemoteData2, d2.callback)
    # print "===r2===="
    # r2 = yield d2
    # print "===r2====", r2

    returnValue( 10 )


def getResult(v):
    print "result=", v


if __name__ == '__main__':
    d = getRemoteData()
    d.addCallback(getResult)

    reactor.callLater(4, reactor.stop);
    reactor.run()
