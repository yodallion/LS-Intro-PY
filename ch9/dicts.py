my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)

my_dict = {'a': 1, 'b': 2, 'c': 3}
for value in my_dict.values():
    print(value)

my_dict = {'a': 1, 'b': 2, 'c': 3}
for items in my_dict.items():
    print(items)

# More 'pythonic' method
my_dict = {'a': 1, 'b': 2, 'c': 3}
for (key, value) in my_dict.items(): # Parentheses around key, value is optional
    print(f'{key} = {value}')