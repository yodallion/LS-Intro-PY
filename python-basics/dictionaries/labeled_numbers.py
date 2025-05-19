# Use a for loop to iterate over the numbers dictionary and print each element's key/value pair.
numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for value in numbers:
    print(f'A {value} number is {numbers[value]}.')

# LS using dict.items() method
for key, value in numbers.items():
    print(f"A {key} number is {value}.")

# A high number is 100.
# A medium number is 50.
# A low number is 10.