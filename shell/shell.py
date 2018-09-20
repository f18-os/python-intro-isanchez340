#!/usr/bin/env python3
import os, sys, time, re, pickle

r, w = os.pipe()
rc = os.fork()
INP = ""
if rc < 0:
    os.write(2, ("fork failed, returning %d\n" % rc).encode())
    sys.exit(1)

elif rc == 0:
    os.close(r)
    w = os.fdopen(w, 'w')
    str = os.system(INP)
    print(str)
    w.close()
    sys.exit(0)

else:  # parent (forked ok)
    INP = input('$ ')
    INP = INP.strip()
    os.set_inheritable(w, True)
    os.set_inheritable(r, True)
    childPidCode = os.wait()
    os.close(w)
    r = os.fdopen(r)
    str = r.read()
    print(os.system('ls'))



