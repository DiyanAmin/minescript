import m
import sys
from keyboard import is_pressed
from time import sleep
import math
m.msf.add_job()
m.options.legacy_dict_return_values = True
entity = sys.argv[1]
ent_num = 1

if len(sys.argv)>2:
    ent_num=len(sys.argv)

entities=m.entities()

names = {h['name']: h['position'] for h in entities}

def distance(pos1, pos2):
    return math.sqrt(
        (pos1[0] - pos2[0])**2 +
        (pos1[1] - pos2[1])**2 +
        (pos1[2] - pos2[2])**2
    )

if entity == "near":
    while not is_pressed('t'):
        entities = m.entities()
        # keep both name and type
        names = {h['name']: (h['position'], h['type']) for h in entities}

        player_pos = m.player_position()  # [x, y, z]

        nearby = []
        for name, (cords, etype) in names.items():
            if etype == "entity.minecraft.player" and name!=m.player_name() :  # ✅ only players
                if distance(cords, player_pos) <= 50:
                    x, y, z = cords
                    dist = round(distance(cords, player_pos), 1)
                    nearby.append(f"{name} [{dist} blocks]")

        if nearby:
            m.echo("\n\n\nNearby players:\n" + "\n".join(nearby) + "\n\n\n")
            
        if is_pressed('t'):
            break

        sleep(0.5)

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
            m.player_look_at(x,(y+1),z)
            sleep(0.01)

else:
    val=1
    while not is_pressed('t'):
        m.echo(f'\n\n\n{entity} is at {names[entity]} [{val}]\n\n\n\n')
        sleep(0.5)
        val+=1

m.msf.add_job(-1)