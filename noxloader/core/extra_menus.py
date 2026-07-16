import time
import datetime
import os
import subprocess
from downloader.engine import UniversalDownloader
from ui.theme import current_color, RESET, clear, print_status, LIGHT_GRAY
from ui.banner import show_banner, print_footer
from ui.animations import spinner
from config.settings import load_settings, save_settings
from utils.helpers import get_urls_input, init_dirs

def noxstream_menu():
    base_dir = init_dirs()
    clear()
    show_banner()
    c = current_color()
    print_status("INFO", "NOXSTREAM (Live Recorder)")
    print(f"{LIGHT_GRAY}  Gwe bakal record live streaming terus sampe dia mati / lu stop (CTRL+C).{RESET}")
    urls = get_urls_input()
    if urls:
        spinner("Siap-siap record live...", 2)
        dl = UniversalDownloader(base_dir)
        dl.download(urls, "Live", format_type='best')
        print_footer()
        input(f"\n{c}  [Enter] Balik ke menu...{RESET}")

def ngalong_mode():
    base_dir = init_dirs()
    clear()
    show_banner()
    c = current_color()
    print_status("INFO", "NGALONG MODE (Download Jam 2 Pagi)")
    print(f"{LIGHT_GRAY}  Link yang lu masukin bakal dieksekusi otomatis pas kuota malam aktif!{RESET}")
    urls = get_urls_input()
    if urls:
        print(f"\n{c}  [1] Best Resolution{RESET}")
        print(f"{c}  [2] Audio Only (MP3){RESET}")
        pilih = input(f"{c}  😈 Pilih format: {RESET}").strip()
        fmt = 'best'
        if pilih == '2': fmt = 'Audio MP3'
        
        now = datetime.datetime.now()
        target = now.replace(hour=2, minute=0, second=0, microsecond=0)
        if target < now:
            target += datetime.timedelta(days=1)
            
        print_status("SUCCESS", f"Sip cok! Gwe bakal nunggu sampe jam {target.strftime('%H:%M:%S')}")
        print(f"{LIGHT_GRAY}  Jangan tutup aplikasinya, biarin aja standby.{RESET}")
        
        while True:
            try:
                now_dt = datetime.datetime.now()
                if now_dt >= target:
                    break
                time.sleep(10)
            except KeyboardInterrupt:
                print_status("WARNING", "Ngalong mode dibatalin.")
                return
                
        print_status("INFO", "Waktunya beraksi cok! Kuota malam gass...")
        dl = UniversalDownloader(base_dir)
        dl.download(urls, "Universal", format_type=fmt)
        print_footer()
        input(f"\n{c}  [Enter] Balik ke menu...{RESET}")

def ghost_mode():
    clear()
    show_banner()
    c = current_color()
    print_status("INFO", "GHOST MODE (Tor/Proxy Rotator)")
    print(f"{LIGHT_GRAY}  Pake ini biar IP lu aman pas mass-download atau nembus blokir.{RESET}")
    print(f"{LIGHT_GRAY}  Pastikan lu udah install & jalanin Tor di Termux (pkg install tor).{RESET}")
    print(f"{c}  [1] Aktifin Ghost Mode (Pake Proxy Tor){RESET}")
    print(f"{c}  [2] Matiin Ghost Mode{RESET}")
    p = input(f"\n{c}  😈 Pilihan: {RESET}").strip()
    
    cfg = load_settings()
    if p == '1':
        cfg['ghost_mode'] = True
        save_settings(cfg)
        print_status("SUCCESS", "Ghost Mode AKTIF! Gwe bakal nyamar pake Proxy.")
    else:
        cfg['ghost_mode'] = False
        save_settings(cfg)
        print_status("WARNING", "Ghost Mode MATI. Balik ke IP asli.")
    
    input(f"\n{c}  [Enter] Balik ke menu...{RESET}")

def noxaudio_menu():
    base_dir = init_dirs()
    clear()
    show_banner()
    c = current_color()
    print_status("INFO", "NOXAUDIO (Spotify / Soundcloud / Apple Music)")
    print(f"{LIGHT_GRAY}  Link musik bakal disedot jadi MP3 320kbps High Quality!{RESET}")
    urls = get_urls_input()
    if urls:
        spinner("Menganalisis link musik...", 2)
        dl = UniversalDownloader(base_dir)
        dl.download(urls, "Music", format_type='Audio MP3')
        print_footer()
        input(f"\n{c}  [Enter] Balik ke menu...{RESET}")

def auto_cutter():
    clear()
    show_banner()
    c = current_color()
    print_status("INFO", "AUTO-CUTTER MAKER (Potong Video/Audio)")
    print(f"{LIGHT_GRAY}  Pastikan file ada di folder Download/NoxLoader{RESET}")
    file_path = input(f"\n{c}  📁 Masukin nama file (contoh: video.mp4): {RESET}").strip()
    start_time = input(f"{c}  ⏳ Mulai di detik ke (contoh: 00:00:10): {RESET}").strip()
    duration = input(f"{c}  ⏱️ Durasi potongan (contoh: 00:00:05 buat 5 detik): {RESET}").strip()
    
    if not file_path or not start_time or not duration:
        return
        
    base = init_dirs()
    
    found_path = None
    for root, dirs, files in os.walk(base):
        if file_path in files:
            found_path = os.path.join(root, file_path)
            break
            
    if not found_path:
        print_status("ERROR", "File nggak ketemu cok. Tulis namanya yg bener sama ekstensinya.")
        input(f"\n{c}  [Enter] Balik ke menu...{RESET}")
        return
        
    out_file = os.path.join(os.path.dirname(found_path), f"cut_{file_path}")
    print_status("INFO", "Gwe potong file nya bentar...")
    
    try:
        subprocess.run(["ffmpeg", "-i", found_path, "-ss", start_time, "-t", duration, "-c", "copy", out_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print_status("SUCCESS", f"Mantap cok! Hasilnya: {out_file}")
    except Exception as e:
        print_status("ERROR", f"Gagal potong: {e}. Pastikan FFmpeg udah diinstall.")
        
    input(f"\n{c}  [Enter] Balik ke menu...{RESET}")

def scraper_menu():
    base_dir = init_dirs()
    clear()
    show_banner()
    c = current_color()
    print_status("INFO", "PREMIUM SCRAPER (Drive / Web Khusus)")
    print(f"{LIGHT_GRAY}  (Pastikan lu udah setup Auto Cookie di Menu 8 biar bisa nembus web login){RESET}")
    urls = get_urls_input()
    if urls:
        spinner("Menganalisis web target...", 2)
        dl = UniversalDownloader(base_dir)
        dl.download(urls, "Scraper", format_type='best')
        print_footer()
        input(f"\n{c}  [Enter] Balik ke menu...{RESET}")

