class Card:



    """
    The Card class represents a single playing card and is initialised by passing a suit and number.
    """
    
    def __init__(self, suit, number):
    """
    this is the constructor with two properties
    """
        self._suit = suit
        self._number = number

    def __repr__(self):
    """
    overwriting to string
    """
        return self.number + " of " + self.suit
    
    @property
    def suit(self):
    """
    gets the property suit"
    """
        return self._suit
    
    @suit.setter
    """
    sets the property suit
    """
    def suit(self, suit):
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")
    
    @property
    def number(self):
    """
    gets the property number
    """
        return self._number
    
    @number.setter
    """
    sets the number values
    """
    def number(self, number):
        if number in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K","A"]:
            self._number = number
        else:
            print("That's not a card!")

 

my_card = Card("hearts", "6")
my_card.suit = "clubs"
another_card = Card("Dinosaurs", "1")

print(my_card)
print(another_card)
