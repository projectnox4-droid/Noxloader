import json
import os
import datetime
from ui.theme import current_color, RESET, clear, print_status, LIGHT_GRAY
from ui.banner import show_banner
from utils.helpers import init_dirs

def get_history_file():
    base = init_dirs()
    return os.path.join(base, "History", "history.json")

def add_history(platform, title, status):
    hf = get_history_file()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {"time": now, "platform": platform, "title": title, "status": status}
    history = []
    if os.path.exists(hf):
        try:
            with open(hf, 'r') as f:
                history = json.load(f)
        except: pass
    history.append(entry)
    with open(hf, 'w') as f:
        json.dump(history, f, indent=4)

def show_history():
    clear()
    show_banner()
    c = current_color()
    print_status("INFO", "RIWAYAT DOWNLOAD")
    hf = get_history_file()
    if not os.path.exists(hf):
        print(f"  {LIGHT_GRAY}Belum ada riwayat cok.{RESET}\n")
    else:
        try:
            with open(hf, 'r') as f:
                history = json.load(f)
            
            # Print last 10 entries
            for h in history[-10:]:
                st_color = "\033[38;2;0;255;0m" if h['status'] == "Sukses" else "\033[38;2;255;0;51m"
                print(f"  {c}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{RESET}")
                print(f"  {c}┃ {LIGHT_GRAY}⏱  {h['time']}{' '*16}{c} ┃{RESET}")
                print(f"  {c}┃ {LIGHT_GRAY}🌐 {h['platform'][:10].ljust(10)} | {st_color}{h['status'].ljust(6)}{' '*14}{c} ┃{RESET}")
                print(f"  {c}┃ {LIGHT_GRAY}📌 {h['title'][:32].ljust(32)}{c} ┃{RESET}")
                print(f"  {c}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{RESET}")
        except:
            print(f"  {LIGHT_GRAY}Gagal load riwayat.{RESET}")
    input(f"\n{c}  [Enter] Balik ke menu...{RESET}")
