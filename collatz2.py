# Collatz try 2
# will use while and appends to create the list of numbers until 1
# combination of whiles, ifs and elses
# Author : MAry Metcalfe


number = int(input("Please enter number :"))

def collatz(number):
    

   
    while number !=1:
        
        if number % 2 == 0:
         number = number//2
         print(number)
        

        else :
            number = 3*number+1
            print(number)
           

collatz(number)



