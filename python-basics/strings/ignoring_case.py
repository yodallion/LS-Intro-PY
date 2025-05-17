# Using the following code, compare the value of name with the string 'RoGeR' while ignoring the case of both strings. 
# Print true if the values are the same; print false if they aren't. 
# Next, perform a case-insensitive comparison between the value of name and the string 'DAVE'.
name = 'Roger'

if name.casefold() == 'RoGeR'.casefold():
    print(True)
else:              # True
    print(False)

if name.casefold() == 'DAVE'.casefold():
    print(True)
else:              # False
    print(False)

# LS Solution
name = 'Roger'

print(name.casefold() == 'RoGeR'.casefold())      # True
print(name.casefold() == 'DAVE'.casefold())       # False

# My logic was still correct, I just forget that operators like '==' 
# automatically evaluate as either True or False so this code is better.