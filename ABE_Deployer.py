import os
import time
#from pytictoc import TicToc 
import sys
import random
from Color import c

# USAGE CASE EXAMPLE: [euler@fedora]~% python3 User_Generator.py 20 5
# which means that we want 20 users and 5 attributes

# ATENCIÓN
# ESTE ARCHIVO VA HASTA LA DIAPOSITVA 9 (INCLUIDA)
# A PARTIR DE LA 10: ENCRYPTION_DECRYPTION.PY

################### USER GENERATION ##################

def checkInput():
    try:
        cmd_args = sys.argv[1:]
    except OSError:
        print(c.FAIL + "Receiving arguments from terminal.")
        sys.exit(1)
    else:
        if len(cmd_args) == 2:
            print(c.OK + "Checking number of arguments passed.")
        else:
            print(c.FAIL + "Checking number of arguments passed.")
            sys.exit(1)
    return cmd_args

def creatingDirectories():
    """
    try:
        ExerciseDir = "/home/abe/ABE_CURRENT"
        os.mkdir(ExerciseDir)
    except OSError:
        print(c.FAIL + "Creating directory: %s" % ExerciseDir)
        sys.exit(1)
    else:
        print(c.OK + "Creating directory: %s" % ExerciseDir)
    """

    userList = ["master", "pub"] + ["user_"+str(i) for i in range(0,n_users)]
    userList = [user + "-dir" for user in userList] # how to improve this??

    # Obtains current working directory
    cwd = os.getcwd()
    dirs = []
    for user in userList:
        newDir = cwd + "/" + user
        dirs.append(newDir)

    for dir in dirs:
        try:
            os.mkdir(dir)
        except OSError:
            print(c.FAIL + "Creating directory: %s" % dir)
            sys.exit(1)
        else:
            print(c.OK + "Creating directory: %s" % dir)

def setCpabeKeys():
    # Now change the directory
    cwd = os.getcwd()
    os.chdir(cwd + "/master-dir")
    try:
        cmd = "cpabe-setup"
        os.system(cmd)
    except OSError:
        print(c.FAIL + "Setting up CPABE.")
        sys.exit(1)
    else:
        print(c.OK + "Setting up CPABE.")

    try:
        cmd = "cp master_key msk"
        os.system(cmd)
    except OSError:
        print(c.FAIL + "Creating Master Key and encryption parameters.")
        sys.exit(1)
    else:
        print(c.OK + "Creating Master Key and encryption parameters.")

    try:
        cmd = "for i in ../*-dir; do cp pub_key $i/pubKey; done"
        os.system(cmd)
    except OSError:
        print(c.FAIL + "Copying Public Key into the directories of all users.")
        sys.exit(1)
    else:
        print(c.OK + "Copying Public Key into the directories of all users.")

################### KEY & ATTRIBUTE GENERATION ##################

def attributeCreation():
    """
    listAllAttributes = []

    departments = ['it_dpt', 'hr_dpt'] # 1
    position = ['worker', 'executive'] # 2
    area = ['area_A', 'area_B'] # 3
    building = ['1','2'] # 4
    office = ['01','02'] # 5
    security_clearance = ['no' , 'yes']
    """
    listAllAttributes = []

################### DRIVER CODE ##################

#n_users, n_attributes = [checkInput()
#n_users, n_attributes = int(n_users), int(n_attributes)
n_users, n_attributes = [int(arg) for arg in checkInput()]
creatingDirectories()
setCpabeKeys()