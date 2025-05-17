# What will the following code do and why? 
# Don't run it until you have tried to answer.
a = 1

def my_function():
    a = 2

my_function()
print(a)

# It will print '1'. Even though 'a' is reassigned inside of 'my_function's definition and then invoked,
# The 'a' on line 6 is treated as a local variable by default, so it ends up being distinct from the
# global 'a' on line 3.