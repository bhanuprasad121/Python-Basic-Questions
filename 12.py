# Write a Python Program to Check Leap Year.
# Enter a year: 2024
# 2024 is a leap year

year=int(input('Enter a year'))

if (year%400==0) and (year%100==0):
    print(f'{year} is a leap year'.format(year))

elif (year%4==0) and (year%100!=0):
    print(f'{year} is a leap year'.format(year))

else:
    print(f'{year} is not leap year'.format(year))    