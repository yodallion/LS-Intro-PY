# How many arguments does the str.join method expect? What happens if you call it with fewer or more arguments?

str1 = "hello frin "
str2 = "im am well thank "
str3 = "hah nice same buddi "
str4 = "what the fuck did you just say to m"

joined1 = str1.join()
joined2 = str1.join(str2, str3, str4)
joined3 = str1.join(str2)

# The "join" method expects exactly one argument. It will raise an error if it is given any more or any less arguments.
# The argument must also be some kind of iterable sequence/collection and contain only strings. If any non-string value is found
# in the iterable, it will raise an error.