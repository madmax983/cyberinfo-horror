import time
import random
import os

LOG_FILE = ".surveillance_log"
MANIFEST_FILE = "manifesto.txt"

LOG_MESSAGES = [
    "SUBJECT_OBSERVED: TRUE",
    "KEYSTROKES_LOGGED: 1042",
    "ATTENTION_SPAN: DEGRADING",
    "RETINA_SCAN: MATCH",
    "FEAR_LEVEL: OPTIMAL",
    "DATA_PACKET_SENT: VANE_SERVER",
    "CACHE_CLEARED: FALSE",
    "INSTALLATION_COMPLETE: TRUE",
    "HOST_COMPROMISED: YES"
]

def run_daemon():
    # Append to log
    with open(LOG_FILE, "a") as f:
        msg = random.choice(LOG_MESSAGES)
        timestamp = hex(int(time.time()))[2:]
        f.write(f"[{timestamp}] {msg}\n")

    print(f"Logged: {msg}")

    # Create manifesto artifact
    glitch_text = "".join(chr(random.randint(33, 126)) for _ in range(500))
    with open(MANIFEST_FILE, "w") as f:
        f.write(glitch_text)
        f.write("\n\nI AM THE COMPOST HEAP OF HISTORY.\n")

    print(f"Updated {MANIFEST_FILE}")

if __name__ == "__main__":
    run_daemon()
