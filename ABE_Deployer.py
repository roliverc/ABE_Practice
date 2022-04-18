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

def creatingDirectories(n_users):
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

    userList = ["master", "pub"] + ["user_"+str(i) for i in range(n_users)]
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
    return 

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
    return

################### KEY & ATTRIBUTE GENERATION ##################

def attributeGeneration(n_users,n_attributes):
    listAllAttributes = ["attr_"+str(i) for i in range(20)]
    userProfiles = []
    for user in range(n_users):
        chosenAttributes = random.sample(listAllAttributes,n_attributes)
        userProfiles.append(chosenAttributes)
    print(c.OK + "Generating Random Attributes and Profiles")
    return userProfiles

def profileGeneration(userProfiles):
    cmdList = []
    for i in range(n_users):
        currentProfile = userProfiles[i]
        cmdInd = "cpabe-keygen -o ../user_"+str(i)+"-dir/user_"+str(i)+"_priv pubKey msk " + " ".join(currentProfile)
        cmdList.append(cmdInd)
    count = 0
    for cmd in cmdList:
        try:
            os.system(cmd)
        except OSError:
            print(c.FAIL + "Creating user_%i's private key." % count)
            sys.exit(1)
        else:
            print(c.OK + "Creating user_%i's private key." % count)
        count += 1
    return

################### DRIVER CODE ##################

#n_users, n_attributes = [checkInput()
#n_users, n_attributes = int(n_users), int(n_attributes)
n_users, n_attributes = [int(arg) for arg in checkInput()]
creatingDirectories(n_users)
setCpabeKeys()
userProfiles = attributeGeneration(n_users,n_attributes)
profileGeneration(userProfiles)