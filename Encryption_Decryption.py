import os
import time
#from pytictoc import TicToc 
import sys
import random
from Color import c

# USAGE CASE EXAMPLE: [euler@fedora]~% python3 Encryption_Decryption.py 5
# which means that we want 20 users and 5 attributes

# ATENCIÓN
# ESTE ARCHIVO VA DESDE LA DIAPOSITVA 10 (INCLUIDA)
# ANTES DE LA 10: ABE_Deployer.py

def checkInput():
    try:
        cmd_args = sys.argv[1:]
    except OSError:
        print(c.FAIL + "Receiving arguments from terminal.")
        sys.exit(1)
    else:
        if len(cmd_args) == 1:
            print(c.OK + "Checking number of arguments passed.")
        else:
            print(c.FAIL + "Checking number of arguments passed.")
            sys.exit(1)
    return cmd_args

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

################### DRIVER CODE ##################

n_attributes = [int(arg) for arg in checkInput()]
downloadingPDF()