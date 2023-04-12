# Bank Account numbers
# Security for bank account numbers - replace first 6 digits with x
# Going to use slicing? Counting length -4
# Author : Mary Metcalfe

original_account_number = input("please enter your 10 digit account number: ")
length = len(original_account_number) # count the number of digits in the account number
hidden = length - 4  # all digits to be hidden except for the last 4
secure_number = original_account_number[hidden: ] # the secure number is the orginal number with the hidden change made
print ("xxxxxx",secure_number) # replace the hidden digits with 6 x and show the last four digits