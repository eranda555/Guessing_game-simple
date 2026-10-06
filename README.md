# Number Guessing Game

A simple Python number guessing game where the computer generates a random number between 1 and 100. The player has 7 attempts to guess the correct number.

The game checks the user's input, gives feedback for incorrect guesses, and shows the number of attempts used when the correct number is guessed.

This project was created to practice Python basics such as functions, loops, conditions, user input, and random number generation. Docker was also used to containerize the application.

## Technologies Used

- Python
- Docker

## How to Run

Run with Python:

python number_guessing_game.py

Or build and run with Docker:

docker build -t guessing-game .
docker run -it guessing-game
