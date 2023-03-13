# Week 07
# Program to count number of e's in a text file
# My text file is called ecount.txt
# Author : Mary Metcalfe

import sys

filename = sys.argv[0]

def count_e ():
    file = open ("ecount.txt")
    content = file.read()
    amounts = list("Ee")
    count = 0

    for amount in content:
        if amount in amounts:
            count+=1

    return (count)
print (f"Total number of es in file are: {count_e()}")
