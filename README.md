# Cộng hòa Xã hội Chủ nghĩa Việt Nam
# Độc lập - Tự do - Hạnh phúc

# Koi Pond Game

Một trò chơi chạy trên terminal, nơi bạn điều khiển một con cá Koi bơi trong ao, ăn thức ăn và tận hưởng môi trường yên bình.

---

# Socialist Republic of Vietnam
# Independence - Freedom - Happiness

# Koi Pond Game

A terminal-based game where you control a koi fish swimming in a pond, eating food, and enjoying a peaceful environment.

## Tính năng / Features

- Nghệ thuật ASCII đẹp mắt / Beautiful ASCII art
- Môi trường động với cây cối, đá, và các sinh vật khác / Dynamic environment with trees, rocks, and other creatures
- Nhiều loại thức ăn với điểm số khác nhau / Various types of food with different scores
- Cơ chế tăng trưởng khi cá ăn nhiều / Growth mechanism as the fish eats more
- Nước và môi trường được hoạt hình / Animated water and environment
- Hệ thống cho ăn tương tác với các loài sinh vật tranh nhau ăn / Interactive feeding system with competing creatures
- Nhạc nền thư giãn / Relaxing background music

## Cách chơi / How to Play

1. Cài đặt game: `pip install -e .` hoặc `pip install .` / Install the game: `pip install -e .` or `pip install .`
2. Chạy game bằng lệnh: `feedmyfish` / Run the game with the command: `feedmyfish`
3. Sử dụng các phím mũi tên để điều khiển cá Koi: / Use arrow keys to control the koi fish:
   - ↑: Di chuyển lên / Move up
   - ↓: Di chuyển xuống / Move down
   - ←: Di chuyển trái / Move left
   - →: Di chuyển phải / Move right
4. Ném thức ăn cho cá: / Throw food for the fish:
   - 1: Ném hạt thức ăn (Pellet) / Throw pellet
   - 2: Ném mảnh thức ăn (Flake) / Throw flake
   - 3: Ném giun (Worm) / Throw worm
5. Điều khiển nhạc: / Control music:
   - +/-: Tăng/giảm âm lượng / Increase/decrease volume
   - P: Bài tiếp theo / Next track
   - O: Tạm dừng/tiếp tục / Pause/resume
   - I: Bài trước / Previous track
6. Nhấn 'q' để thoát game / Press 'q' to exit the game

## Loại thức ăn / Types of Food

- Pellet (O): 1 điểm / 1 point
- Flake (*): 1 điểm / 1 point
- Worm (~): 2 điểm / 2 points

## Yêu cầu / Requirements

- Python 3.6+
- pygame (nhạc nền / background music)
- windows-curses (cho Windows / for Windows)

## Cài đặt / Installation

### Từ GitHub / From GitHub

1. Clone repository về: / Clone the repository:
   ```
   git clone <your-repository-url>
   cd koi-game
   ```

2. Cài đặt trò chơi: / Install the game:
   ```
   # Cài đặt trong chế độ phát triển / Install in development mode
   pip install -e .
   
   # Hoặc cài đặt thông thường / Or install normally
   pip install .
   ```

3. Chạy trò chơi: / Run the game:
   ```
   feedmyfish
   ```

### Từ PyPI (Khi đã xuất bản) / From PyPI (When published)

```
pip install feedmyfish
feedmyfish
```

## Tương thích / Compatibility

Game hoạt động trên cả Linux và Windows. Trên Windows, package windows-curses sẽ được tự động cài đặt. / The game works on both Linux and Windows. On Windows, the windows-curses package will be automatically installed.