# Write a Python Program to Find HCF.
# Highest Common Factor(HCF):
# HCF, or Highest Common Factor, is the largest positive integer that divides two or more
# numbers without leaving a remainder.
# Formula:

# Basic Python Program - Jupyter Notebook

# 13/95

# For two numbers a and b, the HCF can be found using the formula:
# HCF(a, b) = GCD(a, b)

# In [2]:
# For more than two numbers, you can find the HCF by taking the GCD of pairs of numbers at
# a time until you reach the last pair.
# Python program to find H.C.F of two numbers

def compute_hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if ((x%i==0)and(y%i==0)):
            hcf=i
    return hcf    
num1=int(input('Enter a number'))
num2=int(input('Enter a number' ))
print('The HCF is',compute_hcf(num1,num2))