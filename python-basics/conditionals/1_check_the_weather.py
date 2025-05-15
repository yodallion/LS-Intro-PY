# Initialize a variable 'weather' with a string value being 'sunny', 'rainy', or whatever weather condition you choose. 
# Then, write an if statement that prints:

#   It's a beautiful day! if weather's value is 'sunny'
#   Grab your umbrella. if weather's value is 'rainy'
#   Let's stay inside. if weather's value is anything else

# Test your code with different values for weather.
weather = input('What\'s the weather like today?\n')

if weather == 'sunny':
    print('It\'s a beautiful day!')
elif weather == 'rainy':
    print('Grab your umbrella.')
else:
    print('Let\'s stay inside.')