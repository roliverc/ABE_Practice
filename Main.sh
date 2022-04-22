#!/bin/bash

counter=0

# EXERCISE 1
echo "##### 5 USERS AND 5 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_1
cd EXERCISE_1
#python3 /home/abe/ABE_Deployer.py 5 5
time python3 /home/abe/Encryption_Decryption.py 5 5

# EXERCISE 2
echo "##### 5 USERS AND 20 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_2
cd EXERCISE_2
#python3 /home/abe/ABE_Deployer.py 5 20
time python3 /home/abe/Encryption_Decryption.py 5 20

# EXERCISE 3
echo "##### 20 USERS AND 5 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_3
cd EXERCISE_3
#python3 /home/abe/ABE_Deployer.py 20 5
time python3 /home/abe/Encryption_Decryption.py 20 5

# EXERCISE 4
echo "##### 20 USERS AND 20 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_4
cd EXERCISE_4
#python3 /home/abe/ABE_Deployer.py 20 20
time python3 /home/abe/Encryption_Decryption.py 20 20

# EXERCISE 5
echo "##### 5 USERS AND 40 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_5
cd EXERCISE_5
#python3 /home/abe/ABE_Deployer.py 5 40
time python3 /home/abe/Encryption_Decryption.py 5 40

# EXERCISE 6
echo "##### 40 USERS AND 5 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_6
cd EXERCISE_6
#python3 /home/abe/ABE_Deployer.py 40 5
time python3 /home/abe/Encryption_Decryption.py 40 5

# EXERCISE 7
echo "##### 40 USERS AND 40 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_7
cd EXERCISE_7
#python3 /home/abe/ABE_Deployer.py 40 40
time python3 /home/abe/Encryption_Decryption.py 40 40

# EXERCISE 8
echo "##### 1000 USERS AND 20 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_8
cd EXERCISE_8
#python3 /home/abe/ABE_Deployer.py 1000 20
time python3 /home/abe/Encryption_Decryption.py 1000 20

# EXERCISE 9
echo "##### 20 USERS AND 1000 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_9
cd EXERCISE_9
#python3 /home/abe/ABE_Deployer.py 20 1000
time python3 /home/abe/Encryption_Decryption.py 20 1000