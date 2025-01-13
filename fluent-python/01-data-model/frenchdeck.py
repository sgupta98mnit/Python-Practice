import collections
import random

# Way to declare class without any special functions
Card = collections.namedtuple('Card', ['rank', 'suit'])

print(Card('Q', 'hearts'))

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]

deck = FrenchDeck()
print(len(deck))

print(deck[0])
print(deck[-1])
print(deck[:3])
print(deck[12::13])

print(random.choice(deck))

# for card in deck:
#     print(card)

# for card in reversed(deck):
#     print(card)

print(Card('Q', 'hearts') in deck)
print(Card('11', 'diamonds') in deck)

# sort cards
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    # print(card, rank_value * len(suit_values) + suit_values[card.suit])
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print("card:", card)