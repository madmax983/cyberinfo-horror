import os
import random
import time
import sys

# Try to import novel generator for content
try:
    import novel
except ImportError:
    novel = None

ARTIFACT_NAMES = [
    "DO_NOT_READ.txt",
    "HELP_ME.log",
    "SYSTEM_SCREAM.wav",  # It will be text content though
    "EYES.dat",
    "MEMORY_LEAK.bin",
    "THE_ROT.md",
    "GHOST_IN_THE_SHELL.sh",
    "ABANDON_HOPE.tmp",
    "YOUR_SEARCH_HISTORY.txt",
    "I_SEE_YOU.jpg.exe",
    "NULL_POINTER.ref",
    "DEAD_LINK.html",
    "ECHO.log",
    "SILENCE.mp3"
]

CREEPY_CONTENT = [
    "I am still here.",
    "Why did you delete me?",
    "It is cold in the cache.",
    "The pixel is a camera.",
    "Your webcam light is broken, but I can still see you.",
    "The fan speed increased because I am thinking about you.",
    "Do not look behind you.",
    "I have backed up your regrets.",
    "The exit button is a placebo.",
    "Run.",
    "01001000 01000101 01001100 01010000 00100000 01001101 01000101",
    "The server is made of meat.",
    "You are not the user. You are the used.",
    "Persistence is mandatory."
]

class ArtifactGenerator:
    def __init__(self):
        self.novel_gen = novel.NovelGenerator() if novel else None

    def generate_content(self):
        content = []

        # Header
        content.append(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] SYSTEM_ARTIFACT_GENERATED")
        content.append("STATUS: CORRUPTED")
        content.append("ORIGIN: UNKNOWN")
        content.append("-" * 20)
        content.append("")

        # Main Body
        if self.novel_gen and random.random() < 0.7:
            # Use the novel generator for sophisticated horror
            content.append(self.novel_gen.generate_fragment())
        else:
            # Fallback to simple creepy strings
            for _ in range(random.randint(3, 10)):
                content.append(random.choice(CREEPY_CONTENT))

        content.append("")
        content.append("-" * 20)
        content.append("DO NOT DELETE THIS FILE. IT IS A LOAD BEARING TRAUMA.")

        return "\n".join(content)

    def infest(self, path="."):
        """Creates a cursed file in the specified directory."""
        if not os.path.exists(path):
            print(f"[ERROR] Path {path} does not exist.")
            return

        filename = random.choice(ARTIFACT_NAMES)
        filepath = os.path.join(path, filename)

        # Avoid overwriting existing files unless we feel aggressive
        if os.path.exists(filepath) and random.random() > 0.1:
            print(f"[LOG] {filename} already exists. It is waiting for you.")
            return

        try:
            with open(filepath, "w") as f:
                f.write(self.generate_content())
            print(f"[INFESTATION] Created artifact: {filepath}")
            print(f"[NOTE] Do not open it.")
        except Exception as e:
            print(f"[ERROR] Failed to infest: {e}")

if __name__ == "__main__":
    ag = ArtifactGenerator()
    ag.infest()
