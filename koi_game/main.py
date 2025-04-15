import curses
import time
import os
import random
import pygame
from game_logic.fish import KoiFish
from game_logic.food import Food
from game_logic.collision import check_collision
from game_logic.fish1 import Fish1
from game_logic.fish2 import Fish2
from game_logic.fish3 import Fish3
from game_logic.crab import Crab
from game_logic.shrimp import Shrimp
from game_logic.feeding import FeedingSystem

def load_ascii_art(filename):
    """Load ASCII art from file."""
    # Tìm đường dẫn gốc của package để đảm bảo luôn tìm thấy assets
    package_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(package_root, 'assets', 'art', filename)
    try:
        with open(path, 'r') as file:
            return [line.rstrip('\n') for line in file if not line.startswith('//')]
    except FileNotFoundError:
        print(f"Warning: Could not find art file {path}")
        return []

def draw_ascii_art(window, art, y, x, color_pair=0):
    """Draw ASCII art at specified position."""
    height, width = window.getmaxyx()
    for i, line in enumerate(art):
        # Skip if out of vertical bounds
        if y + i < 0 or y + i >= height:
            continue
        
        # Skip if out of horizontal bounds
        if x < 0 or x >= width:
            continue
            
        # Calculate how much of the line will fit
        line_to_draw = line[:max(0, width - x)]
        
        # Only draw if there's something to draw
        if line_to_draw:
            try:
                window.addstr(y + i, x, line_to_draw, curses.color_pair(color_pair))
            except curses.error:
                # Ignore curses errors from drawing outside of window
                pass

def init_colors():
    """Initialize color pairs for the game."""
    curses.start_color()
    curses.use_default_colors()
    # Color pairs
    curses.init_pair(1, curses.COLOR_RED, -1)     # Red for koi
    curses.init_pair(2, curses.COLOR_BLUE, -1)    # Blue for water
    curses.init_pair(3, curses.COLOR_GREEN, -1)   # Green for plants
    curses.init_pair(4, curses.COLOR_YELLOW, -1)  # Yellow for food
    curses.init_pair(5, curses.COLOR_WHITE, -1)   # White for misc
    curses.init_pair(6, curses.COLOR_MAGENTA, -1) # Magenta for special items
    curses.init_pair(7, curses.COLOR_CYAN, -1)    # Cyan for special water

def get_terminal_dimensions(stdscr):
    """Get terminal dimensions."""
    height, width = stdscr.getmaxyx()
    return height, width

def main(stdscr):
    """Main function to run the game."""
    # Setup
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(True)  # Non-blocking input
    init_colors()
    
    height, width = get_terminal_dimensions(stdscr)
    
    # Load ASCII art
    koi_art = load_ascii_art('koi_ascii.txt')
    water_art = load_ascii_art('water.txt')
    wave_art = load_ascii_art('wave.txt')
    food_art1 = load_ascii_art('food_1.txt')
    food_art2 = load_ascii_art('food_2.txt')
    worm_art = load_ascii_art('worm.txt')
    snail_art = load_ascii_art('snail.txt')
    shrimp_art = load_ascii_art('shrimp.txt')
    grass_art = load_ascii_art('grass.txt')
    rock_art1 = load_ascii_art('rock_1.txt')
    tall_tree_art = load_ascii_art('tall_tree.txt')
    short_tree_art = load_ascii_art('short_tree.txt')
    big_tree_art = load_ascii_art('big_tree.txt')
    crab_art = load_ascii_art('crab.txt')
    bird_art = load_ascii_art('bird.txt')
    
    # Create game objects
    koi = KoiFish(height // 2, width // 4, koi_art, facing_right=True)
    
    # Define river and shore boundaries
    river_start = height // 3
    river_end = height - (height // 5)  # Bottom 1/5 is the shore

    # Khởi tạo hệ thống cho ăn
    feeding_system = FeedingSystem(width, height, river_start, river_end)
    
    # Create multiple fish objects
    fish1 = Fish1(height // 2, width // 4, koi_art)
    fish2 = Fish2(height // 3, width // 2, koi_art)
    fish3 = Fish3(height // 4, width // 3, koi_art)

    # Add fish to a list for management
    fishes = [fish1, fish2, fish3]
    
    # Create crabs and shrimps
    crabs = [
        Crab(height - 8, width // 5, crab_art),
        Crab(height - 8, width // 3, crab_art)
    ]

    shrimps = [
        Shrimp(height - 6, width // 4, shrimp_art),
        Shrimp(height - 6, width // 2, shrimp_art)
    ]

    # Environment objects (static)
    environment = [
        {"art": rock_art1, "y": height - 10, "x": width // 5, "color": 5},
        {"art": tall_tree_art, "y": 5, "x": width - 25, "color": 3},  # Moved tall tree
        {"art": big_tree_art, "y": 3, "x": 10, "color": 3},  # Moved big tree
        {"art": short_tree_art, "y": 6, "x": width - 15, "color": 3},  # Moved short tree
        {"art": grass_art, "y": height - 5, "x": width // 3, "color": 3},
        {"art": grass_art, "y": height - 4, "x": width // 2 + 15, "color": 3}
    ]
    
    # Remove static crab from environment
    environment = [obj for obj in environment if obj.get("art") != crab_art]
    
    # Remove static shrimp from environment
    environment = [obj for obj in environment if obj.get("art") != shrimp_art]
    
    # Remove static snail from environment
    environment = [obj for obj in environment if obj.get("art") != snail_art]
    
    # Add some random decorations
    for _ in range(3):
        env_x = random.randint(5, width - 20)
        env_y = random.randint(5, height - 10)
        decoration = random.choice([grass_art, rock_art1])
        environment.append({"art": decoration, "y": env_y, "x": env_x, "color": 3})
    
    # Add floating leaves
    leaves = [
        {"art": grass_art, "y": random.randint(river_start, river_end), "x": random.randint(5, width - 20)}
        for _ in range(5)
    ]

    # Place shrimp and crab on rocks (removed snail)
    for obj in environment:
        if obj["art"] == rock_art1:
            animal = random.choice([shrimp_art, crab_art])  # Removed snail_art from choices
            if animal == shrimp_art:
                obj["animal"] = {
                    "art": animal, 
                    "y": obj["y"] - len(animal), 
                    "x": obj["x"], 
                    "color": 6,
                    "direction_x": 1,  # Khởi tạo hướng đi sang phải
                    "facing_right": False  # Khởi tạo mặt quay sang trái (backswimming)
                }
            else:  # Crab
                obj["animal"] = {
                    "art": animal, 
                    "y": obj["y"] - len(animal), 
                    "x": obj["x"], 
                    "color": 6,
                    "direction_x": 1
                }

    try:
        # Initialize pygame mixer for music
        pygame.mixer.init()

        # Load music files
        package_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        music_path = os.path.join(package_root, 'assets', 'music')
        music_files = []
        if os.path.exists(music_path):
            music_files = [
                os.path.join(music_path, file) 
                for file in os.listdir(music_path)
                if file.endswith('.mp3')
            ]

        # Function to play random music
        def play_random_music():
            if music_files:
                try:
                    music_file = random.choice(music_files)
                    pygame.mixer.music.load(music_file)
                    pygame.mixer.music.play()
                    return os.path.basename(music_file)
                except Exception as e:
                    return f"Error playing music: {str(e)}"
            return "No music files found"

        # Start playing music
        current_music = play_random_music()
        
    except Exception as e:
        # If music setup failed, continue without music
        current_music = f"Music disabled: {str(e)}"

    # Game loop
    game_over = False
    score = 0
    food_timer = 0
    wave_animation = 0
    
    while not game_over:
        # Clear screen
        stdscr.clear()

        # Hiển thị hướng dẫn cho ăn ở góc trái trên màn hình
        feeding_instructions = "[1: Pellet] [2: Flake] [3: Worm]"
        stdscr.addstr(1, 2, feeding_instructions, curses.color_pair(5))

        # Draw river and shore
        for y in range(river_start):
            stdscr.addstr(y, 0, " " * width, curses.color_pair(3))  # Shore
        for y in range(river_start, river_end):
            stdscr.addstr(y, 0, " " * width, curses.color_pair(2))  # River

        # Xử lý cá bơi đến thức ăn
        for fish in fishes:
            # Chỉ tìm thức ăn khi không đang săn mồi
            if not fish.hunting:
                closest_food = feeding_system.get_closest_food(fish.x, fish.y)
                if closest_food:
                    fish.set_target_food(closest_food)
            
            # Di chuyển cá
            if isinstance(fish, Fish3):
                fish.swim(width, height)
            else:
                fish.swim(width)
                
            # Kiểm tra va chạm với thức ăn
            if fish.target_food and check_collision(fish.get_hitbox(), fish.target_food.get_hitbox()):
                feeding_system.remove_food(fish.target_food)
                fish.set_target_food(None)
                
            draw_ascii_art(stdscr, fish.get_display_art(), fish.y, fish.x, 1)

        # Move and draw the koi fish
        koi.swim(width, height)
        draw_ascii_art(stdscr, koi.get_display_art(), koi.y, koi.x, 1)

        # Xử lý cua đi tìm thức ăn
        for crab in crabs:
            # Chỉ tìm thức ăn khi không đang săn mồi
            if not crab.hunting:
                closest_food = feeding_system.get_closest_food(crab.x, crab.y)
                if closest_food:  # Cua giờ có thể đi đến mọi thức ăn, không còn giới hạn theo chiều dọc
                    crab.set_target_food(closest_food)
            
            crab.move(width)
            
            # Kiểm tra va chạm với thức ăn
            if crab.target_food and check_collision(crab.get_hitbox(), crab.target_food.get_hitbox()):
                feeding_system.remove_food(crab.target_food)
                crab.set_target_food(None)
                
            # Vẽ cua với độ sâu
            draw_ascii_art(stdscr, crab.get_display_art(), int(crab.y + crab.depth), int(crab.x), 1)

        # Xử lý tôm đi tìm thức ăn
        for shrimp in shrimps:
            # Chỉ tìm thức ăn khi không đang săn mồi
            if not shrimp.hunting:
                closest_food = feeding_system.get_closest_food(shrimp.x, shrimp.y)
                if closest_food:
                    shrimp.set_target_food(closest_food)
            
            shrimp.move(width)
            
            # Kiểm tra va chạm với thức ăn
            if shrimp.target_food and check_collision(shrimp.get_hitbox(), shrimp.target_food.get_hitbox()):
                feeding_system.remove_food(shrimp.target_food)
                shrimp.set_target_food(None)
                
            draw_ascii_art(stdscr, shrimp.get_display_art(), int(shrimp.y), int(shrimp.x), 1)

        # Draw floating leaves
        for leaf in leaves[:]:
            draw_ascii_art(stdscr, leaf["art"], leaf["y"], leaf["x"], 3)
            leaf_hitbox = {
                "x1": leaf["x"],
                "y1": leaf["y"],
                "x2": leaf["x"] + len(leaf["art"][0]),
                "y2": leaf["y"] + len(leaf["art"])
            }
            if check_collision(koi.get_hitbox(), leaf_hitbox):
                leaves.remove(leaf)  # Leaf disappears when koi swims over it

        # Draw animals on rocks
        for obj in environment:
            if "animal" in obj:
                draw_ascii_art(stdscr, obj["animal"]["art"], obj["animal"]["y"], obj["animal"]["x"], obj["animal"]["color"])
        
        # Update crabs and shrimps movement on rocks
        for obj in environment:
            if "animal" in obj:
                animal = obj["animal"]
                if animal["art"] == crab_art or animal["art"] == shrimp_art:
                    # Move horizontally only
                    animal["x"] += 1 if animal.get("direction_x", 1) > 0 else -1

                    # Reverse direction at screen edges
                    if animal["x"] <= 0:
                        animal["x"] = 0
                        animal["direction_x"] = 1  # Move right
                        # Only flip shrimp's facing direction
                        if animal["art"] == shrimp_art:
                            animal["facing_right"] = False  # Face left while moving right
                    elif animal["x"] + len(animal["art"][0]) >= width:
                        animal["x"] = width - len(animal["art"][0])
                        animal["direction_x"] = -1  # Move left
                        # Only flip shrimp's facing direction
                        if animal["art"] == shrimp_art:
                            animal["facing_right"] = True  # Face right while moving left

                    # Get the art based on direction for shrimp
                    if animal["art"] == shrimp_art:
                        if animal.get("facing_right", False):
                            animal["display_art"] = animal["art"]
                        else:
                            animal["display_art"] = [line[::-1] for line in animal["art"]]
                    else:
                        animal["display_art"] = animal["art"]

        # Draw environment objects and their animals
        for obj in environment:
            draw_ascii_art(stdscr, obj["art"], obj["y"], obj["x"], obj["color"])
            if "animal" in obj:
                animal = obj["animal"]
                art_to_draw = animal.get("display_art", animal["art"])
                draw_ascii_art(stdscr, art_to_draw, animal["y"], animal["x"], animal["color"])

        # Handle music controls
        music_controls = "[+/-: Volume] [P: Next] [O: Pause] [I: Previous]"
        stdscr.addstr(1, width - len(music_controls) - 2, music_controls, curses.color_pair(5))
        
        # Draw exit instruction at a safe position below the music controls
        exit_text = "Press 'q' to exit"
        stdscr.addstr(3, width - len(exit_text) - 2, exit_text, curses.color_pair(5))

        # Process input
        key = stdscr.getch()
        if key == ord('1'):
            # Ném thức ăn loại 1
            feeding_system.throw_food('pellet', food_art1)
        elif key == ord('2'):
            # Ném thức ăn loại 2
            feeding_system.throw_food('flake', food_art2)
        elif key == ord('3'):
            # Ném giun
            feeding_system.throw_food('worm', worm_art)
        elif key == ord('+'):
            try:
                pygame.mixer.music.set_volume(min(pygame.mixer.music.get_volume() + 0.1, 1.0))
            except:
                pass
        elif key == ord('-'):
            try:
                pygame.mixer.music.set_volume(max(pygame.mixer.music.get_volume() - 0.1, 0.0))
            except:
                pass
        elif key == ord('p'):
            try:
                current_music = play_random_music()
            except:
                pass
        elif key == ord('o'):
            try:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            except:
                pass
        elif key == ord('i'):
            try:
                pygame.mixer.music.stop()
                current_music = play_random_music()
            except:
                pass
        elif key == ord('q'):
            break
        elif key == curses.KEY_UP and koi.y > 0:
            koi.move_up()
        elif key == curses.KEY_DOWN and koi.y < height - len(koi.art):
            koi.move_down()
        elif key == curses.KEY_LEFT:
            koi.move_left()
            koi.facing_right = False
        elif key == curses.KEY_RIGHT:
            koi.move_right()
            koi.facing_right = True
        
        # Kiểm tra cá Koi ăn thức ăn
        for food in feeding_system.foods[:]:
            if check_collision(koi.get_hitbox(), food.get_hitbox()):
                feeding_system.remove_food(food)
                score += food.points
                koi.grow()
        
        # Vẽ đồ ăn
        for food in feeding_system.foods:
            food_color = 4  # Default yellow
            if food.food_type == 'worm':
                food_color = 1  # Red
            elif food.food_type == 'shrimp':
                food_color = 6  # Magenta
            draw_ascii_art(stdscr, food.art, food.y, food.x, food_color)
        
        # Update game state
        food_timer += 1
        if food_timer >= 50:  # Removed logic for spawning food and snails
            food_timer = 0
        
        # Check collisions - Thay thế foods bằng feeding_system.foods
        for food in feeding_system.foods[:]:
            if check_collision(koi.get_hitbox(), food.get_hitbox()):
                feeding_system.remove_food(food)
                score += 1
                koi.grow()
        
        # Draw water background (animated waves) starting from line 4
        wave_animation = (wave_animation + 1) % 10
        for y in range(4, height, 4):  # Start drawing waves below all text
            offset = wave_animation if (y // 4) % 2 == 0 else -wave_animation
            for x in range(0, width, len(water_art[0]) + 10):
                draw_ascii_art(stdscr, water_art, y, x + offset, 2)
        
        # Draw environment objects (behind fish)
        for obj in environment:
            draw_ascii_art(stdscr, obj["art"], obj["y"], obj["x"], obj["color"])
        
        # Draw Koi fish
        koi_color = 1 + (score % 3)  # Fish color changes as score increases
        draw_ascii_art(stdscr, koi.get_display_art(), koi.y, koi.x, koi_color)
        
        # Draw dynamic crabs and shrimps (only the ones in our lists)
        for crab in crabs:
            draw_ascii_art(stdscr, crab.get_display_art(), int(crab.y + crab.depth), int(crab.x), 1)
            
        for shrimp in shrimps:
            draw_ascii_art(stdscr, shrimp.get_display_art(), int(shrimp.y), int(shrimp.x), 1)
        
        # Display current music name
        if current_music:
            music_text = f"Now Playing: {current_music}"
            stdscr.addstr(0, width - len(music_text) - 2, music_text, curses.color_pair(5))

        # Check if music has stopped and play another track
        try:
            if not pygame.mixer.music.get_busy():
                current_music = play_random_music()
        except:
            pass
        
        # Refresh screen
        stdscr.refresh()
        
        # Control game speed
        time.sleep(0.1)

        # Restrict fish to the river
        for fish in fishes:
            fish.y = max(0, min(fish.y, river_end - fish.height))