import ctypes
so = ctypes.cdll.LoadLibrary
pyc = so("./build/lib.macosx-10.13-intel-2.7/pyc.so")

print pyc.fac(5)
