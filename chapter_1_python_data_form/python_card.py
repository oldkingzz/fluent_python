# @Time: 2024-03-19 14:15
# @Author: DORK3333
# @File: python_card.py
# Software: PyCharm

import collections
from random import choice
Card = collections.namedtuple("Card", ["rank", 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = "spads diamonds clubs hearts".split()

    def __init__(self):
        self._card = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._card)

    def __getitem__(self, position):
        return self._card[position]

deck = FrenchDeck()