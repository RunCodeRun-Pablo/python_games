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

deck = Deck()
player_1 = Player("player 1")
player_2 = Player("Player 2")

deck.shuffle()

for i in range(len(deck.all_cards) // 2):
    player_1.add_cards(deck.card())
    player_2.add_cards(deck.card())
    
game_on = True
round = 0

while game_on:

    round += 1
    print(f"Round {round}")

    if len(player_1.all_cards) == 0:
        print("Player 1 ran out of cards, player 2 wins")
        game_on = False
        break

    if len(player_2.all_cards) == 0:
        print("Player 2 ran out of cards, player 1 wins")
        game_on = False
        break

    player_1_cards = []
    player_1_cards.append(player_1.remove_cards())
    
    player_2_cards = []
    player_2_cards.append(player_2.remove_cards())
    
    at_war = True

    while at_war:


        if player_1_cards[-1].value > player_2_cards[-1].value:

            player_1.add_cards(player_1_cards)
            player_1.add_cards(player_2_cards)
            
            
            at_war = False
        
        elif player_1_cards[-1].value < player_2_cards[-1].value:

          
            player_2.add_cards(player_1_cards)
            player_2.add_cards(player_2_cards)
            
            # No Longer at "war" , time for next round
            at_war = False

        else:
            print('WAR!')

            if len(player_1.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player_2.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break
            else:
                for num in range(5):
                    player_1_cards.append(player_1.remove_cards())
                    player_2_cards.append(player_2.remove_cards())




    







    






