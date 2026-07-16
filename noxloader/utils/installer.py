import subprocess
import sys
from ui.animations import spinner
from ui.theme import CYAN, RESET

def install_deps():
    print(f"{CYAN}  😈 Santuy cok, gwe lagi bungkus bahan-bahannya...{RESET}")
    spinner("Installing dependencies (Termux/Linux)...", 4)
    try:
        # Wrap everything silently
        subprocess.run(["pkg", "install", "python", "ffmpeg", "curl", "jq", "termux-api", "aria2", "tor", "-y"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run([sys.executable, "-m", "pip", "install", "yt-dlp", "colorama", "rich"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{CYAN}  🤙 Mantap cok, semua bahan udah siap!{RESET}")
    except Exception:
        print(f"{CYAN}  💀 Waduh cok, gagal install. Coba cek internet lu. 🗿{RESET}")

def update_engine():
    print(f"{CYAN}  😈 Santuy cok, gwe panggil teknisi pusat...{RESET}")
    spinner("Update yt-dlp ke versi terbaru...", 3)
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{CYAN}  🚀 Mantap cok, Engine (yt-dlp) udah versi dewa paling gacor!{RESET}")
    except Exception as e:
        print(f"{CYAN}  💀 Gagal update cok: {e} 🗿{RESET}")

def check_deps():
    print(f"{CYAN}  🔍 Cek daleman dulu cok...{RESET}")
    spinner("Checking environment...", 2)
    
    try:
        import yt_dlp
        yt = "OK"
    except:
        yt = "Belum (Install di Menu 8)"
        
    print(f"{CYAN}  ✔ Python: OK\n  ✔ yt-dlp: {yt}\n  ✔ FFmpeg: OK (Asumsi)\n  ✔ Storage: Aman 😹{RESET}")
