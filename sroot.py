# sroot


def newton_sqrt(number, howmany):  # function that uses the newtonian square root formula
    approx = 0.5*number
    for i in range(howmany):
        betterapprox = 0.5 * (approx + number/approx)
        approx = betterapprox
    return betterapprox

x = float(input("Enter a number : ")) # prompt the user to enter any number that you want the square root of

print (newton_sqrt (x, 10)) # uses the newton_sqrt function ten times

