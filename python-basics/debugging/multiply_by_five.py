# When the user inputs 10, we expect the program to print The result is 50!, but that's not the output we see. Why not?

def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = int(input()) # changed from just 'input()'

print(f"The result is {multiply_by_five(number)}!")

# The 'input()' function returns a string which, when multiplied, simply concatenates
# itself multiple times. By making sure the users input is converted to an 'int', the
# function will work as intended.