"""Blackjack rules:
It is played with 4 decks of 52 cards, and consists in obtaining
a sum of 21 points without surpassing this amount. Each player plays
against the crupier, and either player or croupier have distinct rules
croupier has to ask for cards whenever his score is less than 16, and
stands if it is 17 or more.

Numeric cards add to each other and figures add 10, except for ace which
either adds 11 or 1 depending on player selection. For the croupier aces
score 11 if the result does not surpass 21, and 1 in the other case.

Best play is achieving a 21 score with only two cards, termed as blackjack,
which is even better than scoring 21 with more than 2 cards

Game starts with croupier giving two cards to each player, if the player directly
obtains a blackjack he wins the round unless croupier also has a blackjack.
The croupier also has two cards in the table. Cards are distributed using
the following order: first card for the player, first card for the croupier,
second card for the player, second hand for the croupier. 

In the first round, the players can see both of their cards but only the first 
card of the croupier, and they can choose whether they want more cards or if
they stand. Players can ask for as much cards as they want meanwhile they do not
surpass a score of 21, else they will loose. Once a player stands, the croupier
shows his second card and adds as much cards as needed to have a number equal or
bigger to 17, then the numbers of the player and the croupier are compared to 
know the winner.

Every player can bet whatever they want (with a minimum and a maximum depending
on the casino). If a player gets a blackjack, he obtains his bet+bet*3/2. If the
croupier first card is an ace, you can secure your bet in case the croupier could
have a blackjack. This secure is a bet max the half of your initial bet, if the
croupier has a blackjack you win secure bet*2 but loose your initial bet (tie),
if the croupier hasn't a blackjack, you loose the secure but continues with your
initial hand

To double means that you can duplicate your initial bet for receiving just one more
additional card, you can only duplicate with your first two cards. Finally, to 
separate happens when your first two cards have the same value, and you can bet them
in two distinct hands, but you also have to bet the same you bet for the first hand.

Possible outcomes:
Player has a blackjack: wins bet + bet*3/2
Croupier has a blacjack: player looses bet
Both have blackjack: tie, player recovers money without winning
Player wins croupier: wins bet*2
Same score: tie, player recovers money
If anyone surpasses 21: automatic loose"""


import random

suits = ("Diamonds","Spades","Hearts","Clubs")
ranks = ("2","3","4","5","6","7","8","9","Ten","Jack","Queen","King","Ace")
values = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,
        "Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":[1,11]}

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
        for i in range(8):
            for suit in suits:
                for rank in ranks:
                    self.all_cards.append(Cards(suit,rank))
    
    def shuffle(self):
        """Once created a deck, it allows you to shuffle it, you can change order"""
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        """Once created a deck, it allows you to take a card out
        and it's eliminated from deck"""
        return self.all_cards.pop(0)

class Hand:
    """This class is going to represent
    the hand of either dealer or player"""
    def __init__(self):
        self.hand_cards = [] # Empty list that will be completed each round
        self.hand_cards_values = [] # Empty list that will be completed each round
        self.sum_values = 0

    def add_card(self,new_card): # Adds a card either when distributing cards at the start or at hit
        self.hand_cards.append(new_card)
        self.hand_cards_values.append(new_card.value)
        self.sum_values = sum(self.hand_cards_values)

    def reset_hand(self):
        self.hand_cards, self.hand_cards_values, self.sum_values = [], [], 0

class Croupier:
    pass # I think its better to diferentiate between player and croupier


class Player:
    """This class is going to represent a player"""
    def __init__(self,name,money,hand):
        self.name = name
        self.all_cards = []
        self.money = money
        self.hand = hand

    def remove_one(self):
        """Allows to show, compare and eliminate a player card"""
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        """Allows to take cards when a player wins a round"""
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."

class Hand:
    pass
# debe tener funciones como hit, stand, double, secure y split

class Bet:
    pass 
# Pensarlo bien pero es una clase para la apuesta del jugador
# Ver si es necesaria realmente o no
 


    

