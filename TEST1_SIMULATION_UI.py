
from TEST1_SIMULATION_FUNCTIONS import *




def user_interface():
    secret_number = generate_four_digit_random()

    input("Start the game when you're ready. Enter any caracter")
    valid = True
    while valid:
        guess = int(input("Enter a four digit number: "))
        if guess == 8086:
            print(f"This was a cheat code. The secret number is {secret_number}")
        if valid_guess(guess) == False:
            print("This was not a valid guess. The computer wins.")
            return
        if guess == secret_number:
            print("Yess, you guessed corectly the secret number. You won!")
        codes, runners = number_of_codes_and_runners(guess, secret_number)
        print(f"{codes} codes and {runners} runners")



user_interface()