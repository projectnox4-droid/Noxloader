import os
from ui.theme import current_color, RESET, clear, print_status, LIGHT_GRAY
from ui.animations import spinner
from ui.banner import show_banner

def recon_url():
    clear()
    show_banner()
    c = current_color()
    print_status("INFO", "INTEL RECON (Cek Metadata Tanpa Download)")
    try:
        url = input(f"{c}  🤪 Tempel linknya sini cok: {RESET}").strip()
    except EOFError:
        return
        
    if not url: return
    
    spinner("Gwe intip servernya dulu cok...", 2)
    
    try:
        import yt_dlp
    except ImportError:
        print_status("ERROR", "Waduh cok, lu belum install bahan.")
        input(f"\n{c}  [Enter] Balik ke menu...{RESET}")
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
                print_status("ERROR", "Gagal ngambil intel cok.")
                input(f"\n{c}  [Enter] Balik ke menu...{RESET}")
                return
                
            print(f"\n{c}  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{RESET}")
            print(f"{c}  ┃ 🕵️ DATA INTEL{' '*23}┃{RESET}")
            print(f"{c}  ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫{RESET}")
            print(f"{c}  ┃ {LIGHT_GRAY}📌 Judul      : {info.get('title', 'Unknown')[:20].ljust(20)}{c} ┃{RESET}")
            print(f"{c}  ┃ {LIGHT_GRAY}👤 Uploader   : {info.get('uploader', 'Unknown')[:20].ljust(20)}{c} ┃{RESET}")
            print(f"{c}  ┃ {LIGHT_GRAY}📺 Platform   : {info.get('extractor_key', 'Unknown')[:20].ljust(20)}{c} ┃{RESET}")
            print(f"{c}  ┃ {LIGHT_GRAY}⏱️ Durasi     : {str(info.get('duration_string', 'Unknown'))[:20].ljust(20)}{c} ┃{RESET}")
            print(f"{c}  ┃ {LIGHT_GRAY}👁️ Views      : {str(info.get('view_count', 'Unknown'))[:20].ljust(20)}{c} ┃{RESET}")
            print(f"{c}  ┃ {LIGHT_GRAY}👍 Likes      : {str(info.get('like_count', 'Unknown'))[:20].ljust(20)}{c} ┃{RESET}")
            desc = str(info.get('description', ''))[:17]
            if len(str(info.get('description', ''))) > 17: desc += "..."
            print(f"{c}  ┃ {LIGHT_GRAY}📝 Deskripsi  : {desc.ljust(20)}{c} ┃{RESET}")
            print(f"{c}  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{RESET}\n")
    except Exception as e:
        print_status("ERROR", "Gagal nembus cok. Linknya private atau error.")
        
    input(f"\n{c}  [Enter] Balik ke menu...{RESET}")
