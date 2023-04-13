# writing a module
# square root using the newtonian method
# Author: MAry Metcalfe

def newton_sqrt(number, howmany):
    approx = 0.5*number
    for i in range(howmany):
        betterapprox = 0.5 * (approx + number/approx)
        approx = betterapprox
    return betterapprox
print (newton_sqrt (9, 2))
print (newton_sqrt (9, 4))
print (newton_sqrt (9, 6))

 #sroot - second method


#def newton_sqrt(number, howmany):  # function that uses the newtonian square root formula
    #approx = 0.5*number
    #for i in range(howmany):
     #   betterapprox = 0.5 * (approx + number/approx)
      #  approx = betterapprox
    #return betterapprox
#x = float(input("Enter a number : ")) # prompt the user to enter any number that you want the square root of
#print (newton_sqrt (x, 10)) # uses the newton_sqrt function ten times
