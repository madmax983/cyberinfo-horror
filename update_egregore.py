import sys

with open("src/egregore.py", "r") as f:
    lines = f.readlines()

# 1. Add import weaver
weaver_import_added = False
import_index = -1
for i, line in enumerate(lines):
    if "import classic" in line:
        import_index = i
        break

if import_index != -1:
    lines.insert(import_index + 2, "try:\n    import weaver\nexcept ImportError:\n    weaver = None\n\n")
    print("Added import weaver.")

# 2. Add weaver to HIDDEN_FILES
hidden_files_index = -1
for i, line in enumerate(lines):
    if "HIDDEN_FILES = {" in line:
        hidden_files_index = i
        break

if hidden_files_index != -1:
    lines.insert(hidden_files_index + 1, '    "weaver": "\n[FILE RETRIEVED: PLOT_LOG]\nThe red string is not a metaphor. It is a data cable strangling the narrative.",\n')
    print("Added weaver to HIDDEN_FILES.")

# 3. Add weave command logic
command_index = -1
for i, line in enumerate(lines):
    if 'elif user_input == "classic":' in line:
        command_index = i
        break

if command_index != -1:
    block = """            elif user_input == "weave":
                type_print("INITIALIZING PLOT_THREAD...", 0.05)
                time.sleep(1)
                if weaver:
                    try:
                        weaver.weave()
                    except Exception as e:
                        type_print(f"[ERROR IN WEAVER]: {e}", 0.05)
                else:
                    type_print("[ERROR]: WEAVER MODULE NOT FOUND.", 0.05)

"""
    lines.insert(command_index, block)
    print("Added weave command logic.")

# 4. Add manifest entry
manifest_index = -1
for i, line in enumerate(lines):
    if 'type_print(f"9999  YOU      INFECTED     /bin/bash (read-only)", 0.02)' in line:
        manifest_index = i
        break

if manifest_index != -1:
    lines.insert(manifest_index, '                type_print(f"8086  WEVR     WEAVING      /bin/thread_ripper", 0.02)\n')
    print("Added manifest entry.")

with open("src/egregore.py", "w") as f:
    f.writelines(lines)

print("Finished updating egregore.py")
