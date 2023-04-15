# writing a module
# square root using the newtonian method
# Author: MAry Metcalfe

def newton_sqrt(number, howmany):
    approx = 0.5*number
    for i in range(howmany):
        betterapprox = 0.5 * (approx + number/approx)
        approx = betterapprox
    return betterapprox

x = float(input("Enter a number : ")) # define a number that you want to get the square root of

print (newton_sqrt (x, 2)) # complete the above 2 times - gives a loose approximation of the xs square root
print (newton_sqrt (x, 4)) # complete the above 4 times - gives a better approximation of xs square root
print (newton_sqrt (x, 6)) # complete the above 6 times - even closer to actual square root
print (newton_sqrt (x, 10)) # closer again !!

 #sroot - second method


#def newton_sqrt(number, howmany):  # function that uses the newtonian square root formula
    #approx = 0.5*number
    #for i in range(howmany):
     #   betterapprox = 0.5 * (approx + number/approx)
      #  approx = betterapprox
    #return betterapprox
#x = float(input("Enter a number : ")) # prompt the user to enter any number that you want the square root of
#print (newton_sqrt (x, 10)) # uses the newton_sqrt function ten times
