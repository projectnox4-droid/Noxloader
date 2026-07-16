import os
import time
from ui.theme import clear, print_neon, CYAN, RESET
from ui.banner import show_banner
from ui.animations import spinner
from utils.installer import install_deps, check_deps, update_engine
from utils.scanner import scan_url
from utils.cleaner import clean_cache
from utils.recon import recon_url
from history.manager import show_history
from config.settings import show_settings
from downloader.engine import UniversalDownloader

def init_dirs():
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

def get_urls_input():
    urls = []
    print(f"\n{CYAN}  🤪 Tempel linknya sini cok (Bisa banyak, pisahkan spasi / paste berjejer): {RESET}")
    print(f"{CYAN}  (Ketik 'gas' trus Enter kalau udah selesai paste){RESET}")
    while True:
        try:
            line = input(f"{CYAN}  > {RESET}").strip()
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

from core.extra_menus import noxstream_menu, ngalong_mode, ghost_mode, noxaudio_menu, auto_cutter, scraper_menu

def submenu(title, options, platform):
    base_dir = init_dirs()
    while True:
        clear()
        show_banner()
        print(f"{CYAN}  === {title} ==={RESET}")
        for i, opt in enumerate(options, 1):
            print(f"{CYAN}  [{i}] {opt}{RESET}")
        print(f"{CYAN}  [0] 🔙 Kembali{RESET}\n")
        
        try:
            pilih = input(f"{CYAN}  😈 Pilih format cok: {RESET}").strip()
        except EOFError:
            continue
            
        if pilih == '0':
            break
            
        try:
            idx = int(pilih) - 1
            if 0 <= idx < len(options):
                opt_name = options[idx]
                
                # Resolusi cuma buat video
                res_fmt = 'best'
                if any(x in opt_name for x in ["Video", "Reels", "Story", "Post", "Shorts"]):
                    print(f"\n{CYAN}  [1] Best (Resolusi Tertinggi){RESET}")
                    print(f"{CYAN}  [2] 1080p{RESET}")
                    print(f"{CYAN}  [3] 720p{RESET}")
                    print(f"{CYAN}  [4] 480p{RESET}")
                    res_input = input(f"{CYAN}  😎 Pilih kualitas resolusi (1-4, Default 1): {RESET}").strip()
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
                    print(f"{CYAN}  🔍 Bentar cok, gwe terawang dulu link lu...{RESET}")
                    spinner("Menganalisis link...", 2)
                    dl = UniversalDownloader(base_dir)
                    dl.download(urls, platform, format_type=opt_name, res_fmt=res_fmt)
                    input(f"\n{CYAN}  [Enter] Balik ke menu...{RESET}")
            else:
                spinner("Menu apaan tuh...", 1)
        except ValueError:
            spinner("Menu apaan tuh...", 1)

def main_menu():
    base_dir = init_dirs()
    while True:
        clear()
        show_banner()
        print(f"{CYAN}  ========================================")
        print(f"{CYAN}           🔥 CORE FEATURES 🔥            ")
        print(f"{CYAN}  ========================================")
        print(f"{CYAN}  [1] 📺 NOXYOU")
        print(f"{CYAN}  [2] 🎵 NOXTOK")
        print(f"{CYAN}  [3] 📷 NOXGRAM")
        print(f"{CYAN}  [4] 📘 NOXBOOK")
        print(f"{CYAN}  [5] ❌ NOXX")
        print(f"{CYAN}  [6] 🎬 NOXVID")
        print(f"{CYAN}  [7] 🌐 Universal")
        print(f"{CYAN}  [8] 🔐 Akses Private (Auto Cookie)")
        print(f"{CYAN}  [9] 🕵️ Intel Recon (Cek Info Meta)")
        print(f"{CYAN}  ========================================")
        print(f"{CYAN}            😈 OP FEATURES 😈             ")
        print(f"{CYAN}  ========================================")
        print(f"{CYAN}  [10] 🔴 NOXSTREAM (Live Recorder)")
        print(f"{CYAN}  [11] 🦇 Ngalong Mode (Jadwal Malam)")
        print(f"{CYAN}  [12] 👻 Ghost Mode (Tor/Proxy Rotator)")
        print(f"{CYAN}  [13] 🎧 NOXAUDIO (Spotify/Soundcloud)")
        print(f"{CYAN}  [14] ✂️ Auto-Cutter Maker")
        print(f"{CYAN}  [15] 🔞 Premium Scraper (Drive/OF)")
        print(f"{CYAN}  ========================================")
        print(f"{CYAN}           ⚙️ SYSTEM TOOLS ⚙️             ")
        print(f"{CYAN}  ========================================")
        print(f"{CYAN}  [16] 📦 Install Bahan")
        print(f"{CYAN}  [17] 🔍 Cek Bahan")
        print(f"{CYAN}  [18] 🔄 Update Engine (yt-dlp)")
        print(f"{CYAN}  [19] 📜 Riwayat")
        print(f"{CYAN}  [20] 🧹 Bersihkan Cache")
        print(f"{CYAN}  [21] ⚙ Pengaturan")
        print(f"{CYAN}  [0] 🚪 Keluar{RESET}")
        print()
        
        try:
            pilih = input(f"{CYAN}  💀 Pilih menu cok: {RESET}").strip()
        except EOFError:
            continue

        if pilih == '0':
            clear()
            print(f"{CYAN}🥱 Balik rebahan dulu cok. See you! 🤙{RESET}")
            break
        elif pilih == '1':
            submenu("📺 NOXYOU", ["Video MP4", "Audio MP3", "Playlist Video", "Playlist MP3", "Channel", "Shorts", "Batch URL"], "YouTube")
        elif pilih == '2':
            submenu("🎵 NOXTOK", ["Video Tanpa Watermark", "Audio Sound", "Slide Foto", "Profile Mass Download", "Batch URL"], "TikTok")
        elif pilih == '3':
            submenu("📷 NOXGRAM", ["Reels", "Post", "Story", "Profile Mass Download", "Batch URL"], "Instagram")
        elif pilih == '4':
            submenu("📘 NOXBOOK", ["Video FB", "Reels FB", "Profile/Page Mass Download", "Batch URL"], "Facebook")
        elif pilih == '5':
            submenu("❌ NOXX", ["Video Tweet", "GIF Tweet", "Media Profile", "Batch URL"], "X")
        elif pilih == '6':
            submenu("🎬 NOXVID", ["Video Format Biasa", "Video Kualitas Tinggi", "Batch URL"], "Vimeo")
        elif pilih == '7':
            urls = get_urls_input()
                
            if not urls: continue
            
            clear()
            show_banner()
            print(f"{CYAN}  🔍 Bentar cok, gwe terawang dulu link lu...{RESET}")
            spinner("Menganalisis domain...", 2)
            
            dl = UniversalDownloader(base_dir)
            dl.download(urls, "Universal", format_type='best')
                
            input(f"\n{CYAN}  [Enter] Balik ke menu...{RESET}")
            
        elif pilih == '8':
            clear()
            show_banner()
            try:
                from utils.clipboard import save_cookie_from_clipboard
            except Exception:
                save_cookie_from_clipboard = lambda: False
                
            print(f"{CYAN}  🔐 SETUP AUTO COOKIE & PRIVATE DOWNLOAD{RESET}\n")
            spinner("Ngecek clipboard keyboard lu...", 2)
            
            if save_cookie_from_clipboard():
                print(f"  {CYAN}✔ Weh, nemu format Cookie di keyboard lu! Udah gwe tempel otomatis. 😈{RESET}")
                time.sleep(1)
                
                urls = get_urls_input()
                if urls:
                    clear()
                    show_banner()
                    print(f"{CYAN}  🔍 Bentar cok, gwe terawang dulu link private lu...{RESET}")
                    spinner("Menganalisis link...", 2)
                    dl = UniversalDownloader(base_dir)
                    dl.download(urls, "Universal", format_type='best')
                    input(f"\n{CYAN}  [Enter] Balik ke menu...{RESET}")
            else:
                print(f"  {CYAN}💀 Clipboard lu kosong atau bukan format cookie.{RESET}\n")
                print(f"  {CYAN}Syarat Auto Cookie (Biar Gwe Bisa Nembus):{RESET}")
                print(f"  {CYAN}1. Buka browser, pake ekstensi 'Get cookies.txt LOCALLY'.{RESET}")
                print(f"  {CYAN}2. Copy semua teks/isi cookie nya.{RESET}")
                print(f"  {CYAN}3. Pastikan lu udah install aplikasi 'Termux:API' di HP lu.{RESET}")
                print(f"  {CYAN}   (Atau jalanin Menu 9 - Install Bahan).{RESET}")
                print(f"  {CYAN}4. Balik ke NoxLoader, pencet Menu 8 lagi. Otomatis ketempel!{RESET}")
                input(f"\n{CYAN}  [Enter] Balik ke menu...{RESET}")
                
        elif pilih == '9':
            recon_url()
        elif pilih == '10':
            noxstream_menu()
        elif pilih == '11':
            ngalong_mode()
        elif pilih == '12':
            ghost_mode()
        elif pilih == '13':
            noxaudio_menu()
        elif pilih == '14':
            auto_cutter()
        elif pilih == '15':
            scraper_menu()
        elif pilih == '16':
            clear()
            show_banner()
            install_deps()
            input(f"\n{CYAN}  [Enter] Balik ke menu...{RESET}")
        elif pilih == '17':
            clear()
            show_banner()
            check_deps()
            input(f"\n{CYAN}  [Enter] Balik ke menu...{RESET}")
        elif pilih == '18':
            clear()
            show_banner()
            update_engine()
            input(f"\n{CYAN}  [Enter] Balik ke menu...{RESET}")
        elif pilih == '19':
            clear()
            show_banner()
            show_history()
            input(f"\n{CYAN}  [Enter] Balik ke menu...{RESET}")
        elif pilih == '20':
            clear()
            show_banner()
            clean_cache()
            input(f"\n{CYAN}  [Enter] Balik ke menu...{RESET}")
        elif pilih == '21':
            show_settings()
        else:
            spinner("Menu apaan tuh...", 1)
