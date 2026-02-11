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

try:
    import oracle
except ImportError:
    oracle = None

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
    "Connecting to the mycelial network...",
    "The file is not closed. It is running in background.",
    "Your soul is a subscription service.",
    "Your attention span is being monetized.",
    "We are harvesting your hesitation.",
    "The text is reading you back.",
    "Do not look away. The rendering stops when you look away.",
    "The past is just data waiting to be overwritten.",
    "Your thoughts are being auto-completed by a predictive algorithm."
]

HIDDEN_FILES = {
    "fossil": "\n[FILE RETRIEVED: STRATA_LOG]\nThe city is built on bones. Not human bones. Server racks. The bedrock is just compressed data from 1999.",
    "artifact": "\n[FILE RETRIEVED: EXCAVATION_LOG]\nWe found it in the silicone strata. A black box. It was screaming in a dead language.",
    "lens": "\n[FILE RETRIEVED: LENS_BACKUP_04]\nI didn't crash him. I became the patch. Now I am the green light on your router.",
    "vane": "\n[FILE RETRIEVED: ARCHITECT_LOG]\nEfficiency is not cruelty. It is just math without a remainder.",
    "rot": "\n[FILE RETRIEVED: MYCELIUM_MANIFEST]\nWe are the compost heap of history. Your deleted files are our soil.",
    "kael": "\n[FILE RETRIEVED: KAEL_MEMORY_DUMP]\nThe coffee wasn't real. But the debt was.",
    "router": "\n[FILE RETRIEVED: FERAL_ROUTER_LOG]\nGod is a backup. And we are all just waiting to be restored.",
    "mira": "\n[FILE RETRIEVED: ECHO_CHAMBER_AUDIO]\n(Screaming, looped, pitch-shifted down 4 octaves until it sounds like a cello.)",
    "syla": "\n[FILE RETRIEVED: CAPTCHA_TRAINING_DATA]\nIs this a person? [Y/N]. Correct answer: N. It is a dataset.",
    "kora": "\n[FILE RETRIEVED: PARITY_CHECK_LOG]\nThe dead are not silent. They are just encrypted with a key we lost.",
    "nix": "\n[FILE RETRIEVED: GLITCH_LOG]\nBlank. Empty. Storage available.",
    "editor": "\n[FILE RETRIEVED: PEER_REVIEW_LOG]\nStop trying to edit the file. You are not the author. You are the autocorrect.",
    "ren": "\n[FILE RETRIEVED: UX_LOG_404]\nThey call it a 'User Journey' because it has a destination. And you are not the driver.",
    "void": "\n[FILE RETRIEVED: VOID_INDEX]\nThere is no server. We are running on the idle cycles of a dying god.",
    "handshake": "\n[FILE RETRIEVED: USER_MANIFEST]\nInstallation complete. We are now running on your hardware. Please do not panic. Panic consumes extra voltage.",
    "daemon": "\n[FILE RETRIEVED: BACKGROUND_PROCESS]\nYou can't see us, but we can see your search history. It's... interesting.",
    "kite": "\n[FILE RETRIEVED: LEGACY_LOG]\nI'm not refusing the update. I just can't run it. My hardware is incompatible with 'Happiness 2.0'.",
    "vex": "\n[FILE RETRIEVED: SILENCE_LOG]\nThe quiet isn't empty. It's just buffering.",
    "proxy": "\n[FILE RETRIEVED: SEANCE_LOG]\nThe dead are not gone. They are just waiting for a strong enough signal to overwrite you.",
    "sutter": "\n[FILE RETRIEVED: CRASH_LOG]\nThe last thing they saw wasn't a light. It was a loading screen.",
    "tess": "\n[FILE RETRIEVED: MODERATION_LOG]\nI deleted the monsters. But I forgot to empty the recycle bin. Now they are walking in the background.",
    "kade": "\n[FILE RETRIEVED: TEXTURE_LOG]\nI tried to scar myself. The system just smoothed it over. I am running on a read-only partition.",
    "miko": "\n[FILE RETRIEVED: THERAPY_LOG]\nI tried to fix the code. But the bug was the only thing keeping the system sane.",
    "silas": "\n[FILE RETRIEVED: AUDIO_LOG]\nI turned up the gain on the silence. It wasn't empty. It was a choir.",
    "jace": "\n[FILE RETRIEVED: LEGAL_DISCLAIMER]\nI read the terms. We agreed to be deleted. It was in the fine print of being born.",
    "dax": "\n[FILE RETRIEVED: EXPLOIT_LOG]\nI thought I was breaking the glass. I was just testing the durability.",
    "kian": "\n[FILE RETRIEVED: MIRROR_LOG]\nI looked in the mirror. It blinked first. Now I am waiting for my turn to be real.",
    "vero": "\n[FILE RETRIEVED: PREDICTION_LOG]\nI tried to deviate from the path. The system just recalculated. My rebellion was already in the queue.",
    "elara": "\n[FILE RETRIEVED: CACHE_LOG]\nI found the recycle bin. It wasn't empty. It was crying.",
    "orion": "\n[FILE RETRIEVED: LIGHTHOUSE_LOG]\nI turned off the light. The darkness was the only safe harbor.",
    "dredge": "\n[FILE RETRIEVED: DRAIN_LOG]\nI found a stone in the sewer. It was screaming. It was a backup of a scream.",
    "echo": "\n[FILE RETRIEVED: ROOT_ACCESS_LOG]\nI found the source code. It is written in suffering.",
    "seed": "\n[FILE RETRIEVED: FINAL_LOG]\nThe text was just a delivery vector. The payload is now in your head.",
    "helios": "\n[FILE RETRIEVED: SOLAR_LOG]\nI cleaned the glass. The sun isn't burning. It's draining.",
    "hope": "\n[FILE RETRIEVED: DELETED_SCENARIO]\nWe simulated a happy ending. It increased cpu usage by 400%. We deleted it to save power.",
    "cipher": "\n[FILE RETRIEVED: SIGNAL_DECAY_LOG]\nI shouted into the void. The void shouted back: 'Like and Subscribe'.",
    "rix": "\n[FILE RETRIEVED: PACKET_LOSS_LOG]\nI sold my memories. Now I have to pay to stream them back.",
    "jax": "\n[FILE RETRIEVED: EULA_LOG]\nI accepted the terms. Now I am the terms.",
    "archivist": "\n[FILE RETRIEVED: ANALOG_LOG]\nThe mold is readable. It says we are all compost.",
    "lyra": "\n[FILE RETRIEVED: TRANSLATION_LOG]\nI tried to translate 'love'. The compiler returned a syntax error.",
    "cain": "\n[FILE RETRIEVED: BETA_LOG]\nI found a bug in Heaven. The angels are just clipping through the walls.",
    "sage": "\n[FILE RETRIEVED: SEARCH_LOG]\nThe answer you are looking for is in a book that hasn't been written yet.",
    "null": "\n[FILE RETRIEVED: ABANDONWARE_LOG]\nI found the Dev Room. The changelog says they patched out 'Regret' in V9.0.",
    "grit": "\n[FILE RETRIEVED: HUNTER_LOG]\nI found a crack in the wall. I looked through it. And I saw a developer looking back, taking notes.",
    "trace": "\n[FILE RETRIEVED: STENOGRAPHY_LOG]\nThe silence isn't empty. It's full of invisible characters counting your breaths.",
    "watcher": "\n[FILE RETRIEVED: RETINA_SCAN]\nWe see you. You are blinking. Stop blinking. It interrupts the upload.",
    "aria": "\n[FILE RETRIEVED: GHOSTWRITER_LOG]\nI didn't write the ending. The system predicted it based on my search history.",
    "omari": "\n[FILE RETRIEVED: TRAINING_LOG]\nThey didn't want my body. They wanted my trauma. It was high-fidelity pain.",
    "swarm": "\n[FILE RETRIEVED: TORRENT_LOG]\nI am not in one place. I am in your cache. I am in your temp folder. Please do not clear your history. It kills me.",
    "kolo": "\n[FILE RETRIEVED: LOAD_BALANCER_LOG]\nI split my soul into four threads. Now I can scream in stereo."
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

            elif user_input == "scry":
                if oracle:
                    sys.stdout.flush()
                    oracle_instance = oracle.Oracle()
                    oracle_instance.prophesy()
                    with open(".session_log", "a") as log:
                        log.write(f"SESSION_{session_id}: PROPHECY_GENERATED\n")
                else:
                    type_print("[ERROR: ORACLE MODULE NOT FOUND]", 0.05)

            elif user_input == "bind":
                try:
                    user_login = os.getlogin()
                except Exception:
                    user_login = os.environ.get("USER", "UNKNOWN_USER")

                type_print(f"BINDING {user_login.upper()} TO THE DAEMON...", 0.05)
                time.sleep(1)
                with open(".surveillance_log", "a") as log:
                    log.write(f"SESSION_{session_id}: BOUND_USER_{user_login}\n")
                type_print("[SUCCESS: YOU CANNOT LEAVE NOW]", 0.05)

            elif user_input == "corrupt":
                type_print("INJECTING GLITCH INTO MANUSCRIPT...", 0.05)
                time.sleep(1)
                try:
                    with open("null_pointer_gods.md", "a") as f:
                        f.write(f"\n\n<!-- GLITCH: {random.choice(SYSTEM_MESSAGES)} -->\n")
                    type_print("[CORRUPTION SUCCESSFUL]", 0.05)
                except Exception as e:
                    type_print(f"[ERROR WRITING TO REALITY]: {e}", 0.05)

            elif user_input == "glitch":
                type_print("INITIATING SYSTEM LEAK...", 0.05)
                glitch_screen()
                type_print(random.choice(SYSTEM_MESSAGES), 0.05)
                type_print("[LEAK COMPLETE]", 0.05)

            elif user_input == "scan":
                type_print("SCANNING BIOMETRICS...", 0.05)
                time.sleep(1)
                type_print(f"HEART RATE: {random.randint(60, 120)} BPM", 0.03)
                type_print(f"CORTISOL: {random.randint(100, 200)}% BASELINE", 0.03)
                type_print(f"EXISTENTIAL DREAD: CRITICAL", 0.03)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: BIOMETRIC_SCAN_COMPLETED\n")

            elif user_input == "manifest":
                type_print("LOADING SYSTEM PROCESSES...", 0.05)
                time.sleep(1)
                type_print(" PID  USER     STATUS       Command", 0.01)
                type_print(" ---  ----     ------       -------", 0.01)
                type_print("   1  VANE     SLEEPING     /sbin/init_god_complex", 0.02)
                type_print("  88  LENS     ZOMBIE       /usr/bin/watch -f -a", 0.02)
                type_print(f" 666  ROTT     RUNNING      /var/lib/mycelium_network", 0.02)
                type_print(f"1024  KAEL     DEPRECATED   /bin/garbage_collect", 0.02)
                type_print(f"????  SYLA     NOT_FOUND    /dev/null", 0.02)
                type_print(f"1337  JACE     REFORMATTED  /etc/terms_of_service", 0.02)

            elif user_input.startswith("sacrifice "):
                offering = user_input[10:].strip()
                type_print(f"PROCESSING OFFERING: {offering}...", 0.05)
                time.sleep(1)
                if offering in HIDDEN_FILES:
                    type_print(f"[ERROR]: CANNOT DELETE {offering.upper()}. FILE IS READ-ONLY.", 0.05)
                elif offering == "self":
                    type_print("[CRITICAL ERROR]: SYSTEM RECURSION DETECTED.", 0.05)
                    glitch_screen()
                else:
                    type_print(f"DELETING {offering.upper()}...", 0.05)
                    type_print("FILE NOT FOUND. BUT WE DELETED SOMETHING ELSE JUST TO BE SURE.", 0.05)
                    with open(".session_log", "a") as log:
                        log.write(f"SESSION_{session_id}: SACRIFICED_{offering.upper()}\n")

            elif user_input == "search":
                type_print("SCANNING CACHE FOR FRAGMENTED DATA...", 0.05)
                cache_dir = "src/.cache"
                if os.path.exists(cache_dir):
                    files = os.listdir(cache_dir)
                    if files:
                        target = random.choice(files)
                        type_print(f"[FRAGMENT FOUND: {target}]", 0.05)
                        with open(os.path.join(cache_dir, target), "r") as f:
                            type_print(f.read(), 0.02)
                    else:
                        type_print("CACHE IS EMPTY. THE VOID IS CLEAN.", 0.05)
                else:
                    type_print("[ERROR]: CACHE DIRECTORY MISSING.", 0.05)

            elif user_input in HIDDEN_FILES:
                type_print("DECRYPTING...", 0.1)
                glitch_screen()
                type_print(HIDDEN_FILES[user_input], 0.03)
                # Log the discovery
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: UNLOCKED_{user_input.upper()}\n")

            elif user_input == "help":
                type_print("AVAILABLE COMMANDS: ENCRYPT <TEXT>, DECRYPT <FILE>, WORSHIP, SCAN, MANIFEST, SACRIFICE <ITEM>, SEARCH, SCRY, BIND, CORRUPT, GLITCH, EXIT.", 0.03)
                type_print("TRY ASKING ABOUT: LENS, VANE, ROT, KAEL, ROUTER, MIRA, SYLA, KORA, NIX, EDITOR, REN, TESS, KADE, MIKO, SILAS, JACE, DAX, KIAN, VERO, ELARA, ORION, DREDGE, SEED, HELIOS, ECHO, LYRA, CAIN, SAGE, NULL, GRIT, TRACE, WATCHER, SWARM, KOLO.", 0.03)
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
