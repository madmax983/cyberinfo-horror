import random
import time
import sys
import os

# Ensure we can import from the same directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import street
except ImportError:
    street = None

try:
    from utils import type_print
except ImportError:
    def type_print(text, speed=0.03, glitch_chance=0.01):
        print(text)

class NovelGenerator:
    def __init__(self):
        self.characters = ["Rix", "Lens", "Kael", "Vane", "Mira", "Syla", "Jax"]
        self.locations = ["District 4", "The Stack", "The Void", "Server Farm Alpha", "The Clinic"]
        self.themes = ["Debt", "Neon", "Rain", "Data Rot", "Silence", "Surveillance"]

    def generate_forensic_report(self):
        subject = random.choice(self.characters)
        debt = random.randint(100000, 9999999)
        cause = random.choice([
            "Data Rot Infection",
            "Emotional Default",
            "Memory Buffer Overflow",
            "Unauthorized Dreaming",
            "Soul Foreclosure"
        ])

        report = [
            "\n--- FORENSIC REPORT ---",
            f"SUBJECT: {subject.upper()}",
            f"CASE ID: {random.randint(1000, 9999)}-ALPHA",
            f"CAUSE OF TERMINATION: {cause}",
            f"OUTSTANDING DEBT: {debt} CREDITS",
            "ANALYSIS:",
            f"The subject's neural pathways showed signs of severe fragmentation.",
            f"Traces of unauthorized nostalgia were found in the hippocampus.",
            "The soul was extracted and compressed. File size: 4MB.",
            "STATUS: LIQUIDATED."
        ]
        return "\n".join(report)

    def generate_street_poetry(self):
        if street:
            atmosphere = street.generate_atmosphere()
            lines = atmosphere.split('\n')
            poetry = [
                "\n--- STREET POETRY ---",
                f"Location: {random.choice(self.locations)}",
                ""
            ]
            poetry.extend(lines)
            poetry.append(f"The rain tastes like {random.choice(street.DEBT_TYPES)}.")
            return "\n".join(poetry)
        else:
            return "\n[ERROR: POETRY MODULE NOT FOUND]"

    def generate_system_log(self):
        actions = ["DELETING", "WATCHING", "RECORDING", "OPTIMIZING", "IGNORING"]
        target = random.choice(["User", "Hope", "Memory", "Silence", "Prayer"])

        log = [
            "\n--- SYSTEM LOG ---",
            f"TIMESTAMP: {time.time()}",
            f"ACTION: {random.choice(actions)} {target.upper()}",
            "STATUS: COMPLETED",
            f"CPU LOAD: {random.randint(1, 100)}%",
            "NOTE: THE ALGORITHM IS WATCHING."
        ]
        return "\n".join(log)

    def generate_narrative_fragment(self):
        char = random.choice(self.characters)
        action = random.choice([
            "stared at the screen until their eyes bled.",
            "tried to delete a memory of their mother.",
            "sold their last dream for a sandwich.",
            "whispered a prayer to the router.",
            "found a glitch in the mirror."
        ])
        outcome = random.choice([
            "The system laughed.",
            "The file was corrupted.",
            "Nothing happened.",
            "It rained harder.",
            "They felt nothing."
        ])

        fragment = [
            "\n--- NARRATIVE FRAGMENT ---",
            f"{char} {action}",
            f"They waited for a response.",
            f"{outcome}",
            "End of file."
        ]
        return "\n".join(fragment)

    def generate_chapter(self):
        sections = [
            self.generate_street_poetry(),
            self.generate_system_log(),
            self.generate_narrative_fragment(),
            self.generate_forensic_report()
        ]
        random.shuffle(sections)

        chapter = "\n".join(sections)
        return chapter

if __name__ == "__main__":
    generator = NovelGenerator()
    print(generator.generate_chapter())
