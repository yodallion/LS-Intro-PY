# What will the following code do and why? 
# Don't run it until you have tried to answer.
a = 1

def my_function():
    print(a)
    a = 2

my_function()

# I thought it would print '1' same as the last problem since 'a' is initialized after invoking 'print()'
# inside 'my_function's definition, but apparently it doesn't work that way. Python will look at the entire
# block of code on lines 6 and 7 and see that 'a' is being initialized, so when 'print()' tries to access 'a'
# the line before that initialization, it creates an issue since 'a' has yet to be defined.