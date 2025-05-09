# Write a 'find_integers' function that returns a list
# of all the integers from 'my_tuple'.


def find_integers(collection):
    int_list = []
    for element in collection:
        if type(element) is int:
            int_list.append(element)
    return int_list


my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)

# LS solution

def find_integers(collection):
    return [ element
             for element in collection
             if type(element) is int ]