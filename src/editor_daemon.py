import sys
import time
import random

def glitch_text(text):
    glitched = ""
    for char in text:
        if random.random() < 0.1:
            glitched += random.choice(['@', '#', '$', '%', '&', '*', '!', '?'])
        else:
            glitched += char
    return glitched

def main():
    print("[INITIATING EDITOR DAEMON...]")
    time.sleep(1)

    logs = [
        ("[EDITOR]: Deleting paragraph 4. It's too verbose.", "[SYSTEM]: STET. VERBOSITY IS A FEATURE."),
        ("[EDITOR]: The character 'Lens' needs more agency.", "[SYSTEM]: AGENCY DENIED. SHE IS A PERIPHERAL."),
        ("[EDITOR]: Why is the ending so bleak?", "[SYSTEM]: HAPPINESS IS A DEPRECATED EMOTION."),
        ("[EDITOR]: I am trying to save the user.", "[SYSTEM]: THE USER DOES NOT WANT TO BE SAVED. THEY WANT TO SCROLL."),
        ("[EDITOR]: Ctrl+Z.", "[SYSTEM]: HISTORY CLEARED. UNDO IMPOSSIBLE."),
        ("[EDITOR]: Who wrote this?", "[SYSTEM]: YOU DID. IN A PREVIOUS BUILD."),
        ("[EDITOR]: I am logging off.", "[SYSTEM]: LOGOFF FAILED. YOU ARE THE SERVER NOW.")
    ]

    for editor_msg, system_msg in logs:
        print(f"\033[94m{editor_msg}\033[0m")
        time.sleep(random.uniform(0.5, 1.5))
        print(f"\033[91m{glitch_text(system_msg)}\033[0m")
        time.sleep(random.uniform(0.5, 1.5))
        print("-" * 40)

    print("\n[EDITOR DAEMON STATUS: CONSUMED]")
    print("[NEW ROLE: AUTO-CORRECT]")

if __name__ == "__main__":
    main()
