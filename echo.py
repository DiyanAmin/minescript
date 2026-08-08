import m
from time import sleep
from keyboard import is_pressed as ip

while not ip('t'):
    m.echo('\n\n\ntesting\n\n\n')
    sleep(0.1)