# we will implement a game of Nim
# we need to store game state which will be just a number of stones
# we also need to store the current player

STARTING_STONES = 21 # In Python uppercase means constant but it is not enforced
current_player = "Player 1"

# we need to loop until the game is over
while STARTING_STONES > 0:
    # print the current game state
    print(f"There are {STARTING_STONES} stones left")
    # get the player's move
    player_move = int(input(f"{current_player} would you like to remove 1 or 2 stones? "))
    # update the game state
    STARTING_STONES -= player_move
    # switch the player
    if current_player == "Player 1":
        current_player = "Player 2"
    else:
        current_player = "Player 1"

# print the winner - we use misere game rules - meaning the player who takes the last stone loses

# if current_player == "Player 1":
#     print("Player 1 wins!")
# else:
#     print("Player 2 wins!")
# simply print the current player
print(f"{current_player} wins!")