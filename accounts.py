# Bank Account numbers
# Security for bank account numbers - replace first 6 digits with x
# Going to use slicing -4
# Author : Mary Metcalfe

original_account_number = input("please enter your 10 digit account number: ")

length = len(original_account_number)
hidden = length - 4
secure_number = original_account_number[hidden: ]

print ("xxxxxx",secure_number)