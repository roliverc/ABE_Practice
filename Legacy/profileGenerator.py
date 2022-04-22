import os
import profile
import time
#from pytictoc import TicToc 
import sys
import random
from Color import c
from ABE_Deployer import n_users, n_attributes

import string
#n_attributes

def attributeGeneration(n_users,n_attributes):
    listAllAttributes = ["attr_"+str(i) for i in range(19)]
    #listAllAttributes = ["attr_"+str(i) for i in range(20)]
    userProfiles = []
    for user in range(n_users):
        chosenAttributes = random.sample(listAllAttributes,n_attributes-1)
        #chosenAttributes = random.sample(listAllAttributes,n_attributes)
        userProfiles.append(chosenAttributes)
    print(c.OK + "Generating Random Attributes and Profiles")
    return userProfiles

def profileGeneration(userProfiles):
    cmdList = []
    for i in range(n_users):
        alphabet = list(string.ascii_lowercase[0:n_users])
        userProfiles[i].append(alphabet[i])
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
if __name__ == "__main__":
    userProfiles = attributeGeneration
    profileGeneration(userProfiles)