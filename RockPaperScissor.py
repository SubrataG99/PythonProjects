
# Create a mini series of Rock, Paper, Scissors between User and Computer and decide winner based on winning the maximum match of the series

#-----------------------------------------------------------------------------------------Imports
import random

#-----------------------------------------------------------------------------------------Basic details or Intro to game
print('\nRules for the Rock-Paper-Scissor game :')
print('Press 0 for Rock')
print('Press 1 for Paper')
print('Press 2 for Scissors')
upoint = 0
cpoint = 0

#-----------------------------------------------------------------------------------------Series of matches (taken 5 match in a series)
for i in range(5) :
    user = int(input('\nWhat do you choose : '))
    comp = random.randint(0, 3)
    if user==0 :                                                                                                    # User choice is taken
        usergame = 'Rock'
    elif user==1 :
        usergame = 'Paper'
    elif user==2 :
        usergame = 'Scissors'
    else :
        usergame = None
        print('Rules for the Rock-Paper-Scissor game :')
        print('Press 0 for Rock')
        print('Press 1 for Paper')
        print('Press 2 for Scissors')
        print('Invalid Choice')
    
    if comp==0 :                                                                                                    # Computer choice is taken
        compgame = 'Rock'
    elif comp==1 :
        compgame = 'Paper'
    elif comp==2 :
        compgame = 'Scissors'
    
    if (user == comp) :                                                                                                             # zero points for same draw
        upoint = upoint + 0
        cpoint = cpoint + 0
    elif ((user==0 and comp==1) or (user==1 and comp==2) or (user==2 and comp==0)) :    # point to computer for defeating
        cpoint = cpoint + 1
        print('You :', usergame, '\t\tComputer :', compgame)
        print('You lost this match bro...\nBetter try next time')
    else :                                                                                                                                  # point to User for defeating
        upoint = upoint + 1
        print('You :', usergame, '\t\tComputer :', compgame)
        print('You win this match...\nKeep it up')

#-----------------------------------------------------------------------------------------Checking the points and deciding winner
if upoint == cpoint :
    print('Series draw...')
elif upoint > cpoint :
    print('\nYou : Comp ::', upoint, ':', cpoint)
    print('You win the series !!!\n')
else :
    print('\nYou : Comp ::', upoint, ':', cpoint)
    print('You lost the series bro...\n')