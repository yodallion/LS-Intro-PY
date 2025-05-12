# The following code raises a TypeError.
tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)

# What does a TypeError indicate? Try running the above code, then use the 
# resulting error message to determine exactly what is wrong. (You don't have to fix this code.)

# A "TypeError" occurs when an operation is attempted on an object that doesn't support it.
# In this case, the string represented by the variable "tweet" is being concatenated with the
# integer '5'. Since strings can only be concatenated with other strings, this error is related
# to some kind of a conflict between the "types" of data. Thus, we receive a "TypeError".