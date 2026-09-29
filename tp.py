from msf import get_json,write_json
import m
from keyboard import is_pressed as ip
import sys
from time import sleep

if m.msf.get_args()==0:
    while not ip('k'):
        if ip('7'):
            bridge_cords = get_json(-1).get("bridging_cords")
            m.execute(f'tp @s {bridge_cords[0]} {bridge_cords[1]} {bridge_cords[2]}')
            m.execute('effect give @s regeneration 10 255 false')
            sleep(1)
        if ip('k'):
            break
        if ip('a+s+d+space'):
            m.execute('give @s red_wool 64')
        sleep(0.1)