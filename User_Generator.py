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
    print(c.FAIL + "Receiving arguments from terminal.")
else:
    if len(cmd_args) == 2:
        print(c.OK + "Checking number of arguments passed.")
    else:
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
    print(c.FAIL + "Creating directory: %s" % ExerciseDir + " .")
else:
    print(c.OK + "Creating directory: %s" % ExerciseDir + " -")

userList = ["master", "pub"] + ["user_"+str(i) for i in range(0,n_users-1)]
userList = [user + "-dir" for user in userList] # how to improve this??

dirs = []
for user in userList:
    newDir = "/home/abe/ABE_CURRENT/" + user
    dirs.append(newDir)

for dir in dirs:
    try:
        os.mkdir(dir)
    except OSError:
        print(c.FAIL + "Creating directory: %s" % dir + " .")
    else:
        print(c.OK + "Creating directory: %s" % dir + " .")

pubDir = "/home/abe/ABE_CURRENT/pub-dir"
try:
    pubDir = "/home/abe/ABE_CURRENT/pub-dir"
    os.mkdir(pubDir)
except OSError:
    print(c.FAIL + "Creating directory: %s" % pubDir + " .")
else:
    print(c.OK + "Creating directory: %s" % pubDir + " .")

# Now change the directory
os.chdir("/home/abe/ABE_CURRENT/master-dir")
try:
    cmd_1 = "cpabe-setup"
    os.system(cmd_1)
except OSError:
    print(c.FAIL + "Setting up CPABE.")
else:
    print(c.OK + "Settip up CPABE.")

try:
    cmd_2 = "cp master_key msk"
    os.system(cmd_2)
except OSError:
    print(c.FAIL + "Creating Master Key and encryption parameters.")
else:
    print(c.OK + "Creating Master Key and encryption parameters.")

try:
    cmd_3 = "for i in ../*-dir; do cp pub_key $i/pubKey; done"
    os.system(cmd_3)
except OSError:
    print(c.FAIL + "Copying Public Key into the directories of all users.")
else:
    print(c.OK + "Copying Public Key into the directories of all users.")

# NEXT GOAL: TURN ALL THESE BLOCKS INTO FUNCTIONS
# AND IMPLEMENT ATTRIBUTE PROFILE CREATION
# AUTOMATIZING IT