import random
board = ['|   |','|   |','|   |',
             '|   |','|   |','|   |','|   |','|   |','|   |']

positions = {'upper left': board[0], 'upper center': board[1], 'upper right': board[2],
             'middle left': board[3], 'middle center': board[4], 'middle right': board[5],
             'lower left': board[6], 'lower center': board[7], 'lower right': board[8],}

player_1_answer = "| X |"
player_2_answer = "| O |"

def generate_board():
    # Generate an interactive board that can be changed according to users' input
    board_1 = " ".join(board[0:3])
    board_2 = " ".join(board[3:6])
    board_3 = " ".join(board[6:])
    board_line = ' ___   ___   ___'
    print("\n".join((board_line,board_1,board_line,board_2,board_line,board_3,board_line)))

def player_start():
    player_options = [0, 1]
    start_answers = ['player 1', 'player 2', 'random']
    start = input("Select start player: \n" \
    "player 1 | player 2 | random \n")
    while start not in start_answers:
        print("Invalid answer, please introduce a valid answer (player 1, player 2 or random)")
        start = input("Select start player: \n player 1 | player 2 | random \n")
    if start == 'player 1':
        generate_board()
        player_1_play()
    elif start == 'player 2':
        generate_board()
        player_2_play()
    else:
        start = random.choice(player_options)
        if start:
            print("Starts player 1")
            generate_board()
            player_1_play()
        else:
            print("Starts player 2")
            generate_board()
            player_2_play()

def player_1_play():
    pass #selection = variable indicating position selected by the player
def player_2_play():
    pass    
def check_play():
    pass

def check_win():
    pass
'''check_play() and check_win() have to be inside player 1 and player 2, the idea is once
    each player have selected its answer, check if the ubication of the answer is valid using the dictionary
    and whether any of the players has won (check_win())or if there is a tie check_play() when there are not
    possible options. After each player selecting their answer and making all necessary corroborations, end
    either player 1 or 2 func calling the opposite player func'''
# Function to determine and include player 1 and 2 answer
# Function to determine whether that an answer is valid or not depending on the content
# Function to determine if a player has won

valid_answers = ['y','n']
answer = input("Initiate tic-tac-toe (y/n)?: ")
while answer not in valid_answers:
    print("Invalid answer, please introduce correct answer")
    answer = input("Initiate tic-tac-toe (y/n)?: ")

if answer == 'y':
    player_start()
elif answer == 'n':
    print("Good bye!")

