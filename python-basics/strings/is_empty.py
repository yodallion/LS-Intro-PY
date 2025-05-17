# Write a function that checks whether a string is empty or not.
def is_empty(str):
    return len(str) == 0


print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

# Alternate solutions
def is_empty(str):
    return str == ''

# Leveraging empty strings being falsy
def is_empty(str):
    return not str