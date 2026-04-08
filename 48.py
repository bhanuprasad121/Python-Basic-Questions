# number guessing
import random
number =random.randint(1,50)

print('Enter a number 1 to 50')
print('you have a 3 chances')
for i in range(3):
    guess=int(input('Enter your guess:'))
    if guess==number:
        print('You have won')
    elif guess>number:
        print('Too High')
    else:
        print('Too low')
else:
    print('you lost')        
    print('Correct number is:',number)