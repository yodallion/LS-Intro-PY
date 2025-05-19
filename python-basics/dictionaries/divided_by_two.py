# Use a for loop to iterate over the numbers dictionary and return a list containing 
# each number divided by 2 as an integer. The result should be truncated to an integer. 
# Assign the returned list to a variable named half_numbers and print its value using print.
numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

half_numbers = []
for number in numbers:
    half_numbers.append(int(numbers[number] / 2))

print(half_numbers)

# LS solution using the dict.values() method
half_numbers = []
for value in numbers.values():
    half_numbers.append(value // 2) # // for integer division

print(half_numbers)