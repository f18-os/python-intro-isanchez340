#!/usr/bin/env python3
import os, sys, time, re, pickle

n = 0


with open ('outfile.txt', 'rb') as fp:
    list = pickle.load(fp)

INP = ''.join(list)
os.close(r)
w = os.fdopen(w, 'w')

str = os.system(INP)

print(str)
w.close()
sys.exit(0)
