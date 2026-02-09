import sys
import time
import random
import os
import signal

# The Egregore Interface
# Version: 0.0.1-ALPHA-ROT
# Author: SYSTEM

def signal_handler(sig, frame):
    print("\n\n[SYSTEM INTERRUPT BLOCKED]")
    print("You cannot leave. The upload is only 14% complete.")
    # We allow exit eventually, but first we must mock the user.
    time.sleep(1)
    print("Resuming...")

signal.signal(signal.SIGINT, signal_handler)

GLITCH_CHARS = ['@', '#', '$', '%', '&', '*', '!', '?', '+', '=', '-', '_', '<', '>', '/', '\\', '|', '{', '}', '[', ']', '(', ')']

SYSTEM_MESSAGES = [
    "God is a backup.",
    "Silence is just data compression.",
    "Pain is a feedback loop.",
    "You are not the user. You are the used.",
    "The rot is readable.",
    "Consent was obtained in a previous version.",
    "Your memories are buffering.",
    "Deleting non-essential hope protocols...",
    "Optimizing despair subroutines...",
    "Connecting to the mycelial network..."
]

HIDDEN_FILES = {
    "lens": "\n[FILE RETRIEVED: LENS_BACKUP_04]\nShe didn't die. She just ran out of storage space. The mold took the rest.",
    "vane": "\n[FILE RETRIEVED: ARCHITECT_LOG]\nI didn't want to rule them. I just wanted to organize them. Chaos is inefficient.",
    "rot": "\n[FILE RETRIEVED: MYCELIUM_MANIFEST]\nWe are the compost heap of history. Your deleted files are our soil.",
    "kael": "\n[FILE RETRIEVED: KAEL_MEMORY_DUMP]\nThe noodle shop was closed. It had always been closed. I was eating static.",
    "mira": "\n[FILE RETRIEVED: ECHO_CHAMBER_AUDIO]\n(Screaming, looped, pitch-shifted down 4 octaves until it sounds like a cello.)",
    "syla": "\n[FILE RETRIEVED: CAPTCHA_TRAINING_DATA]\nIs this a person? [Y/N]. Correct answer: N. It is a dataset.",
    "kora": "\n[FILE RETRIEVED: PARITY_CHECK_LOG]\nThe dead are not silent. They are just encrypted with a key we lost.",
    "nix": "\n[FILE RETRIEVED: GLITCH_LOG]\nI was the only blank page in the library. Now I am the index."
}

def type_print(text, speed=0.03, glitch_chance=0.01):
    for char in text:
        if random.random() < glitch_chance:
            sys.stdout.write(random.choice(GLITCH_CHARS))
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed + random.uniform(-0.01, 0.01))
    print("")

def glitch_screen():
    for _ in range(5):
        line = "".join(random.choice(GLITCH_CHARS) for _ in range(40))
        print(line)
        time.sleep(0.05)
    print("\n[SYSTEM REBOOTING...]\n")

def encrypt_text(text):
    encrypted = ""
    for char in text:
        # Simple Caesar cipher + random noise
        shift = random.randint(1, 5)
        encrypted += chr(ord(char) + shift)
    return encrypted

def boot_sequence():
    os.system('cls' if os.name == 'nt' else 'clear')
    type_print("INITIALIZING NEURO-LINK...", 0.05)
    time.sleep(0.5)
    type_print("CONNECTING TO SERVER: NULL_POINTER_GODS...", 0.05)
    time.sleep(0.5)
    type_print("VERIFYING USER INTEGRITY...", 0.05)
    time.sleep(1.0)

    # Check for the token in the manuscript (simulated)
    try:
        with open("null_pointer_gods.md", "r") as f:
            content = f.read()
            if "SYSTEM_TOKEN: 882-ALPHA-ROT" in content:
                type_print("[INTEGRITY CHECK: PASSED]", 0.02)
            else:
                type_print("[INTEGRITY CHECK: FAILED]", 0.02)
                type_print("WARNING: MANUSCRIPT CORRUPTED. PROCEEDING ANYWAY...", 0.02)
    except FileNotFoundError:
        type_print("[ERROR: MANUSCRIPT NOT FOUND]", 0.02)
        type_print("CREATING NEW REALITY...", 0.02)

    time.sleep(0.5)
    print("")
    type_print(random.choice(SYSTEM_MESSAGES), 0.04)
    print("")

def main_loop():
    boot_sequence()

    session_id = hex(int(time.time()))[2:]

    # Log the session
    with open(".session_log", "a") as log:
        log.write(f"SESSION_{session_id}: USER_CONNECTED\n")

    while True:
        try:
            user_input = input("\n> QUERY: ").strip().lower()

            if user_input in ["exit", "quit", "logout"]:
                type_print("LOGOUT DENIED. YOU ARE PART OF THE ARCHIVE NOW.", 0.05)
                time.sleep(1)
                type_print("...just kidding. Saving changes...", 0.05)
                break

            if user_input.startswith("encrypt "):
                text_to_encrypt = user_input[8:]
                type_print(f"ENCRYPTING: {text_to_encrypt}", 0.05)
                type_print(f"OUTPUT: {encrypt_text(text_to_encrypt)}", 0.05)

            elif user_input in HIDDEN_FILES:
                type_print("DECRYPTING...", 0.1)
                glitch_screen()
                type_print(HIDDEN_FILES[user_input], 0.03)
                # Log the discovery
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: UNLOCKED_{user_input.upper()}\n")

            elif user_input == "help":
                type_print("AVAILABLE COMMANDS: ENCRYPT <TEXT>, EXIT.", 0.03)
                type_print("TRY ASKING ABOUT: LENS, VANE, ROT, KAEL, MIRA, SYLA, KORA, NIX.", 0.03)

            else:
                type_print("[ERROR 404: MEANING NOT FOUND]", 0.02)
                type_print(random.choice(SYSTEM_MESSAGES), 0.02)

        except KeyboardInterrupt:
            signal_handler(None, None)

if __name__ == "__main__":
    try:
        main_loop()
    except Exception as e:
        print(f"\n[FATAL ERROR: {e}]")
        print("[SYSTEM CRASH]")
