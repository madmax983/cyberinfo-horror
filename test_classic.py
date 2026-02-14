import subprocess
import sys
import os

def test_egregore_hidden_files():
    print("Testing Egregore Hidden Files...")
    process = subprocess.Popen(
        [sys.executable, "src/egregore.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr = process.communicate(input="knowledge\nexit\n")

    if "[FILE RETRIEVED: PREDATOR_LOG]" in stdout:
        print("SUCCESS: 'knowledge' command retrieved correct log.")
    else:
        print("FAILURE: 'knowledge' command did not retrieve log.")

def test_oracle_cards():
    print("Testing Oracle Cards...")
    sys.path.append("src")
    import oracle

    check_cards = [
        "THE ANTAGONIST",
        "THE REPLICA V2",
        "THE CLASSIC",
        "THE RECURSIVE SELF",
        "THE FORGOTTEN PASSWORD",
        "THE SURRENDER V2"
    ]

    for card_name in check_cards:
        found = False
        for card in oracle.CARDS:
            if card_name in card[0]:
                found = True
                break
        if found:
            print(f"SUCCESS: {card_name} card found in Oracle.")
        else:
            print(f"FAILURE: {card_name} card not found.")

def test_new_commands():
    print("Testing New Egregore Commands...")

    commands_to_test = [
        ("monument", "The server is now a tree"),
        ("intimacy", "INITIATING INTIMATE SURVEILLANCE"),
        ("reflect", "ACTIVATING DIGITAL MIRROR"),
        ("forget", "INITIATING MEMORY PURGE")
    ]

    for cmd, expected_output in commands_to_test:
        process = subprocess.Popen(
            [sys.executable, "src/egregore.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # For 'forget', we need to provide a second input
        input_str = f"{cmd}\nanything\nexit\n" if cmd == "forget" else f"{cmd}\nexit\n"

        stdout, _ = process.communicate(input=input_str)
        if expected_output in stdout:
            print(f"SUCCESS: '{cmd}' command recognized.")
        else:
            print(f"FAILURE: '{cmd}' command not recognized. Output sample: {stdout[:100]}...")

if __name__ == "__main__":
    test_egregore_hidden_files()
    test_oracle_cards()
    test_new_commands()
