#coding=utf-8

import struct


age = 32
lAge = struct.pack('>L', age)

print lAge

age, = struct.unpack('>L', lAge)

print age
