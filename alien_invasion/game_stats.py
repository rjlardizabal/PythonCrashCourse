class GameStats():
    """Track statistics for Alien invasion"""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start the game in an inactive state.
        self.game_active = False

        # Set the High score to 0
        self.high_score = 0

        self.level = 1

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0

