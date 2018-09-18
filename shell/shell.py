import os, sys, time, re

r, w = os.pipe()
rc = os.fork()
if rc < 0:
    os.write(2, ("fork failed, returning %d\n" % rc).encode())
    sys.exit(1)


while 0:
    INP = input("$ ")

