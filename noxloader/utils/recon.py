import os
from ui.theme import CYAN, RESET, clear
from ui.animations import spinner
from ui.banner import show_banner

def recon_url():
    clear()
    show_banner()
    print(f"{CYAN}  🕵️ INTEL RECON (Cek Metadata Tanpa Download){RESET}\n")
    try:
        url = input(f"{CYAN}  🤪 Tempel linknya sini cok: {RESET}").strip()
    except EOFError:
        return
        
    if not url: return
    
    spinner("Gwe intip servernya dulu cok...", 2)
    
    try:
        import yt_dlp
    except ImportError:
        print(f"  {CYAN}💀 Waduh cok, lu belum install bahan.{RESET}")
        return
        
    opts = {
        'quiet': True,
        'no_warnings': True,
        'nocheckcertificate': True,
        'extract_flat': False
    }
    
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(url, download=False)
            if not info:
                print(f"  {CYAN}💀 Gagal ngambil intel cok.{RESET}")
                return
                
            print(f"\n{CYAN}  === [ 🕵️ DATA INTEL ] ==={RESET}")
            print(f"{CYAN}  📌 Judul      : {info.get('title', 'Unknown')}{RESET}")
            print(f"{CYAN}  👤 Uploader   : {info.get('uploader', 'Unknown')}{RESET}")
            print(f"{CYAN}  📺 Platform   : {info.get('extractor_key', 'Unknown')}{RESET}")
            print(f"{CYAN}  ⏱️ Durasi     : {info.get('duration_string', 'Unknown')}{RESET}")
            print(f"{CYAN}  👁️ Views      : {info.get('view_count', 'Unknown')}{RESET}")
            print(f"{CYAN}  👍 Likes      : {info.get('like_count', 'Unknown')}{RESET}")
            desc = str(info.get('description', ''))[:100]
            if len(str(info.get('description', ''))) > 100: desc += "..."
            print(f"{CYAN}  📝 Deskripsi  : {desc}{RESET}")
            print(f"{CYAN}  ========================={RESET}\n")
    except Exception as e:
        print(f"  {CYAN}💀 Gagal nembus cok. Linknya private atau error.{RESET}")
        
    input(f"\n{CYAN}  [Enter] Balik ke menu...{RESET}")
