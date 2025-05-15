# Using the code below as a starting point, write a while loop that prints the elements of 'lst' at 
# each index and terminates after printing the last element of the list.
lst = [1, 3, 7, 15]
index = 0

# Using the index variable
while index < 4:      # Better to use len(lst) instead of 4
    print(lst[index])
    index += 1

# For loop w/o index
for element in lst:
    print(element)