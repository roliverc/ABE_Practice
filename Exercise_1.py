import os
import time
from pytictoc import TicToc
#hey
t = TicToc()

try:
    ExerciseDir = "/home/abe/EXERCISE_1"
    os.mkdir(ExerciseDir)
except OSError:
    print("ERROR CREATING DIRECTORY: /home/abe/EXERCISE_1")
else:
    print("DIRECTORY CREATED: /home/abe/EXERCISE_1")

userList = ["master-dir", "user_1-dir", "user_2-dir", "user_3-dir", "user_4-dir", "user_5-dir"]
dirs = []
for user in userList:
    newDir = "/home/abe/EXERCISE_1/" + user
    dirs.append(newDir)

for dir in dirs:
    try:
        os.mkdir(dir)
    except OSError:
        print("ERROR CREATING DIRECTORY: %s" % dir)
    else:
        print("DIRECTORY CREATED: %s" % dir)

pubDir = "/home/abe/EXERCISE_1/pub-dir"
try:
    pubDir = "/home/abe/EXERCISE_1/pub-dir"
    os.mkdir(pubDir)
except OSError:
    print("ERROR CREATING DIRECTOR: %s" % dir)
else:
    print("DIRECTORY CREATED: %s" % dir)

# Now change the directory
os.chdir("/home/abe/EXERCISE_1/master-dir")
try:
    cmd_1 = "cpabe-setup"
    os.system(cmd_1)
except OSError:
    print("ERROR CPABE-SETUP")
else:
    print("CPABE SET UP SUCCESSFULLY")

try:
    cmd_2 = "cp master_key msk" 
    os.system(cmd_2)
except OSError:
    print("ERROR CREATE MASTER KEY AND ENCRYPTION PARAMETERS")
else:
    print("MASTER KEY AND ENCRYPTION PARAMETERS CREATED SUCCESSFULLY")

try:
    cmd_3 = "for i in ../*-dir; do cp pub_key $i/pubKey; done"
    os.system(cmd_3)
except OSError:
    print("ERROR COPYING PUBKEY INTO DIRECTORIES OF ALL USERS")
else:
    print("PUBKEY COPIED SUCCESSFULLY TO ALL USERS")

"""Attributes that we will use: department, position,area, building, office
Departments -> it_dpt, hr_dpt, call_dpt, fin_dpt, markt_dpt
Position -> ceo, intern, executive, worker, customer
Area -> area_A, area_B, area_C, area_D, area_E
Building -> 1,2,3,4,5
Office -> 01, 02, 03, 04, 05
"""

cmd_4 = [
"cpabe-keygen -o ../user_1-dir/user_1_priv pubKey msk \
it_dpt ceo \
area_C 'building = 2' 'office = 02'",

"cpabe-keygen -o ../user_2-dir/user_2_priv pubKey msk \
fin_dpt intern \
area_E 'building = 4' 'office = 04'", 

"cpabe-keygen -o ../user_3-dir/user_3_priv pubKey msk \
markt_dpt executive \
area_B 'building = 3' 'office = 03'",

"cpabe-keygen -o ../user_4-dir/user_4_priv pubKey msk \
rh_dpt worker area_D 'building = 1' \
'office = 05'",

"cpabe-keygen -o ../user_5-dir/user_5_priv pubKey msk \
rh_dpt customer area_D 'building = 1' \
'office = 02'"]

count = 0
for keygen in cmd_4:
    try:
        os.system(keygen)
        count += 1
    except OSError:
        print("ERROR CREATING PRIVATE KEY FROM USER %d" % count)
    else:
        print("PRIVATE KEY FOR USER %d SUCCESSFULLY CREATED" % count)
    
# Now change the directory
os.chdir("/home/abe/EXERCISE_1/pub-dir")

try:
    cmd_5 = "wget https://download.support.xerox.com/pub/docs/FlowPort2/userdocs/any-os/en/fp_dc_setup_guide.pdf"
    #cmd_5 = "mv /home/abe/MergedPDF.pdf /home/abe/EXERCISE_1/pub-dir/MergedPDF.pdf"
    os.system(cmd_5)
except OSError:
    print("ERROR PAGE NOT FOUND OR NOT ACCESSIBLE. CHECK YOUR INTERNET CONNECTION")
    #print("ERROR MOVING /home/abe/merged.pdf TO /home/abe/EXERCISE_1/pub-dir/MergedPDF.pdf")
else:
    print("PDF FILE SUCCESFULLY DOWLOADED (5 MB)")
    #print("SUCCESSFULLY MOVED /home/abe/merged.pdf TO /home/abe/EXERCISE_1/pub-dir/MergedPDF.pdf")

#Let us measure the time

startTime=time.time()
t.tic()

try:
    cmd_6 = "cpabe-enc -k pubKey fp_dc_setup_guide.pdf ceo"
    os.system(cmd_6)
except OSError:
    print("ERROR FIRST ENCRYPTION STEP")
else:
    print("FIRST ENCRYPTION STEP PASSED")

try:
    cmd_7 = "exit"
    os.system(cmd_7)
except OSError:
    print("ERROR SECOND ENCRYPTION STEP")
else:
    print("SECOND ENCRYPTION STEP PASSED")

try:
    cmd_8 = "mv fp_dc_setup_guide.pdf.cpabe ceo.cpabe"
    os.system(cmd_8)
except OSError:
    print("ERROR RENAMING FILE FROM fp_dc_setup_guide.pdf.cpabe  TO ceo.cpabe")
else:
    print("FILE SUCCESSFULLY RENAMED FROM fp_dc_setup_guide.pdf.cpabe  TO ceo.cpabe")

os.chdir("../user_1-dir")

try:
    cmd_9 = "cpabe-dec -k -o fp_dc_setup_guide.pdf pubKey user_1_priv ../pub-dir/ceo.cpabe"
    os.system(cmd_9)
except OSError:
    print("ERROR DECRYPTON ceo.cpabe")
else:
    print("DECRYPTION ceo.cpabe PASSED")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
t.toc()
