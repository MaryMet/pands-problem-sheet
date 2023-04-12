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