# Write a Python Program to Print all Prime Numbers in an Interval of 1-10.

lower=1
higher=10

print(f'the prime numbers between',lower,'and',higher,'are:')

for num in range(lower,higher+1):
    if num >1:
        for i in range(2,num):
            if (num%i==0):
                break
        else:
            print(num)        


    