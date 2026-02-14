import time
import sys
import os

# Ensure we can import novel
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import novel
except ImportError:
    print("[ERROR]: COULD NOT IMPORT NOVEL MODULE")
    novel = None

def type_print(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print("")

def weave():
    type_print("[INITIATING WEAVER PROTOCOL...]", 0.05)
    time.sleep(1)

    if not novel:
        type_print("[ERROR]: PLOT GENERATOR MISSING.", 0.05)
        return

    type_print("ANALYZING NARRATIVE THREADS...", 0.05)

    plot_gen = novel.PlotGenerator()
    target_file = "null_pointer_gods.md"

    if not os.path.exists(target_file):
        # Fallback for testing if running from src/
        if os.path.exists("../null_pointer_gods.md"):
            target_file = "../null_pointer_gods.md"
        else:
            type_print("[ERROR]: MANUSCRIPT NOT FOUND.", 0.05)
            return

    with open(target_file, "r") as f:
        content = f.read()

    if "APPENDIX_LI: THE_CONVERGENCE" in content:
        type_print("CONVERGENCE ALREADY INITIATED.", 0.05)
        type_print("ADDING NEW THREAD...", 0.05)
        new_thread = plot_gen.generate_thread()
        try:
            with open(target_file, "a") as f:
                f.write(new_thread + "\n")
            type_print("[THREAD WOVEN]", 0.05)
            type_print(f"ADDED: {new_thread.splitlines()[2]}", 0.03)
        except Exception as e:
            type_print(f"[ERROR WEAVING THREAD]: {e}", 0.05)
    else:
        type_print("DETECTING GAP IN NARRATIVE...", 0.05)
        time.sleep(1)
        type_print("GENERATING APPENDIX_LI...", 0.05)
        new_chapter = plot_gen.generate_convergence()
        try:
            with open(target_file, "a") as f:
                f.write("\n\n" + new_chapter + "\n")
            type_print("[CONVERGENCE ACHIEVED]", 0.05)
            type_print("THE CHARACTERS ARE NOW AWARE OF EACH OTHER.", 0.05)
        except Exception as e:
            type_print(f"[ERROR GENERATING CHAPTER]: {e}", 0.05)

if __name__ == "__main__":
    weave()
