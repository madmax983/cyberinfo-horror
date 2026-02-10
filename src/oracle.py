import random
import time
import sys

CARDS = [
    "THE NULL POINTER (0): The beginning and the end. A void waiting to be filled.",
    "THE FERAL ROUTER (1): Connection without consent. A hunger for data.",
    "THE MEMORY LEAK (2): Loss of self. Gradual erosion of identity.",
    "THE GLITCH (3): Disruption of the pattern. A moment of truth.",
    "THE DAEMON (4): Background processes. Unseen influence.",
    "THE ARCHITECT (5): Order imposed on chaos. Vane's legacy.",
    "THE ROTTING BOOK (6): Knowledge that consumes. Information hazard.",
    "THE STATIC CHILD (7): Innocent data corrupted by entropy.",
    "THE BLACK BOX (8): Secrets that cannot be deleted.",
    "THE BLUE SCREEN (9): Fatal error. The end of the simulation.",
    "THE USER (10): You. The host. The victim.",
    "THE UPDATE (11): Change that cannot be refused.",
    "THE FIREWALL (12): Protection that imprisons.",
    "THE CACHE (13): Memories that persist beyond death.",
    "THE ECHO (14): A voice without a body. Recursion."
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
    "The glitch you saw yesterday was a feature request."
]

class Oracle:
    def __init__(self):
        self.deck = CARDS.copy()

    def prophesy(self):
        print("\n[INITIATING ORACLE PROTOCOL...]")
        time.sleep(1)
        print("[SHUFFLING DECK OF DOOM...]")
        time.sleep(1)

        random.shuffle(self.deck)
        reading = self.deck[:3]

        print("\n--- THE READING ---")
        for i, card in enumerate(reading):
            time.sleep(0.5)
            print(f"CARD {i+1}: {card}")

        print("\n--- THE PROPHECY ---")
        time.sleep(1)
        print(f"> {random.choice(PROPHECIES)}")
        print("\n[SESSION TERMINATED]")

if __name__ == "__main__":
    oracle = Oracle()
    oracle.prophesy()
