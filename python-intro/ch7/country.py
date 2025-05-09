# Consider the data in the following table:
# Name 	Country
# Alice 	USA
# Francois 	Canada
# Inti 	    Peru
# Monika 	Germany
# Sanyu 	Uganda
# Yoshitaka 	Japan

country = {'Alice': 'USA', 'Francois': 'Canada', 'Inti': 'Peru', 'Monika': 'Germany', 'Sanyu': 'Uganda', 'Yoshitaka': 'Japan'}
name = input('What name would you like to check?\n')
country_origin = country[name]
print(f'{country_origin}')

# Launch Schools solution. Better variable name and prettier formatting for the dictionary.

countries = {
    'Alice':     'USA',
    'Francois':  'Canada',
    'Inti':      'Peru',
    'Monika':    'Germany',
    'Sanyu':     'Uganda',
    'Yoshitaka': 'Japan',
}

print(countries['Monika'])