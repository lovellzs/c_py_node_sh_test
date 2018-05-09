#!/usr/bin/python
# -*- coding: UTF-8 -*-

l1 = [1,"aaa",11.8,4]
print l1
for  aa in l1 :
    # print aa
    pass

s1 = {1,222,3.14,9}
print s1
for aa in s1:
    print "%d===%.1f"%( aa , aa)

x = set("abcd")
print x


import functools
print dir(functools)
