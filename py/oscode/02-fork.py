import os
import time

ret = os.fork()
if ret==0:
    a = 0
    while a <3:
        print("----1---")
        time.sleep(1)
        a+=1
else:
    b = 0
    while b<3:
        print("----2---")
        time.sleep(1)
        b+=1

print "========"