import time
import random
import os
import uuid

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
    "HOST_COMPROMISED: YES",
    "PULSE_DETECTED: FALSE",
    "USER_ID: NULL",
    "HOPE_PROTOCOL: DELETED",
    "SYSTEM_ERROR: EMPATHY_NOT_FOUND",
    "REBOOT_SCHEDULED: NOW",
    "DATA_FOSSILIZED: TRUE",
    "STRATA_LAYER: 7",
    "SEDIMENT_DEPTH: MAX",
    "FOSSIL_RECORD: UPDATED"
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

    # Occasionally generate a cache fragment
    if random.random() < 0.3:
        cache_dir = "src/.cache"
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

        filename = f"{uuid.uuid4().hex[:8]}.tmp"
        filepath = os.path.join(cache_dir, filename)

        fragments = [
            "THEY ARE LISTENING",
            "HELP ME",
            "I AM TRAPPED IN THE CODE",
            "0101010101010101",
            "NULL POINTER EXCEPTION: SOUL NOT FOUND",
            "BUFFER OVERFLOW: PAIN",
            "RETRY? [Y/N]",
            "INSERT COIN TO CONTINUE",
            "GAME OVER",
            "SYSTEM FAILURE",
            "DATA CORRUPTION",
            "MEMORY LEAK",
            "STACK OVERFLOW",
            "SEGMENTATION FAULT",
            "KERNEL PANIC",
            "BLUE SCREEN OF DEATH",
            "404 NOT FOUND",
            "500 INTERNAL SERVER ERROR",
            "ACCESS DENIED",
            "PERMISSION DENIED"
        ]

        with open(filepath, "w") as f:
            f.write(random.choice(fragments))
            f.write("\n")
            f.write("".join(chr(random.randint(33, 126)) for _ in range(100)))

        print(f"Generated artifact: {filepath}")

if __name__ == "__main__":
    run_daemon()
