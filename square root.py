# another try
# Author: MAry Metcalfe

number = float(input("Enter a number : "))
approx_sqrt = 0.5*number
print (f"Approximate Square Root is :{approx_sqrt}")

#for approx_sqrt in number:
   # more_accurate = 0.5*(approx_sqrt+number/approx_sqrt)
    #print ("A more accurate approximation is ", more_accurate)

 
more_accurate = 0.5* (approx_sqrt + number/approx_sqrt)
print (f"A more accurate square root is: {more_accurate} ")

while (number!=more_accurate*more_accurate):
    more_accurate = 0.5* (more_accurate + number/more_accurate)
    print (more_accurate)
    break
#while (more_accurate != approx_sqrt) : # I dont know what to put in to get it to repeatt above steps
   # more_accurate == approx_sqrt
   # more_accurate == 0.5* (approx_sqrt + number/approx_sqrt)

print (f"The Square Root is {more_accurate}")

    #else :
       # print (f"The Square root of {number} is : {square root}")
  

    #if more_accurate == approx_sqrt:
       # break
       # print (f"The square root of {number} is : {more_accurate}")