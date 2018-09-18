import os, sys, time, re, pickle

r, w = os.pipe()
rc = os.fork()
if rc < 0:
    os.write(2, ("fork failed, returning %d\n" % rc).encode())
    sys.exit(1)

elif rc == 0:
    os.execve(os.getcwd(), exec.py)

else:  # parent (forked ok)
    INP = input("$ ")
    INP = INP.strip()
    List = list(INP.split(" "))
    for i in range(len(List)):
        List[i] = List[i].lower()
    with open('outfile', 'wb') as fp:
        pickle.dump(list, fp)
    childPidCode = os.wait()



