my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
my_list.reverse()
reverse = tuple(my_list[1:4])
print(reverse)

# Alternatively

my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[3:0:-1] # or [-2:-5:-1]
print(result)       # (4, 3, 2)