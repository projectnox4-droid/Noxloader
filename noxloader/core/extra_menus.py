import time
import datetime
import os
import subprocess
from downloader.engine import UniversalDownloader
from ui.theme import CYAN, RESET, clear
from ui.animations import spinner
from config.settings import load_settings, save_settings
from core.menu import get_urls_input, init_dirs

def noxstream_menu():
    base_dir = init_dirs()
    clear()
    print(f"{CYAN}  🔴 NOXSTREAM (Live Recorder){RESET}")
    print(f"{CYAN}  Gwe bakal record live streaming terus sampe dia mati / lu stop (CTRL+C).{RESET}")
    urls = get_urls_input()
    if urls:
        spinner("Siap-siap record live...", 2)
        dl = UniversalDownloader(base_dir)
        dl.download(urls, "Live", format_type='best')

def ngalong_mode():
    base_dir = init_dirs()
    clear()
    print(f"{CYAN}  🦇 NGALONG MODE (Download Jam 2 Pagi){RESET}")
    print(f"{CYAN}  Link yang lu masukin bakal dieksekusi otomatis pas kuota malam aktif!{RESET}")
    urls = get_urls_input()
    if urls:
        print(f"\n{CYAN}  [1] Best Resolution{RESET}")
        print(f"{CYAN}  [2] Audio Only (MP3){RESET}")
        pilih = input(f"{CYAN}  😈 Pilih format: {RESET}").strip()
        fmt = 'best'
        if pilih == '2': fmt = 'Audio MP3'
        
        now = datetime.datetime.now()
        target = now.replace(hour=2, minute=0, second=0, microsecond=0)
        if target < now:
            target += datetime.timedelta(days=1)
            
        print(f"\n{CYAN}  😴 Sip cok! Gwe bakal nunggu sampe jam {target.strftime('%H:%M:%S')}{RESET}")
        print(f"{CYAN}  Jangan tutup aplikasinya, biarin aja standby.{RESET}")
        
        while True:
            try:
                now_dt = datetime.datetime.now()
                if now_dt >= target:
                    break
                time.sleep(10)
            except KeyboardInterrupt:
                print(f"\n{CYAN}  💀 Ngalong mode dibatalin.{RESET}")
                return
                
        print(f"\n{CYAN}  🦇 Waktunya beraksi cok! Kuota malam gass...{RESET}")
        dl = UniversalDownloader(base_dir)
        dl.download(urls, "Universal", format_type=fmt)

def ghost_mode():
    clear()
    print(f"{CYAN}  👻 GHOST MODE (Tor/Proxy Rotator){RESET}")
    print(f"{CYAN}  Pake ini biar IP lu aman pas mass-download atau nembus blokir.{RESET}")
    print(f"{CYAN}  Pastikan lu udah install & jalanin Tor di Termux (pkg install tor).{RESET}")
    print(f"{CYAN}  [1] Aktifin Ghost Mode (Pake Proxy Tor){RESET}")
    print(f"{CYAN}  [2] Matiin Ghost Mode{RESET}")
    p = input(f"\n{CYAN}  😈 Pilihan: {RESET}").strip()
    
    cfg = load_settings()
    if p == '1':
        cfg['ghost_mode'] = True
        save_settings(cfg)
        print(f"\n{CYAN}  👻 Ghost Mode AKTIF! Gwe bakal nyamar pake Proxy.{RESET}")
    else:
        cfg['ghost_mode'] = False
        save_settings(cfg)
        print(f"\n{CYAN}  👻 Ghost Mode MATI. Balik ke IP asli.{RESET}")

def noxaudio_menu():
    base_dir = init_dirs()
    clear()
    print(f"{CYAN}  🎧 NOXAUDIO (Spotify / Soundcloud / Apple Music){RESET}")
    print(f"{CYAN}  Link musik bakal disedot jadi MP3 320kbps High Quality!{RESET}")
    urls = get_urls_input()
    if urls:
        spinner("Menganalisis link musik...", 2)
        dl = UniversalDownloader(base_dir)
        dl.download(urls, "Music", format_type='Audio MP3')

def auto_cutter():
    clear()
    print(f"{CYAN}  ✂️ AUTO-CUTTER MAKER (Potong Video/Audio){RESET}")
    print(f"{CYAN}  Pastikan file ada di folder Download/NoxLoader{RESET}")
    file_path = input(f"\n{CYAN}  📁 Masukin nama file (contoh: video.mp4): {RESET}").strip()
    start_time = input(f"{CYAN}  ⏳ Mulai di detik ke (contoh: 00:00:10): {RESET}").strip()
    duration = input(f"{CYAN}  ⏱️ Durasi potongan (contoh: 00:00:05 buat 5 detik): {RESET}").strip()
    
    if not file_path or not start_time or not duration:
        return
        
    base = init_dirs()
    
    found_path = None
    for root, dirs, files in os.walk(base):
        if file_path in files:
            found_path = os.path.join(root, file_path)
            break
            
    if not found_path:
        print(f"\n{CYAN}  💀 File nggak ketemu cok. Tulis namanya yg bener sama ekstensinya.{RESET}")
        return
        
    out_file = os.path.join(os.path.dirname(found_path), f"cut_{file_path}")
    print(f"\n{CYAN}  ✂️ Gwe potong file nya bentar...{RESET}")
    
    try:
        subprocess.run(["ffmpeg", "-i", found_path, "-ss", start_time, "-t", duration, "-c", "copy", out_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{CYAN}  ✅ Mantap cok! Hasilnya: {out_file}{RESET}")
    except Exception as e:
        print(f"{CYAN}  💀 Gagal potong: {e}. Pastikan FFmpeg udah diinstall.{RESET}")

def scraper_menu():
    base_dir = init_dirs()
    clear()
    print(f"{CYAN}  🔞 PREMIUM SCRAPER (Drive / Web Khusus){RESET}")
    print(f"{CYAN}  (Pastikan lu udah setup Auto Cookie di Menu 8 biar bisa nembus web login){RESET}")
    urls = get_urls_input()
    if urls:
        spinner("Menganalisis web target...", 2)
        dl = UniversalDownloader(base_dir)
        dl.download(urls, "Scraper", format_type='best')
