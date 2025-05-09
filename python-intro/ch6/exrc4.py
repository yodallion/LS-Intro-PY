# Write a function that takes a single integer argument and prints a message that describes whether:

    # the value is between 0 and 50 (inclusive)
    # the value is between 51 and 100 (inclusive)
    # the value is greater than 100
    # the value is less than 0

def number_range(int):
    if int > 100:
        print('The value is greater than 100')
    elif int <= 100 and int > 50:
        print('The value is between 51 and 100')
    elif int <= 50 and int >= 0:
        print('The value is between 0 and 50')
    else:
        print('The value is less than 0')


number_range(0)
number_range(25)
number_range(50)
number_range(75)
number_range(100)
number_range(101)
number_range(-1)

# This is launch schools solution, which is better since it actually takes advantage
# of the flow of elif statements. Mine is more similar to match case. Better to start
# from the bottom than the top.

def number_range(number):
    if number < 0:
        print(f'{number} is less than 0')
    elif number <= 50:
        print(f'{number} is between 0 and 50')
    elif number <= 100:
        print(f'{number} is between 51 and 100')
    else:
        print(f'{number} is greater than 100')