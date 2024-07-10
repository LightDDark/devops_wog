import random
from utils import get_input_digit


def generate_number(difficulty):
    return random.randint(0, difficulty)


def get_guess_from_user(difficulty):
    return get_input_digit(f"Guess a number from 0 to {difficulty}: ", 0, difficulty)


def compare_results(user_guess, secret_number):
    return user_guess == secret_number


def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    return compare_results(user_guess, secret_number)