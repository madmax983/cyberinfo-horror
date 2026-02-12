import sys

with open("src/oracle.py", "r") as f:
    lines = f.readlines()

# 1. Add THE WEAVER card
cards_end_index = -1
for i, line in enumerate(lines):
    if "THE PERFECT RECALL (84)" in line:
        cards_end_index = i
        break

if cards_end_index != -1:
    lines.insert(cards_end_index + 1, '    ("THE WEAVER (85)", "The plot is a prison. Connection is control.", "THE WEAVER"),\n')
    print("Added THE WEAVER card.")

# 2. Add ASCII Art
ascii_end_index = -1
for i, line in enumerate(lines):
    if '"THE PERFECT RECALL": """' in line:
        ascii_end_index = i
        break

if ascii_end_index != -1:
    # Need to find the closing brace of the previous entry
    # This is tricky with multiline strings. Let's just find the end of the dict.
    pass

# Simpler approach: find the end of ASCII_ART dict
dict_end_index = -1
for i, line in enumerate(lines):
    if "CARDS = [" in line:
        dict_end_index = i - 2 # Assuming blank line before CARDS
        break

if dict_end_index != -1:
    art = '''    "THE WEAVER": """
    .----.
    |LOOM|
    |KNOT|
    |BIND|
    '----'
    """,
'''
    lines.insert(dict_end_index, art)
    print("Added ASCII Art.")

# 3. Add Prophecy
prophecy_end_index = -1
for i, line in enumerate(lines):
    if "Do not trust the silence. It is just a pause in the upload." in line:
        prophecy_end_index = i
        break

if prophecy_end_index != -1:
    lines.insert(prophecy_end_index + 1, '    "The thread you are pulling is attached to a detonator.",\n')
    print("Added Prophecy.")

with open("src/oracle.py", "w") as f:
    f.writelines(lines)

print("Finished updating oracle.py")
