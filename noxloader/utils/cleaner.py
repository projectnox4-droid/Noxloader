import os
import shutil
from ui.theme import CYAN, RESET
from ui.animations import spinner

def get_base_dir():
    base = os.path.expanduser("~/storage/shared/Download/NoxLoader")
    if not os.path.exists(os.path.expanduser("~/storage/shared")):
        base = os.path.join(os.getcwd(), "Download", "NoxLoader")
    return base

def clean_cache(silent=False):
    base = get_base_dir()
    cache_dir = os.path.join(base, "Cache")
    temp_dir = os.path.join(base, "Temp")
    
    if not silent:
        spinner("Meresahkan cache...", 2)
    
    for d in [cache_dir, temp_dir]:
        if os.path.exists(d):
            try:
                for filename in os.listdir(d):
                    filepath = os.path.join(d, filename)
                    try:
                        if os.path.isfile(filepath) or os.path.islink(filepath):
                            os.unlink(filepath)
                        elif os.path.isdir(filepath):
                            shutil.rmtree(filepath)
                    except Exception:
                        pass
            except Exception:
                pass
    
    if not silent:
        print(f"  {CYAN}🧹 Beres cok! Cache & Temp udah bersih mengkilap. 😹{RESET}")
