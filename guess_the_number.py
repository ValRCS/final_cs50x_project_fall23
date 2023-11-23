# we will write a simple guess the number game
# we will define min and max numbers
# user will be given a number of guesses
# we will generate a random number between min and max
# we will loop until the user guesses correctly or runs out of guesses

# now we need to generate a random number
# for that we need to import the random module
import random # this is a built-in module so we don't need to install it with pip
# link to the documentation: https://docs.python.org/3/library/random.html

# these numbers in advanced version could come from some storage such as a file or database
MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_GUESSES = 6 # optimal number of guesses is log2(MAX_NUMBER - MIN_NUMBER + 1) rounded up
# reminder in Python uppercase means constant but it is not enforced

# example of PvC game - Player vs Computer

def main(): # again after : we need to indent
    guesses_left = MAX_GUESSES
    # we will use the randint function
    random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    # print for testing
    print(f"Random number is {random_number}") # TODO remove when done testing

    # let's ask the user for their guess
    # we will use a while loop
    # now we will put this into while loop
    # our while loop will run until the user guesses correctly or runs out of guesses
    while guesses_left > 0:
        # let's print the number of guesses left
        print(f"You have {guesses_left} guesses left")
        try:
            guess = int(input(f"Guess a number between {MIN_NUMBER} and {MAX_NUMBER}: "))
            # this line will be only reached if int() does not throw an exception
            print(f"You guessed {guess}") # again only runs when int() does not throw an exception
        except ValueError:
            print("You can only enter a number")
            continue # this goes back to the beginning of the loop without decrementing guesses_left

        if guess < MIN_NUMBER or guess > MAX_NUMBER:
            print(f"Your guess is out of range")
            continue # returns to the beginning of the loop without decrementing guesses_left

        if guess == random_number:
            print("You guessed correctly congratulations!")
            # here I could set a flag to indicate that the user guessed correctly
            break # we do not need to be in loop anymore since we guessed correctly
        elif guess < random_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        # now decrease the number of guesses left
        guesses_left -= 1 # same as guesses_left = guesses_left - 1
    print("Game over") # this will run when the loop ends

# now we need to call main using main guard
if __name__ == "__main__": # this means main() will only run if this file is run directly
    main()