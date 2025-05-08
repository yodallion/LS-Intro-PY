squares = { f'{number}-squared': number * number
            for number in range(1, 6) }
print(squares)

# Set comprehension example, very similar to dict comprehension.
# Lacks key/value expression pair to the left of 'for'
squares = { number * number for number in range(1, 6) }