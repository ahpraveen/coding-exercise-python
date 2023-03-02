''''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''

input_to_enter_game = input("do you want to play game (yes/no) ")

while input_to_enter_game == "yes":
    option_to_play_game_again = False
    input_player_a = input("input to play your game player a  ")
    input_player_b = input("input to play your game player b  ")
    if input_player_a == "rock" and input_player_b == "scissors":
        print("Congrats! player a wins")
    elif input_player_a == "paper" and input_player_b == "scissors":
        print("Congrats! player b wins")
    elif input_player_a == "scissors" and input_player_b == "paper":
        print("Congrats! player a wins")
    elif input_player_a == "rock" and input_player_b == "paper":
        print("Congrats! player b wins")
    elif input_player_a == "paper" and input_player_b == "rock":
        print("Congrats! player a wins")
    elif input_player_a == "rock" and input_player_b == "rock" \
            or input_player_a == "scissors" and input_player_b == "scissors" \
            or input_player_a == "paper" and input_player_b == "paper":
        print("draw")
    input_to_enter_game = input("do you want to play game again (yes/no) ")
    if input_to_enter_game == "yes":
        continue
    else:
        print("Thank you! for participating the game")
        break
