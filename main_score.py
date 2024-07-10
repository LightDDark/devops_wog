from flask import Flask, render_template_string
from utils import SCORES_FILE_NAME
import os

app = Flask(__name__)


@app.route('/')
def score_server():
    if os.path.exists(SCORES_FILE_NAME):
        try:
            with open(SCORES_FILE_NAME, 'r') as file:
                current_score = int(file.read())
            return f"""<html>
                        <head>
                            <title>Scores Game</title>
                        </head>
                        <body>
                            <h1>The score is:</h1>
                            <div id="score">{current_score}</div>
                        </body>
                        </html>"""
        except Exception as e:
            return f"""<html>
                        <head>
                            <title>Scores Game</title>
                        </head>
                        <body>
                            <h1>ERROR:</h1>
                            <div id="score" style="color:red">{str(e)}</div>
                        </body>
                        </html>"""
    else:
        return f"""<html>
                        <head>
                            <title>Scores Game</title>
                        </head>
                        <body>
                            <h1>The score is:</h1>
                            <div id="score">{0}</div>
                        </body>
                        </html>"""


app.run(host='0.0.0.0', port=5000)
