import m
import sys
from msf import write_json,get_json
from diyanLib.data import retrieve

#Data needed for minescript files.

cmd_his = retrieve('command_history.txt').split('\n')
cmd_his.append('data.py')

ms_data = {
    'username':m.player_name(),
    'cmd_his':cmd_his
}

write_json(ms_data,-1)
m.echo(get_json(-1))