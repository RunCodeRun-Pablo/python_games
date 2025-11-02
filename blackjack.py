"""Blackjack rules:
It is played with 4 decks of 52 cards, and consists in obtaining
a sum of 21 points without surpassing this amount. Each player plays
against the crupier, and either player or croupier have distinct rules
croupier has to ask for cards whenever his score is less than 16, and
stands if it is 17 or more.

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
        if type(new_card.value) != list:
            self.hand_cards.append(new_card)
            self.hand_cards_values.append(new_card.value)
            self.sum_values = sum(self.hand_cards_values)
        else:
            self.hand_cards.append(new_card)
            if self.sum_values > 10:
                self.hand_cards_values.append(new_card.value[0])
                self.sum_values = sum(self.hand_cards_values)
            elif self.sum_values <= 10:
                self.hand_cards_values.append(new_card.value[1])
                self.sum_values = sum(self.hand_cards_values)     

    def reset_hand(self): # Resets the hand after each round
        self.hand_cards, self.hand_cards_values, self.sum_values = [], [], 0

class Bet:
    """This class defines the money a player bets
    each round and will be modified by diferent
    player methods"""
    def __init__(self,value):
        self.value = value

    def bet_secure(self): # To establish a secure for bet
        self.secure = self.value / 2

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
            return True
        else:
            print("Not enough money for this bet")
            return False
        
    def p_income(self): #Adds money to the player account
        try:
            self.account = self.bet.value + self.account
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
        self.bet.bet_secure()
        self.account -= self.bet.secure
        print(f"Your actual bet is {self.bet.value}€ plus {self.bet.secure}€ secure")
        
    def split(self): # Splits initial bet into two bets, a list of bets for example
        self.account = self.account - self.bet.value
        self.bet = [self.bet,self.bet]
        hand1,hand2 = Hand(),Hand()
        hand1.add_card(self.hand.hand_cards[0])
        hand2.add_card(self.hand.hand_cards[1])
        self.hand = [hand1,hand2]
        print("You have splitted bets:\n" \
        f"card 1 bet: {self.bet[0].value}€\n"\
        f"card 2 bet: {self.bet[1].value}€\n"\
        f"cash in account: {self.account}€")

deck = Deck()
deck.shuffle()
croupier = Croupier("Croupier")

initiate = True
start_game = input("Initiate blackjack game?(y/n): ")

def define_player():
    """Should allow to define player class attribute
    of user, first introducing a name and then selecting
    an initial money amount for account among the distinct
    options"""
    opt_account = [100,500,1000]
    player_name = input("Please introduce a player name: ")

    defined_player = False
    while not defined_player:
        try:
            player_account = int(input("Please select an initial money account: \n [100] [500] [1000] \n"))
            defined_player = True
        except ValueError:
            continue

    while player_account not in opt_account:
        player_account = int(input("Please enter a valid money amount: \n [100] [500] [1000] \n"))
    return player_name, player_account

def card_distr():
    """This makes initial distribution of cards to each player"""
    player.p_hand()
    croupier.c_hand()
    player.hand.add_card(deck.deal_one())
    croupier.hand.add_card(deck.deal_one())
    player.hand.add_card(deck.deal_one())
    croupier.hand.add_card(deck.deal_one())

def set_bet():
    """This function will set the player's bet"""
    while True:
        try:
            player_bet = int(input("Please enter a bet for this round: "))
            if player_bet > 0:
                return player_bet
            else:
                print("A valid bet should be entered")
        except ValueError:
            continue

def play_round(p_hand,c_hand):
    """This function is going to check if more cards
    are added to the hand and then add cards to the 
    croupier hand and return values of each hand to be
    compared in comp_values()"""

    answ = ['y','n']

    if 'dup_answ' in globals():
        if dup_answ == "y":
            morecards = input("You duplicated and can add only one more card\nWant to add an additional card?(y/n): ")
            while morecards not in answ:
                morecards = input("Invalid answer\nWant to add an additional card?(y/n): ")
            if morecards == 'y':
                p_hand.add_card(deck.deal_one())            
    else:
        cycle = True
        while cycle:
            if p_hand.sum_values < 21:
                morecards = input("Want to add an additional card?(y/n): ")
                while morecards not in answ:
                    morecards = input("Invalid answer\nWant to add additional card?(y/n): ")
                if morecards == 'y':
                    p_hand.add_card(deck.deal_one())
                    print(f"New card added: {p_hand.hand_cards[-1]}")
                    print(f"Actual player hand value: {p_hand.sum_values}")
                elif morecards == 'n':
                    cycle = False
            else:
                cycle = False

    while c_hand.sum_values < 17:
        c_hand.add_card(deck.deal_one())

    print("Player cards:")
    for p_card in p_hand.hand_cards:
        print(p_card)
    print(f"Player value: {p_hand.sum_values}")
    
    print("Croupier cards:")
    for c_card in c_hand.hand_cards:
        print(c_card)
    print(f"Croupier values {c_hand.sum_values}")

    return p_hand.sum_values,c_hand.sum_values

def comp_values(p_value, c_value):
    """This function is going to compare values of both
    hands and determine if player wins or not and return
    either win, lost or tie which will be passed to ret_money()"""

    if p_value > 21:
        print("Surpassed 21!, player looses")
        return "Lost"
    
    if not p_value > 21 and c_value > 21:
        print("Surpassed 21! croupier looses")
        return "Win"

    if not p_value > 21 and not c_value > 21:
        if p_value == c_value:
            print("It's a tie, player recovers money")
            return "Tie"
        elif p_value > c_value:
            print("Player has higher value! Player wins!")
            return "Win"
        else:
            print("Player has lower value! Player looses!")
            return "Lost"  
    
def ret_money(player_win):
    """This function is going to return the money of the bet
    and the secure to the player depending on the input"""
    pass

while initiate:
    if start_game == "y":
        print("Game initiated")
        initiate = False
        name,account = define_player()
        player = Player(name,account)
    elif start_game == "n":
        print("See you next time!")
        initiate = False
    else:
        start_game = input("Invalid answer, please select y or n: ")

round_answers = {"y": True, "n": False} # Will make easier to transform player answer
answ = True

while answ: 
    print("Round initiated")

    if player.account > 0: # First check, if player has enough money in the account and if the bet can be made
        bet_success = player.p_bet(set_bet())
        while not bet_success:
            bet_success = player.p_bet(set_bet())
    else:
        answ = False
        print("You lost all your money!")
        break

    card_distr() 
    print(f"Your cards: [{player.hand.hand_cards[0]}][{player.hand.hand_cards[1]}]\nYour value: [{player.hand.sum_values}]")
    print(f"Croupier cards: [{croupier.hand.hand_cards[0]}]")
    
    
    if player.hand.sum_values == 21: # Second check, if initial blackjack happens
        print("BLACKJACK!")
        if player.hand.sum_values > croupier.hand.sum_values:
            print(f"Your cards: [{player.hand.hand_cards[0]}][{player.hand.hand_cards[1]}]\nYour value: [{player.hand.sum_values}]")
            print(f"Croupier cards: [{croupier.hand.hand_cards[0]}][{croupier.hand.hand_cards[1]}]\nCroupier actual value: [{croupier.hand.sum_values}]")
            print(f"You win this round, total money won: {player.bet.value+player.bet.value*1.5}")
            player.bet.value += player.bet.value*1.5
            player.p_income()

        elif player.hand.sum_values == croupier.hand.sum_values:
            print(f"Your cards: [{player.hand.hand_cards[0]}][{player.hand.hand_cards[1]}]\nYour value: [{player.hand.sum_values}]")
            print(f"Croupier cards: [{croupier.hand.hand_cards[0]}][{croupier.hand.hand_cards[1]}]\nCroupier actual value: [{croupier.hand.sum_values}]")
            print(f"It is a tie!, total money won: {player.bet.value}")
            player.p_income()

    if croupier.hand.hand_cards[0].ranks == "Ace" and player.account >= player.bet.value/2: # Check if player wants to secure bet
        sec_answ = input("Want to secure your bet?(y/n): ")

        while sec_answ not in round_answers.keys():
            sec_answ = input("Please introduce a valid response\nDo you want to secure bet?(y/n): ")

        if round_answers[sec_answ] == True: # Remember to later include a check if secure should be lost or not
            player.secure()

    
    if (player.hand.hand_cards_values[0] == player.hand.hand_cards_values[1] or player.hand.hand_cards_values[1] == 1) and player.account >= player.bet.value: # Check if player has two equal cards and wants to split
        spl_answ = input("Want to split your bet?(y/n): ")

        while spl_answ not in round_answers.keys():
            spl_answ = input("Please introduce a valid response\nDo you want to split your bet?(y/n): ")
        
        if round_answers[spl_answ] == True:
            player.split() # Depending on if split or not two pathways can be followed

    if 'spl_answ' in globals() and round_answers[spl_answ] == True:
        print("Hand 1 results:")
        p_sum, c_sum = play_round(player.hand[0],croupier.hand)
        retmoney = comp_values(p_sum, c_sum)
        ret_money(retmoney)
        print("Hand 2 results:")
        p_sum, c_sum = play_round(player.hand[1],croupier.hand)
        retmoney = comp_values(p_sum, c_sum)
        ret_money(retmoney)

    if 'spl_answ' not in globals() or ('spl_answ' in globals() and round_answers[spl_answ] != True):
        if player.account >= player.bet.value:
            dup_answ = input("Do you want to duplicate your bet?(y/n): ")

            while dup_answ not in round_answers.keys():
                dup_answ = input("Please introduce a valid response\nDo you want to duplicate your bet?(y/n): ")
            
            if round_answers[dup_answ] == True:
                player.duplicate()
                p_sum, c_sum = play_round(player.hand,croupier.hand)
                retmoney = comp_values(p_sum, c_sum)
                ret_money(retmoney)
        else:
            p_sum, c_sum = play_round(player.hand,croupier.hand)
            retmoney = comp_values(p_sum, c_sum)
            ret_money(retmoney)
            



# Only lacks function detecting if 







        # while loop after card_distr() to check for player answer and options
    # Another while loop after player play to check for croupier play





    

    # After a round finishes player gets asked
    rnd_answ = input("Want to play another round?(y/n): ")
    while rnd_answ not in round_answers.keys():
        rnd_answ = input("Please enter valid answer \nWant to play another round?(y/n): ")

    answ = round_answers[rnd_answ]

print("Thank you for playing!\nCome back soon!")

# This is just for proofs
card1 = Cards("Diamonds","Ace")
card2 = Cards("Spades","Ace")
card3 = Cards("Diamonds", "6")
deck = Deck()

player = Player("Pablo", 500)
player.p_hand()
croupier = Croupier("Croupier")
croupier.c_hand()



player.hand.add_card(card1)
player.hand.add_card(card2)
croupier.hand.add_card(card1)
croupier.hand.add_card(card2)


p_value, c_value  = play_round(player.hand,croupier.hand)

comp_values(p_value,c_value)



            
