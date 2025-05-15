# Building on your solutions from the previous exercises, 
# write a function 'local_greet' that takes a locale as input, and returns a greeting. 
# The locale lets us greet people from different countries appropriately, even when they share a common language,
# for example:
# print(local_greet('en_US.UTF-8'))       # Hey!
# print(local_greet('en_GB.UTF-8'))       # Hello!
# print(local_greet('en_AU.UTF-8'))       # Howdy!
# Distinguish greetings for English speaking countries like the US, UK, Canada, or Australia in your implementation, 
# and feel free to fall back on the language-specific greetings in all other cases, for example:
# print(local_greet('fr_FR.UTF-8'))       # Salut!
# print(local_greet('fr_CA.UTF-8'))       # Salut!
# print(local_greet('fr_MA.UTF-8'))       # Salut!
# When implementing local_greet, make sure you re-use your extract_language, extract_region, and greet functions from the previous exercises.
def local_greet(locale):
    match extract_region(locale):
        case 'US':
            return 'Hey!'
        case 'GB':
            return 'Hello!'
        case 'AU':
            return 'G\'day, mate!'
        case 'IE':
            return 'Howaya!'
        case 'FR':
            return 'Bonjour!'
        case 'CA':
            if extract_language(locale) == 'en':
                return 'How\'s it going, eh?'
            elif extract_language(locale) == 'fr':
                return "'Kisses your cheek without consent'"
        case _:
            return greet(extract_language(locale))


def extract_language(locale):
    return locale.split('_')[0]


def extract_region(locale):
    return locale.split('_')[1].split('.')[0]


def greet(lang):
    match lang:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'
        case 'id':
            return 'Hai!'
        case 'ru':
            return 'Privet!'
        case 'ja':
            return 'Kon\'nichiwa!'
        case 'it':
            return 'Ciao!'


print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # G'day, mate!
print(local_greet('en_CA.UTF-8'))       # How's it going, eh?
print(local_greet('en_IE.UTF-8'))       # Howaya!
print(local_greet('fr_FR.UTF-8'))       # Bonjour!
print(local_greet('fr_MA.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # 'Kisses your cheek without consent'
print(local_greet('it_IT.UTF-8'))       # Ciao!
print(local_greet('it_VA.UTF-8'))       # Ciao!
print(local_greet('it_SM.UTF-8'))       # Ciao!


# LS solution for the 'local_greet' function.
def local_greet(locale):
    language = extract_language(locale)  # Sets 'extract_language(locale)' and
    region = extract_region(locale)      # 'extract_region(locale)' to reusable variables

    match (language, region):  # match case statement with multiple arguments
        case ('en', 'US'):
            return 'Hey!'
        case ('en', 'GB'):
            return 'Hello!'
        case ('en', 'AU'):
            return 'Howdy!'
        case _:
            return greet(language)

# Definitely a nicer solution, I would've benefited from reading more about 'match case' statements.
# Didn't know you could compare multiple arguments like that.
# Creating variables at the start was also good practice to reduce instances of function invocation.