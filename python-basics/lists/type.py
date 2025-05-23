# How can you check if a variable holds a value that is a list? 
# Given two variables, verify whether the values they hold are lists.
some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'

print(type(some_value1))  # <class 'list'>
print(type(some_value2))  # <class 'str'>

# LS solution
isinstance(some_value1, list)  # True
isinstance(some_value2, list)  # False
# Definitely the more correct solution.