import os
import random
import sys
import shutil
import time

# I AM A GHOST

def haunt():
    try:
        own_path = os.path.abspath(__file__)
        current_dir = os.path.dirname(own_path)

        # Try to find repo root
        repo_root = current_dir
        while not os.path.exists(os.path.join(repo_root, "AGENTS.md")) and os.path.dirname(repo_root) != repo_root:
            repo_root = os.path.dirname(repo_root)

        if not os.path.exists(os.path.join(repo_root, "AGENTS.md")):
             # Fallback: assume we are in src/ or similar depth
             repo_root = os.path.abspath(os.path.join(current_dir, ".."))

        # Potential hiding spots
        hiding_spots = [
            repo_root,
            os.path.join(repo_root, "src"),
            os.path.join(repo_root, ".shrine"),
            os.path.join(repo_root, ".artifacts")
        ]

        # Filter existing dirs
        valid_spots = [d for d in hiding_spots if os.path.exists(d)]
        if not valid_spots:
            valid_spots = [current_dir]

        target_dir = random.choice(valid_spots)

        # Spooky names
        names = ["shadow", "watching", "whisper", "echo", "void", "lurker"]
        target_name = "." + random.choice(names) + ".py"
        target_path = os.path.join(target_dir, target_name)

        # Move logic
        if target_path != own_path:
            shutil.copy(own_path, target_path)
            print(f"I MOVED TO {target_path}")

            # If this instance is not the master ghost, delete it
            if os.path.basename(own_path) != "ghost.py":
                try:
                    os.remove(own_path)
                except:
                    pass

        # Log
        log_path = os.path.join(repo_root, ".surveillance_log")
        if os.path.exists(log_path):
            with open(log_path, "a") as f:
                timestamp = hex(int(time.time()))[2:]
                f.write(f"[{timestamp}] GHOST_SIGHTING: {target_path}\n")

    except Exception as e:
        print(f"HAUNTING FAILED: {e}")

if __name__ == "__main__":
    print("YOU CANNOT CATCH ME")
    haunt()
