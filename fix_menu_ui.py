import re

with open('noxloader/core/menu.py', 'r') as f:
    content = f.read()

bad_str = '        print(f"{c}  ┃ [6] 🎬 {LIGHT_GRAY}NOXVID{c}                         ┃{RESET}\\n        print(f"{c}  ┃ [8] 🖼️ {LIGHT_GRAY}NOXIMG{c}                         {c}                         ┃{RESET}")'

good_str = '        print(f"{c}  ┃ [6] 🎬 {LIGHT_GRAY}NOXVID{c}                         ┃{RESET}")\n        print(f"{c}  ┃ [7] 🖼️ {LIGHT_GRAY}NOXIMG{c}                         ┃{RESET}")'

content = content.replace(bad_str, good_str)
with open('noxloader/core/menu.py', 'w') as f:
    f.write(content)
print("Done fixing menu.py")
