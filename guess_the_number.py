# we will write a simple guess the number game
# we will define min and max numbers
# user will be given a number of guesses
# we will generate a random number between min and max
# we will loop until the user guesses correctly or runs out of guesses

# these numbers in advanced version could come from some storage such as a file or database
MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_GUESSES = 6 # optimal number of guesses is log2(MAX_NUMBER - MIN_NUMBER + 1) rounded up
# reminder in Python uppercase means constant but it is not enforced
guesses_left = MAX_GUESSES

# now we need to generate a random number
# for that we need to import the random module
import random # this is a built-in module so we don't need to install it with pip
# link to the documentation: https://docs.python.org/3/library/random.html

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
    guess = int(input(f"Guess a number between {MIN_NUMBER} and {MAX_NUMBER}: "))
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