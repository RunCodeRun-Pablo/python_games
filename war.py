"""This file's code purpose is to create the war card game"""
import random

suits = ("Diamonds","Spades","Hearts","Clubs")
ranks = ("2","3","4","5","6","7","8","9","Ten","Jack","Queen","King","Ace")
values = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,
        "Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}

class Cards:
    """This class is going to define cards of the game"""

    def __init__(self,suits,ranks):
        self.suits = suits
        self.ranks = ranks
        self.value = values[ranks]
    
    def __str__(self):
        return f"{self.ranks} of {self.suits}"

class Deck:
    """This class is going to define all the cards of a deck"""
    def __init__(self):
        """Creates a complete deck using cards class"""
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Cards(suit,rank))
    
    def shuffle(self):
        """Once created a deck, it allows you to shuffle it, you can change order"""
        random.shuffle(self.all_cards)
    
    def card(self):
        """Once created a deck, it allows you to take a card out
        and it's eliminated from deck"""
        return self.all_cards.pop()
    
    def restart(self):
        """Once created a deck and finished using it, allows you
        to restore all the deck"""
        self.__init__() 

class Player:
    """This class is going to represent a player"""
    def __init__(self,name):
        self.name = name
        self.all_cards = []
    
    def remove_cards(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."
    
#Example
player = Player("Pablo")
deck = Deck()
player.add_cards(deck.card())
player.remove_cards()
print(player)
'''Como lo estoy entendiendo por ahora,
es que una forma de hacerlo (seguro que hay más)
es creando los diferentes objetos y luego usar los
objetos y sus métodos dentro de funciones del script
probarlo la próxima vez que siga con esto'''
    


    






