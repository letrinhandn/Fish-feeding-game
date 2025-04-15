from game_logic.fish import KoiFish
import random

class Fish3(KoiFish):
    def __init__(self, y, x, art):
        super().__init__(y, x, art, facing_right=random.choice([True, False]))
        self.direction = 1 if self.facing_right else -1

    def swim(self, width, height):
        """Move the fish horizontally similar to other fish."""
        self.x += self.direction * self.speed

        # Reverse direction if hitting the screen boundary
        if self.x <= 0:
            self.x = 0
            self.direction = 1
            self.facing_right = True
        elif self.x + self.width >= width:
            self.x = width - self.width
            self.direction = -1
            self.facing_right = False
            
        # Keep the fish within vertical bounds but don't change y randomly
        self.y = max(0, min(self.y, height - self.height))