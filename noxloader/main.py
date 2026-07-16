import os
import sys

sys.dont_write_bytecode = True

try:
    from core.menu import main_menu
except Exception as e:
    import os
    os.system('clear || cls')
    print(f"\n\033[96m💀 Waduh cok, ada error nih: {e}\033[0m\n")
    import sys
    sys.exit(1)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        os.system('clear || cls')
        print("\n\033[96m\033[1m🥱 Cabut dulu cok. Santuy!\033[0m\n")
        sys.exit(0)
    except Exception as e:
        os.system('clear || cls')
        print(f"\n\033[96m💀 Waduh cok... aplikasi ngambek. (Error: {e}) 🗿\033[0m\n")
        sys.exit(1)
