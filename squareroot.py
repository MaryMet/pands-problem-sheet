# Getting the square root of a number
# Use the Newtonian method - not in built functions - x**5 or math.sqrt(x)
# Show I can do research!!



number = float(input("Enter a number : "))

approx_sqrt = 0.5*number
print ("Approximate Square Root is :", approx_sqrt)

more_accurate = 0.5*(approx_sqrt+number/approx_sqrt)
print ("A more accurate approximation is ", more_accurate)

while (more_accurate!=approx_sqrt):
    if approx_sqrt = 0.5*number :
     print (f"Approximate Square Root is {approx_sqrt}:")
    else:
     # more_accurate = 0.5*(approx_sqrt+number/approx_sqrt)
     print = (f"A more accuate approximation {more_accurate}")

print ("The Square root of your number is : ", more_accurate)
