class GameStats:
    """Tracks statistics for Alien invasion"""
    def __init__(self,ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset
        self.high_score = 0

        # start game in an inactive state 
        self.game_active = False
    def reset_stats(self):
        """Initialize statistics that can change within the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        

