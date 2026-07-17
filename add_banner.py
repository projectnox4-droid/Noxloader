import re

with open('noxloader/ui/banner.py', 'r') as f:
    content = f.read()

new_banner = """    elif menu == "NOXIMG":
        banner = f\"\"\"{c}{BOLD}
╔══════════════════════════════════════╗
║ ███╗   ██╗ ██████╗ ██╗  ██╗██╗███╗   ███╗║
║ ████╗  ██║██╔═══██╗╚██╗██╔╝██║████╗ ████║║
║ ██╔██╗ ██║██║   ██║ ╚███╔╝ ██║██╔████╔██║║
║ ██║╚██╗██║██║   ██║ ██╔██╗ ██║██║╚██╔╝██║║
║ ██║ ╚████║╚██████╔╝██╔╝ ██╗██║██║ ╚═╝ ██║║
║ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝║
╚══════════════════════════════════════╝
        {LIGHT_GRAY}Image/Photo Downloader{RESET}\"\"\"
    elif menu == "UNIVERSAL":"""

content = content.replace('    elif menu == "UNIVERSAL":', new_banner)

with open('noxloader/ui/banner.py', 'w') as f:
    f.write(content)
print("Added banner to banner.py")
