import os
import sys
import random
from Color import c
import string

# USAGE CASE EXAMPLE: [euler@fedora]~% python3 User_Generator.py 20 5
# which means that we want 20 users and 5 attributes

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

# USAGE CASE EXAMPLE: [euler@fedora]~% python3 Encryption_Decryption.py 5
# which means that we want 20 users and 5 attributes

# ATENCIÓN
# ESTE ARCHIVO VA DESDE LA DIAPOSITVA 10 (INCLUIDA)
# ANTES DE LA 10: ABE_Deployer.py

def downloadingPDF():
    # Now change the directory
    #os.chdir("/home/abe/EXERCISE_1/pub-dir")
    cmd_1 = "cd /home/abe/"
    os.system(cmd_1)
    try:
        environment = os.environ
        counter = environment['counter']
        cmd_2 = "wget -P /home/abe/EXERCISE_"+str(counter)+"/pub-dir https://download.support.xerox.com/pub/docs/FlowPort2/userdocs/any-os/en/fp_dc_setup_guide.pdf"
        #cmd = "wget https://download.support.xerox.com/pub/docs/FlowPort2/userdocs/any-os/en/fp_dc_setup_guide.pdf"
        #cmd_2 = "for i in ../EXERCISE_*/; do wget -P $i/pub-dir https://download.support.xerox.com/pub/docs/FlowPort2/userdocs/any-os/en/fp_dc_setup_guide.pdf; done"
        os.system(cmd_2)
    except OSError:
        print(c.FAIL + "Downloading PDF file.")
        sys.exit(1)
    else:
        print(c.OK + "Downloading PDF file.")

def encipherForUsers(userProfiles):
    cmdList = []
    environment = os.environ
    counter = environment['counter']
    os.chdir("/home/abe/EXERCISE_"+str(counter)+"/pub-dir")
    for i in range(len(userProfiles)):
        currentProfile = userProfiles[i]
        pol = " and ".join(currentProfile)
        cmdInd = f'echo "{pol}" | cpabe-enc -k pubKey fp_dc_setup_guide.pdf -o ./encPdf{i}.cpabe '
        cmdList.append(cmdInd)
    count = 0
    for cmd in cmdList:
        try:
            os.system(cmd)
            #cmd_2 = "exit"
            #os.system(cmd_2)
        except OSError:
            print(c.FAIL + "Enciphering the pdf file with user_%i's attributes." % count)
            sys.exit(1)
        else:
            print(c.OK + "Enciphering the pdf file with user_%i's attributes." % count)
        count += 1
    return

def encipherForUserZero(userProfiles):
    environment = os.environ
    counter = environment['counter']
    os.chdir("/home/abe/EXERCISE_"+str(counter)+"/pub-dir")
    userZeroProfile = userProfiles[0]
    print(userZeroProfile)
    pol = " and ".join(userZeroProfile)
    cmd = f'echo "{pol}" | cpabe-enc -k pubKey fp_dc_setup_guide.pdf -o ./encPdf0.cpabe '
    try:
        os.system(cmd)
    except OSError:
        print(c.FAIL + "Encrypting the pdf file with user_0's attributes.")
        sys.exit(1)
    else:
        print(c.OK + "Encrypting the pdf file with user_0's attributes.")
    return

def decipherForUsers():
    pass

def decipherForUserZero():
    environment = os.environ
    counter = environment['counter']
    os.chdir("/home/abe/EXERCISE_"+str(counter)+"/user_0-dir")
    cmd = "cpabe-dec -k -o decPdf0.pdf pubKey user_0_priv ../pub-dir/encPdf0.cpabe"
    try:
        os.system(cmd)
    except OSError:
        print(c.FAIL + "Decrypting the pdf file encrypted with user_0's private key.")
        sys.exit(1)
    else:
        print(c.OK + "Decrypting the pdf file encrypted with user_0's private key.")
    return

def encDecLoopUserZero():
    count = 1
    for rep in range(20):
        try:
            encipherForUserZero(userProfiles)
            decipherForUserZero()
        except OSError:
            print(c.FAIL + "Encrypting and Decrypting for user_0. Round %i" % count)
            sys.exit(1)
        else:
            print(c.OK + "Encrypting and decrypting for user_0. Round %i" % count)
        count += 1
    return

if __name__ == "__main__":
    n_users, n_attributes = [int(arg) for arg in cmdReturn()]
    creatingDirectories(n_users)
    setCpabeKeys()
    userProfiles = attributeGeneration(n_users, n_attributes)
    profileGeneration(userProfiles)
    downloadingPDF()
    encipherForUserZero(userProfiles)
    decipherForUserZero()

    #userProfiles = attributeGeneration(n_users,n_attributes)
    #profileGeneration(userProfiles)