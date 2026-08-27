import m
import sys
from time import sleep

entity = sys.argv[1]
amount = sys.argv[2]
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
    'LuigiToan',
    'Twirps',
    'Found2',
    'Derapchu',
    'Pangi',
    'Mapicc',
    'baconwaffles0',
    'Spongs',
    'Only_A_Squid',
    'leekleek',
    'Infume',
    'Reddoons',
    'CaptainSparklez',
    'SB737',
    'ClownPierce',
    'FerreMC',
    'BranzyCraft'
    ]
if amount=='all':
    amount = len(player_list)
else:
    amount=int(amount)

if entity=='players' or entity=='$':

    while len(player_list)>amount:
        player_list.pop()

    for i in player_list:
        m.execute(f'/player {i} spawn')
    if amount==len(player_list) and entity=='$':
        sleep(1)
        for i in player_list:
            m.execute(r'\give armour '+i)
else:
    val = 0
    while val!=amount:
        m.execute(f'/summon {entity}')
        val+=1
    m.execute('gamemode survival @a')
    m.execute('gamemode creative @s')