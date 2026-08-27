import m
import sys 
from keyboard import is_pressed as ip
from time import sleep

cmd = sys.argv[1]
if len(sys.argv)==3:
    target = sys.argv[2]

if cmd=='look':

    while not ip('t'):
        if ip('t'):
            break
        else:
            if target=='@s':
                m.execute(f'player Wemmbu look at ~ {m.player_position()[1]+1.5} ~')
            elif target=='$':
                if ip('t'):
                    break
                player_list = ''
                with open('players.txt','r') as f:
                    data = f.read()
                player_list = data.split(',')
                for i in player_list:
                    m.execute(f'player {i} look at ~ {m.player_position()[1]+1.5} ~')

    m.echo('You pressed t so its over.')