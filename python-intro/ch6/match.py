value = 5

match value:
    case 1 | 2 | 3 | 4:
        print('value is less than 5')
    case 5 | 6:
        print('value is 5 or 6')
    case _: # default case
        print('value is greater than 6')