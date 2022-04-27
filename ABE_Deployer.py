import os
import sys
import random
from Color import c

# ATENCIÓN
# ESTE ARCHIVO VA HASTA LA DIAPOSITVA 9 (INCLUIDA)
# A PARTIR DE LA 10: ENCRYPTION_DECRYPTION.PY

################### USER GENERATION ##################

def cmdReturn():
    cmd_args = sys.argv[1:]
    return cmd_args

def creatingDirectories(n_users):
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
    listAllAttributes = ["attr_"+str(i) for i in range(1000)]
    #listAllAttributes = ["attr_"+str(i) for i in range(20)]
    userProfiles = []
    for user in range(n_users):
        chosenAttributes = random.sample(listAllAttributes,n_attributes-1)
        userProfiles.append(chosenAttributes)
    print(c.OK + "Generating Random Attributes and Profiles")
    return userProfiles

def profileGeneration(userProfiles):
    cmdList = []
    for i in range(n_users):
        unique = "a"+str(i)
        #alphabet = list(string.ascii_lowercase[0:n_users])
        userProfiles[i].append(unique)
        currentProfile = userProfiles[i]
        print(currentProfile)
        #currentProfile = userProfiles[i]
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
n_users, n_attributes = [int(arg) for arg in cmdReturn()]
creatingDirectories(n_users)
setCpabeKeys()
userProfiles = attributeGeneration(n_users,n_attributes)
profileGeneration(userProfiles)