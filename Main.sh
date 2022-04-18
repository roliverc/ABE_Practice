#!/bin/bash

# EXERCISE 1
echo "##### 5 USERS AND 5 ATTRIBUTES #####"
cd $HOME
mkdir EXERCISE_1
cd EXERCISE_1
python3 /home/abe/ABE_Deployer.py 5 5
python3 /home/abe/Encryption_Decryption.py 5

# EXERCISE 2
echo "##### 5 USERS AND 20 ATTRIBUTES #####"
cd $HOME
mkdir EXERCISE_2
cd EXERCISE_2
python3 /home/abe/ABE_Deployer.py 5 20
python3 /home/abe/Encryption_Decryption.py 20

# EXERCISE 3
echo "##### 20 USERS AND 5 ATTRIBUTES #####"
cd $HOME
mkdir EXERCISE_3
cd EXERCISE_3
python3 /home/abe/ABE_Deployer.py 20 5
python3 /home/abe/Encryption_Decryption.py 5

# EXERCISE 4
echo "##### 5 USERS AND 5 ATTRIBUTES #####"
cd $HOME
mkdir EXERCISE_4
cd EXERCISE_4
python3 /home/abe/ABE_Deployer.py 20 20
python3 /home/abe/Encryption_Decryption.py 20
