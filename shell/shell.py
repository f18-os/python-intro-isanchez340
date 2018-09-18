import os, sys, time, re, pickle

r, w = os.pipe()
List = []
rc = os.fork()
if rc < 0:
    os.write(2, ("fork failed, returning %d\n" % rc).encode())
    sys.exit(1)

elif rc == 0:
    args = ["exec.py"]
    os.execve("exec.py", args, os.environ)

else:  # parent (forked ok)
    INP = input("$ ")
    INP = INP.strip()
    List = list(INP.split(" "))
    for i in range(len(List)):
        List[i] = List[i].lower()
    with open('outfile.txt', 'wb') as fp:
        pickle.dump(list, fp)
    os.set_inheritable(w, True)
    os.set_inheritable(r, True)
    childPidCode = os.wait()
    os.close(w)
    r = os.fdopen(r)
    str = r.read()



