
from TEST1_SIMULATION_FUNCTIONS import *
import time
import signal, os

def handler(signum, frame):
    print('60 seconds passed, exiting')


def user_interface():
    secret_number = generate_four_digit_random()

    # input("Start the game when you're ready. Enter any caracter. You have 60 seconds.")
    valid = True
    start_time = time.time()

    while valid:
        actual_time = time.time()
        if actual_time - start_time > 60:
            print("Time run out. The computer wins")
        guess = int(input("Enter a four digit number: "))
        if guess == 8086:
            print(f"This was a cheat code. The secret number is {secret_number}")
            return
        if valid_guess(guess) == False:
            print("This was not a valid guess. The computer wins.")
            return
        if guess == secret_number:
            print("Yess, you guessed corectly the secret number. You won!")
        codes, runners = number_of_codes_and_runners(guess, secret_number)
        print(f"{codes} codes and {runners} runners")


user_interface()