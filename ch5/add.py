def add(a, b):
    return a + b

print(add(2, 3))

# Example of a predicate function
def is_digit(char):
    if char >= '0' and char <= '9':
        return True

    return False