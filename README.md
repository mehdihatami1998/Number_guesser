# Number Guesser Game
## Introduction
This is a game in which the computer chooses a random number between 1 and 100, and you are supposed to guess what number it has chosen each time. You start with 100 scores, and for each wrong guess, you will lose 10 scores. 

This solution provides a Modular approach to code this game.

## Prerequisits
This game doesn't need any specific requirements to be run on your machine

## Directory Structure
```
number-guesser project/
|-- src/
| |-- main.py
| |-- utils/
| | |-- input_validator.py
| | |-- random_generator.py
| |-- game_logic/
| | |-- hint_generator
| | |-- score_calculator
|-- README.md
|-- requirements.txt
```

## How to Run
1. Navigate to the project main directory (NUMBER-GUESSER-PROJECT)
2. Add current directory to the `PYTHONPATH` and run `main.py`
```
export PYTHONPATH=$PYTHONPATH:$(pwd)
python src/main.py
```
3. Follow on-screen prompt to run the game

## Modules
- `src/main.py`: The main entry point of the game, it handles the game loop, user input, and display
- `src/game_logic/`: It contains core game logic
  - `hint_generator.py`: Generates hints based on user's input
  - `score_calculator.py`: calculates the score of the user based on the number of tries
- `src/utils/`: It contains the utility functions
  - `input_validator.py`: It checks if user's input is valid or not, and provides appropriate feedback if not.
  - `random_generator.py`: It generates random numbers that user need to guess
  
