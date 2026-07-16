import sys
import time
from .theme import CYAN, RESET

def spinner(text, duration=2):
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end = time.time() + duration
    i = 0
    while time.time() < end:
        sys.stdout.write(f"\r  {CYAN}{chars[i]} {text}{RESET}")
        sys.stdout.flush()
        time.sleep(0.08)
        i = (i + 1) % len(chars)
    sys.stdout.write("\r" + " " * (len(text) + 10) + "\r")

def type_text(text, speed=0.03):
    for char in text:
        sys.stdout.write(f"{CYAN}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(speed)
    print()
