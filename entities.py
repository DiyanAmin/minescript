import m
import sys
m.options.legacy_dict_return_values = True

tp=''
ds = False
num = sys.argv[1]
if len(sys.argv)>=3:
    search = sys.argv[2]
    ds=True
    if len(sys.argv)==4:
        tp = sys.argv[3]

entities=m.entities()
entities_list = []

for i in entities:
    entities_list.append(i['name'])

if num=='all':
    m.echo(entities_list)

elif ds:
    names = {}
    if search in entities_list:
        for h in entities:
            name = h['name']
            cords = h['position']
            names[name] = cords
        m.echo(f'{search} is at {names[search]}')

        if tp!='':
            x = names[search][0]
            y = names[search][1]
            z = names[search][2]
            m.execute(f'/tp @s {x} {y} {z}')

else:
    try:
        num = int(num)
    except ValueError:
        m.echo('Unknown Argument')

    val = -1
    display=[]
    
    for j in entities_list:
        if val!=num:
            display.append(j)
            val+=1
        else:
            break

    display.pop(0)

    m.echo('\n\n')
    for k in display:
        m.echo(k)
    m.echo('\n\n')