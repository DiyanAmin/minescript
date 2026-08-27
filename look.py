import m
import sys

if len(sys.argv)!=1: #is arg is provided
    direction = sys.argv[1]
    yaw = 0
    if direction=='north':
        yaw=180
    elif direction=='northwest':
        yaw = 135
    elif direction=='northeast':
        yaw = 225
    elif direction=='east':
        yaw = 270
    elif direction=='west':
        yaw = 90
    elif direction=='south':
        yaw = 0
    elif direction=='southeast':
        yaw = 315
    elif direction=='southwest':
        yaw = 45
        
    m.player_set_orientation(yaw,0)

else:#Auto precise look at nearest direction
    yaw  = m.player_orientation()[0]
    if -45 <= yaw < 45:
        direction = "south"
    elif 45 <= yaw < 135:
        direction = "west"
    elif -135 <= yaw < -45:
        direction = "east"
    else:
        direction = "north"

    if direction=='north':
        yaw=180
    elif direction=='east':
        yaw = 270
    elif direction=='west':
        yaw = 90
    elif direction=='south':
        yaw = 0
        
    m.player_set_orientation(yaw,0)