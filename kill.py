import m
import sys
from msf import cide
target = sys.argv[1]

if target=='item' or target=='i':
    cide("item")

elif target=='mobs':
    for i in ['skeleton','creeper','spider','zombie']:
        cide(i)

elif target=='orb':
    cide('experience_orb')

elif target=='fake':
    cide('mannequin')

else:
    cide(target)