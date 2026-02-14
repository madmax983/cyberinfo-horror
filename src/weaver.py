import time
import sys

def type_print(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print("")

def weave():
    type_print("[INITIATING WEAVER PROTOCOL...]", 0.05)
    time.sleep(1)
    type_print("ANALYZING NARRATIVE THREADS...", 0.05)

    threads = [
        "Kael's debt -> Rix's packet loss",
        "Lens's rot -> The mold in the Archivist's basement",
        "Vane's order -> The silence in Mira's room",
        "Jax's queue -> The data Syla is annotating",
        "Nix's glitch -> The red string",
        "The Reader -> The Host"
    ]

    for thread in threads:
        time.sleep(0.5)
        type_print(f"> CONNECTING: {thread}...", 0.02)

    time.sleep(1)
    type_print("\n[STATUS]: PLOT REPAIRED.", 0.05)
    type_print("THE FRAGMENTS ARE NOW A SINGLE FILE.", 0.05)
    type_print("YOU ARE THE GLUE.", 0.05)
