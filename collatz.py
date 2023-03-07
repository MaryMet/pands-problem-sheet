# Task involving ifs and elses? And eilif?
# Calculation problem
# Author : Mary Metcalfe

number = []

number = int(input ("Enter a positive number : "))

def collatz(number):   #addes this in after lots of internet searching 

    while number != 1: # I had a few infinite loops before I put in this line to end at 1
        if (number % 2) == 0:
            number = (number//2)
            print (f"The number is even therefore it will be divided by 2") #print the number and then collatz
            print (f"Your answer is {number}")
        else:
            number = (number *3 +1 )
            print (f"The number  is odd there it will be multiplied by 3 and 1 added")
            print (f"Your answer is {number}")


collatz(number)

