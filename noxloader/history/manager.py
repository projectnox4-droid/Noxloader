import json
import os
from datetime import datetime

def get_history_file():
    base = os.path.expanduser("~/storage/shared/Download/NoxLoader")
    if not os.path.exists(os.path.expanduser("~/storage/shared")):
        base = os.path.join(os.getcwd(), "Download", "NoxLoader")
    hist_dir = os.path.join(base, "History")
    os.makedirs(hist_dir, exist_ok=True)
    return os.path.join(hist_dir, "history.json")

def add_history(platform, title, status, file_path=""):
    hist_file = get_history_file()
    data = []
    if os.path.exists(hist_file):
        try:
            with open(hist_file, 'r') as f:
                data = json.load(f)
        except: pass
    
    data.append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "platform": platform,
        "title": title,
        "status": status,
        "path": file_path
    })
    
    with open(hist_file, 'w') as f:
        json.dump(data[-50:], f, indent=4)

def show_history():
    from ui.theme import CYAN, RESET
    hist_file = get_history_file()
    if not os.path.exists(hist_file):
        print(f"  {CYAN}📜 Belum ada riwayat nih cok. Kosong melompong.{RESET}")
        return
        
    try:
        with open(hist_file, 'r') as f:
            data = json.load(f)
        if not data:
            print(f"  {CYAN}📜 Belum ada riwayat nih cok.{RESET}")
            return
            
        print(f"  {CYAN}📜 RIWAYAT DOWNLOAD (50 Terakhir):{RESET}\n")
        for item in reversed(data):
            print(f"  {CYAN}[{item['date']}] {item['platform']} - {item['status']}{RESET}")
            print(f"  {CYAN}↳ {item['title'][:50]}...{RESET}\n")
    except:
        print(f"  {CYAN}💀 File riwayat error cok.{RESET}")
