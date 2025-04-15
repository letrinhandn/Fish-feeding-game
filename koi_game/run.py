#!/usr/bin/env python3
"""
Entry point for the Koi Pond game when run as a command-line application.
"""
import os
import sys
import curses

# Thêm đường dẫn gốc của dự án vào sys.path để import được các module
package_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if package_root not in sys.path:
    sys.path.insert(0, package_root)

from game_logic.fish import KoiFish
from game_logic.food import Food
from game_logic.collision import check_collision
from game_logic.fish1 import Fish1
from game_logic.fish2 import Fish2
from game_logic.fish3 import Fish3
from game_logic.crab import Crab
from game_logic.shrimp import Shrimp
from game_logic.feeding import FeedingSystem

# Import hàm main từ main.py
from koi_game.main import main as game_main

def main():
    """Entry point when run as a command-line application."""
    try:
        curses.wrapper(game_main)
    except KeyboardInterrupt:
        print("Game terminated by user")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())