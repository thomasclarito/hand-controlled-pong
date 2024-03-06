# Hand Controlled Pong Game

Welcome to the Hand Controlled Pong Game! This Python project allows you to play the classic game of Pong using hand gestures detected via a webcam. It utilizes computer vision techniques to track the movement of your hand and translate it into paddle movements within the game.

## Getting Started

### Installation

Clone or download this repository to your local machine.

### Prerequisites   

Before running the game, make sure you have the following dependencies installed:

- Python 3.8 or greater
- OpenCV
- MediaPipe
- Pygame

You can install each required module manually using pip:

```bash
pip install opencv-python
pip install mediapipe
pip install pygame
```

or you can navigate to the project directory and run:

```bash
pip install -r ./requirements.txt
```
## How To Play

### Running the game

While in the project directory, run the following command to start the game:

```bash
python -m HandPong
```

### How to Play

The objective is to bounce the ball for as long as possible without it touching the bottom of the screen.
Each time you bounce the ball, you score a point, but the speed of the ball increases as your score gets higher!
The game ends when the ball touches the bottom of the screen. Try to go for a high score!

To start the game in the main menu, simple gesture a thumbs up!

To move the pong paddle simply move your hand on the screen. 
The paddle position follows your index finger. There is a red cursor to show you where your finger is being detected.

To quit the game simply gesture thumbs down in the game over screen or the intro streen.

## Demo video
