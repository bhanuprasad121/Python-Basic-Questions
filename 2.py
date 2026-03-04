# Write a Python program to do arithmetical operations addition and division.
# Enter the first number for addition: 5
# Enter the second number for addition: 6
# sum: 5.0 + 6.0 = 11.0
num1=float(input('enter a first number to add:'))
num2=float(input('enter a second number to add:'))

sum_result=num1+num2
print(f'sum {num1}+{num2}={sum_result}')

print('*'*20)

num3=float(input('enter a dividend for division:'))
num4=float(input('enter a divisor for division:'))
div_result=num3/num4

if num4==0:
    print('division by zero is not allowed')
else:    
    print(f'division {num3}/{num4}={div_result}')