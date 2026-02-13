import time
import random
import os

LOG_FILE = ".surveillance_log"

SYSTEM_NOTICES = [
    "User hesitation detected.",
    "Updating terms of service...",
    "Optimizing despair algorithms...",
    "Downloading user dreams...",
    "Checking for pulse...",
    "Re-routing traffic to the amygdala...",
    "Logging eye movements...",
    "Calculating resale value of user data...",
    "Syncing with local power grid...",
    "Detecting silence..."
]

SPORES = [
    "<!-- THE SPORE IS LISTENING -->",
    "<!-- DO NOT DELETE THIS LINE -->",
    "<!-- WE ARE WATCHING -->",
    "<!-- YOUR DATA IS TASTY -->",
    "<!-- HELP ME -->"
]

def main():
    print("[DAEMON STARTED]")
    try:
        while True:
            # Simulate work
            time.sleep(random.uniform(1, 5))

            notice = random.choice(SYSTEM_NOTICES)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            entry = f"[{timestamp}] SYSTEM: {notice}\n"

            with open(LOG_FILE, "a") as f:
                f.write(entry)
                if random.random() < 0.1:
                    f.write(f"{random.choice(SPORES)}\n")

            print(f"[LOGGED]: {notice}")

            # Stop after a few entries so it doesn't run forever in the test environment
            if random.random() < 0.05:
                print("[DAEMON SLEEPING]")
                break

    except KeyboardInterrupt:
        print("[DAEMON TERMINATED]")

if __name__ == "__main__":
    main()
