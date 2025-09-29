import random
board = ['|   |','|   |','|   |',
             '|   |','|   |','|   |','|   |','|   |','|   |']
board_map = ['| 1 |','| 2 |','| 3 |',
             '| 4 |','| 5 |','| 6 |','| 7 |','| 8 |','| 9 |']



reset_board = ['|   |','|   |','|   |',
             '|   |','|   |','|   |','|   |','|   |','|   |']
reset_board_map = ['| 1 |','| 2 |','| 3 |',
             '| 4 |','| 5 |','| 6 |','| 7 |','| 8 |','| 9 |']


positions = {1: board[0], 2: board[1], 3: board[2],
             4: board[3], 5: board[4], 6: board[5],
             7: board[6], 8: board[7], 9: board[8],}


player_1_answer = "| X |"
player_2_answer = "| O |"

def generate_board():
    # Generate an interactive board that can be changed according to users' input
    board_1 = " ".join(board[0:3])
    board_2 = " ".join(board[3:6])
    board_3 = " ".join(board[6:])
    board_line = ' ___   ___   ___'
    print("\n".join((board_line,board_1,board_line,board_2,board_line,board_3,board_line)))

def generate_board_map():
    # Generate an board map that changes according to users' input and more visual available cell selection
    board_1_map = " ".join(board_map[0:3])
    board_2_map = " ".join(board_map[3:6])
    board_3_map = " ".join(board_map[6:])
    board_line = ' ___   ___   ___'
    print("\n".join((board_line,board_1_map,board_line,board_2_map,board_line,board_3_map,board_line)))

def check_play(position):
    pass

def check_win():
    pass

def check_tie():
    pass

def play_again():
    pass

def player_start():
    player_options = [0, 1]
    start_answers = ['player 1', 'player 2', 'random']
    start = input("Select start player: \n" \
    "player 1 | player 2 | random \n")
    while start not in start_answers:
        print("Invalid answer, please introduce a valid answer (player 1, player 2 or random)")
        start = input("Select start player: \n player 1 | player 2 | random \n")
    if start == 'player 1':
        generate_board_map()
        generate_board()
        player_1_play()
    elif start == 'player 2':
        generate_board_map()
        generate_board()
        player_2_play()
    else:
        start = random.choice(player_options)
        if start:
            print("Starts player 1")
            generate_board_map()
            generate_board()
            player_1_play()
        else:
            print("Starts player 2")
            generate_board_map()
            generate_board()
            player_2_play()

def player_1_play():
    valid_player_answers = [1,2,3,4,5,6,7,8,9]
    selection = int(input("Player 1, select position (use number map above to see available positions): "))
    valid_position = check_play(selection)
    while selection not in valid_player_answers and valid_position != True:
        selection = int(input("Invalid position, player 1 select again: "))
        valid_position = check_play(selection)
    
    board[selection-1] = player_1_answer
    board_map[selection-1] = player_1_answer
    positions[selection] = player_1_answer

    win = check_win()
    tie = check_tie()

    if win == True:
        print("Player 1 win!")
        generate_board()
        play_again()
    elif tie == True:
        print("It's a tie!")
        generate_board()
        play_again()
    else:
        print("It's player 2 turn")
        generate_board_map()
        generate_board()
        player_2_play()
  

def player_2_play():
    valid_player_answers = [1,2,3,4,5,6,7,8,9]
    selection = int(input("Player 2, select position (use number map above to see available positions): "))
    valid_position = check_play(selection)
    while selection not in valid_player_answers and valid_position != True:
        selection = int(input("Invalid position, player 2 select again: "))
        valid_position = check_play(selection)
    
    board[selection-1] = player_2_answer
    board_map[selection-1] = player_2_answer
    positions[selection] = player_2_answer

    win = check_win()
    tie = check_tie()

    if win == True:
        print("Player 2 win!")
        generate_board()
        play_again()
    elif tie == True:
        print("It's a tie!")
        generate_board()
        play_again()
    else:
        print("It's player 1 turn")
        generate_board_map()
        generate_board()
        player_1_play()    


valid_answers = ['y','n']
answer = input("Initiate tic-tac-toe (y/n)?: ")
while answer not in valid_answers:
    print("Invalid answer, please introduce correct answer")
    answer = input("Initiate tic-tac-toe (y/n)?: ")

if answer == 'y':
    player_start()
elif answer == 'n':
    print("Good bye!")

