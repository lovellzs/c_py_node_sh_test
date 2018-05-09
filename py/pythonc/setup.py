#!/usr/bin/python


from distutils.core import setup, Extension

pyc_module = Extension("pyc",
                       sources=['pyc.c',"pycmodule.c"],
                       include_dirs=['.'])

setup(name="pyc",
      ext_modules=[pyc_module])