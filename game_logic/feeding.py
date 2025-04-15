import random
from game_logic.food import Food

class FeedingSystem:
    """Hệ thống quản lý việc cho cá ăn trong trò chơi."""
    
    def __init__(self, width, height, river_start, river_end):
        """Khởi tạo hệ thống cho ăn.
        
        Args:
            width: Chiều rộng của màn hình
            height: Chiều cao của màn hình
            river_start: Vị trí bắt đầu của dòng sông
            river_end: Vị trí kết thúc của dòng sông
        """
        self.width = width
        self.height = height
        self.river_start = river_start
        self.river_end = river_end
        self.foods = []
        self.active_food = None
    
    def throw_food(self, food_type, food_art):
        """Ném đồ ăn vào ao.
        
        Args:
            food_type: Loại đồ ăn ('pellet', 'flake', 'worm')
            food_art: ASCII art của đồ ăn
        """
        # Tạo đồ ăn ở vị trí ngẫu nhiên trong khu vực sông
        x = random.randint(5, self.width - 10)
        y = random.randint(self.river_start + 2, self.river_end - 5)
        
        food = Food(y, x, food_art, food_type)
        self.foods.append(food)
        
        return food
    
    def get_closest_food(self, x, y):
        """Tìm đồ ăn gần nhất so với vị trí hiện tại.
        
        Args:
            x: Tọa độ x hiện tại
            y: Tọa độ y hiện tại
            
        Returns:
            Đồ ăn gần nhất hoặc None nếu không có đồ ăn
        """
        if not self.foods:
            return None
            
        closest_food = None
        min_distance = float('inf')
        
        for food in self.foods:
            distance = ((food.x - x) ** 2 + (food.y - y) ** 2) ** 0.5
            if distance < min_distance:
                min_distance = distance
                closest_food = food
                
        return closest_food
    
    def remove_food(self, food):
        """Xóa đồ ăn khỏi danh sách.
        
        Args:
            food: Đồ ăn cần xóa
        """
        if food in self.foods:
            self.foods.remove(food)
    
    def get_foods(self):
        """Lấy danh sách đồ ăn hiện tại.
        
        Returns:
            Danh sách đồ ăn
        """
        return self.foods