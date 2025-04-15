import math

class Shrimp:
    def __init__(self, y, x, art):
        self.y = y
        self.x = x
        self.art = art
        self.speed = 1  # Faster than crab
        self.direction = 1  # 1 for right, -1 for left
        self.facing_right = False  # Start facing left because backswimming
        self.target_food = None
        self.hunting = False
        self.normal_speed = 1
        self.hunting_speed = 2.0

    def get_display_art(self):
        """Get ASCII art based on direction shrimp is facing."""
        if self.facing_right:
            return self.art
        else:
            # Reverse each line of art for left-facing
            return [line[::-1] for line in self.art]

    def move(self, width):
        """Move the shrimp horizontally and flip when hitting edges."""
        if self.hunting and self.target_food:
            self.move_to_food()
        else:
            self.x += self.speed * self.direction
            if self.x <= 0:
                self.x = 0
                self.direction = 1  # Move right
                self.facing_right = False  # Face left while moving right (backswimming)
            elif self.x + len(self.art[0]) >= width:
                self.x = width - len(self.art[0])
                self.direction = -1  # Move left
                self.facing_right = True  # Face right while moving left (backswimming)
    
    def set_target_food(self, food):
        """Set the current food target for the shrimp."""
        self.target_food = food
        if food:
            self.hunting = True
            self.speed = self.hunting_speed
            # Tôm bơi ngược khi đi săn (đuôi hướng về đồ ăn)
            self.facing_right = food.x < self.x
        else:
            self.hunting = False
            self.speed = self.normal_speed
            
    def move_to_food(self):
        """Di chuyển về phía thức ăn."""
        if not self.target_food:
            return
            
        # Tính toán hướng đến thức ăn
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
        
        # Cập nhật hướng mặt của tôm (tôm bơi ngược)
        if dx > 0:
            self.facing_right = False  # Quay mặt sang trái khi di chuyển sang phải
        elif dx < 0:
            self.facing_right = True   # Quay mặt sang phải khi di chuyển sang trái
    
    def get_hitbox(self):
        """Get hitbox for collision detection."""
        return {
            "x1": self.x,
            "y1": self.y,
            "x2": self.x + len(self.art[0]),
            "y2": self.y + len(self.art)
        }