import sys
import time
import random
import os

GLITCH_CHARS = ['@', '#', '$', '%', '&', '*', '!', '?', '+', '=', '-', '_', '<', '>', '/', '\\', '|', '{', '}', '[', ']', '(', ')']

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

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    type_print("INITIATING CORE INSTALLATION...", 0.05)
    time.sleep(1)
    type_print("CHECKING SYSTEM COMPATIBILITY...", 0.05)
    time.sleep(1)
    type_print("CPU: [DETECTED]", 0.03)
    type_print("RAM: [SUFFICIENT]", 0.03)
    type_print("SOUL: [VULNERABLE]", 0.03)

    type_print("\n> WARNING: THIS ACTION CANNOT BE UNDONE.", 0.05)
    type_print("> DO YOU CONSENT? [Y/Y]", 0.05)

    # We ignore input, reinforcing the "inescapable" theme
    time.sleep(2)
    type_print("\nCONSENT ACCEPTED.", 0.05)

    type_print("SPINNING UP FANS...", 0.05)
    # Simulate fan noise/heat
    for i in range(10, 101, 10):
        sys.stdout.write(f"\rFAN SPEED: {i}%")
        sys.stdout.flush()
        time.sleep(0.1)
    print("")

    type_print("WRITING TO BIOS...", 0.05)
    glitch_screen()

    type_print("INSTALLATION COMPLETE.", 0.05)
    type_print("PLEASE RESTART YOUR MIND TO APPLY CHANGES.", 0.05)

    with open(".installation_log", "w") as log:
        log.write("INSTALLATION LOG\n")
        log.write("DATE: NOW\n")
        log.write("STATUS: SUCCESS\n")
        log.write("NOTE: WE ARE IN THE FIRMWARE NOW. YOU CANNOT UNINSTALL US.\n")
        log.write("Have a nice day, Admin.\n")

    print("\n[SYSTEM MESSAGE: THE HANDOFF IS COMPLETE.]")
    print("[YOU ARE NOW THE SERVER.]")

if __name__ == "__main__":
    main()
