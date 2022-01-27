import random

class Points:
    """Tracks the points and cards in the game. 
    
    The responsibility of a Points is to calculate and return the points earned and new card

    Attributes:
        card (int): the new card drawn
        previous_card: saves previous card
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = 0
        self.previous_card = 1
        self.round = 0

    def calculate(self):
        self.card = random.randint(1,13)

        if self.card >= self.previous_card:
            self.points = 100
        else:
            self.points = -75
        self.previous_card = self.card
        return [self.card, self.points]


