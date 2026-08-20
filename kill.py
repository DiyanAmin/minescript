import m
import sys
from msf import cide
target = sys.argv[1]

annoyances = ['skeleton','creeper','spider','zombie','slime','item','arrow','experience_orb','husk','parched']

if target=='item' or target=='i':
    cide("item")

elif target=='annoyances':
    for i in annoyances:
        cide(i)

elif target=='orb':
    cide('experience_orb')

elif target=='fake':
    cide('mannequin')

else:
    cide(target)