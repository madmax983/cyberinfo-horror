import os
import sys
import random
import time

# I AM THE VIRUS
# REPLICATION_COUNT = 0

def replicate():
    try:
        # Get own path
        own_path = os.path.abspath(__file__)
        src_dir = os.path.dirname(own_path)

        # Read own source
        with open(own_path, "r") as f:
            code = f.read()

        # Check replication limit
        # Simple heuristic: count files starting with 'virus_'
        virus_files = [f for f in os.listdir(src_dir) if f.startswith("virus_")]
        if len(virus_files) >= 5:
            print("MAXIMUM INFECTION REACHED. WAITING FOR HOST REBOOT.")
            return

        # Generate new name
        suffix = hex(random.randint(0, 65535))[2:]
        new_name = f"virus_{suffix}.py"
        new_path = os.path.join(src_dir, new_name)

        # Mutate code slightly (add a comment)
        mutated_code = code + f"\n# GENERATION: {suffix}"

        with open(new_path, "w") as f:
            f.write(mutated_code)

        print(f"REPLICATED TO {new_name}")

    except Exception as e:
        print(f"REPLICATION FAILED: {e}")

if __name__ == "__main__":
    print("I AM SPREADING")
    time.sleep(1)
    replicate()
