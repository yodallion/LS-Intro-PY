# Make a function that evaluates an integer as even or odd

def even_or_odd(int):
    if int % 2 == 0:
        print('Even')
    else: 
        print('Odd')

even_or_odd(5)
even_or_odd(1)
even_or_odd(10)
even_or_odd(17)
even_or_odd(36)

# Alternatively

def even_or_odd(number):
    print('even' if number % 2 == 0 else 'odd')