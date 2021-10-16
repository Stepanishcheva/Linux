#!/usr/bin/python3
import os
import random
import sys
# Stepanishcheva Nastya 11-902
n=sys.argv[1]
for i in range(0, int(n)):
    pid=os.fork()
    if pid>0:
        r=os.wait()
        print("Child process with pid {0} ended. Exit status {1}\n".format(r[0],r[1]))
    else:
        arg1=random.randint(5,10)
        argv=["child.py",arg1]
        os.execl("child.py","child.py", str(arg1), )
