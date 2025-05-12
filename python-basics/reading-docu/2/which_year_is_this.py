# The Python documentation for the datetime module provides two attributes to retrieve the year 
# from a date or datetime object: year and isocalendar. What is the difference between the year attribute and the isocalendar method?
from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]

# "today.year" accesses the "year" attribute of the date object created by date.today(). 
# It simply returns the current year, in this case, '2025'. "today.isocalendar()" returns a named tuple consisting of the year, week, and day
# of the current year. The biggest difference is that this datetime information is based on the "ISO week date" calendar system, which focuses
# more on weeks to define the start and end of a year. This differs slightly from the way the gregorian calendar accounts for dates and as
# such should only be used when actively working with ISO weeks.