from game_logic.fish import KoiFish

class Fish1(KoiFish):
    def __init__(self, y, x, art):
        super().__init__(y, x, art, facing_right=True)

    def swim(self, width):
        """Move the fish from left to right."""
        self.x += self.speed
        if self.x > width:
            self.x = 0