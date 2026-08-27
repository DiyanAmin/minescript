import m
import sys

file = sys.argv[1]

with open(file,'r') as f:
    m.echo(f.read())