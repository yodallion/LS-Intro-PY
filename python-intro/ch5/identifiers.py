# Identify all of the identifiers on each line of the following code.

def multiply(left, right): # function indentifier = multiply. Parameter identifiers = left, right
    return left * right # local variables = left, right. 

def get_num(prompt): # function identifier = get_num. Parameter identifier = prompt
    return float(input(prompt)) # function identifiers = float, input which are being invoked. Argument identifier = prompt

first_number = get_num('Enter the first number: ') # Variable identifier = first_number. # Function identifier = get_num which is being invoked
second_number = get_num('Enter the second number: ') # Variable identifier = second_number. # Function identifier = get_num which is being invoked
product = multiply(first_number, second_number) # Variable = product. Function name/invocation = multiply. Arguments = first_number, second_number
print(f'{first_number} * {second_number} = {product}') # Function name/invocation = print. Variables = first_number, second_number, product

# Using the code below, classify the identifiers as global, local, or built-in.

def multiply(left, right):                                # Identifiers are:
    return left * right                                   # multiply - global
                                                          # left - local
def get_num(prompt):                                      # right - local
    return float(input(prompt))                           # get_num - global
                                                          # prompt - local
first_number = get_num('Enter the first number: ')        # float - built-in
second_number = get_num('Enter the second number: ')      # input - built-in
product = multiply(first_number, second_number)           # first_number - global
print(f'{first_number} * {second_number} = {product}')    # second_number - global
                                                          # product - global
                                                          # print - built-in

# identify all of the function names and parameters present in the code. Include the line numbers for each item identified.

def multiply(left, right):                                # Function names:
    return left * right                                   #   multiply - lines 31 and 39
                                                          #   get_num lines 34, 37, and 38
def get_num(prompt):                                      #   float - line 35
    return float(input(prompt))                           #   input - line 35
                                                          #   print - line 40
first_number = get_num('Enter the first number: ')        # Parameters:
second_number = get_num('Enter the second number: ')      #   left - lines 31 and 32
product = multiply(first_number, second_number)           #   right - lines 31 and 32
print(f'{first_number} * {second_number} = {product}')    #   prompt - lines 34 and 35

# Which of the identifiers in the following program are function names? Which are method names? Which are built-in functions?

def say(message):                           # Function names:
    print(f'==> {message}')                 #   say
                                            # Built-in functions:
string1 = input()                           #   print
string2 = input()                           #   input
                                            #   max
say(max(string1.upper(), string2.lower()))  # Method names:
                                            #   upper
                                            #   lower