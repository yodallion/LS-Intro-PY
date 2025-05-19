# Create a dictionary that contains the following data, and assign it to a variable named car.
# type 	   color 	mileage
# sedan    blue 	80000
car = {'type': 'sedan', 'color': 'blue', 'mileage': '80000'}
print(type(car))  # <class 'dict'>

# LS solution with pretier formatting
car = {
    'type': 'sedan',
    'color': 'blue',
    'mileage': 80_000,
}