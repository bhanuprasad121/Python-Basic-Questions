# Write a Python program to convert kilometers to miles.
kilometer=float(input('Enter the kilometer travelled:'))

# 1 kilometer = 0.621371
conversion_factor = 0.621371
miles=conversion_factor*kilometer

print(f'{kilometer} is equals to miles:{miles}')

