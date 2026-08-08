import m
import sys

armour = []
materials = ['diamond','diamond','diamond','diamond','netherite','netherite','netherite','netherite','iron','iron','iron','iron','copper','copper','copper','copper']
pieces = ['helmet','chestplate','leggings','boots','helmet','chestplate','leggings','boots','helmet','chestplate','leggings','boots','helmet','chestplate','leggings','boots']

val = 0
while len(armour)!=16:
    armour.append(
        f'minecraft:{materials[val]}_{pieces[val]}'
    )

    val+=1


display_x = sys.argv[1]

if display_x=='inv':
    inv = m.player_inventory()
    items = []
    for i in inv:
        items.append(i.item)

    val = 0
    for k in items:
        if k in armour:
            items.pop(val)
        val+=1

    m.echo(f'No. of Items: {len(items)}\nAvailable slots: {41-len(items)}\nItems:\n\n{items}')

        