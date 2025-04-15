class Food:
    """Class representing food items in the game."""
    
    def __init__(self, y, x, art, food_type="pellet"):
        """Initialize food with position and appearance."""
        self.y = y
        self.x = x
        self.art = art
        self.food_type = food_type
        self.width = max(len(line) for line in art) if art else 1
        self.height = len(art) if art else 1
        self.points = self._calculate_points()
    
    def _calculate_points(self):
        """Calculate points based on food type."""
        points_map = {
            "pellet": 1,
            "flake": 1, 
            "worm": 2,
            "snail": 3,
            "shrimp": 5
        }
        return points_map.get(self.food_type, 1)
    
    def get_hitbox(self):
        """Get hitbox for collision detection."""
        return {
            "x1": self.x,
            "y1": self.y,
            "x2": self.x + self.width,
            "y2": self.y + self.height
        }