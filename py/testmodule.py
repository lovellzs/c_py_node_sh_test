#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mymodule,testfunction

mymodule.print_name('张三');

content = dir(mymodule)
 
print content;
print mymodule.__file__;
print mymodule.__name__;