#!/usr/bin/env python3

import os
import sys
import time
from urllib.parse import quote
import random
import requests
import qrcode
import json
import uuid

# ========= COLOR (RED ONLY) =========
RED = "\033[91m"
W   = "\033[0m"

def red(t): return RED + t + W

# ========= BASIC =========
def clear():
    os.system("clear")

# ========= WELCOME (ANIMATED TEXT ART) =========
def welcome():
    clear()

    # TEXT ART
    art = [
        "▀▄░▄▀ █▀▀█ █▀▀█ ─▀─ █▀▄▀█ █▀▀ █▀▀█",
        "─░█── █──█ █▄▄▀ ▀█▀ █─▀─█ █▀▀ █▄▄▀",
        "▄▀░▀▄ █▀▀▀ ▀─▀▀ ▀▀▀ ▀───▀ ▀▀▀ ▀─▀▀"
    ]
    for line in art:
        print(red(line))
        time.sleep(0.3)

    print()
    for c in "WELCOME TO TOOLS XPRIMER V2":
        sys.stdout.write(red(c))
        sys.stdout.flush()
        time.sleep(0.10)
    print("\n")
    time.sleep(0.10)

    # LOADING SETUP 10% -> 100%
    steps = [10,20,30,40,50,60,70,80,90,100]
    bar_len = 30
    for p in steps:
        filled = int(bar_len * p / 100)
        bar = "█" * filled + "░" * (bar_len - filled)
        sys.stdout.write("\r" + red(f"[{bar}] {p}%  Loading Setup"))
        sys.stdout.flush()
        time.sleep(0.2)
    print("\n")

    # SYSTEM MESSAGE
    for c in "WAIT, SYSTEM IS IN PROCESS OF SETTING UP":
        sys.stdout.write(red(c))
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")
    time.sleep(1)

    for c in "WAITING FOR 30 SECOND":
        sys.stdout.write(red(c))
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")

    # COUNTDOWN 60 SECONDS
    total = 30
    for s in range(total, 0, -1):
        done = total - s
        filled = int(bar_len * done / total)
        bar = "█" * filled + "░" * (bar_len - filled)
        sys.stdout.write(
            "\r" + red(f"[{bar}] {s:02d}s remaining")
        )
        sys.stdout.flush()
        time.sleep(1)
    print("\n")

# TRANSISI ELEGAN MASUK MENU
    slow_transition()

# SLOW TRANSITION
def slow_transition():
    text = "SYSTEM SETTING UP COMPLETED SUCCESSFULLY"
    bar_len = 30

    print()
    for c in text:
        sys.stdout.write(red(c))
        sys.stdout.flush()
        time.sleep(0.12)  # slow typing
    print("\n")

    # slow progress bar
    for i in range(101):
        fill = int(bar_len * i / 100)
        bar = "█" * fill + "░" * (bar_len - fill)
        sys.stdout.write("\r" + red(f"[{bar}] {i}%"))
        sys.stdout.flush()
        time.sleep(0.05)  # slowmo feel
    print("\n")

    # soft pause before clear
    time.sleep(0.8)
    clear()

# ========= BANNER =========
def banner():
    print(red("""
▀▄░▄▀ █▀▀█ █▀▀█ ─▀─ █▀▄▀█ █▀▀ █▀▀█
─░█── █──█ █▄▄▀ ▀█▀ █─▀─█ █▀▀ █▄▄▀
▄▀░▀▄ █▀▀▀ ▀─▀▀ ▀▀▀ ▀───▀ ▀▀▀ ▀─▀▀
"""))
    print(red(" 🝮︎ XPRIMER V2 🝮︎"))
    print(red(" Team : XPrimer Project"))
    print(red(" Version : 2.0\n"))

# ========= EFFECT =========
def spinner(text, dur=3):
    spin = ["|", "/", "-", "\\"]
    end = time.time() + dur
    i = 0
    while time.time() < end:
        sys.stdout.write("\r" + red(text + " " + spin[i % 4]))
        sys.stdout.flush()
        time.sleep(0.12)
        i += 1
    print()

def progress(duration=4):
    bar_len = 30
    for i in range(101):
        fill = int(bar_len * i / 100)
        bar = "█" * fill + "░" * (bar_len - fill)
        sys.stdout.write("\r" + red(f"[{bar}] {i}%"))
        sys.stdout.flush()
        time.sleep(duration / 100)
    print("\n")

def empty_exit():
    print(red("\n[!] Input kosong, keluar dari tools\n"))
    sys.exit()

# ========= MENU =========
def menu():
    clear()
    banner()
    print(red("===================================="))
    print(red("           MAIN MENU"))
    print(red("===================================="))
    print(red("[1] Banned Whatsapp"))
    print(red("[2] Tracking IP"))
    print(red("[3] Short Link"))
    print(red("[4] QR Generator"))
    print(red("[5] Send Malware To Phone"))
    print(red("[6] Kudeta Grub"))
    print(red("[7] Control Bot Telegram"))
    print(red("[8] OTP Spammer WhatsApp"))
    print(red("[0] Exit"))
    print(red("===================================="))

    choice = input(red("\nSelect Menu : ")).strip()
    if choice == "":
        empty_exit()

    if choice == "1":
        banned_whatsapp()
    elif choice == "2":
        tracking_ip()
    elif choice == "3":
        short_link()
    elif choice == "4":
        qr_generator()
    elif choice == "5":
        send_malware_simulation()
    elif choice == "6":
        kudeta_grub_simulation()
    elif choice == "7":
        control_bot_telegram_simulation()
    elif choice == "8":
        otp_spammer_simulation()
    elif choice == "0":
        clear()
        print(red("Bye Bye Terimakasih Telah Menggunakan Tools XPrimer👋"))
        sys.exit()
    else:
        print(red("Menu tidak valid!"))
        time.sleep(1)
        menu()

# ========= FEATURE 1 =========
def banned_whatsapp():
    clear()
    banner()
    target = input(red("Input Target Number (08xxxx): ")).strip()
    if target == "":
        empty_exit()

    spinner("Process To Banned Whatsapp", 4)
    progress(5)
    print(red("✔ Succesfully To Banned Whatsapp"))
    input(red("\nPress Enter To Back Menu..."))
    menu()

# ========= FEATURE 2 =========
FAKE_LOC = [
    ("New York", "USA", "40.7128", "-74.0060"),
    ("Tokyo", "Japan", "35.6895", "139.6917"),
    ("Berlin", "Germany", "52.5200", "13.4050"),
    ("Paris", "France", "48.8566", "2.3522"),
    ("Sydney", "Australia", "-33.8688", "151.2093"),
]

def tracking_ip():
    clear()
    banner()
    ip = input(red("Input IP Target : ")).strip()
    if ip == "":
        empty_exit()

    spinner("Process To Tracking IP", 4)
    progress(5)

    city, country, lat, lon = random.choice(FAKE_LOC)
    print(red("✔ Succesfully To Tracking IP\n"))
    print(red(f"IP Address : {ip}"))
    print(red(f"City       : {city}"))
    print(red(f"Country    : {country}"))
    print(red(f"Latitude   : {lat}"))
    print(red(f"Longitude  : {lon}"))
    print(red(f"Maps URL   : https://maps.google.com/?q={lat},{lon}"))

    input(red("\nPress Enter To Back Menu..."))
    menu()

# ========= SHORT LINK =================
def short_link():
    clear()
    banner()

    url = input(red("Input URL : ")).strip()
    if url == "":
        empty_exit()

    spinner("Connecting To Short Link Server", 2)
    progress(3)

    try:
        res = requests.get(
            "https://tinyurl.com/api-create.php",
            params={"url": url},
            timeout=10
        )

        if res.status_code == 200 and res.text.startswith("http"):
            print(red("\n✔ Short Link Successfully Generated"))
            print(red(f"Original : {url}"))
            print(red(f"Short    : {res.text}"))
        else:
            print(red("\n[!] Failed to generate short link"))

    except Exception as e:
        print(red(f"\n[!] Error : {e}"))

    input(red("\nPress Enter To Back Menu..."))
    menu()

# ========= QR GENERATOR ===============
def qr_generator():
    clear()
    banner()
    data = input(red("Input Text / URL : ")).strip()
    if not data:
        return

    folder = "/storage/emulated/0/Download/PutraXPrimer"
    os.makedirs(folder, exist_ok=True)

    path = f"{folder}/PutraX_QR_{int(time.time())}.png"
    qr_url = (
        f"https://api.qrserver.com/v1/create-qr-code/"
        f"?size=400x400&data={quote(data)}"
    )

    os.system(f'curl -s "{qr_url}" -o "{path}"')

    if os.path.exists(path):
        os.system(
            f'am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE '
            f'-d file://{path} >/dev/null 2>&1'
        )
        print(red("\nBERHASIL MEMBUAT QR ✔"))
        print(red(f"Saved : {path}"))
    else:
        print(red("Gagal membuat QR"))

    input(red("\nPress Enter..."))

# ========= FEATURE 6 : SEND MALWARE (SIMULATION) =========
def send_malware_simulation():
    clear()
    banner()

    target = input(red("Input Target Phone (08xxxx): ")).strip()
    if target == "":
        empty_exit()

    clear()
    banner()
    print(red("Select Malware Type:\n"))
    payloads = {
        "1": ("Trojan", [
            "Initializing Trojan Core...",
            "Injecting Persistence Layer...",
            "Hooking Injecting To Layer Phone Process..."
        ]),
        "2": ("Adware", [
            "Loading Adware Engine...",
            "Registering Ads Service...",
            "Syncing Injecting Layer To Phone Ads Module..."
        ]),
        "3": ("Spyware", [
            "Starting Spyware Listener...",
            "Collecting Metadata...",
            "Syncing Stealth Channel..."
        ]),
        "4": ("Ransomware", [
            "Deploying Crypto Module...",
            "Encrypting Inject File System...",
            "Locking Inject Layer Phone..."
        ]),
        "5": ("Botnet", [
            "Connecting To C2...",
            "Registering Bot Identity...",
            "Syncing Botnet Layer Phone..."
        ]),
    }

    for k, v in payloads.items():
        print(red(f"[{k}] {v[0]}"))

    pick = input(red("\nSelect Malware : ")).strip()
    if pick not in payloads:
        print(red("Invalid payload!"))
        time.sleep(1)
        menu()

    payload_name, messages = payloads[pick]

    dur = input(red("Input Duration : ")).strip()
    if not dur.isdigit() or int(dur) <= 0:
        print(red("Invalid duration!"))
        time.sleep(1)
        menu()

    duration = int(dur)

    spinner("Process Send Malware To Phone", 3)
    progress(3)

    clear()
    banner()
    print(red(f"Target  : {target}"))
    print(red(f"Payload : {payload_name}"))
    print(red("\nStarting Send Malware To Phone...\n"))

    start = time.time()
    i = 0
    while time.time() - start < duration:
        msg = messages[i % len(messages)]
        sys.stdout.write(red(f"\r>> {msg}"))
        sys.stdout.flush()
        time.sleep(1)
        i += 1

    print("\n")
    print(red("✔ Send Malware To Phone Successfully"))
    print(red("(Mohon Jangan Disalah Gunakan !!)\n"))
    input(red("Press Enter To Back Menu..."))
    menu()

# ========= FEATURE 7 : KUDETA GRUB (SIMULATION) =========
def kudeta_grub_simulation():
    clear()
    banner()

    link = input(red("Input Link Grub Target : ")).strip()
    if link == "":
        empty_exit()

    clear()
    banner()
    print(red("Initializing Kudeta Grub Process...\n"))

    # Progress 1 - 100
    bar_len = 30
    for i in range(1, 101):
        fill = int(bar_len * i / 100)
        bar = "█" * fill + "░" * (bar_len - fill)
        sys.stdout.write(
            "\r" + red(f"[{bar}] {i}%  Process Kudeta Grub")
        )
        sys.stdout.flush()
        time.sleep(0.05)  # smooth & elegan
    print("\n")

    # Detail proses (visual only)
    steps = [
        "Scanning Group Metadata...",
        "Syncing Admin...",
        "Currently in the Process of Becoming a Group Admin...", 
        "The Process of Seizing Grub ...",
        "Finalizing Seizing the Kudeta Grub ..."
    ]

    for s in steps:
        sys.stdout.write(red(f">> {s}\n"))
        sys.stdout.flush()
        time.sleep(0.8)

    print("\n" + red("✔ Succesfully Kudeta Grub"))
    print(red(f"✔ To Link : {link}"))
    print(red("(Mohon Jangan Disalah Gunakan !!)\n"))

    input(red("Press Enter To Back Menu..."))
    menu()

# ========= FEATURE 8 : CONTROL BOT TELEGRAM (SIMULATION) =========
def control_bot_telegram_simulation():
    clear()
    banner()

    token = input(red("Input Token Bot Telegram : ")).strip()
    if token == "":
        empty_exit()

    clear()
    banner()
    print(red("Waiting Process Control Bot Telegram...\n"))

    # Progress 1-100 (Process Control)
    bar_len = 30
    for i in range(1, 101):
        fill = int(bar_len * i / 100)
        bar = "█" * fill + "░" * (bar_len - fill)
        sys.stdout.write(
            "\r" + red(f"[{bar}] {i}%  Controlling Bot Telegram")
        )
        sys.stdout.flush()
        time.sleep(0.04)
    print("\n")

    telegram_id = input(red("Input Id Telegram Anda : ")).strip()
    if telegram_id == "":
        empty_exit()

    clear()
    banner()
    print(red("Process To Connecting Control Bot Telegram To Id Telegram Anda...\n"))

    # Progress 1-100 (Connecting)
    for i in range(1, 101):
        fill = int(bar_len * i / 100)
        bar = "█" * fill + "░" * (bar_len - fill)
        sys.stdout.write(
            "\r" + red(f"[{bar}] {i}%  Connecting To Telegram ID")
        )
        sys.stdout.flush()
        time.sleep(0.04)
    print("\n")

    # Visual logs
    logs = [
        "Initializing Bot Controller...",
        "Procces Connecting Token Dengan Id Telegram Anda...",
        "Binding Control Session...",
        "Syncing Permission..."
    ]

    for log in logs:
        print(red(f">> {log}"))
        time.sleep(0.6)

    print("\n" + red("✔ Succesfully Control Bot Telegram"))
    print(red(f"✔ Token : {token}"))
    print(red("(Mohon Jangan Disalah Gunakan !!)\n"))

    input(red("Press Enter To Back Menu..."))
    menu()

# ========= OTP SPAMMER =============
def otp_spammer_simulation():
    clear()
    banner()

    target = input(red("Input Nomor Target (08xxxx): ")).strip()
    if target == "":
        empty_exit()

    total = input(red("Input Jumlah Otp Spammer : ")).strip()
    if not total.isdigit() or int(total) <= 0:
        print(red("Jumlah tidak valid!"))
        time.sleep(1)
        menu()

    total = int(total)

    clear()
    banner()

    # WAIT 5 SECOND TRYING TO CONNECT
    for c in "WAIT 5 SECOND TRYING TO CONNECT TO OTP SPAMMER SYSTEM":
        sys.stdout.write(red(c))
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")

    for i in range(5, 0, -1):
        sys.stdout.write(red(f"\rConnecting... {i}s"))
        sys.stdout.flush()
        time.sleep(1)
    print("\n")

    # CONNECTED
    for c in "SUCCESSFULLY CONNECTED TO THE OTP SPAMMER SYSTEM":
        sys.stdout.write(red(c))
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n\n")

    # PERCENT 1% - 100%
    bar_len = 30
    for i in range(1, 101):
        fill = int(bar_len * i / 100)
        bar = "█" * fill + "░" * (bar_len - fill)
        sys.stdout.write(
            "\r" + red(f"[{bar}] {i}%")
        )
        sys.stdout.flush()
        time.sleep(0.04)
    print("\n")

    # SYSTEM MESSAGE
    for c in "THE SYSTEM IS TRYING TO SEND AN OTP CODE":
        sys.stdout.write(red(c))
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n\n")

    print(red(f"PROSES SEND OTP SPAMMER WHATSAPP TO NOMOR : {target}\n"))

    # SEND OTP (SIMULATION)
    for i in range(1, total + 1):
        sys.stdout.write(
            red(f">> Sending OTP {i}/{total} To {target}\n")
        )
        sys.stdout.flush()
        time.sleep(5)  # jeda 5 detik

    print("\n" + red(f"✔ Successfully Otp Spammer WhatsApp To          Target : {target}\n"))
    input(red("Press Enter To Back Menu..."))
    menu()