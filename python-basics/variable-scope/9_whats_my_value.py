# What will the following code do and why? 
# Don't run it until you have tried to answer.
a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

# I think it will still print '7' since 'my_function' isnt actually returning a value.
# ^Right answer, wrong logic. Even if 'my_function' returned a value you would need to use
# function composition (print(my_function(a))) for it to print '17', a would still be '7'.
# The real reason is because integers are immutable and cannot be changed. 
# 'a' would have to be reassigned, which doesn't happen here.