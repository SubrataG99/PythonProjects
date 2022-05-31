import time
import os

def clr():
    os.system('cls')

clr()

h = int(input('\nEnter hours value : '))
m = int(input('Enter minute value : '))
s = int(input('Enter second value : '))
print('Time :', h, 'hr', m, 'min', s, 'sec')
clr()

t = (h*60*60) + (m*60) + s
hh = 0
mm = 0
ss = 0

for i in range(t):
    if ss==59:                                                                  # Changing seconds to next minute
        ss = 0
        mm = mm + 1
    else:
        ss = ss + 1
    
    if mm==59:                                                              # Changing minutes to next hour
        mm = 0
        hh = hh + 1
    
    print('Time elapsed ==>', hh, 'hr :', mm, 'min :', ss, 'sec')
    time.sleep(1)
    clr()

print('Time up...!!!\n\n')