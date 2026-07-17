with open('noxloader/core/extra_menus.py', 'r') as f:
    content = f.read()

new_func = """

def noximg_menu():
    base_dir = init_dirs()
    clear()
    ThemeManager.current_menu = "NOXIMG"
    show_banner()
    c = current_color()
    print_status("INFO", "NOXIMG (Download Foto / Image)")
    print(f"{LIGHT_GRAY}  Link IG Post, Pinterest, Reddit, Twitter, dll bakal disedot gambarnya aja!{RESET}")
    urls = get_urls_input()
    if urls:
        spinner("Menganalisis link foto...", 2)
        dl = UniversalDownloader(base_dir)
        # yt-dlp might need specific formats or just bestvideo/best, but for images it's tricky.
        # usually gallery-dl is better, but since it's using UniversalDownloader (yt-dlp), 
        # let's try to extract images or just call it with default.
        dl.download(urls, "Images", format_type='best')
        print_footer()
        input(f"\\n{c}  [Enter] Balik ke menu...{RESET}")
"""
with open('noxloader/core/extra_menus.py', 'a') as f:
    f.write(new_func)
print("Updated extra_menus.py")
