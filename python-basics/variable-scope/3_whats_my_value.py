# What will the following code do and why? 
# Don't run it until you have tried to answer.
def my_function():
    a = 1

    if True:
        print(a)

my_function()

# It will print '1'. Since 'a' is defined inside 'my_functions' scope, it can be used as an
# argument for other functions as long as they are also within 'my_functions' scope.
# This includes the 'if True' statement.