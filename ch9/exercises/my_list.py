# Use a while loop to print the numbers in my_list, 
# one number per line. Then, do the same with a for loop.

my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

for number in my_list:
    print(number)

# Seperating by even and odd numbers
index = 0
while index < len(my_list):
    if my_list[index] % 2 == 0:
        print(my_list[index])
    index += 1

for number in my_list:
    if number % 2 != 0:
        print(number)