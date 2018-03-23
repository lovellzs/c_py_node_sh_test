#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

from twisted.internet.defer import Deferred
from twisted.python.failure import Failure

from twisted.internet import reactor, defer



def loadRemoteData(callback, errback, url):
    # 此处加载url内容
    # callback('url数据')
    # 或 errback(...)

    time.sleep(3)
    # callback(url)
    errback( Exception("Invalid level! 1111") )



def getRemoteData():
    d = defer.Deferred()
    reactor.callInThread(loadRemoteData, d.callback, d.errback, "http://www.baidu.com")
    return d


def getResult(v):
    print "result=", v

def dealErr(err):
    print "err=" , err

if __name__ == '__main__':
    d = getRemoteData()
    d.addCallbacks(getResult,dealErr)

    reactor.callLater(4, reactor.stop);
    reactor.run()