import m 
from keyboard import is_pressed
import sys
m.options.legacy_dict_return_values = True

utility = sys.argv[1]

master_switch = False

#Utility Checker Dict
utility_checker = {
    'void':False,
    'inv_slots':False,
    'immortal':False
}

if utility=='$':
    for i in utility_checker:
        utility_checker[i]=True
else:
    utility_checker[utility] = True

immortallity_toggle = True

while not is_pressed('t'):
    if utility_checker['void']:
        y = m.player_position()[1]
        if y<-87:
            m.echo('\n\n\n\n\n[VOID SAFETY] Below Void!!!!\n')
            m.execute('/tp @s ~ -64 ~')

    elif utility_checker['inv_slots']:
        if is_pressed('7'):
            m.execute(r'\d')

    elif utility_checker['immortal']:
        while not is_pressed('z'):
            if is_pressed('z'):
                utility_checker['immortal']=False
                break
            try:
                offhand = m.player_hand_items()['off_hand']['item']
            except TypeError:
                m.execute('item replace entity @s weapon.offhand with minecraft:totem_of_undying')

    elif master_switch:
        m.echo('No utilities active.')
        break

    else:
        m.echo('No utilities active.')
        break
