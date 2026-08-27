import m
import sys

item = sys.argv[1]

if item=='armour':
    if len(sys.argv)==3:
        m.execute('/item replace entity @a armor.chest with minecraft:netherite_chestplate[minecraft:unbreakable={},minecraft:enchantments={protection:5}]')
        m.execute('/item replace entity @a armor.legs with minecraft:netherite_leggings[minecraft:unbreakable={},minecraft:enchantments={protection:5,swift_sneak:5}]')
        m.execute('/item replace entity @a armor.feet with minecraft:netherite_boots[minecraft:unbreakable={},minecraft:enchantments={protection:5,feather_falling:5}]')
        m.execute('/item replace entity @a armor.head with minecraft:netherite_helmet[minecraft:unbreakable={},minecraft:enchantments={protection:5}]')
        m.execute('/item replace entity @a weapon.offhand with minecraft:totem_of_undying[minecraft:enchantments={protection:10}]')
    
    elif len(sys.argv)==2:
        m.execute('/item replace entity '+{sys.argv[2]}+' armor.chest with minecraft:netherite_chestplate[minecraft:unbreakable={},minecraft:enchantments={protection:5}]')
        m.execute('/item replace entity '+{sys.argv[2]}+' armor.legs with minecraft:netherite_leggings[minecraft:unbreakable={},minecraft:enchantments={protection:5,swift_sneak:5}]')
        m.execute('/item replace entity '+{sys.argv[2]}+' armor.feet with minecraft:netherite_boots[minecraft:unbreakable={},minecraft:enchantments={protection:5,feather_falling:5}]')
        m.execute('/item replace entity '+{sys.argv[2]}+' armor.head with minecraft:netherite_helmet[minecraft:unbreakable={},minecraft:enchantments={protection:5}]')
        m.execute('/item replace entity '+{sys.argv[2]}+' weapon.offhand with minecraft:totem_of_undying[minecraft:enchantments={protection:10}]')

    elif len(sys.argv)==4:
        m.execute('/item replace entity @s armor.chest with minecraft:netherite_chestplate[minecraft:unbreakable={},minecraft:enchantments={protection:5}]')
        m.execute('/item replace entity @s armor.legs with minecraft:netherite_leggings[minecraft:unbreakable={},minecraft:enchantments={protection:5,swift_sneak:5}]')
        m.execute('/item replace entity @s armor.feet with minecraft:netherite_boots[minecraft:unbreakable={},minecraft:enchantments={protection:5,feather_falling:5}]')
        m.execute('/item replace entity @s armor.head with minecraft:netherite_helmet[minecraft:unbreakable={},minecraft:enchantments={protection:5}]')

elif item=='e':
    m.execute(r'/give @s elytra[minecraft:unbreakable={}]')

else:
    m.execute(f'/give @s {item}')