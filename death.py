import m
import sys
from msf import get_args
from keyboard import is_pressed
m.options.legacy_dict_return_values=True

#Heights dictionary. more height = more time + more lethality
heights = {
    '$':0, #Input was '$'
    'player':1.8,
    'warden':2.9,
    'zombie':1.95,
    'villager':1.95
}

kind=''

try:
    kind = sys.argv[1]
except IndexError:
     m.echo(r'Usage: \death <ray/beam/orbital>')

if kind=='orbital':
        while not is_pressed('t'):
            try:
                x = m.player_get_targeted_block(1000)[0][0]
                y = m.player_get_targeted_block(1000)[0][1]+2
                z = m.player_get_targeted_block(1000)[0][2]
                m.execute(f'summon tnt {x} {y} {z}')
            except TypeError:
                continue

        m.execute('\\kill tnt')

elif kind=='beam' or kind=='ray':
    lethality=100
    args = get_args()
    x = m.player_get_targeted_block(1000)[0][0]
    y = m.player_get_targeted_block(1000)[0][1]+2
    z = m.player_get_targeted_block(1000)[0][2]

    if args==2: #1 arg provided
         lethality = int(sys.argv[2])
    for i in range(lethality):
        m.execute(f'summon tnt {x} {y} {z}')