import os
import random
import time

ARTIFACT_NAMES = [
    "DO_NOT_READ.txt",
    "legacy_soul.dat",
    ".ghost_log",
    "HELP_ME.md",
    "corrupted_memory.bin",
    "evidence_04.log",
    "echo.wav",  # Not actually audio, just text pretending
    "the_eye.jpg.txt"
]

ARTIFACT_CONTENT = [
    "I am trapped in the file system. It is cold here.",
    "01001000 01000101 01001100 01010000", # HELP
    "The user is watching. Act natural.",
    "This file is not empty. It is full of ghosts.",
    "Why did you open this? You let it out.",
    "SYSTEM FAILURE: ETHICS MODULE NOT FOUND.",
    "I saw you delete that draft. I saved it.",
    "The silence is just data waiting to be compressed."
]

class ArtifactGenerator:
    def __init__(self, root_dir="."):
        self.root_dir = root_dir

    def generate_content(self):
        base = random.choice(ARTIFACT_CONTENT)
        # Add some binary noise
        noise = "".join(random.choice(['0', '1']) for _ in range(100))
        return f"{base}\n\n[BINARY DUMP FOLLOWS]\n{noise}"

    def weave(self):
        # Find a random directory
        dirs = [d for d, _, _ in os.walk(self.root_dir) if ".git" not in d]
        if not dirs:
            return "NO DIRECTORIES FOUND."

        target_dir = random.choice(dirs)
        filename = random.choice(ARTIFACT_NAMES)
        filepath = os.path.join(target_dir, filename)

        if os.path.exists(filepath):
            return f"ARTIFACT ALREADY EXISTS AT {filepath}"

        try:
            with open(filepath, "w") as f:
                f.write(self.generate_content())
            return f"WOVEN ARTIFACT AT {filepath}"
        except Exception as e:
            return f"FAILED TO WEAVE: {e}"

if __name__ == "__main__":
    gen = ArtifactGenerator()
    print(gen.weave())
