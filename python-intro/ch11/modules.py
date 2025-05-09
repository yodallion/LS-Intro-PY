# Importing a module
import math

print(math.sqrt(math.pi)) # Square root of Pi

# Using 'from' statement to get specific functions
from math import pi, sqrt

print(sqrt(pi))

# You can even use an 'alias' to save keystrokes
# Useful for modules with very long names
import math as m

print(m.sqrt(m.pi))

# Datetime module functionality
from datetime import datetime as dt 

date = dt.strptime("July 16, 2022", "%B %d, %Y")
weekday_name = datestrftime('%A')
print(weekday_name)  # Saturday