import math

class Crab:
    def __init__(self, y, x, art):
        self.y = y
        self.x = x
        self.art = art
        self.speed = 0.5  # Slow speed
        self.direction = 1  # 1 for right, -1 for left
        self.facing_right = True  # Always face right, won't flip
        self.target_food = None
        self.hunting = False
        self.normal_speed = 0.5
        self.hunting_speed = 1.2
        self.depth = 0  # Độ sâu của cua trong nước (0 = mặt nước, càng cao càng sâu)
        self.max_depth = 5  # Độ sâu tối đa
        self.depth_direction = 1  # Hướng thay đổi độ sâu (1 = đi xuống, -1 = đi lên)

    def get_display_art(self):
        """Luôn trả về nghệ thuật ASCII gốc, không đảo ngược."""
        return self.art

    def move(self, width):
        """Cua di chuyển ngang và thay đổi độ sâu theo thời gian."""
        if self.hunting and self.target_food:
            self.move_to_food()
        else:
            # Di chuyển ngang
            self.x += self.speed * self.direction
            if self.x <= 0:
                self.x = 0
                self.direction = 1  # Move right
            elif self.x + len(self.art[0]) >= width:
                self.x = width - len(self.art[0])
                self.direction = -1  # Move left
                
            # Thay đổi độ sâu
            self.depth += 0.2 * self.depth_direction
            if self.depth >= self.max_depth:
                self.depth = self.max_depth
                self.depth_direction = -1  # Đổi hướng, đi lên
            elif self.depth <= 0:
                self.depth = 0
                self.depth_direction = 1  # Đổi hướng, đi xuống
    
    def set_target_food(self, food):
        """Set the current food target for the crab."""
        self.target_food = food
        if food:
            self.hunting = True
            self.speed = self.hunting_speed
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
        
        # Xác định hướng di chuyển (nhưng không đổi hướng mặt)
        if dx > 0:
            self.direction = 1
        else:
            self.direction = -1
    
    def get_hitbox(self):
        """Get hitbox for collision detection."""
        return {
            "x1": self.x,
            "y1": self.y + self.depth,  # Điều chỉnh y theo độ sâu
            "x2": self.x + len(self.art[0]),
            "y2": self.y + len(self.art) + self.depth  # Điều chỉnh y theo độ sâu
        }