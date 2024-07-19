import os
from utils.utils import SCORES_FILE_NAME


def add_score(difficulty):
    new_points = (difficulty * 3) + 5
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'r') as f:
            current_score = int(f.read())
    else:
        current_score = 0
    current_score += new_points
    with open(SCORES_FILE_NAME, 'w') as f:
        f.write(str(current_score))
