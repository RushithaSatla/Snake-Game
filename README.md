# 🐍 Snake Game

This project is a classic Snake Game built using Python's `turtle` graphics library. It features a modern twist with dynamic food colors, shapes, and an interactive scoring system.

# Features

- Classic Snake Gameplay: Control the snake with the arrow keys to eat food and grow longer.
- Dynamic Food Appearance: Food appears with random colors and shapes to make the game more visually engaging.
- Real-Time Scoring: Displays the current score and high score at the top of the screen.
- Start and Restart Functionality: Press any arrow key to start the game, and after game over, an option to play again or exit is provided.

# How to Play

1. Starting the Game: 
   - Run the code, and you'll see the message, "Press any arrow key to start!" in the middle of the screen.
   - Press any arrow key to start.

2. Gameplay:
   - Use the arrow keys to move the snake:
     - Up Arrow: Moves the snake up
     - Down Arrow: Moves the snake down
     - Left Arrow: Moves the snake left
     - Right Arrow: Moves the snake right
   - Goal: Eat the food that appears on the screen to grow the snake longer and increase your score.
   - Avoid the screen edges and your own tail to prevent the game from ending.

3. Game Over:
   - If the snake hits the wall or itself, the game will end.
   - A message will appear in the middle of the screen showing your final score with options to:
     - Left-click to play again.
     - Right-click to exit the game.

# Scoring

- Score: You gain 10 points each time the snake eats the food.
- High Score: The highest score achieved during the session is displayed at the top of the screen.

# Installation and Setup

1. Install Python: Ensure you have Python installed (version 3.6 or higher).
2. Install Turtle (usually pre-installed with Python):
   ```bash
   pip install PythonTurtle
   ```
3. Run the Game: Download the code and run it in any Python IDE (or run it from the terminal with `python snake_game.py`).

# Code Overview

- Snake Movement: Functions (`group`, `godown`, `goleft`, `goright`) control the snake's movement in each direction.
- Randomized Food: The food color and shape are randomly selected each time it appears, enhancing visual variety.
- Collision Detection: Checks for collisions with walls or the snake's body to trigger game over.
- Score Tracking: Displays the score and high score on the screen.

