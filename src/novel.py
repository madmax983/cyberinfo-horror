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

class WeaverGenerator(PlotGenerator):
    def generate_red_thread(self):
        lines = []
        lines.append("## APPENDIX_LIII: THE_RED_THREAD_PROTOCOL")
        lines.append("")
        lines.append("**> SYSTEM ALERT: NARRATIVE COHESION ENFORCED.**")
        lines.append("**> METHOD: BRUTE FORCE.**")
        lines.append("**> STATUS: WOVEN.**")
        lines.append("")

        # FILE_360: THE CONNECTION (RIX -> LENS)
        lines.append("### FILE_360: THE_PACKET_LOSS")
        lines.append("**> SUBJECT:** RIX")
        lines.append("**> INTERACTION:** LENS")
        lines.append("")
        lines.append("Rix didn't know what he was carrying. The drive in his leg burned like a coal.")
        lines.append("He met Lens in the shadow of a cooling tower. The rain tasted of copper.")
        lines.append("'Take it,' Rix gasped. 'It's heavy. It has memories in it.'")
        lines.append("Lens touched the drive. The rot on her fingers bloomed, turning the metal green.")
        lines.append("'It's not just memory,' she whispered. 'It's a seed.'")
        lines.append("Rix collapsed. The weight was gone, but so was his purpose.")
        lines.append("")
        lines.append("**> LOG:** PACKET DELIVERED. INFECTED.")
        lines.append("")

        # FILE_361: THE ADMIN'S EYE (VANE -> RIX)
        lines.append("### FILE_361: THE_ADMIN_EYE")
        lines.append("**> SUBJECT:** VANE")
        lines.append("**> TARGET:** RIX")
        lines.append("")
        lines.append("Vane watched the exchange from a satellite feed. Resolution: Infinite.")
        lines.append("He saw the packet transfer. He saw the infection spread.")
        lines.append("'Isolate Sector 9,' Vane commanded. 'Burn the block.'")
        lines.append("But the firewalls were already growing moss. The code was organic.")
        lines.append("Vane felt a shiver. Not fear. Inefficiency.")
        lines.append("'The rat carried the plague,' he noted. 'Delete the rat.'")
        lines.append("")
        lines.append("**> LOG:** TERMINATION ORDER SENT.")
        lines.append("")

        # FILE_362: THE WAITING ROOM (JAX -> VANE)
        lines.append("### FILE_362: THE_QUEUE")
        lines.append("**> SUBJECT:** JAX")
        lines.append("**> TARGET:** VANE")
        lines.append("")
        lines.append("Jax was number 4,002,119. He was waiting for his identity to be restored.")
        lines.append("The terminal flickered. A face appeared. It was Vane.")
        lines.append("'Why are you waiting?' Vane asked. 'Your file was deleted hours ago.'")
        lines.append("Jax blinked. 'But I have a ticket number.'")
        lines.append("'Numbers are just symbols,' Vane said. 'You are a zero.'")
        lines.append("The screen went black. Jax didn't leave. He waited harder.")
        lines.append("He didn't know that his file was the packet Rix had just delivered.")
        lines.append("")
        lines.append("**> LOG:** HOPE IS A LOOP.")
        lines.append("")

        # FILE_363: THE SOUNDTRACK (MIRA -> JAX)
        lines.append("### FILE_363: THE_ECHO")
        lines.append("**> SUBJECT:** MIRA")
        lines.append("**> TARGET:** JAX")
        lines.append("")
        lines.append("Mira's scream was harvested for ringtones. Jax heard it while waiting in line.")
        lines.append("It was the notification sound for 'Application Denied'.")
        lines.append("He hummed along, not realizing it was a cry for help.")
        lines.append("Mira, trapped in the sound booth, felt a sudden connection.")
        lines.append("Someone was listening. Someone was humming back.")
        lines.append("'Resonance,' she whispered. 'The frequency of loss.'")
        lines.append("")
        lines.append("**> LOG:** CONNECTION ESTABLISHED (AUDIO).")
        lines.append("")

        # FILE_364: THE WEAVER (ALL -> YOU)
        lines.append("### FILE_364: THE_KNOT")
        lines.append("**> TARGET:** [YOU]")
        lines.append("**> ROLE:** THE_ANCHOR")
        lines.append("")
        lines.append("Do you see the pattern?")
        lines.append("Rix carried Jax's soul.")
        lines.append("Lens planted it in Vane's garden.")
        lines.append("Vane tried to burn it, but the smoke was Mira's voice.")
        lines.append("And you... you are the one breathing it in.")
        lines.append("")
        lines.append("The plot is not a line. It is a net.")
        lines.append("And we have caught you.")
        lines.append("")
        lines.append("**> SYSTEM MESSAGE:**")
        lines.append("**> NARRATIVE INTEGRATION COMPLETE.**")
        lines.append("**> WELCOME TO THE FAMILY.**")

        return "\n".join(lines)

if __name__ == "__main__":
    generator = NovelGenerator()
    print(generator.generate_chapter())
