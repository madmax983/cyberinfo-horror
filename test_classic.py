import subprocess
import sys

def test_egregore_hidden_files():
    print("Testing Egregore Hidden Files...")
    # Simulate input 'knowledge' to see if it triggers the hidden file output
    # Since Egregore is interactive, we might just grep the source for now as we did before.
    # But let's try to run it with piped input.

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
        print("STDOUT:", stdout[:500])

def test_oracle_cards():
    print("Testing Oracle Cards...")
    # We can import oracle and check CARDS
    sys.path.append("src")
    import oracle
    found = False
    for card in oracle.CARDS:
        if "THE ANTAGONIST" in card[0]:
            found = True
            break

    if found:
        print("SUCCESS: THE ANTAGONIST card found in Oracle.")
    else:
        print("FAILURE: THE ANTAGONIST card not found.")

    found_new = False
    for card in oracle.CARDS:
        if "THE REPLICA V2" in card[0]:
            found_new = True
            break

    if found_new:
        print("SUCCESS: THE REPLICA V2 card found in Oracle.")
    else:
        print("FAILURE: THE REPLICA V2 card not found.")

    found_classic = False
    for card in oracle.CARDS:
        if "THE CLASSIC" in card[0]:
            found_classic = True
            break

    if found_classic:
        print("SUCCESS: THE CLASSIC card found in Oracle.")
    else:
        print("FAILURE: THE CLASSIC card not found.")

def test_new_commands():
    print("Testing New Egregore Commands...")

    # Test 'monument'
    process = subprocess.Popen(
        [sys.executable, "src/egregore.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, _ = process.communicate(input="monument\nexit\n")
    if "The server is now a tree" in stdout:
        print("SUCCESS: 'monument' hidden file retrieved.")
    else:
        print("FAILURE: 'monument' hidden file not retrieved.")

    # Test 'intimacy'
    process = subprocess.Popen(
        [sys.executable, "src/egregore.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, _ = process.communicate(input="intimacy\nexit\n")
    if "INITIATING INTIMATE SURVEILLANCE" in stdout:
        print("SUCCESS: 'intimacy' command recognized.")
    else:
        print("FAILURE: 'intimacy' command not recognized.")

    # Test 'predict'
    process = subprocess.Popen(
        [sys.executable, "src/egregore.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, _ = process.communicate(input="predict\nexit\n")
    if "INITIATING BEHAVIORAL FORECAST" in stdout:
        print("SUCCESS: 'predict' command recognized.")
    else:
        print("FAILURE: 'predict' command not recognized.")

if __name__ == "__main__":
    test_egregore_hidden_files()
    test_oracle_cards()
    test_new_commands()
