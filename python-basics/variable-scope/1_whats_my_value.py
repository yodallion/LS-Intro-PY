# What will the following code do and why? 
# Don't run it until you have tried to answer.
if True: 
    my_value = 20

print(my_value)

# The code will print '20'. True is truthy, 
# so the if statement here will execute and assign the 'my_value' variable the value of 20.
# In python, variables initialized with 'if' statements are accessible outside that block of code.

# Bonus Question, what would this code print?
if False:
    my_new_value = 42

print(my_new_value)

# This code would raise a NameError, since 'my_new_value' has not been initialized.