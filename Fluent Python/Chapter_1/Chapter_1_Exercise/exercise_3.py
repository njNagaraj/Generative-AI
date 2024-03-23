#demonstrating the working of some special methods using a FrenchDeck class

# Importing necessary modules
import collections
import random

# Defining Card namedtuple
Card = collections.namedtuple('Card', ['rank', 'suit'])

# Definition of the FrenchDeck class
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def __repr__(self):
        return f"FrenchDeck(cards={self._cards})"

deck = FrenchDeck()

# Displaying the initial deck
beer_card = Card('7', 'diamonds')
print(beer_card) # return Card(rank='7', suit='diamonds')

print(len(deck)) # 52

# will call __getitem__()
print(deck[0]) # Card(rank='2', suit='spades')
print(deck[-1]) # Card(rank='A', suit='hearts')

# will call __getitem__()
print(deck[:3])
# [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
print(deck[12::13])
# [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]

for card in deck: 
    print(card)
'''Card(rank='2', suit='spades')
Card(rank='3', suit='spades')
Card(rank='4', suit='spades')'''

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
    
    for card in sorted(deck, key=spades_high):
        print(card)
''' Card(rank='2', suit='clubs')
Card(rank='2', suit='diamonds')
Card(rank='2', suit='hearts')
... (46 cards omitted)
Card(rank='A', suit='diamonds')
Card(rank='A', suit='hearts')
Card(rank='A', suit='spades')'''
