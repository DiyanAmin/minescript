
#Code written by Diyan the Great Amin

import m
import sys

kind = sys.argv[1]

items = sys.argv[2]

if len(items)!=9:
    m.echo('Insufficient Items.')

if kind=='s' or kind=='single':
    if items=='fwr':
        m.execute('give @s firework_rocket 64')
    elif items=='e':
        m.execute('give @s ender_pearl 16')
    elif items=='w':
        m.execute('give @s wind_charge 64')
    elif items=='gap':
        m.execute('give @s enchanted_golden_apple 64')
    else:
        m.echo('Item not found...\nGiving data')
        m.execute(f'give @s {items}')

elif kind=='m' or kind=='p':
    binary=[]
    correspondent = {
        "mace[minecraft:enchantments={breach:4,density:5,wind_burst:3},minecraft:unbreakable={},minecraft:custom_name='Death']":1,
        'firework_rocket':64,
        'elytra[minecraft:unbreakable={}]':1,
        'totem_of_undying[minecraft:enchantments={protection:10}]':1,
        'enchanted_golden_apple':64,
        "netherite_sword[minecraft:unbreakable={},minecraft:enchantments={sharpness:10,fire_aspect:5,looting:3,sweeping_edge:5},minecraft:custom_name='Null']":1,
        'ender_pearl':16,
        'wind_charge':64,
        "netherite_axe[minecraft:unbreakable={},minecraft:enchantments={efficiency:10,sharpness:5,fire_aspect:5},minecraft:custom_name='Void']":1
    }
    for i in items:
        try:
            binary.append(int(i))
        except ValueError:
            m.echo(f'Couldnt now convert {i} to integer form')
    m.echo('Conversion Complete')

    for i in correspondent:
        for j in binary:
            if j==1:
                m.execute(f'give @s {i} {correspondent[i]}')
                break
            elif j==0:
                continue
        continue