def mult(a, b):
    return float(a) * float(b)

first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
product = mult(first_number, second_number)
print(f"{first_number} * {second_number} = {product}")