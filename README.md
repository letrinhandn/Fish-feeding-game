# 🐟 Koi Pond Game

*A terminal-based koi fish simulation game.*

---

## 🧩 Overview

**Koi Pond Game** is a lightweight, terminal-based simulation where the player controls a koi fish swimming peacefully in a pond.
The goal is simple: eat food, grow over time, and enjoy a dynamic ASCII-art environment accompanied by relaxing background music.

The project combines simple behavioral simulation, visual ASCII aesthetics, and ambient sound design to create a calm and meditative gameplay experience.

---

## 🌟 Features

* 🎨 **Beautiful ASCII art** — handcrafted ASCII visuals representing water, plants, rocks, and other creatures.
* 🌿 **Dynamic environment** — animated pond life and interactive elements.
* 🍽️ **Multiple food types** — each with unique point values and effects.
* 🐡 **Growth system** — your koi grows as it consumes more food.
* 💧 **Animated water and movement** — subtle, continuous motion throughout the environment.
* 🎵 **Relaxing background music** — integrated through `pygame`.
* 🤖 **Interactive AI creatures** — other pond inhabitants compete for food.

---

## 🎮 How to Play

1. **Install the game:**

   ```bash
   pip install -e .
   # or
   pip install .
   ```

2. **Run the game:**

   ```bash
   feedmyfish
   ```

3. **Controls:**

   | Key   | Action                     |
   | ----- | -------------------------- |
   | ↑     | Move up                    |
   | ↓     | Move down                  |
   | ←     | Move left                  |
   | →     | Move right                 |
   | 1     | Throw pellet (1 point)     |
   | 2     | Throw flake (1 point)      |
   | 3     | Throw worm (2 points)      |
   | + / - | Increase / decrease volume |
   | P     | Next track                 |
   | O     | Pause / resume             |
   | I     | Previous track             |
   | q     | Quit the game              |

---

## ⚙️ Requirements

* Python ≥ 3.6
* `pygame` (for background music)
* `windows-curses` (required on Windows only)

---

## 📦 Installation

### From GitHub

```bash
git clone https://github.com/letrinhandn/Fish-feeding-game.git
cd koi-game

# Development mode
pip install -e .

# or standard installation
pip install .
```

### Run the Game

```bash
feedmyfish
```

### From PyPI (once published)

```bash
pip install feedmyfish
feedmyfish
```

---

## 💻 Compatibility

* Fully compatible with **Linux** and **Windows**.
* On Windows, the `windows-curses` package will be installed automatically.

---

## 🧠 Future Development

* Expand AI behavior for other pond creatures.
* Enhance koi movement and response realism.
* Add multiplayer (LAN) support.
* Improve visual effects and soundscapes.
* Introduce save/load and scoring system.

---

## 📜 License

This project is released under the **MIT License**.
