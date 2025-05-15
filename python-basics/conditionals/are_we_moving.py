# Determine what the following code snippet prints. 
# First solve it in your head or on paper, then run it in your Python environment to check the result.
speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)

# True
# LS breakdown of this question is worth going over again.
# For the bonus question, I correctly determined that the code would print 'True' with or without the parentheses on line 6.
# However, the bonus question was not asking 'Do we need the parentheses for the output to be the same?'
# It was asking 'Do we need the parenthese, period?.', as in, will we always get the same output no matter
# what the variables are with both versions of code (with or without parentheses).
# In that case the answer is yes, we do need the parentheses, since 'and' has a higher operator precedence than 'or'.