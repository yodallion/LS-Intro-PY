# Example of return value of functions being passed as arguments for other functions, i.e., composition
print(list(range(3, 17, 4)))

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

sum = add(20, 45)
print(sum) # 65

difference = subtract(80, 10)
print(difference) # 70

# Composition of lines 10-11 and 13-14
print(add(20, 45))      # 65
print(subtract(80, 10)) # 70

def times(num1, num2):
    return num1 * num2

print(times(add(20, 45), subtract(80, 10))) # 4550
# 4550 == ((20 + 45) * (80 - 10))