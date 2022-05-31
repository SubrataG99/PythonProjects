
# Create a Tic-Tac-Toe game and return for who wins the game

#----------------------------------------------------------------------------------------- Imports
import os

def clr():                                                                                      # To clear the screen (terminal)
    os.system('cls')
def sum(a, b, c):
    return a+b+c

#----------------------------------------------------------------------------------------- Defining the game board
def board(xstate, zstate):
    print('\n')
    zero = 'x' if xstate[0] else ('0' if zstate[0] else ' ')
    one = 'x' if xstate[1] else ('0' if zstate[1] else ' ')
    two = 'x' if xstate[2] else ('0' if zstate[2] else ' ')
    three = 'x' if xstate[3] else ('0' if zstate[3] else ' ')
    four = 'x' if xstate[4] else ('0' if zstate[4] else ' ')
    five = 'x' if xstate[5] else ('0' if zstate[5] else ' ')
    six = 'x' if xstate[6] else ('0' if zstate[6] else ' ')
    seven = 'x' if xstate[7] else ('0' if zstate[7] else ' ')
    eight = 'x' if xstate[8] else ('0' if zstate[8] else ' ')
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")

#----------------------------------------------------------------------------------------- Defining how a win is decided
def CheckMate(xstate, zstate):
    win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for x in win :
        if (sum(xstate[x[0]], xstate[x[1]], xstate[x[2]]) == 3) :
            clr()
            board(xstate, zstate)
            print('X won this match...\n')
            return 1
        if (sum(zstate[x[0]], zstate[x[1]], zstate[x[2]]) == 3) :
            clr()
            board(xstate, zstate)
            print('0 won this match...\n')
            return 0
    return -1

#----------------------------------------------------------------------------------------- Intro to Game
clr()
print('Welcome to the Game of\n\t\t\tTic - Tac - Toe\n')
xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
zstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
print('Press 0 for choosing Zero...\nPress 1 for choosing Cross...')
dec = int(input('What do you choose ? : '))
if ((dec == 0) or (dec == 1)) :
    turn = dec
else :
    print('Invalid choice, Try again later')
# turn = 1                                                                    # 1 for cross ; 0 for zero
while (True):
    board(xstate, zstate)
    if (turn == 1) :
        print('\nCROSS turn --> ')
        value = int(input('Enter your position for cross : '))
        xstate[value-1] = 1
    else :
        print('\nZERO turn --> ')
        value = int(input('Enter your position for zero : '))
        zstate[value-1] = 1
    ttt = CheckMate(xstate, zstate)
    if (ttt != -1) :
        break
    turn = 1 - turn
    clr()