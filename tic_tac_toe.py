def generate_board():
    # Generate an interactive board that can be changed according to users' input
    board = ['|   |','|   |','|   |',
             '|   |','|   |','|   |','|   |','|   |','|   |']
    board_1 = " ".join(board[0:3])
    board_2 = " ".join(board[3:6])
    board_3 = " ".join(board[6:])
    board_line = ' ___   ___   ___'
    print("\n".join((board_line,board_1,board_line,board_2,board_line,board_3,board_line)))

# Next function to generate accept users input
# Function to determine whether that an answer is valid or not depending on the content

valid_answers = ['y','n']
answer = input("Initiate tic-tac-toe (y/n)?: ")
while answer not in valid_answers:
    print("Invalid answer, please introduce correct answer")
    answer = input("Initiate tic-tac-toe (y/n)?: ")

if answer == 'y':
    generate_board()

