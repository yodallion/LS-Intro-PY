suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10',
    'Jack', 'Queen', 'King', 'Ace'
]

# With nested loops
deck = []
for suit in suits:
    for rank in ranks:
        card = f'{rank} of {suit}'
        deck.append(card)

# With comprehensions
deck = [ f'{rank} of {suit}'
         for suit in suits
         for rank in ranks ]

print(deck)