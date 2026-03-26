#  Single-Digit or Multi-Digit Number
# Given an integer number, write a program to determine whether the number is a single-digit number or a multi-digit number.

# A single-digit number contains exactly one digit (from -9 to 9).
# A multi-digit number contains more than one digit (either positive or negative).

# The program should analyze the number and display the appropriate result based on the number of digits.
def single_digit_or_milti_digit_number():
    num=int(input('Enter a number: '))
    if len(str(abs(num)))==1:
        return 'single_digit_number'
    else:
        return 'multi_digit_number'
print('The number is',single_digit_or_milti_digit_number())    

