# Week 07
# Program to count number of e's in a text file - using arguments in command prompts
# My text file is called ecount.txt
# Author : Mary Metcalfe

import sys # I used some resources on youtube for this - but i am still unsure what this actually does - see readme for referencing

filename = sys.argv[0]

def count_e (): # created a function that counts the number of es
    file = open ("ecount.txt")
    content = file.read()
    amounts = list("Ee") # count upper and lower case es
    count = 0

    for amount in content:
        if amount in amounts:
            count+=1

    return (count)
print (f"Total number of es in file are: {count_e()}") # Ic reated my own text file -count e but you can sub in whatever text file that you wish
