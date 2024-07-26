# World Of Games (wog) Repository

Welcome to the **World Of Games (wog)** repository! This project combines gaming fun with DevOps practices. Here, we'll explore three CLI-based games, a Flask-based web score display, and the DevOps infrastructure that ties it all together.

## Table of Contents

1. [Introduction](#introduction)
2. [Games](#games)
3. [Web Score Display](#web-score-display)
4. [DevOps Pipeline](#devops-pipeline)
5. [Getting Started](#getting-started)
---

## Introduction

The **World Of Games (wog)** repository is designed to demonstrate my DevOps skills. It comprises three main components:

1. **CLI Games**: Three interactive command-line games where players can earn points. The points are saved to a file for persistence.

2. **Web Score Display**: Using Flask to showcase the game scores in a web interface.

3. **DevOps Infrastructure**: The heart of this repository! It includes Dockerfiles, Docker Compose, automated testing with Selenium, and a Jenkins pipeline for seamless deployment.

---

## Games

### 1. Guess Game

The Guess Game module challenges players to guess a secret number. Here's how it works:

1. The game generates a random number between 0 and a specified difficulty level.
2. Players are prompted to input a number within the range of 0 to the difficulty.
3. The game compares the player's input with the generated secret number.
4. If they match, the player wins!

### 2. Currency Roulette

In the Currency Roulette Game, players test their currency conversion skills. Here's the setup:

1. We use a free currency API to retrieve the current exchange rate from USD to ILS (Israeli Shekel).
2. A random number (between 1 and 100) is generated in USD.
3. Players must guess the value of this random number converted to ILS.
4. The acceptable difference (accuracy) depends on the game's difficulty level. It's calculated as follows:
   - Acceptable Difference = 10 NIS - Difficulty Level
   - For example, if the difficulty level is 3, the acceptable range is 7 NIS.

### 3. Memory Game

The Memory Game tests players' memory skills. Here's the challenge:

1. A sequence of random numbers is briefly displayed (e.g., 100, 15, 80).
2. Players must memorize this sequence during a short duration.
3. After the display, they input the remembered numbers.
4. The goal is to match their input with the original sequence.

## Scoring

Players accumulate points based on their performance in the games. Here's how scoring works:

- Winning a game earns points: **POINTS_OF_WINNING = (DIFFICULTY X 3) + 5**
- Each time a player wins, their points are added to their total score, which is saved in a file.

---

## Web Score Display

Using Flask, we've created a simple web page that shows the current scores.

---

## DevOps Pipeline

Our DevOps pipeline ensures smooth development, testing, and deployment. Here's how it works:

1. **Dockerization**:
   - The Dockerfile sets up the environment for our web score display.
   - Docker Compose orchestrates the entire stack, including the Flask app and any necessary dependencies.

2. **Automated Testing**:
   - Selenium tests the web score display by navigating to `localhost:port` (the port mapped from Docker to localhost).
   - We verify that scores are displayed correctly.

3. **Jenkins Pipeline**:
   - Our Jenkinsfile defines a declarative pipeline.
   - Stages include building the Docker image, running tests, publishing the image to Docker Hub, and cleaning up resources.

---

## Getting Started

To get started with the **World Of Games (wog)** repository:

You can use the Jenkinsfile to do it all for you, or:

1. Clone this repository to your local machine.
2. To install dependencies: `pip install -r requierments.txt`.
3. Run main.py for the games.
4. Either use docker with `docker compose up` for the front, or run the front with `python -m front.main_score`
5. For testings you can run the e2e.py file inside the tests packages `python e2e.py <url>`.

---

