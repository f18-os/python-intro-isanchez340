#!/usr/bin/env python3
import os, sys, time, re, pickle
INP = ""
while INP is not "exit":
    INP = ""
    r, w = os.pipe()         #creates pipe
    for f in (r, w):
        os.set_inheritable(f, True)

    rc = os.fork()          #fork
    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" % rc).encode())
        sys.exit(1)

    elif rc == 0:
        INP = input('$ ')
        if INP == "exit":
            os.close(1)  # redirect child's stdout
            os.dup(w)
            for fd in (r, w):
                os.close(fd)
            print(1)
            sys.exit(0)
        try:
            INP = os.system(INP)                     #command
        except:
            os.close(1)  # redirect child's stdout
            os.dup(w)
            for fd in (r, w):
                os.close(fd)
            print("command not found")
            os.close(0)
            sys.exit(0)

        os.close(1)   # redirect child's stdout
        os.dup(w)
        for fd in (r, w):
            os.close(fd)
        print(INP)
        os.close(0)
        sys.exit(0)

    else:  # parent (forked ok)
        childPidCode = os.wait()
        os.close(w)
        r = os.fdopen(r)
        str = r.read()          #saves pipe info to str
        if str == 1:
            sys.exit(0)

        print(str)              #prints str



