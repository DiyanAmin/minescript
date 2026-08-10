import m
import sys
import pyperclip as clipboard

code = sys.argv[1]
ret = ''

if len(sys.argv)==3:
    ret = ord(code)
else:
    ret = chr(int(code))

m.echo(f'[OUTPUT]: {ret}')
clipboard.copy(ret)