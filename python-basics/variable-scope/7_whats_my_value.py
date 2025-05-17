# What will the following code do and why? 
# Don't run it until you have tried to answer.
a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# '2'. This time, since the 'global' keyword is being used inside of 'my_function's' definition,
# Python knows that any 'a' variable used on this level will be referencing the global 'a' variable
# defined on the first line/top level.