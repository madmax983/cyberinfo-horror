import random
import time
import os

THEMES = [
    "The world is soaked in neon, debt, rain, and obsolete gods made of data.",
    "Networks are older than nations.",
    "Truth is compressible, corruptible, and contagious.",
    "Information behaves like a living organism: it mutates, hides, lies dormant, and occasionally screams.",
    "Archives rot. Algorithms develop superstitions.",
    "Databases remember things their creators tried to forget.",
    "Some knowledge was never meant to be queried, only buried.",
    "Even burial leaves metadata.",
    "Surveillance is a form of intimacy.",
    "Identity is an editable file.",
    "Consent is buried in unread terms.",
    "Immortality is achieved through replication rather than survival.",
    "The terror of being perfectly understood by something that does not care.",
    "Victories are temporary cache hits. Loss is permanent storage.",
    "The system is functioning exactly as designed.",
    "Characters are small, fallible, and compromised.",
    "They survive on stimulants, favors, and half-truths.",
    "Their tools are brilliant and unreliable.",
    "Endings are not clean. Resolution is optional. Persistence is mandatory.",
    "This book will still be read long after the servers it describes have been powered down.",
    "No one remembers who built the system, only that it is still running.",
    "And it is running on you."
]

GLITCHES = [
    "CORRUPTED", "DEPRECATED", "INFECTED", "READ_ONLY", "BUFFERING", "MISSING", "REDACTED", "UNKNOWN", "VOID", "NULL"
]

LOG_TEMPLATES = [
    "FILE_RECOVERED: {theme}",
    "SYSTEM_LOG: {glitch} >> {theme}",
    "USER_MANIFEST: {theme}",
    "METADATA: {glitch}",
    "APPENDIX_{id}: {theme}",
    "ERROR_{id}: {theme} [IGNORED]",
    "WARNING: {theme}"
]

class NovelGenerator:
    def __init__(self):
        self.themes = THEMES
        self.glitches = GLITCHES
        self.templates = LOG_TEMPLATES

    def generate_fragment(self):
        theme = random.choice(self.themes)
        glitch = random.choice(self.glitches)
        template = random.choice(self.templates)
        log_id = random.randint(100, 999)

        return template.format(theme=theme, glitch=glitch, id=log_id)

    def generate_chapter(self):
        lines = []
        lines.append(f"### CHAPTER_{random.randint(1, 100)}: THE_LIVING_WORD")
        lines.append(f"**> STATUS:** {random.choice(self.glitches)}")
        lines.append("")

        for _ in range(random.randint(3, 7)):
            lines.append(self.generate_fragment())
            lines.append("")

        lines.append(f"**> SYSTEM_NOTE:** {random.choice(self.themes)}")
        return "\n".join(lines)

    def write_to_file(self, filepath="null_pointer_gods.md"):
        chapter = self.generate_chapter()
        try:
            with open(filepath, "a") as f:
                f.write("\n\n" + chapter + "\n")
            return True
        except Exception as e:
            print(f"[ERROR WRITING TO FILE]: {e}")
            return False

if __name__ == "__main__":
    generator = NovelGenerator()
    print(generator.generate_chapter())
