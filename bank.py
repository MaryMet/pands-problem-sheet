# bank.py
# author : Mary Metcalfe
# messing with banks and money
 
print ("we are going to add two numbers together") # what I want to happen
amount1 = input("Please enter first amount in cents: ") # using decimal place to show euros and cents
amount2 = input("Please enter second amount in cents: ")


ans = float(amount1) + float(amount2) #takes into account the decimals. Adds the totals together

print ("The sum of amount1 and amount2 is: €" + str(ans)) # add the two value to give an answer in eros and cents

