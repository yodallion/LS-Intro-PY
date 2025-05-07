stuff = ('hello', 'world', 'bye', 'now')
stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)
print(stuff)

# Identify at least 2 differences between lists and tuples. 
# Identify at least 2 ways that lists and tuples are similar.


# Lists are mutable, tuples are immutable
# List literals use [] and tuple literals use ()

# Lists and tuples share the same constructor format
# Lists and tuples are both classified as ordered collections
# Lists and tuples are both heterogeneous


# Why can strings be treated as sequences?
# Because they are always ordered and can be accessed via indexing

# How do the set types differ from the sequence types?
# Sets are unordered and thus do not support indexing

pi = 3.141592
str_pi = str(pi)

# Without running the following code, identify the numbers that are included in each of the following ranges

range(7)         # [0, 1, 2, 3, 4, 5, 6]
range(1, 6)      # [1, 2, 3, 4, 5]
range(3, 15, 4)  # [3, 7, 11]
range(3, 8, -1)  # []
range(8, 3, -1)  # [8, 7, 6, 5, 4]

# How would you print all the numbers in the following range?
range(3, 17, 4)
print(list(range(3, 17, 4)))

# Given the code below, answer the following questions
my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Are the lists assigned to my_list and another_list equal? Yes
# Are the lists assigned to my_list and another_list the same object? No
# Are the nested lists at index 3 of my_list and another_list equal? Yes
# Are the nested lists at index 3 of my_list and another_list the same object? Yes
