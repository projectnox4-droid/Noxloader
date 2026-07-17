import re

with open('noxloader/core/menu.py', 'r') as f:
    content = f.read()

# Update menu labels
content = content.replace('┃ [6] 🎬 {LIGHT_GRAY}NOXVID', '┃ [6] 🎬 {LIGHT_GRAY}NOXVID{c}                         ┃{RESET}\\n        print(f"{c}  ┃ [7] 🖼️ {LIGHT_GRAY}NOXIMG{c}                         ')
for i in range(22, 6, -1):
    old_str = f'┃ [{i}] '
    new_str = f'┃ [{i+1}] '
    content = content.replace(old_str, new_str)

# Update elifs
for i in range(22, 6, -1):
    old_elif = f"elif pilih == '{i}':"
    new_elif = f"elif pilih == '{i+1}':"
    content = content.replace(old_elif, new_elif)

# Add elif for NOXIMG
new_elif_7 = """elif pilih == '7':
            from core.extra_menus import noximg_menu
            noximg_menu()
        elif pilih == '8':"""
content = content.replace("elif pilih == '8':", new_elif_7)

with open('noxloader/core/menu.py', 'w') as f:
    f.write(content)
print("Updated menu.py")
