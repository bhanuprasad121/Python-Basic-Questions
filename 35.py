# Student Pass if Passed Any Two Subjects

maths=int(input('Enter maths marks:'))
physics=int(input('Enter physics marks:'))
chemistry=int(input('Enter chemistry marks:'))

def Student_Pass_if_Passed_Any_Two_Subjects(maths,physics,chemistry):
    count=0
    pass_marks=35
    if maths >= pass_marks:
        count+=1
    if physics >= pass_marks:
        count+=1
    if chemistry >= pass_marks:
        count+=1
    if count >= 2:
        return 'Pass'                
    else:
        return 'Fail'
    
result=Student_Pass_if_Passed_Any_Two_Subjects(maths,physics,chemistry)    
print(result)