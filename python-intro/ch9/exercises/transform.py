# Write code that creates a new list with one element for
# each number in 'my_list'. If the original number is an even,
# then the corresponding element in the new list should
# contain the string 'even'; otherwise, the element should
# contain 'odd'.

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

new_list = []
for number in my_list:
    if number % 2 == 0:
        number = 'even'          # LS solution simplfies this
        new_list.append(number)  # to new_list.append('even')
    else:
        number = 'odd'           # LS solution simplfies this
        new_list.append(number)  # to new_list.append('odd')

print(new_list)

# Using a ternary expression
new_list = [ 'even' if number % 2 == 0 else 'odd'
           for number in my_list ]
print(new_list)

# Using a helper function
def odd_or_even(number):
    return 'even' if number % 2 == 0 else 'odd'

new_list = [ odd_or_even(number)
           for number in my_list ]
print(new_list)