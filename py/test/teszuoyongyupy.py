#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import os

a = 1

def func1():

    global  a
    a = 3
    print a


func1()
print a

class Person():
    pass

p1 = Person()
print vars( p1.__dict__ )