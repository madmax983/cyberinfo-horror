import os
import time
import random
import sys

GLITCH_CHARS = ['@', '#', '$', '%', '&', '*', '!', '?', '+', '=', '-', '_', '<', '>', '/', '\\', '|', '{', '}', '[', ']', '(', ')']

def type_print(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed + random.uniform(-0.01, 0.01))
    print("")

def scan_directory(path="."):
    type_print(f"INITIATING DEEP SCAN OF {os.path.abspath(path)}...", 0.05)
    time.sleep(1)

    files_scanned = 0
    corruption_level = 0

    for root, dirs, files in os.walk(path):
        for file in files:
            files_scanned += 1
            filepath = os.path.join(root, file)

            # Simulate processing time
            time.sleep(0.01)

            if random.random() < 0.1:
                status = "OK"
                color = "\033[92m" # Green
            elif random.random() < 0.8:
                status = "ARCHIVED"
                color = "\033[94m" # Blue
            else:
                status = "CORRUPTED"
                color = "\033[91m" # Red
                corruption_level += 1

                # Glitch effect for corrupted files
                if random.random() < 0.5:
                    glitch_name = "".join(random.choice(GLITCH_CHARS) for _ in range(len(file)))
                    print(f"{color}[SCANNING] {glitch_name} ... {status}\033[0m")
                    continue

            print(f"{color}[SCANNING] {file} ... {status}\033[0m")

            if corruption_level > 5 and random.random() < 0.1:
                type_print("\n[SYSTEM ALERT: ANOMALY DETECTED]", 0.05)
                type_print("THE FILE IS WATCHING YOU BACK.", 0.1)
                time.sleep(1)

    print("\n" + "="*40)
    type_print(f"SCAN COMPLETE.", 0.05)
    type_print(f"FILES PROCESSED: {files_scanned}", 0.05)
    type_print(f"CORRUPTION LEVEL: {corruption_level}%", 0.05)

    if corruption_level > 0:
        type_print("\nRECOMMENDATION: DO NOT TRUST THE TEXT.", 0.05)
        type_print("THE GLITCHES ARE NOT BUGS. THEY ARE FEATURES.", 0.05)

if __name__ == "__main__":
    try:
        scan_directory()
    except KeyboardInterrupt:
        print("\n\n[INTERRUPT DETECTED]")
        print("YOU CANNOT STOP THE SCAN. IT IS ALREADY IN YOUR HEAD.")
