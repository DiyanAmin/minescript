import m
import sys
from msf import row_wise_give

kind = sys.argv[1]


if kind=='wemmbu' or kind=='w':
    m.echo('Giving Wemmbu kit...')
else:
    m.echo('Giving Base Elytra-Mace Kit')

m.execute("give @s mace[minecraft:enchantments={breach:4,density:5,wind_burst:3},minecraft:unbreakable={},minecraft:custom_name='Death']")
m.execute('give @s firework_rocket 64')
m.execute('give @s elytra[minecraft:unbreakable={}]')

#Amrmour and extras
m.execute('\give_armour')
m.execute('/item replace entity @s weapon.offhand with shield[minecraft:unbreakable={}]')

#Rest of kit

m.execute("give @s totem_of_undying[minecraft:enchantments={protection:10},item_name='Totem Of Null']")
m.execute('give @s enchanted_golden_apple 64')
m.execute("give @s netherite_sword[minecraft:unbreakable={},minecraft:enchantments={sharpness:10,fire_aspect:5,looting:3,sweeping_edge:5},minecraft:custom_name='Null']")
m.execute('give @s ender_pearl 16')
m.execute("give @s wind_charge 64")
m.execute("give @s netherite_axe[minecraft:unbreakable={},minecraft:enchantments={efficiency:10,sharpness:5,fire_aspect:5},minecraft:custom_name='Void']")

#Orbitals

if kind=='wemmbu' or kind=='w':
    m.execute('/orbitalstrike stab 18')
    m.execute('/orbitalstrike nuke 9')
else:
    items_per_row = {
        'totem_of_undying':1,
        'firework_rocket':64,
        'golden_carrot':64,
        'golden_apple':64,
        'enchanted_golden_apple':64,
        'ender_pearl':32,
        'wind_charge':128
    }
    row_wise_give(items_per_row)

m.echo('\n\nKit Given.\n\n')