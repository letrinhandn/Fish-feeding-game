import math

class KoiFish:
    """Class representing the player-controlled koi fish."""
    
    def __init__(self, y, x, art, facing_right=True):
        """Initialize fish with position and appearance."""
        self.y = y
        self.x = x
        self.art = art
        self.facing_right = facing_right
        self.size = 1
        self.speed = 1
        self.width = max(len(line) for line in art)
        self.height = len(art)
        self.target_food = None
        self.hunting = False
        self.normal_speed = 1
        self.hunting_speed = 2
    
    def move_up(self):
        """Move fish upward."""
        self.y -= self.speed
    
    def move_down(self):
        """Move fish downward."""
        self.y += self.speed
    
    def move_left(self):
        """Move fish leftward."""
        self.x -= self.speed
    
    def move_right(self):
        """Move fish rightward."""
        self.x += self.speed
    
    def grow(self):
        """Fish grows when it eats."""
        if self.size < 3:
            self.size += 0.1
    
    def get_display_art(self):
        """Get ASCII art oriented according to direction fish is facing."""
        if self.facing_right:
            return self.art
        else:
            # Reverse the art for left-facing
            reversed_art = []
            for line in self.art:
                # Replace < with temp, > with <, then temp with >
                reversed_line = line.replace('<', 'TEMP').replace('>', '<').replace('TEMP', '>')
                # Reverse the line
                reversed_art.append(reversed_line[::-1])
            return reversed_art
    
    def get_hitbox(self):
        """Get hitbox for collision detection."""
        return {
            "x1": self.x,
            "y1": self.y,
            "x2": self.x + self.width,
            "y2": self.y + self.height
        }

    def swim(self, width, height):
        """Move the fish automatically in a simple pattern."""
        if self.hunting and self.target_food:
            self.swim_to_food()
        else:
            self.x += self.speed if self.facing_right else -self.speed

            # Reverse direction if hitting the screen boundary
            if self.x < 0:
                self.x = 0
                self.facing_right = True
            elif self.x + self.width > width:
                self.x = width - self.width
                self.facing_right = False
    
    def set_target_food(self, food):
        """Set the current food target for the fish."""
        self.target_food = food
        if food:
            self.hunting = True
            self.speed = self.hunting_speed
            # Đặt hướng mặt dựa trên vị trí của thức ăn
            self.facing_right = food.x > self.x
        else:
            self.hunting = False
            self.speed = self.normal_speed
    
    def swim_to_food(self):
        """Di chuyển về phía thức ăn."""
        if not self.target_food:
            return
            
        # Tính toán hướng để đi đến thức ăn
        dx = self.target_food.x - self.x
        dy = self.target_food.y - self.y
        
        # Tính toán khoảng cách
        distance = math.sqrt(dx*dx + dy*dy)
        
        if distance < 1:
            return  # Đã đến gần thức ăn
            
        # Chuẩn hóa vector hướng
        dx = dx / distance
        dy = dy / distance
        
        # Di chuyển theo hướng thức ăn
        self.x += dx * self.speed
        self.y += dy * self.speed
        
        # Cập nhật hướng mặt của cá
        if dx > 0:
            self.facing_right = True
        elif dx < 0:
            self.facing_right = False