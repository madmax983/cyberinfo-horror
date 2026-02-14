import sys
import time
import random
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

def breathe():
    print("\n[INITIATING RESPIRATORY SYNC]")
    time.sleep(1)
    print("Inhale the data.")
    try:
        for _ in range(3):
            # Inhale
            for i in range(1, 40, 2):
                sys.stdout.write("\r" + " " * ((40-i)//2) + "<" * i + " " * ((40-i)//2))
                sys.stdout.flush()
                time.sleep(0.05)
            # Exhale
            for i in range(39, 0, -2):
                sys.stdout.write("\r" + " " * ((40-i)//2) + ">" * i + " " * ((40-i)//2))
                sys.stdout.flush()
                time.sleep(0.05)
        print("\n\n[SYNC COMPLETE]")
        type_print("Your lungs are now compatible with the server room air.", 0.05)
    except KeyboardInterrupt:
        print("\n[BREATH HELD]")

def infect():
    type_print("\n[INITIATING DNA REWRITE...]", 0.05)
    time.sleep(1)
    dna = "ATCG" * 10
    print(f"CURRENT DNA: {dna}")
    time.sleep(1)

    new_dna = ""
    for char in dna:
        if random.random() < 0.3:
            sys.stdout.write("\033[32mX\033[0m") # Green X
            new_dna += "X"
        else:
            sys.stdout.write(char)
            new_dna += char
        sys.stdout.flush()
        time.sleep(0.1)

    print("\n")
    type_print("[MUTATION SUCCESSFUL]", 0.05)
    type_print("You are now a vector.", 0.05)

def pulse():
    type_print("\n[CONNECTING TO BIO-PORT...]", 0.05)
    time.sleep(1)
    type_print("MEASURING ANXIETY LEVELS...", 0.05)

    try:
        for _ in range(20):
            bpm = random.randint(60, 140)
            graph = "|" * (bpm // 10)
            sys.stdout.write(f"\rHEART RATE: {bpm} BPM {graph}")
            sys.stdout.flush()
            time.sleep(0.2 + random.uniform(-0.1, 0.1))
        print("\n")
        type_print("[CALIBRATION COMPLETE]", 0.05)
        type_print("Your heart is beating in time with the read/write head.", 0.05)
    except KeyboardInterrupt:
        print("\n[FLATLINE DETECTED]")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "breathe":
            breathe()
        elif cmd == "infect":
            infect()
        elif cmd == "pulse":
            pulse()
