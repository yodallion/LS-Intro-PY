# You are trying to access a value in a dictionary, but the code is giving you an error. 
# Can you change the last line so that it prints "Unknown" instead of raising an error?

info = {'name': 'Srdjan', 'age': 38}

try:
    print(info['city'])  # Originally just this line by itself.
except KeyError:
    print('Unknown')

# LS solution

info = {'name': 'Srdjan', 'age': 38}

print(info.get('city', 'Unknown'))