# Write a Python program to swap two variables.
# Enter the value of the first variable (a): 5
# Enter the value of the second variable (b): 9
# Original values: a = 5, b = 9
# Swapped values: a = 9, b = 5

a=int(input('Enter the value of the first variable (a):'))
b=int(input('Enter the value of th second variable (b):'))
print(f'Orginal value a={a},b={b}')

temp=a
a=b
b=temp
print(f'Swapped values a={a},b={b}')
