# Modify the following code so the loop continues iterating until the user inputs 'yes'.
while True:
    print('Should I stop looping?')
    answer = input()
    if answer == 'yes':
        break
    # print('Incorrect answer. Please answer "yes".')
    # ^ giving the user feedback is often a good practice.