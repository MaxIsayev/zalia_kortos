import random

class Card:

    def __init__(self, suit: str = '', weight: int = 0, color: str = ''):
        self.suit = suit
        self.weight = weight
        self.color = color
        self.rank = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
        self.suit = ('spades', 'clubs', 'hearts', 'diamonds')  
    

    

class Deck:

    def __inir__(self, deck: list = []):
        self.deck = deck

    def shufle(self):
        random.shuffle(self.deck)

    def take_top(self):
        pass
    
    def take_bottom(self):
        pass

    def take_random(self):
        r_card = random.randint(1, 52)
        pass

class GameLogic():

    def __init__(self):
        pass

class Computer1():

    def __init__(self):
        pass



    def forkinimas(self):
      pass

    def new_function():
        pass

# Kortų kaladė
# Korta: Objektas (Class)
# def rank (2-9, T, J, Q, K, A)
# def suit (spades, clubs, hearts, diamonds)
# def sign (suit + rank)
# def weight
# Kortų kaladė: Objektas (Class)
# def cards - kortų sąrašas []
# def shuffle
# def take from top
# def take from bottom
# def take random
# Mąstom apie žaidimą
