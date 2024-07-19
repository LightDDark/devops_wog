import os

SCORES_FILE_NAME = 'Scores.txt'
BAD_RETURN_CODE = 404


def get_input_digit(prompt, lower_bound, upper_bound):
    while True:
        user_input = input(prompt)
        if str.isdigit(user_input) and lower_bound <= int(user_input) <= upper_bound:
            return int(user_input)
        else:
            print(f"Please enter a number between {lower_bound} and {upper_bound} (inclusive).")


def screen_cleaner():
    _ = os.system('cls' if os.name == 'nt' else 'clear')
