import os
import sys

# Global Base Colors (24-bit ANSI)
def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

NEON_CYAN = rgb(0, 255, 255)
NEON_BLUE = rgb(0, 85, 255)
LIGHT_GRAY = rgb(204, 204, 204)
NEON_GREEN = rgb(0, 255, 0)
NEON_YELLOW = rgb(255, 255, 0)
NEON_RED = rgb(255, 0, 51)
RESET = "\033[0m"
BOLD = "\033[1m"

# Default theme (Universal / Core)
CYAN = NEON_CYAN

class ThemeManager:
    current_menu = "CORE"
    
    @classmethod
    def get_color(cls):
        if cls.current_menu == "NOXYOU":
            return NEON_RED
        elif cls.current_menu == "NOXTOK":
            return rgb(0, 255, 255) # We'll do simple cyan for now, can gradient later
        elif cls.current_menu == "NOXGRAM":
            return rgb(255, 0, 128) # Pink/Purple
        elif cls.current_menu == "NOXBOOK":
            return NEON_BLUE
        elif cls.current_menu == "NOXX":
            return rgb(170, 170, 170) # Silver/Gray
        elif cls.current_menu == "NOXVID":
            return NEON_GREEN
        elif cls.current_menu == "UNIVERSAL":
            return rgb(0, 150, 255)
        return NEON_CYAN

def current_color():
    return ThemeManager.get_color()

def clear():
    """Clear screen cross-platform, kept silent."""
    os.system('clear 2>/dev/null') if os.name == 'posix' else os.system('cls 2>nul')

def print_neon(text):
    print(f"{current_color()}{BOLD}{text}{RESET}")

def print_status(status_type, msg):
    color = NEON_CYAN
    icon = "ℹ"
    if status_type == "INFO":
        color = NEON_BLUE
        icon = "😈"
    elif status_type == "SUCCESS":
        color = NEON_GREEN
        icon = "✅"
    elif status_type == "WARNING":
        color = NEON_YELLOW
        icon = "⚠"
    elif status_type == "ERROR":
        color = NEON_RED
        icon = "💀"
        
    width = len(msg) + 6
    top = "┏" + "━" * width + "┓"
    bot = "┗" + "━" * width + "┛"
    
    print(f"{color}{top}{RESET}")
    print(f"{color}┃ {icon} {msg} ┃{RESET}")
    print(f"{color}{bot}{RESET}")
