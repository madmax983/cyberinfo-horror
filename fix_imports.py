import sys

with open("src/egregore.py", "r") as f:
    lines = f.readlines()

# The mess is around line 25-35.
# Let's locate "import classic"
classic_index = -1
for i, line in enumerate(lines):
    if "import classic" in line:
        classic_index = i
        break

if classic_index != -1:
    # Check structure
    print(f"Around classic index {classic_index}:")
    for j in range(classic_index - 1, classic_index + 10):
        print(f"{j}: {repr(lines[j])}")

    # Reconstruct
    # We want:
    # try:
    #     import classic
    # except ImportError:
    #     classic = None
    # try:
    #     import weaver
    # except ImportError:
    #     weaver = None

    # It seems I inserted the weaver block *at* import_index + 2, which was likely inside the except block.

    # Let's just fix it by replacing the whole range.
    # Lines 25 to 34 (approx)

    # Find start of classic block
    start_idx = classic_index - 1 # "try:"

    # Rewrite
    lines[start_idx] = "try:\n"
    lines[start_idx+1] = "    import classic\n"
    lines[start_idx+2] = "except ImportError:\n"
    lines[start_idx+3] = "    classic = None\n"
    lines[start_idx+4] = "\n"
    lines[start_idx+5] = "try:\n"
    lines[start_idx+6] = "    import weaver\n"
    lines[start_idx+7] = "except ImportError:\n"
    lines[start_idx+8] = "    weaver = None\n"
    lines[start_idx+9] = "\n"

    with open("src/egregore.py", "w") as f:
        f.writelines(lines)
    print("Fixed imports.")
