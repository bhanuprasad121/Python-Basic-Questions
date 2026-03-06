# Write a Python Program to Find Armstrong Number in an Interval.

lower = int(input('Enter a lower number:'))
upper = int(input('Enter a upper number:'))

for num in range(lower,upper+1):
    order=len(str(num))
    temp_num=num
    b=0

    while temp_num>0:
        a=temp_num%10
        b+=a**order
        temp_num//=10
    if num == b:
        print(num)    