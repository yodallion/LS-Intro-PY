def hello():
    print('Hello')
    return True

hello()         # invoking function; ignore return value
print(hello())  # using return value in a `print` call

print('Hello', 'Goodbye', 'Farewell')

numbers = [2, 5, 8, 10, 13]
print(any(number % 2 == 0 for number in numbers))
print(all(number % 2 == 0 for number in numbers))