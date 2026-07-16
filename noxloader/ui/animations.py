import sys
import time
from .theme import current_color, RESET

def spinner(text, duration):
    """Animasi loading ala termux"""
    chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end_time = time.time() + duration
    c = current_color()
    
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f'\r{c}  {chars[i]} {text}{RESET}')
        sys.stdout.flush()
        time.sleep(0.1)
        i = (i + 1) % len(chars)
    sys.stdout.write('\r' + ' ' * (len(text) + 6) + '\r')

def progress_bar(current, total, prefix='', suffix='', length=30, fill='█', printEnd="\r"):
    """Call in a loop to create terminal progress bar"""
    c = current_color()
    percent = ("{0:.1f}").format(100 * (current / float(total)))
    filledLength = int(length * current // total)
    bar = fill * filledLength + '░' * (length - filledLength)
    print(f'\r{c}  {prefix} |{bar}| {percent}% {suffix}{RESET}', end=printEnd)
    if current == total: 
        print()

def typing_effect(text, delay=0.03):
    c = current_color()
    sys.stdout.write(f"{c}")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(f"{RESET}\n")

