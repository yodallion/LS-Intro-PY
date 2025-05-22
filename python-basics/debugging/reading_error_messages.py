# What errors does this code raise and what exactly do the error messages mean?

def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0)
find_first_nonzero_among(1)

# Both function calls raise a type error. The first raises an error because the 'find_first_nonzero_among'
# function only takes one argument, but was given 6. The second call raises an error because the function
# contains a for loop for iterating through a collection, but was given an 'int' as an argument. In both cases,
# the issue would be solved if the numbers were placed in some kind of collection, such as a list or a tuple,
# and then that collection was used as an argument.