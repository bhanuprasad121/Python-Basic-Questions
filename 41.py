# Rock,Paper,Scissors Game

import random

while True:
    player=input('Enter rock, paper or scissors: ').lower()
    choice=['rock','paper','scissors']
    computer=random.choice(choice)

    if player== computer:
        print('Its a tie')
    elif player =='rock':
        if computer=='scissors':
            print('player won')
        else:
            print('computer won')    
    elif player=='paper':
        if computer=='rock':
            print('player won')
        else:
            print('computer won')    
    elif player == 'scissors':
        if computer=='paper':
            print('player won')
        else:
            print('computer won')        
    else:
        print('invalid input! choice rock,paper,scissors')            
    play_again=input('Want to play again (yes/no): ').lower()
    if play_again == 'no':
        break