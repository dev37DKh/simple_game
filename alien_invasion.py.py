import sys 
from settings import Settings
import pygame
from ship import Ship
import game_functions as gf

def run_game():
    """
    Initialize the game and create a window to display the game elements.

    This function sets up the game environment, initializes Pygame, and manages 
    the main game loop. It includes handling user inputs, updating the game state, 
    and rendering the game objects to the screen.
    """

    # Initialize Pygame
    pygame.init()

    # Create an instance of Settings to retrieve game configuration
    ai_settings = Settings()

    # Set up the game screen with specified width and height from settings
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    # Set the window title
    pygame.display.set_caption("Alien Invasion")

    # Create an instance of the Ship class for player control
    ship = Ship(ai_settings, screen)

    # Define the background color
    bg_color = (230, 230, 230)

    # Main game loop
    while True:
        # Fill the screen with the background color
        screen.fill(ai_settings.bg_color)

        # Draw the ship at its current location
        ship.blitme()

        # Check for user input events and update the ship's position
        gf.check_events(ship)
        ship.update()

        # Update the screen with the latest drawn elements
        gf.update_screen(ai_settings, screen, ship)

        # Event loop to listen for quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Exit the game if the quit event is detected
                sys.exit()

        # Refresh the display to show the latest game state
        pygame.display.flip()

# Call the run_game function to start the game
run_game()
