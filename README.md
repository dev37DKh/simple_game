# Alien Invasion

## Description

Alien Invasion is a simple 2D arcade-style game developed using Python and Pygame. The player controls a ship that can move left and right to dodge incoming alien threats. The game is designed to be both entertaining and a foundational project for learning game development concepts.

## Features

- **Player Control:** Move the ship horizontally across the bottom of the screen.
- **Graphics:** Basic ship graphics loaded from image files.
- **Simple Game Mechanics:** Responsive controls using keyboard events.
- **Continuous Loop:** The game runs in a continuous loop, checking for user inputs and updating the screen.

## Installation

To get started with Alien Invasion, follow these steps:

1. **Clone the repository:**

  
   git clone https://github.com/yourusername/alien-invasion.git
   cd alien-invasion



2. Install Python and Pygame: Make sure you have Python installed on your machine. Then, install the Pygame library using pip:


    ```bash

    pip install pygame

    Add Ship Image: Ensure the ship image (ship.bmp) is placed in the images directory within your project folder. You can replace it with any ship image of your choice.

Usage

To start the game, run the following command in your terminal:

    ```bash

    python main.py

Use the right arrow key to move the ship to the right and the left arrow key to move it to the left. The game will continue to run until you close the window.
Game Structure

The game is structured into several classes and modules:

    settings.py: Contains configuration settings for the game, such as screen dimensions and ship speed.
    ship.py: Manages the player's ship, including its position and movement.
    game_functions.py: Handles game events and updates the screen.
    main.py: The main script to run the game, initializing Pygame, creating the game screen, and handling the game loop.