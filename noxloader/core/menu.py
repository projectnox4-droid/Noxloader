import os
import time
from ui.theme import clear, print_neon, print_status, current_color, ThemeManager, RESET, BOLD, rgb, LIGHT_GRAY, NEON_GREEN, NEON_CYAN, NEON_BLUE
from ui.banner import show_banner, print_footer
from ui.animations import spinner
from utils.installer import install_deps, check_deps, update_engine
from utils.scanner import scan_url
from utils.cleaner import clean_cache
from utils.recon import recon_url
from history.manager import show_history
from config.settings import show_settings
from downloader.engine import UniversalDownloader

def old_init_dirs():
    dirs = [
        "YouTube", "TikTok", "Instagram", "Facebook",
        "X", "Vimeo", "Universal", "History",
        "Cache", "Temp", "Logs", "Config"
    ]
    # Path default termux
    base = os.path.expanduser("~/storage/shared/Download/NoxLoader")
    if not os.path.exists(os.path.expanduser("~/storage/shared")):
        base = os.path.join(os.getcwd(), "Download", "NoxLoader")

    for d in dirs:
        os.makedirs(os.path.join(base, d), exist_ok=True)
    return base

def old_get_urls_input():
    urls = []
    c = current_color()
    print(f"\n{c}  🤪 Tempel linknya sini cok (Bisa banyak, pisahkan spasi / paste berjejer): {RESET}")
    print(f"{LIGHT_GRAY}  (Ketik 'gas' trus Enter kalau udah selesai paste){RESET}")
    while True:
        try:
            line = input(f"{c}  > {RESET}").strip()
            if line.lower() == 'gas':
                break
            if line:
                for u in line.split():
                    if u.startswith('http'):
                        urls.append(u)
        except EOFError:
            break
        except KeyboardInterrupt:
            break
    return urls

from utils.helpers import get_urls_input, init_dirs
from core.extra_menus import noxstream_menu, ngalong_mode, ghost_mode, noxaudio_menu, auto_cutter, scraper_menu

def submenu(title, options, platform, menu_id):
    ThemeManager.current_menu = menu_id
    c = current_color()
    base_dir = init_dirs()
    while True:
        clear()
        show_banner()
        print(f"{c}  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{RESET}")
        print(f"{c}  ┃ {BOLD}😎 {title.ljust(33)}{c}┃{RESET}")
        print(f"{c}  ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫{RESET}")
        for i, opt in enumerate(options, 1):
            print(f"{c}  ┃ [{i}] {LIGHT_GRAY}{opt.ljust(30)}{c} ┃{RESET}")
        print(f"{c}  ┃ {rgb(100,100,100)}[0] 🔙 Kembali{' '*20}{c} ┃{RESET}")
        print(f"{c}  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{RESET}")
        
        try:
            pilih = input(f"{c}  😈 Pilih format: {RESET}").strip()
        except EOFError:
            continue
            
        if pilih == '0':
            ThemeManager.current_menu = "CORE"
            break
            
        try:
            idx = int(pilih) - 1
            if 0 <= idx < len(options):
                opt_name = options[idx]
                res_fmt = 'best'
                if any(x in opt_name for x in ["Video", "Reels", "Story", "Post", "Shorts"]):
                    print(f"\n{c}  [1] Best (Resolusi Tertinggi){RESET}")
                    print(f"{c}  [2] 1080p{RESET}")
                    print(f"{c}  [3] 720p{RESET}")
                    print(f"{c}  [4] 480p{RESET}")
                    res_input = input(f"{c}  😎 Pilih resolusi (1-4, Default 1): {RESET}").strip()
                    if res_input == '2':
                        res_fmt = 'bestvideo[height<=1080]+bestaudio/best[height<=1080]/best'
                    elif res_input == '3':
                        res_fmt = 'bestvideo[height<=720]+bestaudio/best[height<=720]/best'
                    elif res_input == '4':
                        res_fmt = 'bestvideo[height<=480]+bestaudio/best[height<=480]/best'

                urls = get_urls_input()
                if urls:
                    clear()
                    show_banner()
                    scan_url() # Call scan progress UI
                    dl = UniversalDownloader(base_dir)
                    dl.download(urls, platform, format_type=opt_name, res_fmt=res_fmt)
                    print_footer()
                    input(f"\n{c}  [Enter] Balik ke menu...{RESET}")
            else:
                spinner("Menu apaan tuh...", 1)
        except ValueError:
            spinner("Menu apaan tuh...", 1)

def main_menu():
    base_dir = init_dirs()
    ThemeManager.current_menu = "CORE"
    c = current_color()
    while True:
        clear()
        ThemeManager.current_menu = "CORE"
        c = current_color()
        show_banner()
        print(f"{c}  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{RESET}")
        print(f"{c}  ┃           🔥 CORE FEATURES 🔥            ┃{RESET}")
        print(f"{c}  ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫{RESET}")
        print(f"{c}  ┃ [1] 📺 {LIGHT_GRAY}NOXYOU{c}                         ┃{RESET}")
        print(f"{c}  ┃ [2] 🎵 {LIGHT_GRAY}NOXTOK{c}                         ┃{RESET}")
        print(f"{c}  ┃ [3] 📷 {LIGHT_GRAY}NOXGRAM{c}                        ┃{RESET}")
        print(f"{c}  ┃ [4] 📘 {LIGHT_GRAY}NOXBOOK{c}                        ┃{RESET}")
        print(f"{c}  ┃ [5] ❌ {LIGHT_GRAY}NOXX{c}                           ┃{RESET}")
        print(f"{c}  ┃ [6] 🎬 {LIGHT_GRAY}NOXVID{c}                         ┃{RESET}")
        print(f"{c}  ┃ [7] 🌐 {LIGHT_GRAY}Universal Hub{c}                  ┃{RESET}")
        print(f"{c}  ┃ [8] 🔐 {LIGHT_GRAY}Akses Private (Auto Cookie){c}    ┃{RESET}")
        print(f"{c}  ┃ [9] 🕵️ {LIGHT_GRAY}Intel Recon (Cek Meta){c}         ┃{RESET}")
        print(f"{c}  ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫{RESET}")
        print(f"{c}  ┃            😈 OP FEATURES 😈             ┃{RESET}")
        print(f"{c}  ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫{RESET}")
        print(f"{c}  ┃ [10] 🔴 {LIGHT_GRAY}NOXSTREAM (Live Recorder){c}     ┃{RESET}")
        print(f"{c}  ┃ [11] 🦇 {LIGHT_GRAY}Ngalong Mode (Jadwal Malam){c}   ┃{RESET}")
        print(f"{c}  ┃ [12] 👻 {LIGHT_GRAY}Ghost Mode (Proxy Rotator){c}    ┃{RESET}")
        print(f"{c}  ┃ [13] 🎧 {LIGHT_GRAY}NOXAUDIO (Music/Spotify){c}      ┃{RESET}")
        print(f"{c}  ┃ [14] ✂️ {LIGHT_GRAY}Auto-Cutter Maker{c}            ┃{RESET}")
        print(f"{c}  ┃ [15] 🔞 {LIGHT_GRAY}Premium Scraper (Drive/OF){c}    ┃{RESET}")
        print(f"{c}  ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫{RESET}")
        print(f"{c}  ┃           ⚙️ SYSTEM TOOLS ⚙️             ┃{RESET}")
        print(f"{c}  ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫{RESET}")
        print(f"{c}  ┃ [16] 📦 {LIGHT_GRAY}Install Bahan{c}                 ┃{RESET}")
        print(f"{c}  ┃ [17] 🔍 {LIGHT_GRAY}Cek Bahan{c}                     ┃{RESET}")
        print(f"{c}  ┃ [18] 🔄 {LIGHT_GRAY}Update Engine{c}                 ┃{RESET}")
        print(f"{c}  ┃ [19] 📜 {LIGHT_GRAY}Riwayat{c}                       ┃{RESET}")
        print(f"{c}  ┃ [20] 🧹 {LIGHT_GRAY}Bersihkan Cache{c}               ┃{RESET}")
        print(f"{c}  ┃ [21] 🕵️ {LIGHT_GRAY}Stalker Mode{c}                  ┃{RESET}")
        print(f"{c}  ┃ [22] ⚙  {LIGHT_GRAY}Pengaturan{c}                    ┃{RESET}")
        print(f"{c}  ┃ {rgb(100,100,100)}[0]  🚪 Keluar{' '*22}{c} ┃{RESET}")
        print(f"{c}  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{RESET}")
        print()
        
        try:
            pilih = input(f"{c}  💀 Pilih menu: {RESET}").strip()
        except EOFError:
            continue

        if pilih == '0':
            clear()
            print_status("INFO", "Balik rebahan dulu cok. See you! 🤙")
            break
        elif pilih == '1':
            submenu("📺 NOXYOU", ["Video MP4", "Audio MP3", "Playlist Video", "Playlist MP3", "Channel", "Shorts", "Batch URL"], "YouTube", "NOXYOU")
        elif pilih == '2':
            submenu("🎵 NOXTOK", ["Video Tanpa Watermark", "Audio Sound", "Slide Foto", "Profile Mass Download", "Batch URL"], "TikTok", "NOXTOK")
        elif pilih == '3':
            submenu("📷 NOXGRAM", ["Reels", "Post", "Story", "Profile Mass Download", "Batch URL"], "Instagram", "NOXGRAM")
        elif pilih == '4':
            submenu("📘 NOXBOOK", ["Video FB", "Reels FB", "Profile/Page Mass Download", "Batch URL"], "Facebook", "NOXBOOK")
        elif pilih == '5':
            submenu("❌ NOXX", ["Video Tweet", "GIF Tweet", "Media Profile", "Batch URL"], "X", "NOXX")
        elif pilih == '6':
            submenu("🎬 NOXVID", ["Video Format Biasa", "Video Kualitas Tinggi", "Batch URL"], "Vimeo", "NOXVID")
        elif pilih == '7':
            ThemeManager.current_menu = "UNIVERSAL"
            c = current_color()
            urls = get_urls_input()
            if not urls: continue
            
            clear()
            show_banner()
            scan_url()
            dl = UniversalDownloader(base_dir)
            dl.download(urls, "Universal", format_type='best')
            print_footer()
            input(f"\n{c}  [Enter] Balik ke menu...{RESET}")
            
        elif pilih == '8':
            ThemeManager.current_menu = "CORE"
            clear()
            show_banner()
            try:
                from utils.clipboard import save_cookie_from_clipboard
            except Exception:
                save_cookie_from_clipboard = lambda: False
                
            print(f"{c}  🔐 SETUP AUTO COOKIE & PRIVATE DOWNLOAD{RESET}\n")
            spinner("Ngecek clipboard keyboard lu...", 2)
            
            if save_cookie_from_clipboard():
                print_status("SUCCESS", "Weh, nemu format Cookie! Udah gwe tempel otomatis. 😈")
                time.sleep(1)
                urls = get_urls_input()
                if urls:
                    clear()
                    show_banner()
                    scan_url()
                    dl = UniversalDownloader(base_dir)
                    dl.download(urls, "Universal", format_type='best')
                    input(f"\n{c}  [Enter] Balik ke menu...{RESET}")
            else:
                print_status("ERROR", "Clipboard kosong atau bukan format cookie.")
                print(f"  {c}Syarat Auto Cookie:{RESET}")
                print(f"  {LIGHT_GRAY}1. Buka browser, pake ekstensi 'Get cookies.txt LOCALLY'.{RESET}")
                print(f"  {LIGHT_GRAY}2. Copy semua teks cookie-nya.{RESET}")
                print(f"  {LIGHT_GRAY}3. Install 'Termux:API' di HP lu (Atau Menu 16).{RESET}")
                print(f"  {LIGHT_GRAY}4. Balik sini, pencet Menu 8 lagi.{RESET}")
                input(f"\n{c}  [Enter] Balik ke menu...{RESET}")
                
        elif pilih == '9':
            ThemeManager.current_menu = "CORE"
            recon_url()
        elif pilih == '10':
            ThemeManager.current_menu = "CORE"
            noxstream_menu()
        elif pilih == '11':
            ThemeManager.current_menu = "CORE"
            ngalong_mode()
        elif pilih == '12':
            ThemeManager.current_menu = "CORE"
            ghost_mode()
        elif pilih == '13':
            ThemeManager.current_menu = "CORE"
            noxaudio_menu()
        elif pilih == '14':
            ThemeManager.current_menu = "CORE"
            auto_cutter()
        elif pilih == '15':
            ThemeManager.current_menu = "CORE"
            scraper_menu()
        elif pilih == '16':
            ThemeManager.current_menu = "CORE"
            clear()
            show_banner()
            install_deps()
            input(f"\n{c}  [Enter] Balik ke menu...{RESET}")
        elif pilih == '17':
            ThemeManager.current_menu = "CORE"
            clear()
            show_banner()
            check_deps()
            input(f"\n{c}  [Enter] Balik ke menu...{RESET}")
        elif pilih == '18':
            ThemeManager.current_menu = "CORE"
            clear()
            show_banner()
            update_engine()
            input(f"\n{c}  [Enter] Balik ke menu...{RESET}")
        elif pilih == '19':
            ThemeManager.current_menu = "CORE"
            clear()
            show_banner()
            show_history()
            input(f"\n{c}  [Enter] Balik ke menu...{RESET}")
        elif pilih == '20':
            ThemeManager.current_menu = "CORE"
            clear()
            show_banner()
            clean_cache()
            input(f"\n{c}  [Enter] Balik ke menu...{RESET}")
        elif pilih == '21':
            ThemeManager.current_menu = "CORE"
            from core.extra_menus import stalker_mode
            stalker_mode()
        elif pilih == '22':
            ThemeManager.current_menu = "CORE"
            show_settings()
        else:
            spinner("Menu apaan tuh...", 1)

