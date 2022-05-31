import time
import os
import winsound
import random

def clr():                                                                              # this function is to clear screen
    os.system('cls')

clr()

h = int(input('\nEnter hours value : '))
m = int(input('Enter minute value : '))
s = int(input('Enter second value : '))
print('Time :', h, 'hr', m, 'min', s, 'sec')
clr()

t = (h*60*60) + (m*60) + s
hh = h
mm = m
ss = s

for i in range(t):
    clr()
    if ss==0:
        ss = 59
        mm = mm - 1
    else:
        ss = ss - 1
    
    if mm==0 and hh>0:
        mm = 59
        hh = hh - 1
    
    print('Time elapsed ==>', hh, 'hr :', mm, 'min :', ss, 'sec')
    time.sleep(1)
    # clr()
clr()
temp = random.randint(5, 20)
for i in range(temp):
    # clr()
    print('Time up...')
    winsound.Beep(1800, 350)
    time.sleep(0.45)
