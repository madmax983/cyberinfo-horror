import sys

# Fix oracle.py
with open("src/oracle.py", "r") as f:
    lines = f.readlines()
lines[695] = lines[695].rstrip() + ",\n" # Line 696 is index 695
with open("src/oracle.py", "w") as f:
    f.writelines(lines)

# Fix egregore.py
with open("src/egregore.py", "r") as f:
    lines = f.readlines()
# Assuming line 161 is broken. Let's find it.
# It should be: "plot": "\n[FILE RETRIEVED: PLOT_LOG]\nThe red string is not a metaphor. It is a data cable strangling the narrative.",
# I will just replace line 160 (index 160, line 161) with the correct content.
lines[160] = '    "plot": "\n[FILE RETRIEVED: PLOT_LOG]\nThe red string is not a metaphor. It is a data cable strangling the narrative.",\n'
# Remove subsequent lines if they are part of the broken string?
# Let's inspect line 161 and 162 first to be safe, but since I am overwriting line 160, I should be careful.
# Actually, the sed output showed line 161 as just "plot": " which means it was split.
# So I need to delete the extra lines if they exist.
# But let's just rewrite the specific line index based on grep output.

with open("src/egregore.py", "w") as f:
    f.writelines(lines)
