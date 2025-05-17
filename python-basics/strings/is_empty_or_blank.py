# Write an is_empty_or_blank function to determine whether a string is either empty or consists entirely of spaces.
def is_empty_or_blank(str):
    return len(str.strip(' ')) == 0


print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

# Alternate solutions
def is_empty_or_blank(str):
    return str.strip(' ') == ''

# Leveraging empty strings being falsy
def is_empty_or_blank(str):
    return not str.strip(' ')