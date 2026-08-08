import m
from time import sleep
import pyautogui as pg
import sys

server = sys.argv[1]

if server!='complex' or server!='c':
    while True:
        #Automated Mining Code

        m.player_press_attack(True)
        pg.rightClick()
        m.player_press_forward(True)

        #Inv Code

        inv = m.player_inventory()
        if len(inv)>=36:
            m.execute('sell')
        else:
            m.funcs.display(f'Slots Left: {36-len(inv)}')
        sleep(0.1)

elif server=='complex' or server=='c':
    while True:
        m.player_press_attack()
        m.execute('rankup')
        pg.leftClick()
        