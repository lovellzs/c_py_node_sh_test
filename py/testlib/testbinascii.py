#coding=utf-8

import StringIO
import binascii
import struct

tx ={
      "data": "02000000011f53df9d5c16c0ba92adf02d011af16decceb8da8224f3b3b3808aea902f4444010000006b483045022100d9da11c288962b1aec4594bfc05948538f1bafc94bb9beb4ab6c1b495bef718c02200fbed4af6c02c391cb5ca26eb8a182c6fffbd8357ac564802611417b5079474b0121032194d10b735d56a8bcbcd213c97314d422d002ac9d1f5d859a8ad0cc74ebf8c0fdffffff0128e3052a0100000017a914654cc28510642016cf2bf2df2e31ec9e6642f6e58776130000",
      "hash": "7dff0b69a33187eeb4b18492cee7e0c9c64cfa302928a29ad96cba5ceb86a727",
      "depends": [
      ],
      "fee": 226,
      "sigops": 2
    }
print  binascii.unhexlify(tx['data'])
print  binascii.hexlify(tx['data'])

print  "%064x" % 0x7dff0b69a33187eeb4b18492cee7e0c9c64cfa302928a29ad96cba5ceb86a727
print "================="

s = 'hello'

aa = binascii.b2a_hex(s)
bb = binascii.a2b_hex(aa)
print aa,type(aa)
print bb # 68656c6c6f

aa = binascii.hexlify(s)
bb = binascii.unhexlify(aa)
print aa,type(aa)
print bb # 68656c6c6f










