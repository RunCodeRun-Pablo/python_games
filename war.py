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
        """Allows to show, compare and eliminate a player card"""
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        """Allows to take cards when a player wins a round"""
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def restart(self):
        "Resets player cards"
        self.all_cards = []

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."
    
player_1 = Player("player 1")
player_2 = Player("player 2")
deck = Deck()

def tie():
    pass

def play():
    """This function should take a card of each player, and compare them,
    the player with the higher card will win, in case of equal card,
    three cards should be taken by each player and the highest within them
    will win the war (another func), the winner players gets all the cards"""
    # For the future
    # while not player_1.all_cards == 0 or not player_2.all_cards == 0:
    card_1 = player_1.remove_cards()
    card_2 = player_2.remove_cards()

    if card_1.value == card_2.value:
        tie()
    elif card_1.value > card_2.value:
        player_1.add_cards(card_1)
        player_1.add_cards(card_1)
    else:
        player_2.add_cards(card_1)
        player_2.add_cards(card_2)

def start_game():
    """Once created a deck, this func shuffles it,
    and distributes it between both players"""

    deck.shuffle()
    for i in range(len(deck.all_cards) // 2):
            player_1.add_cards(deck.card())
            player_2.add_cards(deck.card())
    
    
    



    





'''Como lo estoy entendiendo por ahora,
es que una forma de hacerlo (seguro que hay más)
es creando los diferentes objetos y luego usar los
objetos y sus métodos dentro de funciones del script
probarlo la próxima vez que siga con esto'''
    


    






