# Game of Knights

**Game of Knights** is a two-player strategy game where each player controls a chess knight on a customizable board. The game simulates the movement of knights as they try to avoid being blocked by each other. The goal of the game is to avoid being in a situation where you have no possible moves, as the player who cannot move loses the game.

## Project Overview

In this game, two players (either two AIs or one human vs an AI) take turns moving their knights across the board. The knights move according to chess rules, in an "L" shape, and each move blocks the square they leave behind. Players must plan their moves carefully to avoid running out of options.

The game supports different board sizes, and players can select the desired size at the beginning. The game is implemented using Python and the easyAI library, which enables AI-based gameplay using the Negamax algorithm.

## Authors

- Henryk Mudlaff, s26071  
  GitHub: [HeniuM](https://github.com/HeniuM)

- Benedykt Borowski, s20685  
  GitHub: [BenedyktB](https://github.com/BenedyktB)

## Game Rules

The rules of the game are described in the `rules.txt` file. Please refer to that file for a full explanation of the game mechanics and objectives.

## How to Play

1. Clone the repository.
2. Run the `Main.py` file to start the game.
3. Choose between AI vs AI or Player vs AI modes.
4. Follow the game prompts and enjoy!

The game requires Python 3.x and the `easyAI` library, which can be installed with:
```bash
pip install easyAI
