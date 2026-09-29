import m
import sys
from keyboard import is_pressed as ip
from time import sleep

item = sys.argv[1]

while not ip('t'):
    if ip('t'):
        break

    m.execute(f'give @s {item} 64')
    sleep(0.3)