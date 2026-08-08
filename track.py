import m
import sys
from keyboard import is_pressed
from time import sleep
m.options.legacy_dict_return_values = True
entity = sys.argv[1]
ent_num = 1

if len(sys.argv)>2:
    ent_num=len(sys.argv)

entities=m.entities()

names={}
for h in entities:
    name = h['name']
    cords = h['position']
    names[name] = cords

if ent_num>2:
    if sys.argv[2]!='look':
        tracking = []
        for i in sys.argv:
            tracking.append(i)
        tracking.pop(0)
        val = 1
        while not is_pressed('t'):
            for k in tracking:
                m.echo(f'{k} is at {names[k]} [{val}]\n')
            sleep(0.5)
            val+=1
    elif sys.argv[2]=='look':
        while not is_pressed('t'):
            m.echo(f'\n\n\n{entity} is at {names[entity]}\n\n\n')
            x,y,z = names[entity][0] , names[entity][1] , names[entity][2]
            m.player_look_at(x,y,z)
            sleep(0.01)

else:
    val=1
    while not is_pressed('t'):
        m.echo(f'\n\n\n{entity} is at {names[entity]} [{val}]\n\n\n\n')
        sleep(0.5)
        val+=1

