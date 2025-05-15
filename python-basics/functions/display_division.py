# Without running the following code, determine what it will print:
def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three

# Well, since the 'multiples_of_three' function is never actually invoked, this code doesn't print anything.
# However, if line 9 was changed to 'multiples_of_three()', the code would then print '3 / 1 = 3', followed by
# '6 / 2 = 3', followed by '9 / 3 = 3', each time the dividend increasing by three and the divisor increasing by 1,
# all the way until we get '30 / 10 = 3'.