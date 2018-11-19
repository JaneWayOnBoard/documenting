from card import Card

class Deck:


    """
    The Card class represents all the cards included in the deck.
    """
    
    def __init__(self):
    """
    this is the constructor
    """
        self.cards = []
        self.populate()
        print(self._cards)

    def populate(self):
    """
    sets a list/array
    """
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K","A"]
        self._cards = [ Card(s, n) for s in suits for n in numbers]

my_deck = Deck()
