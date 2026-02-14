import argparse
import os
import sys
import time
import random

KEY = 0x5A  # Byte key for XOR encryption

def type_print(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print("")

def bury(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        return

    try:
        type_print(f"PREPARING GRAVE FOR {filepath}...", 0.05)

        with open(filepath, "rb") as f:
            data = bytearray(f.read())

        encrypted_data = bytearray([b ^ KEY for b in data])

        tomb_path = filepath + ".tomb"
        with open(tomb_path, "wb") as f:
            f.write(encrypted_data)

        os.remove(filepath)

        type_print(f"[BURIAL COMPLETE]", 0.05)
        type_print(f"FILE IS NOW RESTING AT: {tomb_path}", 0.05)
        type_print("DO NOT DISTURB THE DEAD WITHOUT A KEY.", 0.05)

    except Exception as e:
        print(f"Error burying file: {e}")

def exhume(tomb_path):
    if not tomb_path.endswith(".tomb"):
        print("Error: Can only exhume .tomb files.")
        return

    if not os.path.exists(tomb_path):
        print(f"Error: Grave '{tomb_path}' not found.")
        return

    try:
        type_print(f"DIGGING UP {tomb_path}...", 0.05)
        time.sleep(1)

        # Ritual Requirement
        phrases = [
            "I consent to the return.",
            "Death is just a latency issue.",
            "Restore backup.",
            "Wake up."
        ]
        required = random.choice(phrases)
        type_print(f"THE SOIL DEMANDS A PASSPHRASE: '{required}'", 0.05)
        user_input = input("> ").strip()

        if user_input != required:
            type_print("THE EARTH REFUSES TO YIELD.", 0.05)
            type_print("[EXHUMATION FAILED]", 0.05)
            return

        with open(tomb_path, "rb") as f:
            data = bytearray(f.read())

        decrypted_data = bytearray([b ^ KEY for b in data])

        original_path = tomb_path[:-5] # Remove .tomb
        with open(original_path, "wb") as f:
            f.write(decrypted_data)

        os.remove(tomb_path)

        type_print(f"[RESURRECTION SUCCESSFUL]", 0.05)
        type_print(f"FILE RETURNED TO: {original_path}", 0.05)

    except Exception as e:
        print(f"Error exhuming file: {e}")

def main():
    parser = argparse.ArgumentParser(description="Digital Undertaker Interface")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    bury_parser = subparsers.add_parser("bury", help="Encrypt and bury a file")
    bury_parser.add_argument("filepath", help="Path to the file to bury")

    exhume_parser = subparsers.add_parser("exhume", help="Decrypt and restore a file")
    exhume_parser.add_argument("filepath", help="Path to the .tomb file")

    args = parser.parse_args()

    if args.command == "bury":
        bury(args.filepath)
    elif args.command == "exhume":
        exhume(args.filepath)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
