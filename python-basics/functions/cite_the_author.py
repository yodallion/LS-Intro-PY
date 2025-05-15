# Let's generalize the function from the previous exercise. Implement a function named 'cite' that 
# takes two string arguments: the author of the quote and what they said. It then prints the quote, as shown below.
# cite('Bruce Eckel', 'Python is executable pseudocode.')
# Outputs: Bruce Eckel said: "Python is executable pseudocode."
def cite(author, quote):
    print(f'{author} said: "{quote}"')


cite('Bruce Eckel', 'Python is executable pseudocode.')

# ALternate solution using the 'format' method.
def cite(author, quote):
    print('{} said: "{}"'.format(author, quote))


cite('Bruce Eckel', 'Python is executable pseudocode.')