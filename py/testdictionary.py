#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
dict['2'] = "This is 2"
 
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
 
 
print dict['one']          # 输出键为'one' 的值
print dict[2]              # 输出键为 2 的值
print dict['2']            # 输出键为 2 的值

print dict      		   # 输出键为'one' 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值

dic11 = { 'name': 'john',"age":19 ,"son":{"name":"zhangsan","age":199} }

# print "dic11.name",dic11["name"]
# print "dic11.age",dic11["age"]
# print "dic11.son",dic11["son"]

print "dic11.name",dic11["name"]
print "dic11.age",dic11["age"]
print "dic11.son",dic11["son"]["name"]