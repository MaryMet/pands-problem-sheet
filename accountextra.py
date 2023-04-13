# extra part of week 3 task
# any length account number 
# does work with accounts .py but only 6 xs
# Author:Mary Metcalfe

original_account_number = input("please enter your account number: ") # change to any length
length = len(original_account_number)
hidden = length - 4
secure_number = original_account_number[hidden: ]

print ("secure_number is {}" .replace )
print ("secure_number is: {}" .format (length -4))# how to put in multiple / changing xs?? - nope just taking 4 from the total no of digits
print ("secure_number is: {}" .format (secure_number))


#See other attempt at this below

# Bank Account numbers
# Security for bank account numbers - replace first 6 digits with x
# Going to use slicing? Counting length -4
# Author : Mary Metcalfe

#original_account_number = input("please enter your 10 digit account number: ")
#length = len(original_account_number) # count the number of digits in the account number
#hidden = length - 4  # all digits to be hidden except for the last 4
#secure_number = original_account_number[hidden: ] # the secure number is the orginal number with the hidden change made
#print ("xxxxxx",secure_number) # replace the hidden digits with 6 x and show the last four digits

# A third try
# giving it a shot
# Author : Mary Metcalfe

#original_account_number = input("please enter your account number: ")
#length = len(original_account_number)
#hidden = length -4
#secure_number = original_account_number[hidden]
#print ("secure_number is : {} " .format(secure_number) )