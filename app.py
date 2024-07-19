from games import memory_game, currency_roulette_game, guess_game
from utils.utils import get_input_digit
from front.score import add_score


def _select_game():
    menu = ("Please choose a game to play:\n"
            "\t1.\tMemory Game - a sequence of numbers will appear for 1 second and you have to\n"
            "\t  \tguess it back.\n"
            "\t2.\tGuess Game - guess a number and see if you chose like the computer\n"
            "\t3.\tCurrency Roulette - try and guess the value of random amount of USD in ILS\n")
    return get_input_digit(menu, 1, 3)


def _select_difficulty():
    return get_input_digit("Please choose a difficulty (1 - 5): ", 1, 5)


def welcome():
    username = input("Enter your username: ")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")


def start_play():
    games = [memory_game.play, guess_game.play, currency_roulette_game.play]
    game, difficulty = _select_game(), _select_difficulty()
    if games[game - 1](difficulty):
        add_score(difficulty)
