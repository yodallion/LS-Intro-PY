# We have a grocery list. As we check off items on that list, 
# from the top of the list to the bottom, we want to remove them from the list.
# Write code that removes the items from grocery_list, one by one, until it is empty. 
grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

for i in range(len(grocery_list)):
    print(grocery_list[0])
    grocery_list.pop(0)

print(grocery_list)
                                                        
# If you print the elements you remove, the expected behavior would look as follows.
# paprika
# tofu
# garlic
# quinoa
# carrots
# broccoli
# hummus
# []

# LS solution using a while loop and utlizing truthiness
while grocery_list:
    checked_item = grocery_list.pop(0)
    print(checked_item)