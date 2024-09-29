import sys
import pygame

def check_keydown_events(event, ship):
    """
    Respond to key presses for movement.

    This function checks if the right or left arrow keys are pressed and
    updates the ship's movement status accordingly.

    Parameters:
    event (pygame.event): The event object containing key press information.
    ship (Ship): The instance of the Ship class representing the player's ship.
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    """
    Respond to key releases for movement.

    This function checks if the right or left arrow keys are released and
    updates the ship's movement status accordingly.

    Parameters:
    event (pygame.event): The event object containing key release information.
    ship (Ship): The instance of the Ship class representing the player's ship.
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """
    Respond to keypresses and mouse events.

    This function processes all events in the Pygame event queue, checking for
    quit events and key presses or releases, updating the ship's movement state.

    Parameters:
    ship (Ship): The instance of the Ship class representing the player's ship.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  # Exit the game if the quit event is detected.
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)  # Call function for key down events.
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)  # Call function for key up events.


def update_screen(ai_settings, screen, ship):
    """
    Update the contents of the screen.

    This function fills the screen with the background color, draws the ship,
    and updates the display to reflect the latest game state.

    Parameters:
    ai_settings (Settings): The instance containing game settings, including background color.
    screen (Surface): The Pygame surface representing the game window.
    ship (Ship): The instance of the Ship class representing the player's ship.
    """
    screen.fill(ai_settings.bg_color)  # Fill the screen with the background color.
    ship.blitme()  # Draw the ship at its current location.

    pygame.display.flip()  # Update the full display surface to the screen.
