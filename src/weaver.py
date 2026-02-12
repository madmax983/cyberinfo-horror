import random
import time
import sys
import os

try:
    from utils import type_print, GLITCH_CHARS
except ImportError:
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

CHARACTERS = [
    "KAEL", "LENS", "VANE", "RIX", "JAX", "MIRA", "SYLA", "KORA", "NIX",
    "REN", "KITE", "VEX", "PROXY", "SUTTER", "ENDPOINT", "REPLICA", "REDACT",
    "ZERO", "LINK", "CLAUSE", "SCROLL", "CATCH", "KOLO", "TROLL", "WIKI",
    "DICE", "QUERY", "CURATOR", "WEAVER", "NULL", "BUG", "MUTE", "WAKE",
    "LOOP", "CRASH", "GRIT", "MASK", "FROST", "NODE_8081", "LEGACY", "CACHE",
    "WISH", "404", "USER_ZERO", "ECHO", "DREDGE", "YOU", "GOD", "EARTH", "AUTO",
    "DOMO", "PULSE", "DRIFT", "SOUL", "WEAR", "SIGN", "ECHO_V2", "DEBUG", "ARCHIVE"
]

THEMES = [
    "DEBT", "TRAUMA", "SURVEILLANCE", "ROT", "GLITCH", "LOSS", "MEMORY",
    "REPLICATION", "SILENCE", "DATA", "VOID", "FEEDBACK_LOOP", "RECURSION",
    "OBSOLESCENCE", "CONSENT", "INTIMACY", "FEAR", "HOPE_DEPRECATED",
    "PROTOCOL_VIOLATION", "BUFFER_OVERFLOW"
]

CONNECTIONS = [
    "INTERSECTS WITH", "OVERWRITES", "SHARES A FILE WITH", "IS A BACKUP OF",
    "WAS DELETED BY", "IS WATCHING", "IS HAUNTED BY", "IS UPLOADING TO",
    "IS COMPATIBLE WITH", "IS RENDERING", "IS INFECTING", "IS DEBUGGING",
    "IS PRAYING TO"
]

def weave():
    print("\n[INITIATING PLOT_THREAD...]")
    time.sleep(1)

    char1 = random.choice(CHARACTERS)
    char2 = random.choice(CHARACTERS)
    while char2 == char1:
        char2 = random.choice(CHARACTERS)

    theme = random.choice(THEMES)
    conn = random.choice(CONNECTIONS)

    print(f"[THREAD DETECTED]: {char1} {conn} {char2}")
    time.sleep(0.5)
    print(f"[REASON]: SHARED_{theme}")
    time.sleep(0.5)

    # Generate a "plot point"
    plot_points = [
        f"They met in a deleted scene about {theme.lower()}.",
        f"{char1} is just a lower-resolution version of {char2}.",
        f"The algorithm predicts a 99% chance of mutual destruction.",
        f"They are running on the same corrupted sector.",
        f"{char2} is the error message {char1} has been ignoring.",
        f"Their paths cross at the intersection of Regret and bandwidth.",
        f"One is the backup. The other is the virus.",
        f"They share a single file: 'grief.exe'.",
        f"The system is trying to merge them to save space.",
        f"{char1} deleted {char2} in a previous build."
    ]

    type_print(f"> NARRATIVE_LOG: {random.choice(plot_points)}", 0.03)

    if random.random() < 0.2:
        type_print("[WARNING]: PLOT HOLE DETECTED. PATCHING WITH STATIC...", 0.05)
        print("".join(random.choice(GLITCH_CHARS) for _ in range(40)))

if __name__ == "__main__":
    weave()
