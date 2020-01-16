#Prompt the user for a number
#compare that number to a predfined value
#If the numbers match, tell the user ther're a mind reader
#If they don't match, tell the user "thanks for playing"

import random

user_input = int(input("What number am I thinking of: "))

MAGICNUMBER = 7

if user_input <= MAGICNUMBER:
    print("ARE YOU A MIND READER??? MINDFREAK!!")
else:
    print("Thanks for playing, that not correct")



