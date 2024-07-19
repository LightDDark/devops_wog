from currency_converter import CurrencyConverter
from utils.utils import get_input_digit
import random


def get_money_interval(difficulty):
    _BASE_DIFFICULTY_RANGE = 10
    seq_range = _BASE_DIFFICULTY_RANGE - difficulty
    usd_amount = random.randint(1, 100)
    c = CurrencyConverter()
    ils_amount = c.convert(usd_amount, 'USD', 'ILS')
    return [ils_amount - seq_range, ils_amount + seq_range], usd_amount


def get_guess_from_user(usd_amount):
    return get_input_digit(f"Guess a the equivalent of {usd_amount} USD in ILS: ", float('-inf'), float('inf'))


def compare_results(user_guess, winning_interval):
    return winning_interval[0] <= user_guess <= winning_interval[1]


def play(difficulty):
    winning_interval, usd_amount = get_money_interval(difficulty)
    guess = get_guess_from_user(usd_amount)
    return compare_results(guess, winning_interval)
