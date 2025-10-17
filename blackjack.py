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

    def reset_hand(self): # Resets the hand after each round
        self.hand_cards, self.hand_cards_values, self.sum_values = [], [], 0

class Bet:
    """This class defines the money a player bets
    each round and will be modified by diferent
    player methods"""
    def __init__(self,value):
        self.value = value

    def add_m(self,money): # To add more money to the bet if possible
        self.value = self.value + money

    def __str__(self):
        return f"Your bet is {self.value}€"
    
    def reset(self): # Resets the bet, although maybe its not necessary
        self.value = 0
        

class Croupier:
    
    def __init__(self,name):
        self.name = name
    def c_hand(self): #Defines a hand for the croupier
        self.hand = Hand()
       

class Player:
    """This class is going to represent a player, it should be able
    of hitting, stand, double, secure or split, initial ammount of money
    will be asked for the player when starts from a list."""
    def __init__(self,name,account):
        self.name = str(name)
        self.account = int(account)

    def p_hand(self): # Establish a hand attribute for the player
        self.hand = Hand()
    
    def p_bet(self,money): # Establish a bet attribute for the player if it has enough money

        if money <= self.account:
            self.bet = Bet(money)
            self.account = self.account - money
            print(f"You bet {self.bet.value}$, cash in account: {self.account}$")
        else:
            print("Not enough money for this bet")
        
    def p_income(self): #Adds money to the player account
        try:
            self.account = self.bet.value + self.bet.secure
            + self.account
            print(f"You won {self.bet.value}€")
            self.bet = 0
        except AttributeError:
            return f"{self.name} has no bet"

    def duplicate(self): # Duplicates bet
        try:
            self.account = self.account-self.bet.value    
            self.bet.value = self.bet.value*2
            print("You have duplicated your bet,\n" \
            f"actual bet: {self.bet.value}€\n" \
            f"cash in account: {self.account}€")
        except AttributeError:
            return f"{self.name} has no bet"

    def secure(self): # Adds a secure to bet
        print(f"Your actual bet is {self.bet.value}€ plus {self.bet.value/2}€ secure")
        self.bet.value = self.bet.value + (self.bet.value / 2)
        
    def split(self): # Splits initial bet into two bets, a list of bets for example
        self.account = self.account - self.bet.value
        self.bet = [self.bet,self.bet]
        print("You have splitted bets:\n" \
        f"card 1 bet: {self.bet[0].value}€\n"\
        f"card 2 bet: {self.bet[1].value}€\n"\
        f"cash in account: {self.account}€")

    
deck = Deck()
deck.shuffle()
croupier = Croupier("Croupier")

initiate = True
start_game = input("Initiate blackjack game?(y/n): ")

while initiate:
        if start_game == "y":
            print("Game initiated")
            initiate = False
        elif start_game == "n":
            print("See you next time!")
            initiate = False
        else:
            start_game = input("Invalid answer, please select y or n: ")


