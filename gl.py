import m
import sys

items_num = int(sys.argv[1])
gl = []

val = 0

while val!=items_num:
    gl.append(sys.argv[val+2])
    val+=1

with open('gl.txt','w') as f:
    f.write(str(gl))

m.echo(f'Wrote {gl} to gl.txt')