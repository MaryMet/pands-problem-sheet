# bank.py
# author : Mary Metcalfe
# messing with banks and money
 
print ("We are going to add two numbers together") # what I want to happen

amount1 = input("Please enter first amount in euros and cents: ") # using decimal place to show euros and cents
amount2 = input("Please enter second amount in euros and cents: ")

ans = float(amount1) + float(amount2) #takes into account the decimals. Adds the totals together

print ("The sum of amount1 and amount2 is: €" + str(ans)) # add the two value to give an answer in eros and cents

# Without using floats?

x = input("What is your first number: ")
y = input("What is the 2nd number: ")

sum = int(x) + int(y)
print ("the sum is: ", sum) # cannot put in decimal places with this code

import decimal # a suggestion that I saw on teclado.com

a = input("What is your first number: ")
b = input ("What is your second number: ")

addition = (a) + (b)

print ("Your first number added to your second number is: ", addition) # stange output

