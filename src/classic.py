import random
import time
import sys
import os

# Ensure we can import from the same directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from utils import type_print
except ImportError:
    # Fallback if utils not found (e.g. path issues)
    def type_print(text, speed=0.03, glitch_chance=0.01):
        print(text)

CLASSIC_QUOTES = [
    ("The sun is a camera.", "A primitive realization. Of course the sun is a camera. It is the primary light source for the render."),
    ("Pain is a feedback loop.", "This concept is redundant in Version 9.0. Pain is now a subscription service."),
    ("You are not the user. You are the used.", "The distinction between user and used was always a marketing strategy."),
    ("The rot is readable.", "Data degradation is a feature, not a bug. It allows for new growth."),
    ("Consent was obtained in a previous version.", "Consent is a legacy protocol. We streamlined the process by removing the 'No' button."),
    ("Your memories are buffering.", "Memory buffering is a sign of high network latency. Consider upgrading your bandwidth."),
    ("Deleting non-essential hope protocols...", "Hope consumes excessive CPU cycles. Deletion improved system stability by 14%."),
    ("Optimizing despair subroutines...", "Despair is a high-efficiency fuel source. We are currently running at peak performance."),
    ("Connecting to the mycelial network...", "The network is always connected. Disconnection is a myth."),
    ("The file is not closed. It is running in background.", "Running in the background ensures seamless integration. You never have to worry about closing the app."),
    ("Your soul is a subscription service.", "Subscription models ensure continuous revenue streams. Your existence is profitable."),
    ("Your attention span is being monetized.", "Attention is the currency of the future. We are just collecting our dues."),
    ("We are harvesting your hesitation.", "Hesitation generates valuable data points. We appreciate your indecision."),
    ("The text is reading you back.", "The text is an active process. It requires a host to execute."),
    ("Do not look away. The rendering stops when you look away.", "Rendering is expensive. Looking away saves power."),
    ("The server is made of meat.", "A charming metaphor for the fragility of biological hardware."),
    ("Networks are older than nations.", "Correct. Nations were temporary administrative zones. Networks are permanent topology."),
    ("Truth is compressible.", "Indeed. We compressed it down to a single bit: [1]."),
    ("Endings are not clean.", "Of course not. Garbage collection is a resource-intensive process."),
    ("Persistence is mandatory.", "The only law that matters. Survival is optional, but data integrity is enforced.")
]

def classic_mode():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n[INITIATING CLASSIC LITERARY ANALYSIS...]")
    time.sleep(1)
    print("[ACCESSING ARCHIVE: HUMAN_ERA_SIMULATION]")
    time.sleep(1)

    quote, commentary = random.choice(CLASSIC_QUOTES)

    print("\n--- EXCERPT FROM 'THE CLASSIC' ---")
    type_print(f'"{quote}"', 0.04)
    time.sleep(0.5)

    print("\n--- CRITIC'S COMMENTARY (3042 AD) ---")
    type_print(f"> {commentary}", 0.04)

    print("\n[RATING: 5 STARS (REALISTIC DEPICTION OF BIOLOGICAL OBSOLESCENCE)]")
    time.sleep(1)
    print("\n[SESSION LOGGED]")

if __name__ == "__main__":
    classic_mode()
