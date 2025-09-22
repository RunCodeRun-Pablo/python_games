from random import randint
valid_answer = ['y','n']

def guess_the_number(player_num:int):
    selected_num = randint(1,100)
    nums_list = []
    while selected_num != player_num:
        if player_num < 1 or player_num > 100:
            player_num = int(input("Number has to be between 1 and 100: "))
        
        nums_list.append(player_num)

        if len(nums_list) == 1:
            if abs(selected_num-player_num) <= 10:
                player_num = int(input("Warm!, introduce new number: "))
            else:
                player_num = int(input("Cold!, introduce new number: "))
        elif abs(selected_num - player_num) < abs(selected_num - nums_list[-2]):
            player_num = int(input('WARMER, introduce new number: '))
        else:
            player_num = int(input('COLDER, introduce new number: ')) 
    print("You guessed it!")
    print(f"It took you {len(nums_list)} guesses")


    player_answer = input("Want to play again (y/n)?: ")
    while player_answer not in valid_answer:
        print("Please introduce valid answer")
        player_answer = input("Want to play GuessTheNumber?(y/n): ")

    if player_answer == 'y':
            player_num = int(input("Introduce a number: "))
            guess_the_number(player_num)
    elif player_answer == 'n':
            print("Nice to meet you, good bye!")
            


        
player_answer = input("Want to play GuessTheNumber?(y/n): ")
while player_answer not in valid_answer:
     print("Please introduce valid answer")
     player_answer = input("Want to play GuessTheNumber?(y/n): ")

if player_answer == 'y':
        player_num = int(input("Introduce a number: "))
        guess_the_number(player_num)
elif player_answer == 'n':
        print("Nice to meet you, good bye!")









