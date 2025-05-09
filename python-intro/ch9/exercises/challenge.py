# Print all of the even numbers in the following list of
# nested lists. This time, don't use any for loops.

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

outer_index = 0
inner_index = 0
while outer_index < len(my_list):
    if inner_index == len(my_list[outer_index]):
        inner_index = 0
        outer_index += 1
    while inner_index < len(my_list[outer_index]):
        if my_list[outer_index][inner_index] % 2 == 0:
            print(my_list[outer_index][inner_index])
        inner_index += 1

# Okay I give up. I can get it to print all the correct
# numbers, but I can't get the loop to properly break
# after iterating through the whole list.

# LS solution
outer_index = 0
while outer_index < len(my_list):
    inner_index = 0
    while inner_index < len(my_list[outer_index]):
        number = my_list[outer_index][inner_index]
        if number % 2 == 0:
            print(number)

        inner_index += 1

    outer_index += 1 
# Aghhhhhh, I was so close. Just couldn't wrap my head
# around where to properly increment my outer/inner index
# variables inside the nested while loop.

# LS solution using a local variable to avoid
# having to type my_list[outer_index][inner_index]
outer_index = 0
while outer_index < len(my_list):
    inner_list = my_list[outer_index]
    inner_index = 0
    while inner_index < len(inner_list):
        number = inner_list[inner_index]
        if number % 2 == 0:
            print(number)

        inner_index += 1

    outer_index += 1