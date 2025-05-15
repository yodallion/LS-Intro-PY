# Use Python's control structures to create a function that takes an ISO 639-1 language code and
# returns a greeting in that language. You can take the examples below or add whatever languages you like.
def greet(lang):
    match lang:
        case 'en':
            greeting = 'Hi!'
        case 'fr':
            greeting = 'Salut!'
        case 'pt':
            greeting = 'Olá!'
        case 'de':
            greeting = 'Hallo!'
        case 'sv':
            greeting = 'Hej!'
        case 'af':
            greeting = 'Haai!'
        case 'id':
            greeting = 'Hai!'
        case 'ru':
            greeting = 'Privet!'
        case 'ja':
            greeting = 'Kon\'nichiwa!'
        case 'it':
            greeting = 'Ciao!'

    return greeting


print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!
print(greet('id'))         # Hai!
print(greet('ru'))         # Privet!
print(greet('ja'))         # Kon'nichiwa!
print(greet('it'))         # Ciao!