# Write a function that returns the first element of a list provided as an argument.
def first(list):
    try:
        return list[0]
    except:
        IndexError
        

print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([]))  # None

# LS solution
def first(list):
    if list:
        return list[0]
    else:
       return None