import pygame

class Ship():
    """A class to manage the player's ship in the Alien Invasion game."""

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        
        self.screen = screen  # The screen where the ship will be drawn.
        self.ai_settings = ai_settings  # Settings for the game, including ship speed.

        # Load the ship image and get its rectangle.
        self.image = pygame.image.load("images/ship.bmp")  # Load the ship's image from the specified file.
        self.rect = self.image.get_rect()  # Get the rectangular area of the ship image.
        self.screen_rect = screen.get_rect()  # Get the rectangular area of the screen.

        # Start the ship in the center bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx  # Center the ship horizontally.
        self.rect.bottom = self.screen_rect.bottom  # Position the ship at the bottom of the screen.

        self.center = float(self.rect.centerx)  # Store the ship's horizontal position as a float.

        # Movement flags.
        self.moving_right = False  # Flag to indicate if the ship is moving right.
        self.moving_left = False  # Flag to indicate if the ship is moving left.

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's center based on the movement flags.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1  # Move the ship right.
            self.center += self.ai_settings.ship_speed_factor  # Update the center position based on speed.
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1  # Move the ship left.
            self.center -= self.ai_settings.ship_speed_factor  # Update the center position based on speed.

        self.rect.centerx = self.center  # Update the rect position to match the float center.

    def blitme(self):
        """Draw the ship at its current position on the screen."""
        self.screen.blit(self.image, self.rect)  # Draw the ship image at its rect position.
