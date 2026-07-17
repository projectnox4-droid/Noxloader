import re

with open('noxloader/main.py', 'r') as f:
    content = f.read()

new_main = """import os
import sys

sys.dont_write_bytecode = True

def safe_clear():
    try:
        if os.name == 'posix':
            os.system('clear 2>/dev/null')
        else:
            os.system('cls 2>nul')
    except:
        pass

try:
    from core.menu import main_menu
except Exception as e:
    safe_clear()
    print(f"\\n\\033[96m💀 Waduh cok, ada error nih: {e}\\033[0m\\n")
    sys.exit(1)

if __name__ == "__main__":
    try:
        import argparse
        parser = argparse.ArgumentParser(description="NoxLoader CLI")
        parser.add_argument("--stalker", help="Run stalker mode on target username without UI")
        
        args, unknown = parser.parse_known_args()
        
        if args.stalker:
            from core.extra_menus import stalker_mode_headless
            stalker_mode_headless(args.stalker)
        else:
            main_menu()
    except KeyboardInterrupt:
        safe_clear()
        print("\\n\\033[96m\\033[1m🥱 Cabut dulu cok. Santuy!\\033[0m\\n")
        sys.exit(0)
    except Exception as e:
        safe_clear()
        print(f"\\n\\033[96m💀 Waduh cok... aplikasi ngambek. (Error: {e}) 🗿\\033[0m\\n")
        sys.exit(1)
"""

with open('noxloader/main.py', 'w') as f:
    f.write(new_main)
print("Updated main.py")
