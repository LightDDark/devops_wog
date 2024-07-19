from flask import Flask
from utils.utils import SCORES_FILE_NAME
import os

app = Flask(__name__)


@app.route('/')
def score_server():
    current_score = 0
    error = None
    if os.path.exists(SCORES_FILE_NAME):
        try:
            with open(SCORES_FILE_NAME, 'r') as file:
                current_score = int(file.read())
        except Exception as e:
            error = str(e)
    return f"""<html>
                    <head>
                        <title>Scores Game</title>
                    </head>
                    <body>
                        <h1>{"ERROR:" if error else "The score is:"}</h1>
                        <div id="score" style={"color:red" if error else ""}>{0 if error else current_score}</div>
                    </body>
                    </html>"""


app.run(host='0.0.0.0', port=5000)
