dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
# dict2['Monty Python'] = 'Holy Grail'
# print(dict1['Monty Python'])
print(dict2['Monty Python'] is dict1['Monty Python'])
print(id(dict2['Monty Python']) is id(dict1['Monty Python']))