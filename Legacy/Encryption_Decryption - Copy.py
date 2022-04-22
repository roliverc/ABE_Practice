import os
import sys
from Color import c
from ABE_Deployer import userProfiles


# USAGE CASE EXAMPLE: [euler@fedora]~% python3 Encryption_Decryption.py 5
# which means that we want 20 users and 5 attributes

# ATENCIÓN
# ESTE ARCHIVO VA DESDE LA DIAPOSITVA 10 (INCLUIDA)
# ANTES DE LA 10: ABE_Deployer.py

def cmdReturn2():
    cmd_args2 = sys.argv[1:]
    return cmd_args2

"""
def checkInput2():
    try:
        cmd_args = sys.argv[1:]
        print(cmd_args)
    except OSError:
        print(cmd_args)
        print(c.FAIL + "Receiving arguments from terminal.")
        sys.exit(1)
    else:
        if len(cmd_args) == 1:
            print(cmd_args)
            print(c.OK + "Checking number of arguments passed.")
        else:
            print(cmd_args)
            print(c.FAIL + "Checking number of arguments passed." + str(len(cmd_args)))
            sys.exit(1)
    return cmd_args
"""

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
    while count <= 20:
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

################### DRIVER CODE ##################

if __name__ == "__main__":
    n_users, n_attributes = [int(arg) for arg in cmdReturn2()]
    #environment = os.environ
    #userProfiles = environment['userProfiles']
    #print(len(n_attributes))
    downloadingPDF()
    #encipherForUsers(userProfiles)
    #decipherForUsers()
    #encipherForUserZero(userProfiles)
    #decipherForUserZero()
    encDecLoopUserZero()