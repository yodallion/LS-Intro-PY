# Write a function that returns the last element of a list provided as an argument.
def last(list):
    if list:
        return list[-1]
    else:
        return None


print(last(['Earth', 'Moon', 'Mars']))  # Mars
print(last([]))