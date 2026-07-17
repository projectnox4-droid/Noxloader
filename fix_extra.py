with open('noxloader/core/extra_menus.py', 'r') as f:
    content = f.read()

new_func = """

def stalker_mode_headless(target):
    import time
    from ui.theme import current_color, print_status, LIGHT_GRAY, RESET
    c = current_color()
    print_status("INFO", f"STALKER MODE HEADLESS STARTED for @{target}")
    print(f"{LIGHT_GRAY}  Memantau @{target} 24/7 di background...{RESET}", flush=True)
    
    try:
        while True:
            # Simulate background stalking
            time.sleep(60)
            print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Masih ngintai @{target}...", flush=True)
    except KeyboardInterrupt:
        print_status("WARNING", f"Berhenti ngintai @{target}.")
"""

with open('noxloader/core/extra_menus.py', 'a') as f:
    f.write(new_func)
print("Updated extra_menus.py")
