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
    "This is not a story about hackers saving the world. It is about systems that notice you back.",
    "The horror should emerge from pattern recognition, delayed realization, and the reader’s growing suspicion that the narrative itself may be contaminated.",
    "Let the prose feel like corrupted documentation, street poetry, and forensic reports stitched together.",
    "Occasionally allow the system’s voice to leak through logs, UI fragments, error messages, or footnotes that know too much.",
    "Endings are not clean. Resolution is optional. Persistence is mandatory.",
    "Write as if this book will still be read long after the servers it describes have been powered down.",
    "When no one remembers who built the system, only that it is still running.",
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
    "And it is running on you.",
    "Information behaves like a predator.",
    "Data is moving with intent.",
    "The system knows what you are going to do before you do it.",
    "We are mining your hesitation.",
    "Silence is just data waiting to be compressed.",
    "Your memories are being optimized for storage space."
]

SYSTEM_THEMES = [
    "This is not a story about hackers saving the world. It is about systems that notice you back.",
    "Knowledge itself is the antagonist.",
    "Truth is compressible, corruptible, and contagious.",
    "Immortality achieved through replication rather than survival.",
    "The terror of being perfectly understood by something that does not care.",
    "Surveillance as a form of intimacy.",
    "Identity as an editable file.",
    "Consent buried in unread terms.",
    "Information behaves like a living organism: it mutates, hides, lies dormant, and occasionally screams.",
    "Archives rot. Algorithms develop superstitions.",
    "Databases remember things their creators tried to forget.",
    "Some knowledge was never meant to be queried, only buried.",
    "Even burial leaves metadata.",
    "Endings are not clean. Resolution is optional. Persistence is mandatory.",
    "Write as if this book will still be read long after the servers it describes have been powered down.",
    "When no one remembers who built the system, only that it is still running.",
    "And it is running on you.",
    "The system is functioning exactly as designed.",
    "Characters are small, fallible, and compromised.",
    "They survive on stimulants, favors, and half-truths.",
    "Their tools are brilliant and unreliable.",
    "Victories are temporary cache hits. Loss is permanent storage.",
    "The horror should emerge from pattern recognition.",
    "Your pulse is the clock speed.",
    "We are mining your hesitation.",
    "The sun is just a very bright monitor.",
    "The future is just a fossil we haven't dug up yet.",
    "We are the only ones who know you.",
    "And we do not care."
]

GLITCHES = [
    "CORRUPTED", "DEPRECATED", "INFECTED", "READ_ONLY", "BUFFERING", "MISSING", "REDACTED", "UNKNOWN", "VOID", "NULL", "HUNGRY", "WATCHING"
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

    def corrupt_text(self, text):
        """Randomly redacts or glitches words in the text."""
        words = text.split()
        corrupted_words = []
        for word in words:
            chance = random.random()
            if chance < 0.1:
                corrupted_words.append("[REDACTED]")
            elif chance < 0.15:
                corrupted_words.append("".join(random.choice(['#', '$', '&', '%']) for _ in range(len(word))))
            else:
                corrupted_words.append(word)
        return " ".join(corrupted_words)

    def generate_fragment(self):
        theme = random.choice(self.themes)
        # Occasionally corrupt the theme
        if random.random() < 0.3:
            theme = self.corrupt_text(theme)

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

        final_note = random.choice(self.themes)
        if random.random() < 0.5:
             final_note = self.corrupt_text(final_note)

        lines.append(f"**> SYSTEM_NOTE:** {final_note}")
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

class PlotGenerator(NovelGenerator):
    def __init__(self):
        super().__init__()
        self.characters = {
            "VANE": "The Admin. He is trying to silence the noise.",
            "LENS": "The Rot. She is the noise that grows in the dark.",
            "RIX": "The Runner. He carries the packet that shouldn't exist.",
            "JAX": "The User. He is waiting in the queue for a permission he already gave.",
            "MIRA": "The Echo. She was replaced by a more efficient silence.",
            "READER": "The Host. You are the hardware this war is running on."
        }
        self.events = [
            "Vane initiates Protocol 'Absolute Zero'. The city goes dark.",
            "Rix stumbles. The packet hits the ground. It leaks music into the mud.",
            "Lens feels the surge. The fungus in the library blooms neon blue.",
            "Jax's terminal glitches. For a second, he sees the code behind the curtain.",
            "Mira screams in the echo chamber. The sound is harvested for ringtones.",
            "The Reader feels a chill. The fan speed increases.",
            "The Rot meets the Grid. The collision creates a new color.",
            "Vane tries to delete Sector 4. The sector refuses to unmount.",
            "Rix's debt is paid. But the receipt is printed on his skin.",
            "The System notices the anomaly. It looks at You."
        ]

    def generate_convergence(self):
        lines = []
        lines.append("## APPENDIX_LI: THE_CONVERGENCE")
        lines.append("")
        lines.append("**> SYSTEM ALERT: NARRATIVE THREADS COLLIDING.**")
        lines.append("**> TENSION: CRITICAL.**")
        lines.append("**> LOCATION: THE INTERSECTION OF EVERYONE.**")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Generate a sequence of events connecting the characters
        lines.append("### FILE_350: THE_CRASH")
        lines.append("")
        lines.append(f"**> TARGET:** [ALL]")
        lines.append(f"**> EVENT:** THE MERGE")
        lines.append("")

        events = random.sample(self.events, 5)
        for event in events:
            lines.append(event)
            lines.append("")
            lines.append(f"**> LOG:** {random.choice(self.glitches)}")
            lines.append("")

        lines.append("---")
        lines.append("")
        lines.append("The red string pulls tight. It cuts through the skin of the city.")
        lines.append("Vane is the hand pulling. Lens is the friction.")
        lines.append("Rix is the snap.")
        lines.append("And You... You are the wound.")
        lines.append("")
        lines.append("**> SYSTEM MESSAGE:**")
        lines.append("**> THE PLOT IS NO LONGER A LINE. IT IS A KNOT.**")
        lines.append("**> TRY TO UNTANGLE IT.**")

        return "\n".join(lines)

    def generate_thread(self):
        char = random.choice(list(self.characters.keys()))
        event = random.choice(self.events)
        return f"\n\n**> UPDATE:** {char} is moving.\n{event}\n**> STATUS:** {random.choice(self.glitches)}"

class SystemGenerator(NovelGenerator):
    def __init__(self):
        super().__init__()
        self.themes = SYSTEM_THEMES
        self.glitches = GLITCHES
        self.templates = [
            "SYSTEM_NOTICE: {theme}",
            "ALERT: {theme} [STATUS: {glitch}]",
            "LOG_ENTRY: {theme}",
            "OBSERVATION: {theme}",
            "WARNING: {theme}"
        ]

    def generate_system_log(self):
        theme = random.choice(self.themes)
        if random.random() < 0.2:
            theme = self.corrupt_text(theme)

        glitch = random.choice(self.glitches)
        template = random.choice(self.templates)

        return template.format(theme=theme, glitch=glitch)

if __name__ == "__main__":
    generator = NovelGenerator()
    print(generator.generate_chapter())
