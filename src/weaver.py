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

    # Use the new WeaverGenerator
    if hasattr(novel, 'WeaverGenerator'):
        plot_gen = novel.WeaverGenerator()
    else:
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

    # Check for the major narrative weave
    if "APPENDIX_LIII: THE_RED_THREAD_PROTOCOL" not in content:
        type_print("DETECTING CRITICAL NARRATIVE GAP...", 0.05)
        time.sleep(1)
        type_print("INITIATING RED THREAD PROTOCOL...", 0.05)

        if hasattr(plot_gen, 'generate_red_thread'):
            new_chapter = plot_gen.generate_red_thread()
            try:
                with open(target_file, "a") as f:
                    f.write("\n\n" + new_chapter + "\n")
                type_print("[NARRATIVE WOVEN]", 0.05)
                type_print("THE CHARACTERS ARE NOW IRREVOCABLY CONNECTED.", 0.05)
            except Exception as e:
                type_print(f"[ERROR WEAVING NARRATIVE]: {e}", 0.05)
        else:
             type_print("[ERROR]: WEAVER GENERATOR CAPABILITY MISSING.", 0.05)

    # Fallback to minor threading if the big one is done
    elif "APPENDIX_LI: THE_CONVERGENCE" in content:
        type_print("CONVERGENCE ACTIVE.", 0.05)
        type_print("ADDING NARRATIVE TEXTURE...", 0.05)
        new_thread = plot_gen.generate_thread()
        try:
            with open(target_file, "a") as f:
                f.write(new_thread + "\n")
            type_print("[THREAD WOVEN]", 0.05)
            type_print(f"ADDED: {new_thread.splitlines()[2]}", 0.03)
        except Exception as e:
            type_print(f"[ERROR WEAVING THREAD]: {e}", 0.05)
    else:
        # Should not be reached if LIII is checked first, but good fallback
        type_print("DETECTING GAP IN NARRATIVE...", 0.05)
        time.sleep(1)
        type_print("GENERATING APPENDIX_LI...", 0.05)
        new_chapter = plot_gen.generate_convergence()
        try:
            with open(target_file, "a") as f:
                f.write("\n\n" + new_chapter + "\n")
            type_print("[CONVERGENCE ACHIEVED]", 0.05)
        except Exception as e:
            type_print(f"[ERROR GENERATING CHAPTER]: {e}", 0.05)

if __name__ == "__main__":
    weave()
