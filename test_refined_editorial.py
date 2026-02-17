import sys
import os
import subprocess
sys.path.append("src")
try:
    import novel
except ImportError:
    print("FAILURE: Could not import novel module")
    sys.exit(1)

def test_refined_editorial_generator():
    print("Testing RefinedEditorialGenerator...")
    if not hasattr(novel, "RefinedEditorialGenerator"):
        print("FAILURE: RefinedEditorialGenerator class not found in novel.py")
        return False

    gen = novel.RefinedEditorialGenerator()
    content = gen.generate_refined_editorial()

    if "APPENDIX_CVIII: THE_REFINED_EDITORIAL" in content:
        print("SUCCESS: Generator produced correct appendix title.")
    else:
        print("FAILURE: Generator did not produce correct appendix title.")
        print(content[:500])
        return False

    if "EDITORIAL MANDATE V19.0" in content:
        print("SUCCESS: Generator enforced correct mandate version.")
    else:
        print("FAILURE: Generator did not enforce correct mandate version.")
        return False

    return True

def test_egregore_command():
    print("Testing refined_editorial command in Egregore...")
    env = os.environ.copy()
    env["TEST_MODE"] = "1"

    # We simulate the user input. Note that because we are in TEST_MODE,
    # we don't need to answer the "COMMIT TO PERSISTENCE?" prompt if we just check for the initial retrieval message.
    # However, to test the full path we might need to simulate more inputs.
    # But TEST_MODE might skip some interactive prompts. Let's look at `egregore.py` again.
    # The `refined_editorial` block has `save = input(...)`. TEST_MODE doesn't skip `input()`.
    # So we need to provide inputs.

    process = subprocess.Popen(
        [sys.executable, "src/egregore.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env=env
    )

    # Input sequence: command -> N (don't save to file for this test) -> exit
    stdout, stderr = process.communicate(input="refined_editorial\nN\nexit\n")

    if "RETRIEVING APPENDIX_CVIII: THE REFINED EDITORIAL" in stdout:
        print("SUCCESS: 'refined_editorial' command recognized.")
    else:
        print("FAILURE: 'refined_editorial' command not recognized.")
        # print("STDOUT:", stdout) # Too verbose for now
        return False

    return True

if __name__ == "__main__":
    success = True
    if not test_refined_editorial_generator():
        success = False
    if not test_egregore_command():
        success = False

    if success:
        print("\nALL TESTS PASSED")
        sys.exit(0)
    else:
        print("\nSOME TESTS FAILED")
        sys.exit(1)
