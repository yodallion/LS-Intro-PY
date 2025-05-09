# Use slicing to write Python code to print a 6-character substring of 'Launch School' that begins with the first c.

slice = 'Launch School'
print(slice[4:10])

# More programmatic solution (Though would require some error checking)

my_str = 'Launch School'
start = my_str.find('c')
print(my_str[start:start + 6])        # ch Sch