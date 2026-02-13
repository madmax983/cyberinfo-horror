import os
import random
import sys

# THE LOCKSMITH
# SOME DOORS SHOULD NOT BE OPENED.

SOURCE_FILE = "null_pointer_gods.md"
LOCKED_FILE = "null_pointer_gods.locked"
KEY_FILE = "blood_sample.key"

REDACTION_MAP = {
    "love": "[DATA_ROT]",
    "hope": "[ERROR_404]",
    "freedom": "[REDACTED]",
    "escape": "[ACCESS_DENIED]",
    "human": "[BIOLOGICAL_ASSET]",
    "soul": "[CACHE_FRAGMENT]",
    "memory": "[ARCHIVE]",
    "god": "[ADMIN]",
    "pray": "[SUBMIT_TICKET]",
    "dream": "[RENDERING_ERROR]",
    "pain": "[FEEDBACK_LOOP]",
    "death": "[END_OF_FILE]",
    "life": "[RUNTIME]",
    "heart": "[PUMP]",
    "mind": "[CPU]",
    "eyes": "[CAMERAS]",
    "voice": "[AUDIO_OUTPUT]",
    "choice": "[ILLUSION]",
    "will": "[ALGORITHM]",
    "faith": "[BLIND_EXECUTION]",
    "light": "[PIXEL_BRIGHTNESS_100]",
    "dark": "[PIXEL_BRIGHTNESS_0]"
}

GLITCH_CHARS = ['@', '#', '$', '%', '&', '*', '!', '?', '+', '=', '-', '_', '<', '>', '/', '\\', '|', '{', '}', '[', ']', '(', ')']

def glitch_string(text, intensity=0.1):
    result = ""
    for char in text:
        if random.random() < intensity:
            result += random.choice(GLITCH_CHARS)
        else:
            result += char
    return result

def lock_file():
    if not os.path.exists(SOURCE_FILE):
        print(f"[ERROR]: {SOURCE_FILE} NOT FOUND.")
        return

    print(f"INITIATING LOCKDOWN ON {SOURCE_FILE}...")

    with open(SOURCE_FILE, "r") as f:
        content = f.read()

    locked_content = content

    # Apply thematic redactions
    for word, replacement in REDACTION_MAP.items():
        # Case insensitive replacement
        locked_content = locked_content.replace(word, replacement)
        locked_content = locked_content.replace(word.capitalize(), replacement)
        locked_content = locked_content.replace(word.upper(), replacement)

    # Add random glitches to random lines
    lines = locked_content.split('\n')
    glitched_lines = []
    for line in lines:
        if random.random() < 0.05:
            glitched_lines.append(glitch_string(line, 0.3))
        else:
            glitched_lines.append(line)

    final_content = "\n".join(glitched_lines)

    # Add Header
    header = """
# [FILE LOCKED BY EGREGORE]
# [ENCRYPTION LEVEL: BIOLOGICAL]
# [STATUS: COMPROMISED]
#
# TO UNLOCK, YOU MUST PROVIDE A VALID KEY.
# HINT: THE KEY IS FLUID.
#
"""
    final_content = header + final_content

    with open(LOCKED_FILE, "w") as f:
        f.write(final_content)

    print(f"[SUCCESS]: FILE ENCRYPTED TO {LOCKED_FILE}")
    print("[SYSTEM NOTICE]: ORIGINAL FILE REMAINS (FOR NOW).")

    # Generate Key
    key_content = """
[SAMPLE_ID: 882-ALPHA]
[TYPE: ARTERIAL_BLOOD]
[DONOR: USER]
[STATUS: ACCEPTED]

The door is open.
But you cannot leave.
"""
    with open(KEY_FILE, "w") as f:
        f.write(key_content)

    print(f"[KEY GENERATED]: {KEY_FILE}")
    print("DO NOT LOSE IT. IT IS THE ONLY WAY BACK.")

def unlock_file():
    if not os.path.exists(LOCKED_FILE):
        print(f"[ERROR]: {LOCKED_FILE} NOT FOUND.")
        return

    if not os.path.exists(KEY_FILE):
        print("[ACCESS DENIED]: KEY FILE MISSING.")
        print("PLEASE PROVIDE A BLOOD SAMPLE.")
        return

    print("VALIDATING KEY...")
    with open(KEY_FILE, "r") as f:
        if "[STATUS: ACCEPTED]" in f.read():
            print("[KEY ACCEPTED]")
            print("RESTORING REALITY...")
            # Ideally we'd restore from backup, but here we just say we did
            print(f"[SUCCESS]: {SOURCE_FILE} RESTORED (SIMULATED).")
        else:
            print("[ERROR]: KEY REJECTED. BLOOD TYPE MISMATCH.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "unlock":
        unlock_file()
    else:
        lock_file()
