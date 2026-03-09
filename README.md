# Pong Game (Python + Pygame)
A simple Pong game implemented using Python and Pygame.

## Description
This is a classic Pong game where the player controls a paddle to bounce a moving ball. The goal is to keep the ball from touching the bottom of the screen. The game keeps score based on successful bounces.

This project was created to practice **Python, Pygame, event handling, and collision detection**.

## Features
- Paddle movement controlled by **Left** and **Right** arrow keys
- Ball bounces off walls and paddle
- Score increases each time the ball hits the paddle
- Game Over screen when the ball reaches the bottom
- Uses an image (`poza.jpg`) for the ball

## Technologies Used
- Python 3
- Pygame
- Event handling and collision detection
- Modular and readable code

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```
## Run the game

```bash
python main.py
```

## What I Learned

- **Event Handling**: Handling user input with `pygame.event.get()` and responding to key presses.
- **Collision Detection**: Detecting collisions between the ball and paddle to update direction and score.
- **Game Loop**: Using a main game loop and `pygame.time.Clock` to control the frame rate.
- **Dynamic Difficulty**: Increasing game speed as the score rises to make the game more challenging.
- **Graphics Handling**: Loading images (`pygame.image.load`) and drawing text (`pygame.font.SysFont`) on the screen.