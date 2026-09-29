import m
import sys
from random import choice,randint
from keyboard import is_pressed as ip
from time import sleep
m.options.legacy_dict_return_values=True
item = sys.argv[1]

if item=='armour':
    if len(sys.argv)==3:
        m.execute('/item replace entity @a armor.chest with minecraft:netherite_chestplate[minecraft:unbreakable={},minecraft:enchantments={protection:5}]')
        m.execute('/item replace entity @a armor.legs with minecraft:netherite_leggings[minecraft:unbreakable={},minecraft:enchantments={protection:5,swift_sneak:5}]')
        m.execute('/item replace entity @a armor.feet with minecraft:netherite_boots[minecraft:unbreakable={},minecraft:enchantments={protection:5,feather_falling:5}]')
        m.execute('/item replace entity @a armor.head with minecraft:netherite_helmet[minecraft:unbreakable={},minecraft:enchantments={protection:5}]')
        m.execute('/item replace entity @a weapon.offhand with minecraft:totem_of_undying[minecraft:enchantments={protection:10}]')
        sleep(0.1)
        m.execute(r'\give armour $ $')
    
    elif len(sys.argv)==3:
        m.execute('/item replace entity '+{sys.argv[2]}+' armor.chest with minecraft:netherite_chestplate[minecraft:unbreakable={},minecraft:enchantments={protection:5}]')
        m.execute('/item replace entity '+{sys.argv[2]}+' armor.legs with minecraft:netherite_leggings[minecraft:unbreakable={},minecraft:enchantments={protection:5,swift_sneak:5}]')
        m.execute('/item replace entity '+{sys.argv[2]}+' armor.feet with minecraft:netherite_boots[minecraft:unbreakable={},minecraft:enchantments={protection:5,feather_falling:5}]')
        m.execute('/item replace entity '+{sys.argv[2]}+' armor.head with minecraft:netherite_helmet[minecraft:unbreakable={},minecraft:enchantments={protection:5}]')
        m.execute('/item replace entity '+{sys.argv[2]}+' weapon.offhand with minecraft:totem_of_undying[minecraft:enchantments={protection:10}]')

    elif len(sys.argv)==4:
        if sys.argv[2]=='Emperor':
            material=r"redstone},item_name='Armour Piece of Hades, Emperor of Elysium']"
        elif sys.argv[2]=='purifier':
            material=r'quartz}]'
        elif sys.argv[2]=='$':
            material = str(choice(['redstone','quartz']))+r'}]'
        elif sys.argv[2]=='schizophrenia':
            while not ip('x'):
                material = str(choice(['redstone','quartz']))+r'}]'
                interval = randint(1,10)
                inv = m.player_inventory()
                replace=True
                for i in inv:
                    if i['item']=='minecraft:elytra' and i['slot']==38:
                        replace=False
                if replace:
                    m.execute('/item replace entity @s armor.head with minecraft:netherite_helmet['+r'minecraft:unbreakable={},minecraft:enchantments={protection:5},trim={pattern:flow,material:'+material)
                    m.execute('/item replace entity @s armor.legs with minecraft:netherite_leggings['+r'minecraft:unbreakable={},minecraft:enchantments={protection:5,swift_sneak:5},trim={pattern:silence,material:'+material)
                    m.execute('/item replace entity @s armor.feet with minecraft:netherite_boots['+r'minecraft:unbreakable={},minecraft:enchantments={protection:5,feather_falling:5},trim={pattern:raiser,material:'+material)
                    m.execute('/item replace entity @s armor.chest with minecraft:netherite_chestplate['+r'minecraft:unbreakable={},minecraft:enchantments={protection:5},trim={pattern:raiser,material:'+material)
                    m.execute('/item replace entity @s weapon.offhand with minecraft:totem_of_undying['+r'minecraft:enchantments={protection:10}]')
                m.echo(replace) 
                sleep(10)
            m.echo('Done.')

        m.execute('/item replace entity @s armor.head with minecraft:netherite_helmet['+r'minecraft:unbreakable={},minecraft:enchantments={protection:5},trim={pattern:flow,material:'+material)
        m.execute('/item replace entity @s armor.legs with minecraft:netherite_leggings['+r'minecraft:unbreakable={},minecraft:enchantments={protection:5,swift_sneak:5},trim={pattern:silence,material:'+material)
        m.execute('/item replace entity @s armor.feet with minecraft:netherite_boots['+r'minecraft:unbreakable={},minecraft:enchantments={protection:5,feather_falling:5},trim={pattern:raiser,material:'+material)
        m.execute('/item replace entity @s armor.chest with minecraft:netherite_chestplate['+r'minecraft:unbreakable={},minecraft:enchantments={protection:5},trim={pattern:raiser,material:'+material)
        m.execute('/item replace entity @s weapon.offhand with minecraft:totem_of_undying['+r'minecraft:enchantments={protection:10}]')

elif item=='e':
    m.execute(r'/give @s elytra[minecraft:unbreakable={}]')

elif item=='kb':
    if len(sys.argv)==3:
        sub_item = sys.argv[2]
    else:
        sub_item='stick'
    
    enchants = r'{knockback:255}'
    m.execute(f"give @s {sub_item}[minecraft:enchantments={enchants},minecraft:custom_name='Flinger']")

else:
    m.execute(f'/give @s {item}')