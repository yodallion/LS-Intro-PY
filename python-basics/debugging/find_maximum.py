# Your colleague has implemented a custom function to find the maximum value in a list. 
# However, the function sometimes works correctly, but other times it produces incorrect results. 
# Can you help your colleague fix the bug?

def find_maximum(numbers):
    if not numbers:
        return None
    max_number = numbers[0]  # Originally was 'max_number= 0'
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum([-1, 0, 5, 3]))         # Expected 5
print(find_maximum([-10, -3, -20, -2]))   # Expected -2

# An alternate solution would be to assign 'max_number' to 'float('-inf')'