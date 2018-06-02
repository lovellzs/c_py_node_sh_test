#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
a1 = "a1" # Global

class Foo:
    a2 = "a2" # Local

    def func(self):
        a3 = "a3" # Local

        for i in range(3):
            a4 = "a4" # Local 和 a3 在同一个作用域，因为 for 不会引入新的作用域

        def _func():
            a5 = "a5"  # Local
            print a4
            print i

        _func()

f = Foo()
f.func()

a = "aaa"
b = "aaa"
print a == b
print 1 == 1.0
print 1 == '1'









