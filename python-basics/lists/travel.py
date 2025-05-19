# Write a function that, without using the built-in 'in' operator, 
# checks whether a specific destination is included within destinations. 
def contains(key, list):
    for location in list:
        if location == key:
           return True
           
    return False


destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False