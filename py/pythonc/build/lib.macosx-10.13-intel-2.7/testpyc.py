import ctypes
so = ctypes.cdll.LoadLibrary
pyc = so("./pyc.so")

print pyc.fac(5)
