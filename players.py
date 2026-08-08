import m
import sys
m.options.legacy_dict_return_values = True

players = m.get_players()
ent_data = {}
names = []
cords = []

val = 0
while val!=len(players):
    ent_data[players[val]['name']] = players[val]['position']
    val+=1

ent_data.pop('Hades18369')

if len(sys.argv)==1:
    player_no = 1
    for e in ent_data:
        m.echo(f'{player_no}. {e} is at {ent_data[e]}\n')
        player_no+=1
elif len(sys.argv)==2:
    for e in ent_data:
        if e==sys.argv[1]:
            m.echo(f'{e} is at {ent_data[e]}')
elif len(sys.argv)==3:
    if sys.argv[2]!='kill':
        for e in ent_data:
            if e==sys.argv[1]:
                m.echo(f'{e} is at {ent_data[e]}')
                m.execute(f'/tp @s {ent_data[e][0]} {ent_data[e][1]} {ent_data[e][2]}')
                break
    elif sys.argv[2]=='kill':
        for e in ent_data:
            m.execute(f'/kill {e}')