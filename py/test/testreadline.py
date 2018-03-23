#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开文件
file = open("mymodule.py", "rw+")

print "文件名为: ", file.name

'''
for index in range(5):
    line = file.next()
    print "第 %d 行 - %s" % (index+1, line)
'''


'''
while 1:
    line = file.readline()
    if not line:
        break
    print line;
'''

for line in file:
	print line.replace('\n','');

# 关闭文件
file.close();