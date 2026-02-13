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

if __name__ == "__main__":
    test_egregore_hidden_files()
    test_oracle_cards()
