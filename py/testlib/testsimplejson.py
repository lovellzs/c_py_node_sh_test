#coding=utf-8

'''
测试simplejson
'''

import json

dict1 = {"jsonrpc":'2.0','method':'post','id':1}
print dict,type(dict1)
print json.dumps( dict1 )

print isinstance(dict1, dict) ## 两个参数不能用dict  命名最好不要和关键字相同
print isinstance(json.dumps( dict1 ), str)

data = json.loads('{"jsonrpc": "2.0", "method": "post", "id": 1}')
print data
print type(data)
print data[u"jsonrpc"]

