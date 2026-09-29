import m
m.options.legacy_dict_return_values = True

inv = m.player_inventory()
items = {}

for i in inv:
    items[(i['item']).split(':')[1]]=i['count'] # Remove minecraft: and make that item name be equal to its amount

m.echo(f'\n\n\n{items}\n\n\n')
