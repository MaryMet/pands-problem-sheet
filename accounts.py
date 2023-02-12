# Bank Account numbers
# Security for bank account numbers - replace first 6 digits with x
# Author : Mary Metcalfe

original_account_number = input("please enter your 10 digit account number: ")

length = len(original_account_number)
hidden = length - 4
secure_number = original_account_number[hidden: ]

print ("*" * hidden + secure_number)