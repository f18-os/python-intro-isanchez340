import os, sys, time, re, pickle

with open ('outfile.txt', 'rb') as fp:
    list = pickle.load(fp)

INP = ''.join(list)
os.close(r)
w = os.fdopen(w, 'w')

str = os.system(INP)

print(str)
w.close()
sys.exit(0)