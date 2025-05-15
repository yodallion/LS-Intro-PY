# Take your code from the previous Check the Weather exercise and rewrite it as a match-case statement. 
# Feel free to add more cases besides 'sunny' and 'rainy'.
weather = input('What\'s the weather like today?\n')

match weather:
    case 'sunny':
        print('It\'s a beautiful day!')
    case 'rainy':
        print('Grab your umbrella.')
    case 'cloudy':
        print('No sunglasses required!')
    case 'snowy':
        print('Put on your long johns')
    case 'windy':
        print('Perfect for kiting')
    case 'humid':
        print('End my life')
    case _:
        print('Let\'s stay inside.')