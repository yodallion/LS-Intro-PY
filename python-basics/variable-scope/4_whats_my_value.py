# What will the following code do and why? 
# Don't run it until you have tried to answer.
a = 1

def my_function():
    print(a)

my_function()

# It will print '1'. This is because 'a' is initialized at the top level of our code, which by default
# makes it a global variable. This allows 'print()' to access 'a' from within 'my_function's definition.