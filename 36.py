# Write a Python Program to Find LCM.
# Least Common Multiple (LCM):
# LCM, or Least Common Multiple, is the smallest multiple that is exactly divisible by two or
# more numbers.
# Formula:
# For two numbers a and b, the LCM can be found using the formula:

# LCM(a, b) =

# |a ⋅ b|
# GCD(a, b)

# In [1]:
# For more than two numbers, you can find the LCM step by step, taking the LCM of pairs of
# numbers at a time until you reach the last pair.
# Python Program to find the L.C.M. of two input number
def compute_lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if ((greater%x==0)and(greater%y==0)):
            lcm=greater
            break
        greater+=1
    return lcm

num1=int(input('Enter a number'))
num2=int(input('Enter a number'))
print('The Lcm of',compute_lcm(num1,num2))