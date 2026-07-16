import json
import os
from ui.theme import current_color, RESET, clear, print_status, LIGHT_GRAY
from ui.banner import show_banner

def get_settings_file():
    base = os.path.expanduser("~/storage/shared/Download/NoxLoader")
    if not os.path.exists(os.path.expanduser("~/storage/shared")):
        base = os.path.join(os.getcwd(), "Download", "NoxLoader")
    conf_dir = os.path.join(base, "Config")
    os.makedirs(conf_dir, exist_ok=True)
    return os.path.join(conf_dir, "settings.json")

def load_settings():
    sf = get_settings_file()
    default = {
        "theme": "cyan",
        "animation": True,
        "speed_limit": 0,
        "download_subtitle": False,
        "download_thumbnail": False,
        "auto_metadata": True,
        "aria2_booster": False
    }
    if os.path.exists(sf):
        try:
            with open(sf, 'r') as f:
                default.update(json.load(f))
        except: pass
    return default

def save_settings(data):
    sf = get_settings_file()
    with open(sf, 'w') as f:
        json.dump(data, f, indent=4)

def show_settings():
    while True:
        cfg = load_settings()
        clear()
        show_banner()
        c = current_color()
        print_status("INFO", "PENGATURAN TONGKRONGAN")
        
        anim_str = "Aktif" if cfg["animation"] else "Mati"
        sub_str = "Aktif" if cfg["download_subtitle"] else "Mati"
        thumb_str = "Aktif" if cfg["download_thumbnail"] else "Mati"
        meta_str = "Aktif" if cfg["auto_metadata"] else "Mati"
        aria_str = "Aktif" if cfg.get("aria2_booster", False) else "Mati"
        spd = cfg["speed_limit"]
        spd_str = f"{spd} KB/s" if spd > 0 else "Ngebut (No Limit)"
        
        print(f"{c}  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{RESET}")
        print(f"{c}  ┃ [1] 🏃 {LIGHT_GRAY}Speed Limit       : {spd_str.ljust(11)}{c} ┃{RESET}")
        print(f"{c}  ┃ [2] 📝 {LIGHT_GRAY}Download Subtitle : {sub_str.ljust(11)}{c} ┃{RESET}")
        print(f"{c}  ┃ [3] 🖼️  {LIGHT_GRAY}Download Sampul   : {thumb_str.ljust(11)}{c} ┃{RESET}")
        print(f"{c}  ┃ [4] 🏷️  {LIGHT_GRAY}Auto Metadata     : {meta_str.ljust(11)}{c} ┃{RESET}")
        print(f"{c}  ┃ [5] ✨ {LIGHT_GRAY}Animasi           : {anim_str.ljust(11)}{c} ┃{RESET}")
        print(f"{c}  ┃ [6] 🚀 {LIGHT_GRAY}Aria2 Booster     : {aria_str.ljust(11)}{c} ┃{RESET}")
        print(f"{c}  ┃ {c}[0] 🔙 Kembali{' '*22}{c} ┃{RESET}")
        print(f"{c}  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{RESET}\n")
        
        try:
            pilih = input(f"{c}  😈 Pilih yg mau diubah cok: {RESET}").strip()
        except:
            break
            
        if pilih == '0':
            break
        elif pilih == '1':
            try:
                limit = input(f"{c}  Masukkan limit (KB/s, 0 = No Limit): {RESET}")
                cfg["speed_limit"] = int(limit)
                save_settings(cfg)
            except: pass
        elif pilih == '2':
            cfg["download_subtitle"] = not cfg["download_subtitle"]
            save_settings(cfg)
        elif pilih == '3':
            cfg["download_thumbnail"] = not cfg["download_thumbnail"]
            save_settings(cfg)
        elif pilih == '4':
            cfg["auto_metadata"] = not cfg["auto_metadata"]
            save_settings(cfg)
        elif pilih == '5':
            cfg["animation"] = not cfg["animation"]
            save_settings(cfg)
        elif pilih == '6':
            cfg["aria2_booster"] = not cfg.get("aria2_booster", False)
            save_settings(cfg)

