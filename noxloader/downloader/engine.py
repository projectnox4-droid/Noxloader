import os
import sys
import time
from ui.theme import current_color, RESET, rgb, LIGHT_GRAY, print_status, BOLD
from utils.scanner import scan_url
from utils.cleaner import clean_cache
from config.settings import load_settings

class QuietLogger:
    def debug(self, msg): pass
    def warning(self, msg): pass
    def error(self, msg): pass

# Global variable to store last progress line length to clear it cleanly
last_len = 0

def hook(d):
    global last_len
    c = current_color()
    
    if d['status'] == 'downloading':
        p = d.get('_percent_str', '0%').strip()
        
        # Parse percentage string
        try:
            percent_val = float(p.replace('%', '').replace('\x1b[0;94m', '').replace('\x1b[0m', '').strip())
        except:
            percent_val = 0.0
            
        s = d.get('_speed_str', '0KiB/s').strip()
        eta = d.get('_eta_str', 'Unknown').strip()
        downloaded = d.get('_downloaded_bytes_str', '0B').strip()
        total = d.get('_total_bytes_str', d.get('_total_bytes_estimate_str', '0B')).strip()
        
        # Build custom progress bar
        length = 20
        filled = int(length * percent_val // 100)
        bar = '█' * filled + '░' * (length - filled)
        
        # Formatting string
        msg = f"\r  {c}📦 {bar} {p} {LIGHT_GRAY}│ ⚡ {s} │ ⏳ {eta} │ 💾 {downloaded}/{total}{RESET}"
        
        # Pad with spaces to clear previous text
        pad = max(0, last_len - len(msg))
        sys.stdout.write(msg + " " * pad)
        sys.stdout.flush()
        last_len = len(msg)
        
    elif d['status'] == 'finished':
        sys.stdout.write("\r" + " " * last_len + "\r")
        last_len = 0
        sys.stdout.write(f"  {c}😹 Download beres, lagi dirapihin...{RESET}\n")

class UniversalDownloader:
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def download(self, urls, platform, format_type='best', res_fmt='best'):
        if isinstance(urls, str):
            urls = [urls]

        total = len(urls)
        berhasil = 0
        gagal = 0
        start_time = time.time()
        
        c = current_color()
        cfg = load_settings()

        try:
            import yt_dlp
            from history.manager import add_history
        except ImportError:
            print_status("ERROR", "Waduh cok, lu belum install bahan. Pilih Menu 16 dulu.")
            return

        print_status("INFO", f"SMART QUEUE: {total} link antre!")

        for i, url in enumerate(urls, 1):
            if platform == 'Universal':
                # Skip scan_url() here because we already did it in the menu
                current_platform = "Universal"
            else:
                current_platform = platform

            print(f"\n  {c}[{i}/{total}] Memproses: {current_platform} - {url[:40]}...{RESET}")
            
            out_dir = os.path.join(self.base_dir, current_platform)
            os.makedirs(out_dir, exist_ok=True)

            out_tmpl = os.path.join(out_dir, '%(title)s.%(ext)s')
            fmt = res_fmt
            is_audio = False
            
            if 'MP3' in format_type or 'Audio' in format_type:
                fmt = 'bestaudio/best'
                is_audio = True
                
            opts = {
                'outtmpl': out_tmpl,
                'logger': QuietLogger(),
                'progress_hooks': [hook],
                'quiet': True,
                'no_warnings': True,
                'nocheckcertificate': True,
                'format': fmt,
                'ignoreerrors': True,
                'retries': 10,
                'fragment_retries': 10,
                'continuedl': True,
                'postprocessors': []
            }
            
            if cfg.get("speed_limit", 0) > 0:
                opts['ratelimit'] = cfg["speed_limit"] * 1024

            if cfg.get("aria2_booster", False):
                opts['external_downloader'] = 'aria2c'
                opts['external_downloader_args'] = ['-c', '-j', '4', '-x', '4', '-s', '4', '-k', '1M']

            if cfg.get("ghost_mode", False):
                opts['proxy'] = 'socks5://127.0.0.1:9050'

            cookie_path = os.path.join(os.getcwd(), 'cookies.txt')
            if os.path.exists(cookie_path):
                opts['cookiefile'] = cookie_path

            if cfg.get("download_subtitle", False) and not is_audio:
                opts['writesubtitles'] = True
                opts['subtitleslangs'] = ['id', 'en', 'all']

            if cfg.get("download_thumbnail", False):
                opts['writethumbnail'] = True
                
            if is_audio:
                opts['postprocessors'].append({
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                })
                
            if cfg.get("auto_metadata", True):
                if cfg.get("download_thumbnail", False):
                    opts['postprocessors'].append({'key': 'EmbedThumbnail'})
                opts['postprocessors'].append({'key': 'FFmpegMetadata'})
                
            if 'Playlist' in format_type or 'Channel' in format_type or 'Profile' in format_type or 'Mass' in format_type:
                opts['extract_flat'] = False
            else:
                opts['noplaylist'] = True

            title = "Unknown"
            file_name = "Unknown"
            final_size = "Unknown"
            
            try:
                with yt_dlp.YoutubeDL(opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    if info:
                        title = info.get('title', 'Unknown')
                        # estimate size if available
                        s = info.get('filesize_approx', info.get('filesize', 0))
                        if s:
                            final_size = f"{round(s/1024/1024, 2)} MB"
                        
                        print(f"  {c}✔ Target: {title[:50]}{RESET}")
                        
                    ydl.download([url])
                    
                add_history(current_platform, title, "Sukses")
                berhasil += 1
                
                # Show premium summary card
                print(f"\n  {c}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{RESET}")
                print(f"  {c}┃ {BOLD}😈 DOWNLOAD BERES{' '*20}{c}┃{RESET}")
                print(f"  {c}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫{RESET}")
                print(f"  {c}┃ {LIGHT_GRAY}📦 File   : {title[:20].ljust(22)}{c} ┃{RESET}")
                print(f"  {c}┃ {LIGHT_GRAY}💾 Size   : {str(final_size).ljust(22)}{c} ┃{RESET}")
                print(f"  {c}┃ {LIGHT_GRAY}📂 Folder : {current_platform.ljust(22)}{c} ┃{RESET}")
                print(f"  {c}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{RESET}")
                
            except KeyboardInterrupt:
                print_status("WARNING", "CTRL+C kepencet! Stop antrean dengan aman...")
                clean_cache(silent=True)
                break
            except Exception as e:
                print_status("ERROR", f"[{i}/{total}] Gagal cok. Skip link ini.")
                add_history(current_platform, "Unknown/Error", "Gagal")
                gagal += 1
            
            clean_cache(silent=True)

        elapsed = int(time.time() - start_time)
        m, s = divmod(elapsed, 60)
        
        print()
        print_status("SUCCESS", "Batch eksekusi kelar cok 🗿")
        print(f"  {LIGHT_GRAY}📦 Total Link: {c}{total}{RESET}")
        print(f"  {LIGHT_GRAY}✅ Berhasil  : {c}{berhasil}{RESET}")
        print(f"  {LIGHT_GRAY}❌ Gagal     : {c}{gagal}{RESET}")
        print(f"  {LIGHT_GRAY}⏱ Total     : {c}{m}m {s}s{RESET}\n")

