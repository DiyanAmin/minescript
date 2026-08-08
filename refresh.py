import m
import sys

if len(sys.argv)==2:
    job = int(sys.argv[1])
else:
    job = 'track'
    ent = sys.argv[2]

if job=='track':
    m.execute(r'\killjob 1')
    cmd = r'\track '+ent+r' look'
    m.execute(cmd)
    m.execute(r'\killjob 2')