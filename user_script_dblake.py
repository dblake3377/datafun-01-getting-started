"""
# Purpose: This script will produce basic statistics over the user's input 

Author: Desiree Blake

"""

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

print("Monthly Books Read Statistics")

book1 = input("Please enter book 1's rating:")
book2 = input("Please enter book 2's rating")
book3 = input("Please enter book 3's rating")

"""This converts user given scores into values"""
int1 = int(book1)
int2 = int(book2)
int3 = int(book3)

"""This combines total scores into a list"""
scores = (int1, int2, int3) 

"""This finds the mimimum score given"""
minimum = int1
if int2 < minimum: 
    miniumum = int2
if int3 < minimum:
    minimum = int3     

print('minimum score is', minimum)

"""This finds the maximum score given"""
max(int1, int2, int3)

print('maximum score is', max)

"""This finds the average"""
average = sum / 3

print('average score is', average)


# Use built-in open() function to read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())