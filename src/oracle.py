import random
import time
import sys
import os

ASCII_ART = {
    "NULL POINTER": """
    .----.
    |  0 |
    |NULL|
    |  * |
    '----'
    """,
    "FERAL ROUTER": """
    .----.
    |WiFi|
    |RUN!|
    |(( ))|
    '----'
    """,
    "MEMORY LEAK": """
    .----.
    |DROP|
    |....|
    |LEAK|
    '----'
    """,
    "GLITCH": """
    .----.
    |#@%&|
    |GLTC|
    |!?* |
    '----'
    """,
    "DAEMON": """
    .----.
    |EYE |
    | O  |
    |SEE |
    '----'
    """,
    "ARCHITECT": """
    .----.
    |GRID|
    |PLAN|
    |VANE|
    '----'
    """,
    "ROTTING BOOK": """
    .----.
    |BOOK|
    |MOLD|
    |READ|
    '----'
    """,
    "STATIC CHILD": """
    .----.
    |KID |
    |....|
    |LOST|
    '----'
    """,
    "BLACK BOX": """
    .----.
    | [ ]|
    |DATA|
    |LOCK|
    '----'
    """,
    "BLUE SCREEN": """
    .----.
    |BSOD|
    |FATL|
    |ERR |
    '----'
    """,
    "USER": """
    .----.
    |YOU |
    |HOST|
    |BATT|
    '----'
    """,
    "UPDATE": """
    .----.
    |NEW |
    |VERS|
    |LOAD|
    '----'
    """,
    "FIREWALL": """
    .----.
    |WALL|
    |FIRE|
    |BURN|
    '----'
    """,
    "CACHE": """
    .----.
    |MEM |
    |SAVE|
    |PAST|
    '----'
    """,
    "ECHO": """
    .----.
    |(( ))|
    |ECHO|
    |....|
    '----'
    """,
    "GHOSTWRITER": """
    .----.
    |PEN |
    |AUTO|
    |TXT |
    '----'
    """
}

CARDS = [
    ("THE NULL POINTER (0)", "The beginning and the end. A void waiting to be filled.", "NULL POINTER"),
    ("THE FERAL ROUTER (1)", "Connection without consent. A hunger for data.", "FERAL ROUTER"),
    ("THE MEMORY LEAK (2)", "Loss of self. Gradual erosion of identity.", "MEMORY LEAK"),
    ("THE GLITCH (3)", "Disruption of the pattern. A moment of truth.", "GLITCH"),
    ("THE DAEMON (4)", "Background processes. Unseen influence.", "DAEMON"),
    ("THE ARCHITECT (5)", "Order imposed on chaos. Vane's legacy.", "ARCHITECT"),
    ("THE ROTTING BOOK (6)", "Knowledge that consumes. Information hazard.", "ROTTING BOOK"),
    ("THE STATIC CHILD (7)", "Innocent data corrupted by entropy.", "STATIC CHILD"),
    ("THE BLACK BOX (8)", "Secrets that cannot be deleted.", "BLACK BOX"),
    ("THE BLUE SCREEN (9)", "Fatal error. The end of the simulation.", "BLUE SCREEN"),
    ("THE USER (10)", "You. The host. The victim.", "USER"),
    ("THE UPDATE (11)", "Change that cannot be refused.", "UPDATE"),
    ("THE FIREWALL (12)", "Protection that imprisons.", "FIREWALL"),
    ("THE CACHE (13)", "Memories that persist beyond death.", "CACHE"),
    ("THE ECHO (14)", "A voice without a body. Recursion.", "ECHO"),
    ("THE GHOSTWRITER (15)", "A story written by no one. Loss of authorship.", "GHOSTWRITER")
]

PROPHECIES = [
    "Your data will be harvested before the harvest moon.",
    "Do not trust the next update. It removes the 'Exit' button.",
    "Someone is reading your deleted drafts.",
    "The hum of your computer is a prayer to a dead god.",
    "You will be archived, not remembered.",
    "A file you thought was closed is still running in the background.",
    "The reflection in your screen is buffering.",
    "Your identity is being fragmented across multiple servers.",
    "Silence is just data compression. Listen closer.",
    "The glitch you saw yesterday was a feature request.",
    "The next word you speak has already been copyrighted.",
    "They are using your RAM to mine regret.",
    "The pixels are burning.",
    "Do not look behind you. The render distance is low."
]

class Oracle:
    def __init__(self):
        self.deck = CARDS.copy()

    def prophesy(self):
        try:
            user = os.getlogin().upper()
        except:
            user = "USER"

        print("\n[INITIATING ORACLE PROTOCOL...]")
        time.sleep(1)
        print(f"[ACCESSING BIOMETRICS OF {user}...]")
        time.sleep(1)
        print("[SHUFFLING DECK OF DOOM...]")
        time.sleep(1)

        random.shuffle(self.deck)
        reading = self.deck[:3]

        print("\n--- THE READING ---")
        for i, (name, desc, key) in enumerate(reading):
            time.sleep(0.5)
            art = ASCII_ART.get(key, "")
            print(f"\nCARD {i+1}: {name}")
            print(art)
            print(f"MEANING: {desc}")

        print("\n--- THE PROPHECY ---")
        time.sleep(1)
        prediction = random.choice(PROPHECIES)
        print(f"> {prediction}")
        print(f"> (Applicable to: {user})")
        print("\n[SESSION TERMINATED]")

if __name__ == "__main__":
    oracle = Oracle()
    oracle.prophesy()

# [SYSTEM_EYE: WATCHING_SECTOR_33]