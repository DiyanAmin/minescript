import m
import sys
import msf

x = m.player_position()[0]
y = m.player_position()[1]-1
z = m.player_position()[2]
radius = 9

layer_0 = [
    [x,y-1,z],
    [x,y-1,z-1],
    [x-1,y-1,z],
    [x,y-1,z+1],
    [x+1,y-1,z],
    [x-1,y-1,z-1],
    [x-1,y-1,z+1],
    [x+1,y-1,z+1],
    [x+1,y-1,z-1], 
]

layer_1 = [
    [x,y,z],
    [x,y,z-1],
    [x-1,y,z],
    [x,y,z+1],
    [x+1,y,z],
    [x-1,y,z-1],
    [x-1,y,z+1],
    [x+1,y,z+1],
    [x+1,y,z-1],
]

layer_2 = [
    [x,y+1,z],
    [x,y+1,z-1],
    [x-1,y+1,z],
    [x,y+1,z+1],
    [x+1,y+1,z],
    [x-1,y+1,z-1],
    [x-1,y+1,z+1],
    [x+1,y+1,z+1],
    [x+1,y+1,z-1],
]

# Layer-0 (Below,Below):
# Layer-1 (Below/On):
# Layer-2 (In):

m.echo(msf.scan(radius=9))