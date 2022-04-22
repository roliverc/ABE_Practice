#!/bin/bash

counter=0

# EXERCISE 1
echo "##### 5 USERS AND 5 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_1
cd EXERCISE_1
(time python3 /home/abe/Encryption_Decryption.py 5 5) 2> time.txt

# EXERCISE 2
echo "##### 5 USERS AND 20 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_2
cd EXERCISE_2
(time python3 /home/abe/Encryption_Decryption.py 5 20) 2> time.txt

# EXERCISE 3
echo "##### 20 USERS AND 5 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_3
cd EXERCISE_3
(time python3 /home/abe/Encryption_Decryption.py 20 5) 2> time.txt

# EXERCISE 4
echo "##### 20 USERS AND 20 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_4
cd EXERCISE_4
(time python3 /home/abe/Encryption_Decryption.py 20 20) 2> time.txt

# EXERCISE 5
echo "##### 5 USERS AND 40 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_5
cd EXERCISE_5
(time python3 /home/abe/Encryption_Decryption.py 5 40) 2> time.txt

# EXERCISE 6
echo "##### 40 USERS AND 5 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_6
cd EXERCISE_6
(time python3 /home/abe/Encryption_Decryption.py 40 5) 2> time.txt

# EXERCISE 7
echo "##### 40 USERS AND 40 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_7
cd EXERCISE_7
(time python3 /home/abe/Encryption_Decryption.py 40 40) 2> time.txt

# EXERCISE 8
echo "##### 1000 USERS AND 20 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_8
cd EXERCISE_8
(time python3 /home/abe/Encryption_Decryption.py 1000 20) 2> time.txt

# EXERCISE 9
echo "##### 20 USERS AND 1000 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_9
cd EXERCISE_9
(time python3 /home/abe/Encryption_Decryption.py 20 1000) 2> time.txt

# EXERCISE 10
echo "##### 1000 USERS AND 1000 ATTRIBUTES #####"
let counter++
export counter
cd $HOME
mkdir EXERCISE_10
cd EXERCISE_10
(time python3 /home/abe/Encryption_Decryption.py 1000 1000) 2> time.txt