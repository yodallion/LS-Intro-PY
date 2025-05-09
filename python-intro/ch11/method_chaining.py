tv_show = "Monty Python's Flying Circus"
tv_show = tv_show.upper()
# "MONTY PYTHON'S FLYING CIRCUS"

tv_show = tv_show.split()
# ['MONTY', "PYTHON'S", 'FLYING', 'CIRCUS']

# Using method chaining
tv_show = "Monty Python's Flying Circus"
tv_show = tv_show.upper().split()
# ['MONTY', "PYTHON'S", 'FLYING', 'CIRCUS']

# Formatting to make multiple method chains more readable
letters = 'abcdefghijklmnopqrstuvwxyz'
consonants = (letters.replace('a', '').  # Surrounding parenthese is
                      replace('e', '').  # required for mult-line chains
                      replace('i', '').
                      replace('o', '').
                      replace('u', ''))
print(consonants) # bcdfghjklmnqrstvwxyz