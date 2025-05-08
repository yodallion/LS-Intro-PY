# Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter.
# The updated code should use a for loop to display the future ages.

time = 10
age = input("How old are you?\n")
age = int(age)
print(f"You are {age} years old")
for num in range(4):
    print(f"In {time} years you will be {age + time} years old")
    time += 10

# Launch School solution
age = int(input('How old are you?\n'))
print(f"You are {age} years old")
print() # called to print an empty line

for future in range(10, 50, 10):
    print(f'In {future} years, you will be '
          f'{age + future} years old.')