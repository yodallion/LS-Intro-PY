# Without running the following code, determine what will be printed.
sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")

# The variable 'sale' is initialized with the boolean 'True'.
# Then, the variable 'admission_price' is being initialized using a ternary expression.
# The ternary expression states "Initialize admission_price to the float '5.25' if the variable 'sale' is not true, i.e., 'False'.
# Else, initialize admission_price to the float '3.99'."
# Since 'sale' is 'True', i.e., 'not False', admission_price will be set to the value of it's ternary expressions 'else' value.
# Thus, 'print(f"${admission_price}")' will print '$3.99'.