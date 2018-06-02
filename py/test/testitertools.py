#!/usr/bin/python
# -*- coding: UTF-8 -*-

import itertools

ns = itertools.repeat('A',10)

for  value in ns :
    print value


for key, group in itertools.groupby('AAABBBCCAAA'):
    # print key, list(group)
    print key, group

    for i in group :
        print i

# A <itertools._grouper object at 0x10e711d10>
# B <itertools._grouper object at 0x10e711d50>
# C <itertools._grouper object at 0x10e711d10>
# A <itertools._grouper object at 0x10e711d50>

