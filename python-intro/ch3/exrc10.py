
obj = 'ABcd' # reassigns the value
obj.upper() # does neither
obj = obj.lower() # reassigns the value
print(len(obj)) # does neither
obj = list(obj) # reassigns the value
obj.pop() # mutates the value
obj[2] = 'X' # reassigns value of obj[2], but mutates the list
obj.sort() # mutates the value
set(obj) # neither
obj = tuple(obj) # reassigns the value