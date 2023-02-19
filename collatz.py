# Task involving ifs and elses? And eilif?
# Calculation problem
# Author : Mary Metcalfe

number = []

number = int(input ("Enter a positive number : "))

if (number % 2) == 0:
    even_num = (number/2)
    print (f"The number {number} is even therefore I will divide it by 2")
    print (f"Your answer is {even_num}")
else:
    odd_num = (number *3 +1 )
    print (f"The number {number} is odd there I will multiply it by 3 and add 1")
    print (f"Your answer is {odd_num}")


