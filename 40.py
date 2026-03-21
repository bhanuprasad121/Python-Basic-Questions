# Write a Python Program to Make a Simple Calculator with 4 basic mathematical
# operations.
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divison(x,y):
    return x/y       

print('Select Operation')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Division')         

while True:
    choice=input('Enter a choice:')

    if choice in('1','2','3','4'):
        try:
            num1=float(input('Enter a 1st number:'))
            num2=float(input('Enter a 2nd number'))
        except ValueError:
            print('invaild number,Enter a correct number')
            continue    
        if choice =='1':
            print(num1,'+',num2,'=',add(num1,num2))
        if choice == '2':
            print(num1,'-',num2,'=',subtract(num2,num2))   
        if choice =='3':
            print(num1,'*',num2,'=',multiply(num1,num2))
        if choice =='4':
            print(num1,'/',num2,'=',divison(num1,num2))
        next_calculation=input('Lets do next calculation?(yes/no) ')
        if next_calculation=='no':
            break        
    else:
        print('Invalid output')       