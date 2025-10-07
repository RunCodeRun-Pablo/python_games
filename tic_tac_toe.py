import random

# Board games
board = ['|   |','|   |','|   |',
             '|   |','|   |','|   |','|   |','|   |','|   |']
board_map = ['| 1 |','| 2 |','| 3 |',
             '| 4 |','| 5 |','| 6 |',
             '| 7 |','| 8 |','| 9 |']

valid_answers = ['y','n']
valid_player_answers = ['1','2','3','4','5','6','7','8','9']
player_1_answer = "| X |"
player_2_answer = "| O |"
player_1_win = ["| X |", "| X |", "| X |"]
player_2_win = ["| O |", "| O |", "| O |"]



def generate_board():
    """Generate an interactive board that can be changed according to users' input"""
    board_1 = " ".join(board[0:3])
    board_2 = " ".join(board[3:6])
    board_3 = " ".join(board[6:])
    board_line = ' ___   ___   ___'
    print("\n".join((board_line,board_1,board_line,board_2,board_line,board_3,board_line)))

def generate_board_map():
    """Generate an board map that changes according to users' input and more visual available cell selection"""
    board_1_map = " ".join(board_map[0:3])
    board_2_map = " ".join(board_map[3:6])
    board_3_map = " ".join(board_map[6:])
    board_line = ' ___   ___   ___'
    print("\n".join((board_line,board_1_map,board_line,board_2_map,board_line,board_3_map,board_line)))

def check_play(position):
    """Function determines whether an option is valid or not and then removes it to avoid picking it again"""
    if position in valid_player_answers:
        valid_player_answers.remove(position)
        return True
    return False

def check_win():
    """Check if a player has won"""
    # Check horizontals
    if board[0:3] == player_1_win or board[3:6] == player_1_win or board[6:] == player_1_win:
        return 'player 1'
    elif board[0:3] == player_2_win or board[3:6] == player_2_win or board[6:] == player_2_win:
        return 'player 2'
    # Check verticals
    elif board[::3] == player_1_win or board[1::3] == player_1_win or board[2::3] == player_1_win:
        return 'player 1'
    elif board[::3] == player_2_win or board[1::3] == player_2_win or board[2::3] == player_2_win:
        return 'player 2'
    # Check diagonals
    elif board[::4] == player_1_win or board[2:7:2] == player_1_win:
        return 'player 1'
    elif board[::4] == player_2_win or board[2:7:2] == player_2_win:
        return 'player 2'


def full_board():
    """Function is called when no more options (no items in valid_player_answers) and determines if there is a tie or someone has won"""
    win = check_win()
    if win == 'player 1':
        print("Player 1 wins!")
        play_again()
    elif win == 'player 2':
        print("Player 2 wins")
        play_again()
    else:
        print("It's a tie!")
        play_again()


def play_again():
    """In case game repeats, reset board games"""
    reset_board = ['|   |','|   |','|   |',
                 '|   |','|   |','|   |','|   |','|   |','|   |']
    reset_board_map = ['| 1 |','| 2 |','| 3 |',
                 '| 4 |','| 5 |','| 6 |','| 7 |','| 8 |','| 9 |']
    reset_answers = ['1','2','3','4','5','6','7','8','9']

    global board, board_map, valid_player_answers

    again_answer = input("Want to play another game? (y/n): ")

    while again_answer not in valid_answers:
        print("Invalid answer, please introduce correct answer")
        again_answer = input("Want to play another game (y/n)?: ")

    if again_answer == 'y':
        board = reset_board
        board_map = reset_board_map
        valid_player_answers = reset_answers
        player_start()
    elif again_answer == 'n':
        print("Good bye!")


def player_start():
    """Determines which player starts the game"""
    player_options = [0, 1]
    start_answers = ['player 1', 'player 2', 'random']
    start = input("Select start player: \n" \
    "player 1 | player 2 | random \n")
    while start not in start_answers:
        print("Invalid answer, please introduce a valid answer (player 1, player 2 or random)")
        start = input("Select start player: \n player 1 | player 2 | random \n")
    if start == 'player 1':
        player_1_play()
    elif start == 'player 2':
        player_2_play()
    else:
        start = random.choice(player_options)
        if start:
            print("Starts player 1")
            player_1_play()
        else:
            print("Starts player 2")
            player_2_play()


def player_1_play():
    """Function to determine if player 1 answer is valid, save it and determine if there's a win, tie or game continues"""
    generate_board_map()
    selection = input("Player 1, select position (use number map above to see available positions): ")
    valid_position = check_play(selection)
    while valid_position != True:
        selection = input("Invalid position, player 1 select again: ")
        valid_position = check_play(selection)

    board[int(selection)-1] = player_1_answer
    board_map[int(selection)-1] = player_1_answer

    if not valid_player_answers:
        full_board()
        generate_board()
    else:
        win = check_win()

        if win == 'player 1':
            print("Player 1 wins!")
            generate_board()
            play_again()
        else:
            print("It's player 2 turn")
            generate_board()
            player_2_play()
 

def player_2_play():
    """Function to determine if player 2 answer is valid, save it and determine if there's a win, tie or game continues"""
    generate_board_map()
    selection = input("Player 2, select position (use number map above to see available positions): ")
    valid_position = check_play(selection)
    while selection not in valid_player_answers and valid_position != True:
        selection = input("Invalid position, player 2 select again: ")
        valid_position = check_play(selection)
    
    board[int(selection)-1] = player_2_answer
    board_map[int(selection)-1] = player_2_answer

    if not valid_player_answers:
        full_board()
        generate_board()
    else:
        win = check_win()

        if win == 'player 2':
            print("Player 2 wins!")
            generate_board()
            play_again()
        else:
            print("It's player 1 turn")
            generate_board()
            player_1_play()


answer = input("Initiate tic-tac-toe (y/n)?: ")
while answer not in valid_answers:
    print("Invalid answer, please introduce correct answer")
    answer = input("Initiate tic-tac-toe (y/n)?: ")

if answer == 'y':
    player_start()
elif answer == 'n':
    print("Good bye!")