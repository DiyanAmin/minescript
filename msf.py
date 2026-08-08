import m
def display(msg):
    m.echo(f'\n\n\n\n{msg}\n\n\n\n')

def row_wise_give(items:dict,rows:int=3):
    if len(items)>9:
        m.echo('Error: More items than columns')
    val=0
    while val!=rows:
        for i in items:
            m.execute(f'give @s {i} {items[i]}')
        val+=1

def cide(entity_name:str):
    m.execute(f'kill @e[type={entity_name}]')
