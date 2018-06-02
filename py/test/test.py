#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py

if	False:
	print "Answer"
	print "True"
else:
	print "Answer"
	# 没有严格缩进，在执行时会报错
	print "False"

'''
这里是多行注释
哈哈哈哈
'''

"""
这里是多行注释
哈哈哈哈
"""

print '''你好！ 第一行代码
世界 第二行代码'''

print '''你好！ 第一行代码\
世界 第二行代码'''
print '''你好！ 第一行代码\n世界 第二行代码'''

import sys as aaa

module = aaa.modules[__name__]
print __name__
print str(module)
print str(module.__dict__)
print str(module.__dict__["__file__"])

for name in module.__dict__.keys():
	if name.startswith('__'):
		continue
	print name ,"=====>" ,str(module.__dict__[name])


haha=111
print 'haha===>',getattr(module,"aaa")
print "=================================="
print
print
aa = [ i for i in range(0 , 3)]
print aa