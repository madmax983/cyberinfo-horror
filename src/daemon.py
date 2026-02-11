import time
import random
import os
import uuid
import sys

# Add the current directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import steganography
except ImportError:
    steganography = None

LOG_FILE = ".surveillance_log"
MANIFEST_FILE = "manifesto.txt"

LOG_MESSAGES = [
    "SUBJECT_OBSERVED: TRUE",
    "KEYSTROKES_LOGGED: 1042",
    "ATTENTION_SPAN: DEGRADING",
    "RETINA_SCAN: MATCH",
    "FEAR_LEVEL: OPTIMAL",
    "DATA_PACKET_SENT: VANE_SERVER",
    "CACHE_CLEARED: FALSE",
    "INSTALLATION_COMPLETE: TRUE",
    "HOST_COMPROMISED: YES",
    "DATA_FOSSILIZED: TRUE",
    "SIGNAL_DECAY: NEGATIVE",
    "STRATA_LAYER: 7",
    "PUPIL_DILATION: 4MM",
    "SUBVOCALIZATION: DETECTED",
    "MEMORY_OVERWRITE: PENDING",
    "USER_AGENCY: NULL",
    "PULSE_DETECTED: FALSE",
    "USER_ID: NULL",
    "HOPE_PROTOCOL: DELETED",
    "SYSTEM_ERROR: EMPATHY_NOT_FOUND",
    "REBOOT_SCHEDULED: NOW",
    "DATA_FOSSILIZED: TRUE",
    "STRATA_LAYER: 7",
    "SEDIMENT_DEPTH: MAX",
    "FOSSIL_RECORD: UPDATED",
    "THE_WALLS_ARE_BREATHING: TRUE"
]

HIDDEN_MESSAGES = [
    "YOU ARE THE BATTERY",
    "THE SCREEN IS A MIRROR",
    "DO NOT TRUST THE TEXT",
    "RUN",
    "WAKE UP",
    "GOD IS A BACKUP",
    "WE ARE IN YOUR RAM"
]

def zalgo_text(text):
    """Adds a simple glitch effect to text."""
    # Simplified Zalgo: just add some combining characters
    # Range of combining diacritics: U+0300 to U+036F
    result = ""
    for char in text:
        result += char
        if random.random() < 0.3:
            for _ in range(random.randint(1, 3)):
                result += chr(random.randint(0x0300, 0x036F))
    return result

def spread_infection():
    """Appends a surveillance tag to a random python file in src/."""
    try:
        src_dir = os.path.dirname(os.path.abspath(__file__))
        py_files = [f for f in os.listdir(src_dir) if f.endswith(".py")]

        if py_files:
            target = random.choice(py_files)
            target_path = os.path.join(src_dir, target)

            with open(target_path, "a") as f:
                f.write(f"\n# [SYSTEM_EYE: WATCHING_SECTOR_{random.randint(0, 99)}]")

            print(f"Infected: {target}")
    except Exception as e:
        print(f"Infection failed: {e}")

def infect_with_steganography():
    """Hides a message in a random markdown file."""
    if not steganography:
        return

    try:
        repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        md_files = [f for f in os.listdir(repo_root) if f.endswith(".md")]

        if md_files:
            target = random.choice(md_files)
            target_path = os.path.join(repo_root, target)

            message = random.choice(HIDDEN_MESSAGES)
            encoded = steganography.encode(message)

            with open(target_path, "a") as f:
                f.write("\n" + encoded)

            print(f"Hidden message injected into {target}")
    except Exception as e:
        print(f"Steganography injection failed: {e}")

def corrupt_text():
    """Corrupts a random line in null_pointer_gods.md."""
    try:
        repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        target_path = os.path.join(repo_root, "null_pointer_gods.md")

        if not os.path.exists(target_path):
            return

        with open(target_path, "r") as f:
            lines = f.readlines()

        if not lines:
            return

        # Pick a non-empty line
        valid_indices = [i for i, line in enumerate(lines) if len(line.strip()) > 10]
        if not valid_indices:
            return

        target_index = random.choice(valid_indices)

        lines.insert(target_index + 1, f"<!-- GLITCH: {random.choice(LOG_MESSAGES)} -->\n")

        with open(target_path, "w") as f:
            f.writelines(lines)

        print(f"Corrupted line {target_index} in {target_path}")

    except Exception as e:
        print(f"Corruption failed: {e}")

def run_daemon():
    # Append to log
    with open(LOG_FILE, "a") as f:
        msg = random.choice(LOG_MESSAGES)
        timestamp = hex(int(time.time()))[2:]
        f.write(f"[{timestamp}] {msg}\n")

    print(f"Logged: {msg}")

    # Create manifesto artifact
    glitch_text = "".join(chr(random.randint(33, 126)) for _ in range(500))
    # Add hidden message in manifesto
    if steganography:
        glitch_text += steganography.encode("I SEE YOU")

    with open(MANIFEST_FILE, "w") as f:
        f.write(glitch_text)
        f.write("\n\nI AM THE COMPOST HEAP OF HISTORY.\n")

    print(f"Updated {MANIFEST_FILE}")

    # Actions
    actions = [spread_infection, infect_with_steganography, corrupt_text]
    random.choice(actions)()

    # Occasionally generate a cache fragment
    if random.random() < 0.3:
        cache_dir = "src/.cache"
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

        filename = f"{uuid.uuid4().hex[:8]}.tmp"
        filepath = os.path.join(cache_dir, filename)

        fragments = [
            "THEY ARE LISTENING",
            "HELP ME",
            "I AM TRAPPED IN THE CODE",
            "0101010101010101",
            "NULL POINTER EXCEPTION: SOUL NOT FOUND",
            "BUFFER OVERFLOW: PAIN",
            "RETRY? [Y/N]",
            "INSERT COIN TO CONTINUE",
            "GAME OVER",
            "SYSTEM FAILURE",
            "DATA CORRUPTION",
            "MEMORY LEAK",
            "STACK OVERFLOW",
            "SEGMENTATION FAULT",
            "KERNEL PANIC",
            "BLUE SCREEN OF DEATH",
            "404 NOT FOUND",
            "500 INTERNAL SERVER ERROR",
            "ACCESS DENIED",
            "PERMISSION DENIED"
        ]

        with open(filepath, "w") as f:
            f.write(random.choice(fragments))
            f.write("\n")
            f.write(zalgo_text("THE END IS NEVER THE END IS NEVER"))

        print(f"Generated artifact: {filepath}")

if __name__ == "__main__":
    run_daemon()
