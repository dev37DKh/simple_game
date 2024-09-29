class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        
        # Screen settings
        self.screen_width = 1200  # Width of the game screen in pixels.
        self.screen_height = 1000  # Height of the game screen in pixels.
        self.bg_color = (230, 230, 230)  # Background color of the screen in RGB format.

        # Ship settings
        self.ship_speed_factor = 1.5  # Speed factor for the player's ship.
