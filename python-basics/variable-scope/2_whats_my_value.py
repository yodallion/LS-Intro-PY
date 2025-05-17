# What will the following code do and why? 
# Don't run it until you have tried to answer.
x = 10

def my_function():
    # Global x <-- Adding this would fix the issue
    x = x + 5
    print(x)

my_function()

# 15 <-- WRONG
# See x = 10 is a global so I thought that meant my_function could use it, but I guess since it's trying
# to reassign x inside its own scope that doesnt really work? Like if I comment out line 5 this code runs fine.
# The reassignment is definitely the issue and would require use of the Global or Non-Local keywords to work.