# sroot


def newton_sqrt(number, howmany):
    approx = 0.5*number
    for i in range(howmany):
        betterapprox = 0.5 * (approx + number/approx)
        approx = betterapprox
    return betterapprox

x = float(input("Enter a number : "))

print (newton_sqrt (x, 10))

