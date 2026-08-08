import m
import sys

oper = sys.argv[1]
text = sys.argv[2]
file_name = sys.argv[3]

if oper == 'remember' or oper=='rem':
    with open(f'{file_name}.txt','w') as f:
        f.write(text)
    m.echo(f'Wrote {text} to {file_name}.txt successfully')

elif oper=='r' or oper=='read':
    with open(f'{file_name}.txt','r') as f:
        m.echo(f.read())
    m.echo('END OF FILE')

elif oper=='_get':
    m.echo('w.i.p.')

elif oper=='a' or oper=='append':
    with open(f'{file_name}.txt','a') as f:
        f.write(f'\n{text}')

else:
    m.echo('Unknown cmd.')