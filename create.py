import m
import sys

entity = sys.argv[1]
amount = int(sys.argv[2])
player_list = [
    'Wemmbu',
    'ParrotX2',
    'SpokeisHere',
    'FlameFrags',
    'Minutetech',
    'rekrap2',
    'Wifies',
    'Yeah_Jaron',
    'aCookiegod',
    'Kenedian',
    'Manepear',
    'TheoBaldTheBird',
    'cubicmeter',
    'JumperWho',
    'yungyx',
    'LuigiToan']

if entity=='players' or entity=='$':

    while len(player_list)>amount:
        player_list.pop()

    for i in player_list:
        m.execute(f'/player {i} spawn')
    if amount==15 and entity=='$':
        m.execute(r"\give_armour $")
else:
    val = 0
    while val!=amount:
        m.execute(f'/summon {entity}')
        val+=1