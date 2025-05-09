def foo():
    def bar():
        print('BAR')

    bar() # BAR

foo()
bar() # NameError: name 'bar' is not defined

# Nested functions are private and can't be accessed outside
# the function where they are defined.