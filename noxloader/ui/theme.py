import os

CYAN = '\033[96m'
DARK_CYAN = '\033[36m'
BLACK = '\033[30m'
RESET = '\033[0m'
BOLD = '\033[1m'

def clear():
    """Clear screen cross-platform, kept silent."""
    os.system('clear 2>/dev/null') if os.name == 'posix' else os.system('cls 2>nul')

def print_neon(text):
    print(f"{CYAN}{BOLD}{text}{RESET}")
