import m
import sys
from keyboard import is_pressed
from time import sleep

if len(sys.argv)==1: #No arg provided
    railgun_type = 'snowball'
else:
    railgun_type = sys.argv[1]

while not is_pressed('t'): #While t key not pressed
    if is_pressed('t'): #Double checking
        break
    
    if railgun_type=='snowball':
        m.execute('give @s snowball 1')
        m.player_press_use(True)
        continue
    elif railgun_type == 'load':
        m.player_press_use(True)
        sleep(0.1)
        m.player_press_use(False)
    else:
        m.execute(f'give @s {railgun_type} 1')
        m.player_press_use(True)
        continue     

m.echo('Done.')