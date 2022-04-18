# Python program to demonstrate
# command line arguments
 
import cmd
import os
import time
#from pytictoc import TicToc 
import sys

class c:
    OK = "[" + '\033[92m' + " OK " + '\033[0m' +"] "
    FAIL = "[" + '\033[91m' + " FAIL " + '\033[0m' + "] " 

# USAGE CASE EXAMPLE: [euler@fedora]~% python3 User_Generator.py 20 5
# which means that we want 20 users and 5 attributes

try:
    cmd_args = sys.argv[1:]
except OSError:
    #print("[" + color.FAIL + "FAILED" + c.ENDC + "]" + " Receiving arguments from terminal.")
    print(c.FAIL + "Receiving arguments from terminal.")
else:
    if len(cmd_args) == 2:
        #print("[" + color.OK + "OK" + c.ENDC + "]" + " Checking number of arguments passed.")
        print(c.OK + "Checking number of arguments passed.")
    else:
        #print("[" + color.FAIL + "FAILED" + c.ENDC + "]" + " Checking number of arguments passed.")
        print(c.FAIL + "Checking number of arguments passed.")
        sys.exit(1)

# Number of users
n_users = int(cmd_args[0])

# Number of attributes
n_attributes = int(cmd_args[1])

try:
    ExerciseDir = "/home/abe/ABE_CURRENT"
    os.mkdir(ExerciseDir)
except OSError:
    print(c.FAIL + "Creating directory: %s" % ExerciseDir)
else:
    print(c.OK + "Creating directory: %s" % ExerciseDir)

userList = ["master", "pub"] + ["user_"+str(i) for i in range(0,n_users-1)]
userList = [user + "-dir" for user in userList]
print(userList)


