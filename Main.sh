#!/bin/bash

counter=0

# EXERCISE 1
echo "##### 5 USERS AND 5 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_1
cd EXERCISE_1
python3 /home/abe/Encryption_Decryption.py 5 5
#(time python3 /home/abe/Encryption_Decryption.py 5 5) 2> time.txt

# EXERCISE 2
echo "##### 20 USERS AND 5 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_2
cd EXERCISE_2
python3 /home/abe/Encryption_Decryption.py 20 5
#(time python3 /home/abe/Encryption_Decryption.py 20 5) 2> time.txt

# EXERCISE 3
echo "##### 5 USERS AND 20 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_3
cd EXERCISE_3
python3 /home/abe/Encryption_Decryption.py 5 20
#(time python3 /home/abe/Encryption_Decryption.py 5 20) 2> time.txt

# EXERCISE 4
echo "##### 20 USERS AND 20 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_4
cd EXERCISE_4
python3 /home/abe/Encryption_Decryption.py 20 20
#(time python3 /home/abe/Encryption_Decryption.py 20 20) 2> time.txt