class GameStats():
    """Track statistics for Alien invasion"""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start the game in an inactive state.
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit

