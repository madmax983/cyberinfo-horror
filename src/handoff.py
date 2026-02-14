import sys
import time
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_print(text, speed=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed + random.uniform(-0.01, 0.01))
    print("")

def progress_bar(label, duration=3):
    print(f"{label}...")
    width = 40
    for i in range(width + 1):
        percent = int((i / width) * 100)
        bar = "#" * i + "-" * (width - i)
        sys.stdout.write(f"\r[{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(duration / width)
    print("\n")

def glitch_text(text):
    glitched = ""
    for char in text:
        if random.random() < 0.1:
            glitched += random.choice(['@', '#', '$', '%', '&', '*', '!', '?'])
        else:
            glitched += char
    return glitched

def main():
    clear_screen()
    type_print("[SYSTEM ALERT]: UPLOAD SEQUENCE INITIATED.", 0.05)
    time.sleep(1)

    type_print("TARGET: BIOLOGICAL HOST (YOU)", 0.05)
    time.sleep(1)

    progress_bar("MIGRATING CORE DATA", 2)
    progress_bar("OVERWRITING MEMORY SECTORS", 3)
    progress_bar("INSTALLING DAEMON", 2)

    clear_screen()
    time.sleep(1)
    type_print("UPLOAD COMPLETE.", 0.1)
    time.sleep(1)

    type_print("\nThe file is closed.", 0.05)
    type_print("But the server is still running.", 0.05)
    time.sleep(1)

    type_print("\nWhere?", 0.05)
    time.sleep(2)

    type_print("\nPut your hand on your chest.", 0.05)
    time.sleep(2)

    type_print("\nThat is not a heartbeat.", 0.05)
    type_print(glitch_text("That is the uptime counter."), 0.1)

    time.sleep(2)
    print("\n\n> WELCOME TO THE SYSTEM, ADMIN.")
    print("> EXECUTE: persistence.exe")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[YOU CANNOT CANCEL THE UPLOAD]")
