# another try
# Author: MAry Metcalfe

number = float(input("Enter a number : "))
approx_sqrt = 0.5*number
print (f"Approximate Square Root is :{approx_sqrt}")

#for approx_sqrt in number:
   # more_accurate = 0.5*(approx_sqrt+number/approx_sqrt)
    #print ("A more accurate approximation is ", more_accurate)
 
more_accurate = 0.5* (approx_sqrt + number/approx_sqrt)

while more_accurate != approx_sqrt :
    print (f"A more accurate square root is: {more_accurate} ")

    if more_accurate == approx_sqrt:
        print (f"The square root of {number} is : {more_accurate}")