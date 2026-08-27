import m
import sys
from keyboard import is_pressed as pressed

if len(sys.argv)==1:
    ent = 'Wemmbu'
elif len(sys.argv)==2:
    ent = sys.argv[1]

while not pressed('t'):
    try:
        x = m.player_get_targeted_block(64.0)[0][0]
        y = m.player_get_targeted_block(64.0)[0][1]
        z = m.player_get_targeted_block(64.0)[0][2]

        block_data = m.player_get_targeted_block(64)[3]
        if 'minecraft:tripwire[attached=true,' in block_data:
            y-=1

        m.execute(f'tp {ent} {x} {y+1} {z}')
    except TypeError:
        m.echo('Looking at nothing.')
        continue