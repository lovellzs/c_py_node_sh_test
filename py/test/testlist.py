#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
 
print list               # 输出完整列表
print list[0]            # 输出列表的第一个元素
print list[1:3]          # 输出第二个至第三个的元素 
print list[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
print list + tinylist    # 打印组合的列表

'''
aaa = list[1:3]
print aaa
print aaa[0]

aaa[0] = 100
print aaa[0]
'''

#测试元组
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list11 = [ 'runoob', 786 , 2.23, 'john', 70.2 ]

bbb = tuple[1:3]
ccc = list11[1:3]

print bbb  #(786, 2.23)
print ccc  #[786, 2.23]
















