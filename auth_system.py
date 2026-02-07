import os
import json
import uuid
import time

# ========= GLOBAL CONFIG =========
TOKEN_FILE = os.path.expanduser("~/.xprimer_tokens.json")
ADMIN_TOKEN = "XPR-ADMIN"

RED = "\033[91m"
W   = "\033[0m"
def red(t): return RED + t + W

def clear():
    os.system("clear" if os.name != "nt" else "cls")

def load_tokens():
    if not os.path.exists(TOKEN_FILE):
        return []
    with open(TOKEN_FILE, "r") as f:
        return json.load(f)

def save_tokens(tokens):
    with open(TOKEN_FILE, "w") as f:
        json.dump(tokens, f, indent=2)

def generate_token():
    return "XPR-" + uuid.uuid4().hex[:4].upper() + "-" + uuid.uuid4().hex[:4].upper()

def banner():
    print(red("""
▀▄░▄▀ █▀▀█ █▀▀█ ─▀─ █▀▄▀█ █▀▀ █▀▀█
─░█── █──█ █▄▄▀ ▀█▀ █─▀─█ █▀▀ █▄▄▀
▄▀░▀▄ █▀▀▀ ▀─▀▀ ▀▀▀ ▀───▀ ▀▀▀ ▀─▀▀
"""))
    print(red(" 🝮︎ XPRIMER V2 🝮︎"))
    print(red(" Authentication\n"))

def login_menu(on_success):
    while True:
        clear()
        banner()
        print(red("=========== LOGIN AUTHENTICATION ==========="))
        print(red("[1] Login Token"))
        print(red("[2] Add Token (Admin Only)"))
        print(red("[0] Exit"))
        print(red("========================================"))
        c = input(red("Select : ")).strip()

        if c == "1":
            token = input(red("TOKEN ANDA : ")).strip()
            if token in load_tokens():
                print(red("\n✔ LOGIN BERHASIL"))
                time.sleep(1)
                on_success(token)
                return
            else:
                print(red("\n✖ TOKEN TIDAK TERDAFTAR"))
                time.sleep(1.5)

        elif c == "2":
            admin = input(red("Input Token Admin : ")).strip()
            if admin != ADMIN_TOKEN:
                print(red("\n✖ TOKEN ADMIN SALAH"))
                time.sleep(1.5)
                continue

            tokens = load_tokens()
            new_token = generate_token()
            tokens.append(new_token)
            save_tokens(tokens)
            print(red("\n✔ TOKEN BERHASIL DITAMBAHKAN"))
            print(red(f"TOKEN USER : {new_token}"))
            input(red("\nPress Enter..."))

        elif c == "0":
            clear()
            print(red("Bye Bye Pengguna XPRIMER V2 👋"))
            raise SystemExit
        else:
            print(red("Pilihan tidak valid!"))
            time.sleep(1)