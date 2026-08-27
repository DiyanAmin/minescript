import m
import sys

amt = float(sys.argv[1])

m.execute(f'attribute @s minecraft:max_health base set {amt*2}')