import os
import sys
import time
from ui.theme import CYAN, RESET
from utils.scanner import scan_url
from utils.cleaner import clean_cache
from config.settings import load_settings

class QuietLogger:
    def debug(self, msg): pass
    def warning(self, msg): pass
    def error(self, msg): pass

def hook(d):
    if d['status'] == 'downloading':
        p = d.get('_percent_str', '0%').strip()
        s = d.get('_speed_str', '0KiB/s').strip()
        sys.stdout.write(f"\r  {CYAN}🥵 Lagi gwe bungkus... {p} | Speed: {s}{RESET}")
        sys.stdout.flush()
    elif d['status'] == 'finished':
        sys.stdout.write(f"\n  {CYAN}😹 Beres cok! Lagi dirapihin...{RESET}\n")

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
        
        cfg = load_settings()

        try:
            import yt_dlp
            from history.manager import add_history
        except ImportError:
            print(f"  {CYAN}💀 Waduh cok, lu belum install bahan. Balik ke menu trus pilih 8 (Install Bahan) dulu.{RESET}")
            return

        print(f"\n  {CYAN}📦 SMART QUEUE: {total} link antre!{RESET}")

        for i, url in enumerate(urls, 1):
            if platform == 'Universal':
                info = scan_url(url)
                current_platform = info['platform']
            else:
                current_platform = platform

            print(f"\n  {CYAN}[{i}/{total}] Memproses: {current_platform} - {url[:40]}...{RESET}")

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
            try:
                with yt_dlp.YoutubeDL(opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    if info:
                        title = info.get('title', 'Unknown')
                        print(f"  {CYAN}✔ Judul: {title[:50]}{RESET}")
                    ydl.download([url])
                    
                print(f"  {CYAN}🤙 [{i}/{total}] File lu udah aman di folder {current_platform}!{RESET}")
                add_history(current_platform, title, "Sukses")
                berhasil += 1
            except KeyboardInterrupt:
                print(f"\n  {CYAN}💀 CTRL+C kepencet! Stop antrean dengan aman...{RESET}")
                clean_cache(silent=True)
                break
            except Exception as e:
                print(f"  {CYAN}💀 [{i}/{total}] Gagal cok. Skip link ini. (Error: {e}) 🗿{RESET}")
                add_history(current_platform, "Unknown/Error", "Gagal")
                gagal += 1

            clean_cache(silent=True)

        elapsed = int(time.time() - start_time)
        m, s = divmod(elapsed, 60)
        
        print(f"\n  {CYAN}😈 Batch selesai cok 🗿{RESET}")
        print(f"  {CYAN}📦 Total Link: {total}{RESET}")
        print(f"  {CYAN}✅ Berhasil: {berhasil}{RESET}")
        print(f"  {CYAN}❌ Gagal: {gagal}{RESET}")
        print(f"  {CYAN}⏱ Total Waktu: {m}m {s}s{RESET}\n")
