import time
from ui.theme import current_color, RESET, print_status
from ui.animations import spinner, progress_bar, typing_effect

def scan_url():
    c = current_color()
    print()
    print_status("INFO", "Ngendus link...")
    for i in range(1, 11):
        progress_bar(i, 10, prefix='Ngendus link... ', suffix='', length=20)
        time.sleep(0.05)
    
    print_status("INFO", "Domain...")
    for i in range(1, 11):
        progress_bar(i, 10, prefix='Domain...       ', suffix='', length=20)
        time.sleep(0.05)
        
    print_status("INFO", "Platform...")
    for i in range(1, 11):
        progress_bar(i, 10, prefix='Platform...     ', suffix='', length=20)
        time.sleep(0.05)
        
    print_status("INFO", "Metadata...")
    for i in range(1, 11):
        progress_bar(i, 10, prefix='Metadata...     ', suffix='', length=20)
        time.sleep(0.05)
        
    print()
    typing_effect("✅ Target dikunci, siap eksekusi...", 0.02)
    print()
