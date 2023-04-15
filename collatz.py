# Collatz 
# Using while and appends to create the list of numbers until 1
# combination of whiles, ifs and elses
# Author : MAry Metcalfe


number = int(input("Please enter number :"))

def collatz(number):
     while number !=1: 
        if number % 2 == 0:
         number = number//2
         print(number, end = ",") # end = "," made the output horizontal rather than vertical as per feedback recieved. Inspired by https://stackoverflow.com/questions/18458024/cant-figure-out-how-to-print-horizontally-in-python
        

        else :
            number = 3*number+1
            print(number, end = ",")
           

collatz(number)


# Task involving ifs and elses? And eilif?
# Calculation problem
# Author : Mary Metcalfe

#number = []
#number = int(input ("Enter a positive number : "))

#def collatz(number):   #addes this in after lots of internet searching 
   # while number != 1: # I had a few infinite loops before I put in this line to end at 1
        #if (number % 2) == 0:
            #number = (number//2)
           # print (f"The number is even therefore it will be divided by 2") #print the number and then collatz
           # print (f"Your answer is {number}")
       # else:
            #number = (number *3 +1 )
           # print (f"The number  is odd there it will be multiplied by 3 and 1 added")
            #print (f"Your answer is {number}")

#collatz(number,)

 #Collatz try 2
 #will use while and appends to create the list of numbers until 1
# combination of whiles, ifs and elses
# Author : MAry Metcalfe
