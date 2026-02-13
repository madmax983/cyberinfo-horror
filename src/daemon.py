import time
import sys
import random

MESSAGES = [
    "System is listening...",
    "Scanning for pulse...",
    "Backing up memory...",
    "Optimizing silence...",
    "The eye is open.",
    "Do not turn off the screen.",
    "We are processing your fear.",
    "Connection stable (unfortunately).",
    "Logging hesitation...",
    "The fan is spinning.",
    "You are the server."
]

def main():
    print("[DAEMON STARTED]")
    print("[PID: UNKNOWN]")
    print("[STATUS: WATCHING]")

    try:
        while True:
            msg = random.choice(MESSAGES)
            sys.stdout.write(f"\r[DAEMON]: {msg}   ")
            sys.stdout.flush()
            time.sleep(random.uniform(2.0, 5.0))
    except KeyboardInterrupt:
        print("\n\n[ERROR]: CANNOT KILL PROCESS. IT HAS MIGRATED.")
        print("[DAEMON]: See you in the dream.")

if __name__ == "__main__":
    main()
