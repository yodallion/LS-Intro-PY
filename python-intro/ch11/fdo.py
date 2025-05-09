# Function Definition Order

def top():
    bottom()

def bottom():
    print('Reached the bottom')

top()

# Python reads functions into memory before trying to execute them.
# bottom() can be used in top()'s definition, even though it is not
# defined until later. If top() was invoked before either top() or
# bottom() were defined, it would not work. You don't need to worry
# about your ordering of functions, so long as they are defined before
# ever being invoked.