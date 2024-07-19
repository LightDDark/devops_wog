import random
from utils.utils import get_input_digit
import time


def _print_list(list_to_display):
    print("Do your best to remember the following sequence, press Enter to continue:")
    input()
    for element in list_to_display:
        print("\r" + str(element), end="")
        time.sleep(0.7)
    print("\r", end="")


def generate_sequence(difficulty):
    return random.choices(range(1, 101), k=difficulty)


def get_list_from_user(difficulty):
    print(f"Input {difficulty} number(s) that match the sequence you just saw.")
    user_input = []
    for i in range(difficulty):
        user_input.append(get_input_digit(f"Number {i+1}: ", float('-inf'), float('inf')))
    return user_input


def is_list_equal(user_input, rand_choices):
    return user_input == rand_choices


def play(difficulty):
    rand_sequence = generate_sequence(difficulty)
    _print_list(rand_sequence)
    user_input = get_list_from_user(difficulty)
    return is_list_equal(user_input, rand_sequence)
