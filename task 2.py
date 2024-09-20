import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("I'm thinking of a number between 1 and 100. Try to guess it!")

    while not guessed_correctly:
        try:
            # Prompt user for their guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Compare the guess to the number
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed the number {number_to_guess} correctly.")
                print(f"It took you {attempts} attempts.")
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Run the game
guess_the_number()
