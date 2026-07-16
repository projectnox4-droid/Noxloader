import os
from ui.theme import current_color, RESET, LIGHT_GRAY

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
