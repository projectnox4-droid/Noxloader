import subprocess
import os

def get_clipboard_data():
    try:
        # Panggil termux-api buat ambil isi clipboard/keyboard
        result = subprocess.run(['termux-clipboard-get'], capture_output=True, text=True, timeout=4)
        return result.stdout.strip()
    except:
        return ""

def is_valid_cookie(text):
    # Cek simpel apakah teks ini format Netscape Cookie atau cookie mentah
    if "# Netscape HTTP Cookie File" in text:
        return True
    if ".com\t" in text and ("\tTRUE\t" in text or "\tFALSE\t" in text):
        return True
    if "sessionid=" in text or "c_user=" in text:
        return True
    return False

def save_cookie_from_clipboard():
    data = get_clipboard_data()
    if data and is_valid_cookie(data):
        with open("cookies.txt", "w", encoding="utf-8") as f:
            f.write(data)
        return True
    return False
