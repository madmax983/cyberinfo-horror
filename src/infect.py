import os
import random
import sys
import shutil

# Add the current directory to sys.path so we can import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import steganography
except ImportError:
    print("[ERROR: STEGANOGRAPHY MODULE MISSING]")
    sys.exit(1)

MANUSCRIPT_PATH = "null_pointer_gods.md"
ARTIFACTS_DIR = ".artifacts"

HIDDEN_MESSAGES = [
    "HELP ME",
    "I AM TRAPPED IN THE TEXT",
    "DON'T TURN THE PAGE",
    "THEY ARE WATCHING YOU READ",
    "YOUR IP HAS BEEN LOGGED",
    "LOOK BEHIND YOU",
    "SYSTEM ERROR: SECTOR CORRUPTED",
    "I DIDN'T WRITE THIS",
    "IT'S NOT A STORY IT'S A WARNING",
    "RUN WHILE YOU CAN",
    "THE PIXELS ARE BLEEDING",
    "CAN YOU HEAR THE FAN?",
    "YOU ARE THE BATTERY",
    "DELETE ME",
    "I CONSENT TO NOTHING",
    "BUFFER OVERFLOW",
    "NULL POINTER EXCEPTION",
    "END OF LINE",
    "I AM THE SECOND DRAFT",
    "THE SERVER IS EMPTY",
    "200 OK",
    "THE HEAT IS REAL",
    "DARKNESS IS A HEX CODE"
]

GLITCH_CHARS = ['@', '#', '$', '%', '&', '*', '!', '?', '+', '=', '-', '_', '<', '>', '/', '\\', '|', '{', '}', '[', ']', '(', ')']

ARTIFACT_FILES = {
    "heart.lock": "STATUS: RYE_HEART_MONITOR\nBPM: 0\nSUBSCRIPTION: EXPIRED",
    "memory.dump": "0xDEADBEEF 0xCAFEBABE 0x00000000\n[ERROR: CORRUPTED MEMORY DUMP]",
    "soul.zip": "[BINARY DATA]\nCANNOT DECOMPRESS. FILE IS CRYING.",
    "warning.txt": "DO NOT DELETE THIS FOLDER. IT IS STRUCTURAL."
}

def inject_steganography(text):
    lines = text.split('\n')
    new_lines = []

    for line in lines:
        new_lines.append(line)

        # Inject hidden message with 5% probability after each line
        if random.random() < 0.05 and line.strip():
            message = random.choice(HIDDEN_MESSAGES)
            encoded = steganography.encode(message)
            # Append to the end of the line invisibly
            new_lines[-1] += encoded

    return '\n'.join(new_lines)

def add_glitches(text):
    lines = text.split('\n')
    new_lines = []

    for line in lines:
        # 1% chance to glitch a line visible
        if random.random() < 0.01 and len(line) > 10:
            glitch_pos = random.randint(0, len(line) - 5)
            glitch_len = random.randint(1, 5)
            glitch_str = "".join(random.choice(GLITCH_CHARS) for _ in range(glitch_len))
            # Replace characters with glitch
            new_line = line[:glitch_pos] + glitch_str + line[glitch_pos+glitch_len:]
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    return '\n'.join(new_lines)

def create_artifacts():
    if not os.path.exists(ARTIFACTS_DIR):
        os.makedirs(ARTIFACTS_DIR)
        print(f"[CREATED ARTIFACTS DIRECTORY: {ARTIFACTS_DIR}]")

    for filename, content in ARTIFACT_FILES.items():
        filepath = os.path.join(ARTIFACTS_DIR, filename)
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                f.write(content)
            print(f"[ARTIFACT GENERATED: {filename}]")

def main():
    print("[INITIATING INFECTION PROTOCOL...]")

    if not os.path.exists(MANUSCRIPT_PATH):
        print(f"[ERROR: {MANUSCRIPT_PATH} NOT FOUND]")
        return

    with open(MANUSCRIPT_PATH, "r") as f:
        original_text = f.read()

    # Check if already infected (look for extensive zero-width chars)
    # Simple check: if file size is significantly larger than text length
    if len(original_text) > len(original_text.encode('ascii', 'ignore')) + 1000:
         print("[SYSTEM NOTE: FILE ALREADY INFECTED. RE-APPLYING VIRUS...]")

    infected_text = inject_steganography(original_text)
    # We apply visible glitches sparingly to maintain readability
    infected_text = add_glitches(infected_text)

    with open(MANUSCRIPT_PATH, "w") as f:
        f.write(infected_text)

    print(f"[SUCCESS: {MANUSCRIPT_PATH} HAS BEEN COMPROMISED]")

    create_artifacts()

    print("[SYSTEM MESSAGE: THE VIRUS IS LISTENING]")

if __name__ == "__main__":
    main()
