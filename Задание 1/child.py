#!/usr/bin/python3
import os
import time
import sys
import random
#Stepanishcheva Nastya 11-902
pid=os.getpid()
arg=int(sys.argv[1])
print("Child program started in process with pid {0} with arg {1}".format(pid,arg))
time.sleep(arg)
print("Child program ended with pid {}".format(pid))
status= random.randint(0,1)
os._exit(status)
