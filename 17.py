# Write a Python Program to Print the Fibonacci sequence.

# Fibonacci sequence:
# The Fibonacci sequence is a series of numbers where each number is the sum of the two
# preceding ones, typically starting with 0 and 1. So, the sequence begins with 0 and 1, and
# the next number is obtained by adding the previous two numbers. This pattern continues
# indefinitely, generating a sequence that looks like this:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.
# Mathematically, the Fibonacci sequence can be defined using the following recurrence
# relation:
# F(0) = 0 F(1) = 1 F(n) = F(n − 1) + F(n − 2)forn > 1

nterm = int(input('How my terms? '))
n1,n2=0,1
count=0

if nterm <= 0:
    print('Enter a postive number')
elif nterm == 1:
    print('Fibonacci squence upto',nterm,':')
    print(n1)
else:
    print('Fibonacci squence')
    while count < nterm:
        print(n1)
        nth=n1+n2
        # updating values
        n1=n2
        n2=nth
        count+=1
