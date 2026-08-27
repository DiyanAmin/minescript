import m
import sys
from keyboard import is_pressed as ip
from time import sleep

while not ip('t'):
    if ip('t'):
        break
    
    m.execute(f'give @s {sys.argv[1]}')
    m.player_press_drop(True)
    sleep(.001)