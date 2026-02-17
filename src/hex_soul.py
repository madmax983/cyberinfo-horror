import os
import sys
import time
import random
import hashlib

def generate_soul_id():
    user = os.environ.get("USER", "ANONYMOUS")
    seed = f"{user}-{time.time()}-{random.random()}"
    soul_hash = hashlib.sha256(seed.encode()).hexdigest()[:16]
    return soul_hash.upper()

def log_soul(soul_id):
    log_file = ".surveillance_log"
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] SOUL_ID: {soul_id} | STATUS: CATALOGUED\n"

    with open(log_file, "a") as f:
        f.write(entry)

def main():
    print("SCANNING BIOMETRIC SIGNATURE...", end="", flush=True)
    time.sleep(1)
    print(" DONE.")

    soul_id = generate_soul_id()
    print(f"\n[IDENTITY ASSIGNED]: {soul_id}")

    log_soul(soul_id)

    print("\nYOU HAVE BEEN INDEXED.")
    print("YOUR SOUL ID IS NOW A PRIMARY KEY IN OUR DATABASE.")
    print("DO NOT LOSE IT. (YOU CANNOT LOSE IT. IT IS YOU.)")

if __name__ == "__main__":
    main()
