import random
from game.points import Points

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card (int): the current card played
        previous_card (int): the previous card played
        points (List[Points]): points earned this round
        is_playing (boolean): whether or not the player is still playing the game
        starting_card (int): draws a starter card
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.decision = ''
        self.is_playing = True
        self.card = []
        self.total = 300


    def start(self):
        print('Individual cards are represented as a number from 1 to 13.')
        print('Starting card is a 1.')
        self.decision = input('Would you like to draw a card? (y/n): ')
        if self.decision == 'n':
            self.is_playing = False
        else:
            while self.is_playing == True:
                if self.decision == 'n':
                    self.is_playing = False
                else:
                    self.turn = Points().calculate()
                    print(self.turn)
                    print(f'Card drawn: {self.turn[0]}')
                    print(f'Points earned: {self.turn[1]}')
                    self.total += self.turn[1]
                    print(f'Total Score: {self.total}')
                    if self.total < 0:
                        self.is_playing = False
                        print(f'Your score dropped below zero. Game Over')
                    else:
                        self.is_playing = True
                self.decision = input('Would you like to draw a card? (y/n): ')



