from game_logic.fish import KoiFish

class Fish2(KoiFish):
    def __init__(self, y, x, art):
        super().__init__(y, x, art, facing_right=False)

    def swim(self, width):
        """Move the fish from right to left."""
        self.x -= self.speed
        if self.x < 0:
            self.x = width