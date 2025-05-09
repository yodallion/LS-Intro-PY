numbers = [1, 2, 3]

numbers2 = numbers

print(id(numbers2) == id(numbers))   # True
print(numbers2 is numbers)           # True

print(id(numbers))                   # 140207360953152
print(id(numbers2))                  # 140207360953152

numbers += [4, 5]
print(numbers2)                      # [1, 2, 3, 4, 5]