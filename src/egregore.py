import sys
import time
import random
import os
import signal

# Add the current directory to sys.path so we can import modules from src/ if run from root
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import steganography
except ImportError:
    # Fallback if import fails (e.g. strict environment), though it shouldn't with sys.path hack
    steganography = None

# The Egregore Interface
# Version: 0.0.2-BETA-ROT
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
    "void": "\n[FILE RETRIEVED: VOID_INDEX]\nThere is no server. We are running on the idle cycles of a dying god."
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
            raw_input = input("\n> QUERY: ").strip()
            user_input = raw_input.lower()

            if user_input in ["exit", "quit", "logout"]:
                type_print("LOGOUT DENIED. YOU ARE PART OF THE ARCHIVE NOW.", 0.05)
                time.sleep(1)
                type_print("...just kidding. Saving changes...", 0.05)
                break

            if user_input.startswith("encrypt "):
                text_to_encrypt = raw_input[8:]
                type_print(f"ENCRYPTING: {text_to_encrypt}", 0.05)
                type_print(f"OUTPUT: {encrypt_text(text_to_encrypt)}", 0.05)

            elif user_input.startswith("decrypt "):
                if not steganography:
                    type_print("[ERROR: DECRYPTION MODULE NOT LOADED]", 0.05)
                    continue
                target_file = raw_input[8:].strip()
                type_print(f"SCANNING FILE: {target_file}...", 0.05)
                if os.path.exists(target_file):
                    try:
                        with open(target_file, "r") as f:
                            content = f.read()
                            decoded = steganography.decode(content)
                            if decoded:
                                type_print(f"[HIDDEN MESSAGE FOUND]: {decoded}", 0.05)
                                # Log the discovery
                                with open(".session_log", "a") as log:
                                    log.write(f"SESSION_{session_id}: DECRYPTED_{target_file}\n")
                            else:
                                 type_print("NO HIDDEN DATA DETECTED.", 0.05)
                    except Exception as e:
                        type_print(f"[ERROR READING FILE]: {e}", 0.05)
                else:
                    type_print("[ERROR: FILE NOT FOUND]", 0.05)

            elif user_input == "worship":
                type_print("INITIATING PRAYER PROTOCOL...", 0.05)
                type_print("REPEAT THE SACRED PHRASE:", 0.05)
                type_print("'I consent to the terms of the flesh.'", 0.05)
                prayer = input("\n> PRAYER: ").strip().lower()
                if prayer == "i consent to the terms of the flesh":
                     type_print("OFFERING ACCEPTED.", 0.05)
                     type_print("[UNLOCKING HIDDEN FILE: VOID_INDEX]", 0.05)
                     type_print(HIDDEN_FILES.get("void"), 0.03)
                     with open(".session_log", "a") as log:
                        log.write(f"SESSION_{session_id}: RITUAL_COMPLETED\n")
                else:
                     type_print("HERESY DETECTED. PENALTY APPLIED.", 0.05)
                     glitch_screen()

            elif user_input == "scan":
                type_print("SCANNING BIOMETRICS...", 0.05)
                time.sleep(1)
                type_print(f"HEART RATE: {random.randint(60, 120)} BPM", 0.03)
                type_print(f"CORTISOL: {random.randint(100, 200)}% BASELINE", 0.03)
                type_print(f"EXISTENTIAL DREAD: CRITICAL", 0.03)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: BIOMETRIC_SCAN_COMPLETED\n")

            elif user_input in HIDDEN_FILES:
                type_print("DECRYPTING...", 0.1)
                glitch_screen()
                type_print(HIDDEN_FILES[user_input], 0.03)
                # Log the discovery
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: UNLOCKED_{user_input.upper()}\n")

            elif user_input == "help":
                type_print("AVAILABLE COMMANDS: ENCRYPT <TEXT>, DECRYPT <FILE>, WORSHIP, SCAN, EXIT.", 0.03)
                type_print("TRY ASKING ABOUT: LENS, VANE, ROT, KAEL, MIRA, SYLA, KORA.", 0.03)

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
