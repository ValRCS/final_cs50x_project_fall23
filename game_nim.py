# we will implement a game of Nim
# we need to store game state which will be just a number of stones
# we also need to store the current player
MIN_MOVE = 1
MAX_MOVE = 3


def main():
    STARTING_STONES = 21 # In Python uppercase means constant but it is not enforced
    current_player = "Player 1"

    # we need to loop until the game is over
    while STARTING_STONES > 0:
        # print the current game state
        print(f"There are {STARTING_STONES} stones left")
        # get the player's move

        # we need to validate the player's move
        try:
            player_move = int(input(f"{current_player} you can remove at least {MIN_MOVE} and at most {MAX_MOVE} stones? "))
            if player_move < MIN_MOVE or player_move > MAX_MOVE:
                print(f"You can only remove {MIN_MOVE} or {MAX_MOVE} stones")
                continue # we go back to the top of the loop
        except ValueError: # this error could happen if int is called on a string that is not a number
            print("You can only enter a number")
            continue # again we go back to the top of the loop
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

# so called main guard it runs if the file is run directly but not if it is imported
if __name__ == "__main__":
    # could do other stuff here such as configure logging
    main()
    # could do other stuff here such as clean up