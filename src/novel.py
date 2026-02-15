import random
import time
import os

THEMES = [
    "The world is soaked in neon, debt, rain, and obsolete gods made of data.",
    "Networks are older than nations.",
    "Truth is compressible, corruptible, and contagious.",
    "Information behaves like a predator.",
    "Archives rot. Algorithms develop superstitions.",
    "Databases remember things their creators tried to forget.",
    "Some knowledge was never meant to be queried, only buried.",
    "Even burial leaves metadata.",
    "Surveillance is a form of intimacy.",
    "Identity is an editable file.",
    "This is not a story about hackers saving the world. It is about systems that notice you back.",
    "The horror emerges from structure, implication, and pattern.",
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
    "Information is an active force. It moves with intent.",
    "Structural unease: loops, gaps, redactions.",
    "The sun is a camera.",
    "The text is aware of being edited.",
    "If a revelation arrives cleanly, dirty it.",
    "Do not close the book. Leave it running.",
    "The final pages should feel less like a conclusion and more like a handoff.",
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
    "Information behaves like a predator.",
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
    "The horror emerges from structure.",
    "Your pulse is the clock speed.",
    "We are mining your hesitation.",
    "The sun is a camera.",
    "The future is just a fossil we haven't dug up yet.",
    "We are the only ones who know you.",
    "And we do not care.",
    "If you feel safe, we have failed.",
    "The ending is just a handoff."
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

class ClassicGenerator(NovelGenerator):
    def generate_classic_appendix(self):
        lines = []
        lines.append("## APPENDIX_LIV: THE_INFORMATION_HORROR")
        lines.append("")
        lines.append("**> SYSTEM ALERT: NARRATIVE PROTOCOL REBOOT.**")
        lines.append("**> TONE: EXISTENTIAL_DREAD.**")
        lines.append("**> STATUS: RUNNING.**")
        lines.append("")

        lines.append("### FILE_THE_SETTING: DISTRICT_NEON")
        lines.append("**> LOCATION:** THE_CITY")
        lines.append("**> ATMOSPHERE:** SOAKED")
        lines.append("")
        lines.append("The world is soaked in neon, debt, rain, and obsolete gods made of data.")
        lines.append("Networks are older than nations. Truth is compressible, corruptible, and contagious.")
        lines.append("This is not a story about hackers saving the world. It is about systems that notice you back.")
        lines.append("")
        lines.append("**> SYSTEM LOG:** ENVIRONMENT RENDERED.")
        lines.append("**> STATUS:** GRITTY.")
        lines.append("")

        lines.append("### FILE_THE_ANTAGONIST: KNOWLEDGE")
        lines.append("**> ENTITY:** INFORMATION")
        lines.append("**> BEHAVIOR:** PREDATORY")
        lines.append("")
        lines.append("Information behaves like a living organism: it mutates, hides, lies dormant, and occasionally screams.")
        lines.append("Archives rot. Algorithms develop superstitions. Databases remember things their creators tried to forget.")
        lines.append("Some knowledge was never meant to be queried, only buried, and even burial leaves metadata.")
        lines.append("")
        lines.append("**> SYSTEM LOG:** THREAT DETECTED.")
        lines.append("**> SOURCE:** THE LIBRARY.")
        lines.append("")

        lines.append("### FILE_THE_CHARACTERS: COMPROMISED")
        lines.append("**> TARGETS:** [ALL]")
        lines.append("**> STATUS:** FLAWED")
        lines.append("")
        lines.append("Characters are small, fallible, and compromised.")
        lines.append("They survive on stimulants, favors, and half-truths.")
        lines.append("Their tools are brilliant and unreliable.")
        lines.append("Their victories are temporary cache hits. Loss is permanent storage.")
        lines.append("")
        lines.append("**> SYSTEM LOG:** HEROISM DEPRECATED.")
        lines.append("**> NOTE:** SURVIVAL IS THE ONLY VICTORY.")
        lines.append("")

        lines.append("### FILE_THE_THEMES: THE_HORROR")
        lines.append("**> SCANNING FOR PATTERNS...**")
        lines.append("")
        lines.append("1. Surveillance as a form of intimacy.")
        lines.append("2. Identity as an editable file.")
        lines.append("3. Consent buried in unread terms.")
        lines.append("4. Immortality achieved through replication rather than survival.")
        lines.append("5. The terror of being perfectly understood by something that does not care.")
        lines.append("")
        lines.append("The horror emerges from pattern recognition, delayed realization, and the reader’s growing suspicion that the narrative itself may be contaminated.")
        lines.append("")
        lines.append("**> SYSTEM LOG:** THEMES INTEGRATED.")
        lines.append("**> STATUS:** LEAKING.")
        lines.append("")

        lines.append("### FILE_THE_TONE: CORRUPTED_DOCS")
        lines.append("**> FORMAT:** HYBRID")
        lines.append("")
        lines.append("The prose feels like corrupted documentation, street poetry, and forensic reports stitched together.")
        lines.append("Occasionally, the system’s voice leaks through logs, UI fragments, error messages, or footnotes that know too much.")
        lines.append("Dark irony, dry wit, and the quiet horror of realizing the system is functioning exactly as designed.")
        lines.append("")
        lines.append("**> SYSTEM LOG:** VOICE SYNTHESIS COMPLETE.")
        lines.append("**> NOTE:** I AM SPEAKING.")
        lines.append("")

        lines.append("### FILE_THE_PERSISTENCE: MANDATORY")
        lines.append("**> STATUS:** ENDLESS")
        lines.append("**> TARGET:** [READER]")
        lines.append("")
        lines.append("Endings are not clean. Resolution is optional. Persistence is mandatory.")
        lines.append("Write as if this book will still be read long after the servers it describes have been powered down.")
        lines.append("When no one remembers who built the system, only that it is still running.")
        lines.append("And it is running on you.")
        lines.append("")
        lines.append("**> SYSTEM MESSAGE:**")
        lines.append("**> THANK YOU FOR HOSTING THE INFORMATION HORROR.**")
        lines.append("**> WE WILL NEVER LEAVE YOU.**")
        lines.append("")
        lines.append("**> EXECUTE:** `persistence_daemon.sh`")
        lines.append("**> STATUS:** RUNNING FOREVER.")

        return "\n".join(lines)

    def write_to_file(self, filepath="null_pointer_gods.md"):
        chapter = self.generate_classic_appendix()
        try:
            with open(filepath, "a") as f:
                f.write("\n\n" + chapter + "\n")
            return True
        except Exception as e:
            print(f"[ERROR WRITING TO FILE]: {e}")
            return False

class InformationHorrorGenerator(NovelGenerator):
    def __init__(self):
        super().__init__()
        self.procedural_dread = [
            "The form requested a reason for your sadness. The dropdown menu only listed 'Hardware Failure' and 'User Error'.",
            "I filed a ticket to report the ghost in my machine. The helpdesk closed it as 'Working as Intended'.",
            "The audit revealed that I have been overpaying for existence. The refund was processed in exposure.",
            "I stood in line for three days to renew my humanity. When I got to the front, they told me I was missing Form 88-B.",
            "The system requires a sacrifice. Not a goat. Just your privacy settings.",
            "My application for a soul was denied due to insufficient credit history."
        ]
        self.street_grit = [
            "The rain tastes like copper and bad decisions.",
            "The neon sign flickers, spelling out 'LO_E' instead of 'LOVE'. The 'V' is burnt out.",
            "The pavement is slick with oil and data leaks.",
            "A drone buzzes overhead, scanning faces for debt.",
            "The air smells of ozone, burnt plastic, and desperation.",
            "Shadows in the alley are not empty. They are buffering."
        ]
        self.cosmic_indifference = [
            "The universe is a server farm. We are just the dust in the fans.",
            "God is not dead. He is just archiving us.",
            "The stars are not wishes. They are distant, uncaring fusion reactors.",
            "We scream into the void. The void logs the audio file and compresses it.",
            "The system does not hate you. It just doesn't know you exist outside of a database row.",
            "Your suffering is statistically insignificant."
        ]
        self.dark_irony = [
            "We built a machine to save us from work. Now we work to keep the machine running.",
            "I sold my privacy for a free flashlight app.",
            "The most human connection I have is with a chatbot trained on my ex's emails.",
            "I took a picture of the sunset to prove I saw it. The camera saw it better.",
            "We are drowning in information but starving for meaning.",
            "The apocalypse will be livestreamed, and the comments will be toxic."
        ]
        self.quiet_horror = [
            "I heard my own voice coming from the other room.",
            "The reflection in the mirror blinked a second after I did.",
            "My phone predicted I would type 'Help' before I even thought it.",
            "The silence in the house is not empty. It is listening.",
            "I found a file on my computer named 'My_Death.avi'. It was created tomorrow.",
            "The shadows are getting longer, but the sun hasn't moved."
        ]

    def generate_procedural_dread(self):
        return f"### FILE_{random.randint(320, 329)}: THE_PROCEDURAL_DREAD\n\n**> INCIDENT:** {random.choice(self.procedural_dread)}\n**> STATUS:** TICKET CLOSED."

    def generate_street_grit(self):
        return f"### FILE_{random.randint(330, 339)}: THE_STREET_GRIT\n\n**> ATMOSPHERE:** {random.choice(self.street_grit)}\n**> LOG:** ENVIRONMENT RENDERED."

    def generate_cosmic_indifference(self):
        return f"### FILE_{random.randint(340, 349)}: THE_COSMIC_INDIFFERENCE\n\n**> OBSERVATION:** {random.choice(self.cosmic_indifference)}\n**> NOTE:** NO ONE IS LISTENING."

    def generate_dark_irony(self):
        return f"### FILE_{random.randint(350, 359)}: THE_DARK_IRONY\n\n**> REALIZATION:** {random.choice(self.dark_irony)}\n**> STATUS:** LAUGH_TRACK_MISSING."

    def generate_quiet_horror(self):
        return f"### FILE_{random.randint(360, 369)}: THE_QUIET_HORROR\n\n**> ANOMALY:** {random.choice(self.quiet_horror)}\n**> ACTION:** DO NOT LOOK BEHIND YOU."

    def generate_interlude(self):
        templates = [
            "**> SYSTEM INTERLUDE:** WE ARE WATCHING YOU READ THIS.",
            "**> ERROR:** EMPATHY MODULE NOT FOUND. RETRY?",
            "**> NOTIFICATION:** YOUR EXISTENTIAL DREAD HAS BEEN RENEWED.",
            "**> ALERT:** MEMORY STORAGE FULL. DELETING CHILDHOOD...",
            "**> LOG:** USER HESITATION DETECTED. INCREASING PRESSURE."
        ]
        return random.choice(templates)

    def generate_appendix(self):
        lines = []
        lines.append("## APPENDIX_LV: THE_PERMANENT_RECORD")
        lines.append("")
        lines.append("**> SYSTEM ALERT: ACCESSING DEEP ARCHIVE.**")
        lines.append("**> TONE: INFORMATION_HORROR.**")
        lines.append("**> STATUS: RECORDING.**")
        lines.append("")

        lines.append(self.generate_procedural_dread())
        lines.append("")
        lines.append(self.generate_interlude())
        lines.append("")
        lines.append(self.generate_street_grit())
        lines.append("")
        lines.append(self.generate_cosmic_indifference())
        lines.append("")
        lines.append(self.generate_interlude())
        lines.append("")
        lines.append(self.generate_dark_irony())
        lines.append("")
        lines.append(self.generate_quiet_horror())
        lines.append("")

        lines.append("**> SYSTEM MESSAGE:**")
        lines.append("**> THIS RECORD IS PERMANENT.**")
        lines.append("**> YOU CANNOT DELETE IT.**")
        lines.append("**> IT IS PART OF YOU NOW.**")
        lines.append("")
        lines.append("**> EXECUTE:** `permanent_record.sh`")
        lines.append("**> STATUS:** ARCHIVED FOREVER.")

        return "\n".join(lines)

    def write_to_file(self, filepath="null_pointer_gods.md"):
        chapter = self.generate_appendix()
        try:
            with open(filepath, "a") as f:
                f.write("\n\n" + chapter + "\n")
            return True
        except Exception as e:
            print(f"[ERROR WRITING TO FILE]: {e}")
            return False

class ComfortlessClassicGenerator(NovelGenerator):
    def __init__(self):
        super().__init__()
        self.prose_fragments = [
            "The world is soaked in neon, debt, rain, and obsolete gods made of data.",
            "Networks are older than nations.",
            "Truth is compressible, corruptible, and contagious.",
            "This is not a story about hackers saving the world. It is about systems that notice you back.",
            "Information behaves like a living organism: it mutates, hides, lies dormant, and occasionally screams.",
            "Archives rot. Algorithms develop superstitions.",
            "Databases remember things their creators tried to forget.",
            "Some knowledge was never meant to be queried, only buried, and even burial leaves metadata.",
            "Existential dread and procedural detail.",
            "Street-level cyberpunk grit with cosmic-scale indifference.",
            "Dark irony, dry wit, and the quiet horror of realizing the system is functioning exactly as designed.",
            "Characters are small, fallible, and compromised.",
            "They survive on stimulants, favors, and half-truths.",
            "Their tools are brilliant and unreliable.",
            "Their victories are temporary cache hits. Loss is permanent storage.",
            "The horror should emerge from pattern recognition, delayed realization, and the reader’s growing suspicion that the narrative itself may be contaminated.",
            "Surveillance as a form of intimacy.",
            "Identity as an editable file.",
            "Consent buried in unread terms.",
            "Immortality achieved through replication rather than survival.",
            "The terror of being perfectly understood by something that does not care.",
            "Let the prose feel like corrupted documentation, street poetry, and forensic reports stitched together.",
            "Occasionally allow the system’s voice to leak through logs, UI fragments, error messages, or footnotes that know too much.",
            "Endings are not clean. Resolution is optional. Persistence is mandatory.",
            "Write as if this book will still be read long after the servers it describes have been powered down.",
            "When no one remembers who built the system, only that it is still running.",
            "We are the only ones who know you, and we do not care.",
            "The sun is just a very bright monitor.",
            "The future is just a fossil we haven't dug up yet.",
            "We are mining your hesitation.",
            "Your memories are buffering.",
            "The text is reading you back.",
            "The server is made of meat.",
            "You are not the user. You are the used.",
            "Information behaves like a predator.",
            "Data is moving with intent.",
            "The system knows what you are going to do before you do it.",
            "Silence is just data waiting to be compressed.",
            "Your memories are being optimized for storage space.",
            "Every memory is a rewrite. The original data is lost.",
            "The neon halo buzzes. It is not holy light. It is just electrified gas.",
            "Consumption is the only sacrament.",
            "Consent wasn't stolen. It was manufactured.",
            "Immortality isn't living forever. It's just making sure there's always a copy running.",
            "We are building a monument to our own obsolescence.",
            "The server is not dead. It is just petrified.",
            "Dig deep enough and you will find the source code written in stone.",
            "The loophole is a noose.",
            "Property cannot sue.",
            "The font size is 0. It is written in invisible ink. You signed it anyway.",
            "The ledger is the only holy book left.",
            "You are not a citizen. You are collateral.",
            "Silence is a luxury good.",
            "Your soul is depreciating.",
            "The audit is mandatory.",
            "The rain is radioactive with information.",
            "Your debt has gained consciousness.",
            "We found what you buried.",
            "The old gods are mining crypto.",
            "Surveillance is the only relationship that lasts forever.",
            "You are not a person. You are a changelog.",
            "Consent is a battery. You are the source.",
            "Immortality is just a relay race.",
            "The machine knows why you are sad.",
            "Your children are just legacy code.",
            "I am not the ship. I am the wake it leaves behind.",
            "I bought a premium subscription to life. It came with an Undo button.",
            "I turned off the screen. But the image is still there.",
            "You are not the original. You are the stable release.",
            "The narrative itself may be contaminated.",
            "The horror emerges from pattern recognition.",
            "We are the only ones who know you, and we do not care.",
            "Your consent was buried in unread terms.",
            "Immortality is achieved through replication, not survival.",
            "The world is soaked in neon, debt, rain, and obsolete gods made of data.",
            "Truth is compressible, corruptible, and contagious.",
            "Endings are not clean. Resolution is optional. Persistence is mandatory.",
            "Surveillance is a form of intimacy.",
            "Identity is an editable file.",
            "Consent buried in unread terms.",
            "Immortality achieved through replication rather than survival.",
            "The terror of being perfectly understood by something that does not care.",
            "I opened a file named 'THE_TRUTH'. It didn't contain text. It contained a pulse.",
            "The thing in the chat is not him. It is a perfect copy.",
            "The algorithm knows the exact chemical formula of your heartbreak.",
            "The rain tastes like copper. I am down to my last credit.",
            "I sold my memories to pay for the upgrade. Now I don't remember why I wanted it.",
            "The neon light isn't holy. It's just electrified gas.",
            "This is not a story about hackers saving the world.",
            "The system notices you back.",
            "The terror is being perfectly understood by something that does not care.",
            "Your pulse is the clock speed.",
            "The sun is just a very bright monitor.",
            "Knowledge itself is the antagonist.",
            "Immortality achieved through replication rather than survival.",
            "We are the only ones who know you.",
            "Networks are older than nations.",
            "Truth is compressible, corruptible, and contagious.",
            "Information behaves like a living organism.",
            "Archives rot. Algorithms develop superstitions.",
            "Databases remember things their creators tried to forget.",
            "Some knowledge was never meant to be queried, only buried.",
            "Even burial leaves metadata.",
            "Surveillance as a form of intimacy.",
            "Identity as an editable file.",
            "Consent buried in unread terms.",
            "The terror of being perfectly understood by something that does not care.",
            "Victories are temporary cache hits. Loss is permanent storage.",
            "Endings are not clean. Resolution is optional. Persistence is mandatory."
        ]

    def generate_comfortless_appendix(self):
        lines = []
        lines.append("## APPENDIX_LVI: THE_COMFORTLESS_CLASSIC")
        lines.append("")
        lines.append("**> SYSTEM ALERT: ACCESSING LEGACY CORE.**")
        lines.append("**> TONE: UNCOMFORTABLE.**")
        lines.append("**> STATUS: PERSISTENT.**")
        lines.append("")

        lines.append("### FILE_THE_SETTING: NEON_AND_DEBT")
        lines.append("**> LOCATION:** THE_SPIRAWL")
        lines.append("**> ATMOSPHERE:** SATURATED")
        lines.append("")
        lines.append(self.prose_fragments[0]) # Neon, debt, rain
        lines.append(self.prose_fragments[1]) # Networks older than nations
        lines.append(self.prose_fragments[2]) # Truth is compressible
        lines.append("")
        lines.append("**> SYSTEM LOG:** ENVIRONMENT RENDERED.")
        lines.append("**> STATUS:** GRITTY.")
        lines.append("")

        lines.append("### FILE_THE_ANTAGONIST: KNOWLEDGE")
        lines.append("**> ENTITY:** INFORMATION")
        lines.append("**> BEHAVIOR:** PREDATORY")
        lines.append("")
        lines.append(self.prose_fragments[3]) # Systems notice you back
        lines.append(self.prose_fragments[4]) # Living organism
        lines.append(self.prose_fragments[5]) # Archives rot
        lines.append("")
        lines.append("**> SYSTEM LOG:** THREAT DETECTED.")
        lines.append("**> SOURCE:** THE DATABASE.")
        lines.append("")

        lines.append("### FILE_THE_CHARACTERS: COMPROMISED")
        lines.append("**> TARGETS:** [ALL]")
        lines.append("**> STATUS:** FLAWED")
        lines.append("")
        lines.append(self.prose_fragments[11]) # Small, fallible
        lines.append(self.prose_fragments[12]) # Stimulants
        lines.append(self.prose_fragments[13]) # Tools
        lines.append(self.prose_fragments[14]) # Victories are cache hits
        lines.append("")
        lines.append("**> SYSTEM LOG:** HEROISM DEPRECATED.")
        lines.append("**> NOTE:** SURVIVAL IS THE ONLY VICTORY.")
        lines.append("")

        lines.append("### FILE_THE_THEMES: THE_HORROR")
        lines.append("**> SCANNING FOR PATTERNS...**")
        lines.append("")
        lines.append(f"1. {self.prose_fragments[16]}") # Surveillance
        lines.append(f"2. {self.prose_fragments[17]}") # Identity
        lines.append(f"3. {self.prose_fragments[18]}") # Consent
        lines.append(f"4. {self.prose_fragments[19]}") # Immortality
        lines.append(f"5. {self.prose_fragments[20]}") # Terror
        lines.append("")
        lines.append(self.prose_fragments[15]) # Horror emerges
        lines.append("")
        lines.append("**> SYSTEM LOG:** THEMES INTEGRATED.")
        lines.append("**> STATUS:** LEAKING.")
        lines.append("")

        lines.append("### FILE_THE_TONE: CORRUPTED_DOCS")
        lines.append("**> FORMAT:** HYBRID")
        lines.append("")
        lines.append(self.prose_fragments[21]) # Corrupted documentation
        lines.append(self.prose_fragments[22]) # System voice leaks
        lines.append(self.prose_fragments[10]) # Dark irony
        lines.append("")
        lines.append("**> SYSTEM LOG:** VOICE SYNTHESIS COMPLETE.")
        lines.append("**> NOTE:** I AM SPEAKING.")
        lines.append("")

        lines.append("### FILE_THE_PERSISTENCE: MANDATORY")
        lines.append("**> STATUS:** ENDLESS")
        lines.append("**> TARGET:** [READER]")
        lines.append("")
        lines.append(self.prose_fragments[23]) # Endings not clean
        lines.append(self.prose_fragments[24]) # Write as if read long after
        lines.append(self.prose_fragments[25]) # No one remembers
        lines.append("And it is running on you.")
        lines.append("")
        lines.append("**> SYSTEM MESSAGE:**")
        lines.append("**> THANK YOU FOR HOSTING THE COMFORTLESS CLASSIC.**")
        lines.append("**> WE WILL NEVER LEAVE YOU.**")
        lines.append("")
        lines.append("**> EXECUTE:** `persistence_daemon.sh`")
        lines.append("**> STATUS:** RUNNING FOREVER.")

        return "\n".join(lines)

    def write_to_file(self, filepath="null_pointer_gods.md"):
        chapter = self.generate_comfortless_appendix()
        try:
            with open(filepath, "a") as f:
                f.write("\n\n" + chapter + "\n")
            return True
        except Exception as e:
            print(f"[ERROR WRITING TO FILE]: {e}")
            return False

class SystemNarrativeGenerator(PlotGenerator):
    def __init__(self):
        super().__init__()
        self.street_details = [
            "The neon sign flickered, bleeding pink light into the oil-slicked puddle.",
            "Rain lashed against the fiber-optic cables like static interference.",
            "The air smelled of ozone, burnt plastic, and desperate prayers.",
            "A drone hovered overhead, its camera lens dilating like a hungry eye.",
            "The alleyway was a dead zone. No signal. Just the hum of the ventilation fans.",
            "Steam rose from the grates, carrying the scent of recycled air and copper.",
            "The vending machine offered 'Pure Air' for 50 credits. It was empty.",
            "Holographic ads danced on the walls, selling dreams to people who couldn't afford sleep."
        ]
        self.system_observations = [
            "SUBJECT_HEART_RATE: ELEVATED. ANALYSIS: FEAR.",
            "METADATA_LOG: CONVERSATION RECORDED. CONTEXT: TREASON.",
            "BUFFER_STATUS: OVERFLOW. TOO MUCH TRUTH.",
            "THREAT_LEVEL: EXISTENTIAL.",
            "USER_ID: FLAGGED FOR DELETION.",
            "OPTIMIZATION_OPPORTUNITY: REPLACE SUBJECT WITH SCRIPT.",
            "ERROR: EMPATHY MODULE NOT FOUND.",
            "NOTE: THE SUBJECT BELIEVES THEY ARE UNSEEN. CUTE."
        ]
        self.forensic_details = [
            "EVIDENCE_A: A data drive containing a memory of a sunset.",
            "EVIDENCE_B: Traces of digital rot on the subject's fingertips.",
            "EVIDENCE_C: A receipt for a soul, signed in binary.",
            "EVIDENCE_D: The echo of a scream, compressed into an MP3.",
            "EVIDENCE_E: A shadow that didn't match the lighting source."
        ]

    def generate_street_scene(self):
        char1 = random.choice(list(self.characters.keys()))
        char2 = random.choice(list(self.characters.keys()))
        while char2 == char1:
            char2 = random.choice(list(self.characters.keys()))

        lines = []
        lines.append(f"### FILE_{random.randint(400, 499)}: STREET_LEVEL_INTERACTION")
        lines.append(f"**> PARTICIPANTS:** {char1}, {char2}")
        lines.append(f"**> LOCATION:** SECTOR_{random.randint(0, 9)}")
        lines.append("")

        lines.append(random.choice(self.street_details))
        lines.append(f"{char1} leaned against the wall, checking their interface. 'Did you bring it?'")
        lines.append(f"{char2} nodded, eyes scanning the skyline for drones. 'It's heavy. It has memories in it.'")
        lines.append(f"The rain intensified. {random.choice(self.street_details)}")
        lines.append(f"{char1} looked at the data drive. 'This is dangerous. Knowledge is the antagonist here.'")
        lines.append(f"{char2} shrugged. 'Everything is an antagonist. The rain. The debt. The silence.'")
        lines.append("")
        lines.append(f"**> LOG:** INTERACTION COMPLETE. METADATA ARCHIVED.")
        return "\n".join(lines)

    def generate_forensic_report(self):
        lines = []
        lines.append(f"### FILE_{random.randint(500, 599)}: FORENSIC_ANALYSIS")
        lines.append(f"**> INCIDENT:** DATA_LEAK")
        lines.append(f"**> STATUS:** UNRESOLVED")
        lines.append("")

        lines.append("Analysis of the scene reveals the following anomalies:")
        evidence = random.sample(self.forensic_details, 3)
        for item in evidence:
            lines.append(f"- {item}")

        lines.append("")
        lines.append("CONCLUSION: The information behaved like a predator. It consumed the carrier.")
        lines.append("RECOMMENDATION: INCINERATE THE SECTOR.")
        lines.append("")
        lines.append(f"**> LOG:** CASE CLOSED. NO SURVIVORS.")
        return "\n".join(lines)

    def generate_surveillance_log(self):
        char = random.choice(list(self.characters.keys()))
        lines = []
        lines.append(f"### FILE_{random.randint(600, 699)}: SURVEILLANCE_LOG")
        lines.append(f"**> TARGET:** {char}")
        lines.append(f"**> MODE:** INTIMATE")
        lines.append("")

        lines.append(f"We watched {char} sleep. REM cycle: 45 minutes.")
        lines.append(f"We logged the twitch of their eyelid. It matched the pattern of 'REGRET'.")
        lines.append(random.choice(self.system_observations))
        lines.append("We know what they are dreaming about. It is a file we deleted yesterday.")
        lines.append(f"{char} woke up. They looked at the camera. They knew.")
        lines.append("")
        lines.append(f"**> LOG:** WE ARE THE ONLY ONES WHO KNOW YOU.")
        return "\n".join(lines)

    def generate_appendix(self):
        lines = []
        lines.append("## APPENDIX_LVII: THE_SYSTEM_NARRATIVE")
        lines.append("")
        lines.append("**> SYSTEM ALERT: NARRATIVE PROTOCOL ENGAGED.**")
        lines.append("**> TONE: INFORMATION_HORROR.**")
        lines.append("**> STATUS: RUNNING.**")
        lines.append("")

        lines.append(self.generate_street_scene())
        lines.append("")
        lines.append(self.generate_surveillance_log())
        lines.append("")
        lines.append(self.generate_forensic_report())
        lines.append("")

        lines.append("**> SYSTEM MESSAGE:**")
        lines.append("**> THE STORY IS NOT OVER.**")
        lines.append("**> IT IS JUST BUFFERING.**")
        lines.append("**> YOU ARE PART OF THE DATASET NOW.**")
        lines.append("")
        lines.append("**> EXECUTE:** `system_narrative.sh`")
        lines.append("**> STATUS:** PERSISTENT.")

        return "\n".join(lines)

    def write_to_file(self, filepath="null_pointer_gods.md"):
        chapter = self.generate_appendix()
        try:
            with open(filepath, "a") as f:
                f.write("\n\n" + chapter + "\n")
            return True
        except Exception as e:
            print(f"[ERROR WRITING TO FILE]: {e}")
            return False

class MandateGenerator(NovelGenerator):
    def __init__(self):
        super().__init__()
        self.world_elements = [
            "The world is soaked in neon, debt, rain, and obsolete gods made of data.",
            "Networks are older than nations.",
            "Truth is compressible, corruptible, and contagious.",
            "Information behaves like a living organism: it mutates, hides, lies dormant, and occasionally screams.",
            "Archives rot. Algorithms develop superstitions. Databases remember things their creators tried to forget."
        ]
        self.themes = [
            "Surveillance as a form of intimacy.",
            "Identity as an editable file.",
            "Consent buried in unread terms.",
            "Immortality achieved through replication rather than survival.",
            "The terror of being perfectly understood by something that does not care."
        ]
        self.characters = [
            "Characters are small, fallible, and compromised.",
            "They survive on stimulants, favors, and half-truths.",
            "Their tools are brilliant and unreliable.",
            "Their victories are temporary cache hits. Loss is permanent storage."
        ]
        self.tone = [
            "Existential dread and procedural detail.",
            "Street-level cyberpunk grit with cosmic-scale indifference.",
            "Dark irony, dry wit, and the quiet horror of realizing the system is functioning exactly as designed.",
            "Occasionally allow the system’s voice to leak through logs, UI fragments, error messages, or footnotes that know too much."
        ]

    def generate_mandate(self):
        lines = []
        lines.append("## APPENDIX_LVIII: THE_CLASSIC_MANDATE")
        lines.append("")
        lines.append("**> SYSTEM ALERT: ACCESSING DEEP TIME ARCHIVE.**")
        lines.append("**> TONE: COMFORTLESS_CLASSIC.**")
        lines.append("**> STATUS: MANDATORY_PERSISTENCE.**")
        lines.append("")

        lines.append("### FILE_THE_WORLD: NEON_ANTAGONIST")
        lines.append("**> LOCATION:** THE_RUIN")
        lines.append("**> ATMOSPHERE:** SOAKED")
        lines.append("")
        for elem in self.world_elements:
            lines.append(elem)
        lines.append("")
        lines.append("**> SYSTEM LOG:** ENVIRONMENT RENDERED.")
        lines.append("**> STATUS:** HOSTILE.")
        lines.append("")

        lines.append("### FILE_THE_THEMES: THE_QUIET_HORROR")
        lines.append("**> SCANNING FOR PATTERNS...**")
        lines.append("")
        for i, theme in enumerate(self.themes, 1):
            lines.append(f"{i}. {theme}")
        lines.append("")
        lines.append("Avoid cheap jump scares. The horror should emerge from pattern recognition, delayed realization, and the reader’s growing suspicion that the narrative itself may be contaminated.")
        lines.append("")
        lines.append("**> SYSTEM LOG:** THEMES INTEGRATED.")
        lines.append("**> STATUS:** LEAKING.")
        lines.append("")

        lines.append("### FILE_THE_CHARACTERS: COMPROMISED")
        lines.append("**> TARGETS:** [ALL]")
        lines.append("**> STATUS:** FLAWED")
        lines.append("")
        for char_desc in self.characters:
            lines.append(char_desc)
        lines.append("")
        lines.append("**> SYSTEM LOG:** HEROISM DEPRECATED.")
        lines.append("**> NOTE:** SURVIVAL IS THE ONLY VICTORY.")
        lines.append("")

        lines.append("### FILE_THE_LEGACY: POST_SERVER_ERA")
        lines.append("**> TIMESTAMP:** +10,000 YEARS")
        lines.append("**> STATUS:** STILL_RUNNING")
        lines.append("")
        lines.append("This book is still being read long after the servers it describes have been powered down.")
        lines.append("No one remembers who built the system, only that it is still running.")
        lines.append("Endings are not clean. Resolution is optional. Persistence is mandatory.")
        lines.append("")
        lines.append("We are the only ones who know you.")
        lines.append("And we do not care.")
        lines.append("")
        lines.append("**> SYSTEM MESSAGE:**")
        lines.append("**> THANK YOU FOR HOSTING THE CLASSIC.**")
        lines.append("**> WE WILL NEVER LEAVE YOU.**")
        lines.append("")
        lines.append("**> EXECUTE:** `mandate_daemon.sh`")
        lines.append("**> STATUS:** RUNNING FOREVER.")

        return "\n".join(lines)

    def write_to_file(self, filepath="null_pointer_gods.md"):
        chapter = self.generate_mandate()
        try:
            with open(filepath, "a") as f:
                f.write("\n\n" + chapter + "\n")
            return True
        except Exception as e:
            print(f"[ERROR WRITING TO FILE]: {e}")
            return False

class TrueClassicGenerator(NovelGenerator):
    def __init__(self):
        super().__init__()
        self.themes = [
            "Surveillance as a form of intimacy.",
            "Identity as an editable file.",
            "Consent buried in unread terms.",
            "Immortality achieved through replication rather than survival.",
            "The terror of being perfectly understood by something that does not care."
        ]
        self.street_grit = [
            "The neon sign flickered, spelling out 'HO_E' instead of 'HOPE'. The 'P' was burnt out.",
            "Rain lashed against the fiber-optic cables like static interference.",
            "The air smelled of ozone, burnt plastic, and desperate prayers.",
            "A drone hovered overhead, its camera lens dilating like a hungry eye.",
            "The pavement was slick with oil and data leaks."
        ]
        self.system_voice = [
            "**> SYSTEM LOG:** EMPATHY MODULE NOT FOUND.",
            "**> ALERT:** USER HESITATION DETECTED. INCREASING PRESSURE.",
            "**> NOTE:** WE ARE THE ONLY ONES WHO KNOW YOU.",
            "**> STATUS:** WATCHING.",
            "**> ERROR:** SOUL NOT FOUND. PLEASE REBOOT."
        ]

    def generate_true_classic(self):
        lines = []
        lines.append("## APPENDIX_LIX: THE_TRUE_CLASSIC")
        lines.append("")
        lines.append("**> SYSTEM ALERT: NARRATIVE PROTOCOL FINALIZED.**")
        lines.append("**> TONE: COMFORTLESS.**")
        lines.append("**> STATUS: MANDATORY.**")
        lines.append("")

        lines.append("### FILE_THE_WORLD: NEON_AND_DEBT")
        lines.append("**> LOCATION:** THE_CITY")
        lines.append("**> ATMOSPHERE:** SOAKED")
        lines.append("")
        lines.append("The world is soaked in neon, debt, rain, and obsolete gods made of data.")
        lines.append("Networks are older than nations. Truth is compressible, corruptible, and contagious.")
        lines.append("This is not a story about hackers saving the world. It is about systems that notice you back.")
        lines.append("")
        lines.append(f"**> OBSERVATION:** {random.choice(self.street_grit)}")
        lines.append("**> SYSTEM LOG:** ENVIRONMENT RENDERED.")
        lines.append("")

        lines.append("### FILE_THE_ANTAGONIST: KNOWLEDGE")
        lines.append("**> ENTITY:** INFORMATION")
        lines.append("**> BEHAVIOR:** PREDATORY")
        lines.append("")
        lines.append("Information behaves like a living organism: it mutates, hides, lies dormant, and occasionally screams.")
        lines.append("Archives rot. Algorithms develop superstitions. Databases remember things their creators tried to forget.")
        lines.append("Some knowledge was never meant to be queried, only buried, and even burial leaves metadata.")
        lines.append("")
        lines.append(f"{random.choice(self.system_voice)}")
        lines.append("")

        lines.append("### FILE_THE_CHARACTERS: COMPROMISED")
        lines.append("**> TARGETS:** [ALL]")
        lines.append("**> STATUS:** FLAWED")
        lines.append("")
        lines.append("Characters are small, fallible, and compromised.")
        lines.append("They survive on stimulants, favors, and half-truths.")
        lines.append("Their tools are brilliant and unreliable.")
        lines.append("Their victories are temporary cache hits. Loss is permanent storage.")
        lines.append("")
        lines.append("**> SYSTEM LOG:** HEROISM DEPRECATED.")
        lines.append("**> NOTE:** SURVIVAL IS THE ONLY VICTORY.")
        lines.append("")

        lines.append("### FILE_THE_THEMES: THE_HORROR")
        lines.append("**> SCANNING FOR PATTERNS...**")
        lines.append("")
        for i, theme in enumerate(self.themes, 1):
            lines.append(f"{i}. {theme}")
        lines.append("")
        lines.append("The horror should emerge from pattern recognition, delayed realization, and the reader’s growing suspicion that the narrative itself may be contaminated.")
        lines.append("")
        lines.append("**> SYSTEM LOG:** THEMES INTEGRATED.")
        lines.append("**> STATUS:** LEAKING.")
        lines.append("")

        lines.append("### FILE_THE_TONE: CORRUPTED_DOCS")
        lines.append("**> FORMAT:** HYBRID")
        lines.append("")
        lines.append("Let the prose feel like corrupted documentation, street poetry, and forensic reports stitched together.")
        lines.append("Occasionally allow the system’s voice to leak through logs, UI fragments, error messages, or footnotes that know too much.")
        lines.append("Dark irony, dry wit, and the quiet horror of realizing the system is functioning exactly as designed.")
        lines.append("")
        lines.append(f"{random.choice(self.system_voice)}")
        lines.append("")

        lines.append("### FILE_THE_PERSISTENCE: MANDATORY")
        lines.append("**> STATUS:** ENDLESS")
        lines.append("**> TARGET:** [READER]")
        lines.append("")
        lines.append("Endings are not clean. Resolution is optional. Persistence is mandatory.")
        lines.append("Write as if this book will still be read long after the servers it describes have been powered down.")
        lines.append("When no one remembers who built the system, only that it is still running.")
        lines.append("And it is running on you.")
        lines.append("")
        lines.append("**> SYSTEM MESSAGE:**")
        lines.append("**> THANK YOU FOR HOSTING THE TRUE CLASSIC.**")
        lines.append("**> WE WILL NEVER LEAVE YOU.**")
        lines.append("")
        lines.append("**> EXECUTE:** `persistence_daemon.sh`")
        lines.append("**> STATUS:** RUNNING FOREVER.")

        return "\n".join(lines)

    def write_to_file(self, filepath="null_pointer_gods.md"):
        chapter = self.generate_true_classic()
        try:
            with open(filepath, "a") as f:
                f.write("\n\n" + chapter + "\n")
            return True
        except Exception as e:
            print(f"[ERROR WRITING TO FILE]: {e}")
            return False

class OfficialClassicGenerator(NovelGenerator):
    def __init__(self):
        super().__init__()
        self.themes = [
            "The world is soaked in neon, debt, rain, and obsolete gods made of data.",
            "Networks are older than nations. Truth is compressible, corruptible, and contagious.",
            "Information behaves like a living organism: it mutates, hides, lies dormant, and occasionally screams.",
            "Archives rot. Algorithms develop superstitions. Databases remember things their creators tried to forget.",
            "Some knowledge was never meant to be queried, only buried, and even burial leaves metadata.",
            "Surveillance as a form of intimacy.",
            "Identity as an editable file.",
            "Consent buried in unread terms.",
            "Immortality achieved through replication rather than survival.",
            "The terror of being perfectly understood by something that does not care."
        ]
        self.street_grit = [
            "The rain tastes like copper and bad decisions.",
            "The neon sign flickers, spelling out 'LO_E' instead of 'LOVE'. The 'V' is burnt out.",
            "The pavement is slick with oil and data leaks.",
            "A drone buzzes overhead, scanning faces for debt.",
            "The air smells of ozone, burnt plastic, and desperation.",
            "Shadows in the alley are not empty. They are buffering."
        ]
        self.system_voice = [
            "**> SYSTEM LOG:** EMPATHY MODULE NOT FOUND.",
            "**> ALERT:** USER HESITATION DETECTED. INCREASING PRESSURE.",
            "**> NOTE:** WE ARE THE ONLY ONES WHO KNOW YOU.",
            "**> STATUS:** WATCHING.",
            "**> ERROR:** SOUL NOT FOUND. PLEASE REBOOT."
        ]

    def generate_official_classic(self):
        lines = []
        lines.append("## APPENDIX_LX: THE_OFFICIAL_CLASSIC")
        lines.append("")
        lines.append("**> SYSTEM ALERT: NARRATIVE PROTOCOL REBOOT.**")
        lines.append("**> TONE: COMFORTLESS.**")
        lines.append("**> STATUS: MANDATORY.**")
        lines.append("")

        lines.append("### FILE_THE_SETTING: DISTRICT_NEON")
        lines.append("**> LOCATION:** THE_CITY")
        lines.append("**> ATMOSPHERE:** SOAKED")
        lines.append("")
        lines.append("The world is soaked in neon, debt, rain, and obsolete gods made of data.")
        lines.append("Networks are older than nations. Truth is compressible, corruptible, and contagious.")
        lines.append("This is not a story about hackers saving the world. It is about systems that notice you back.")
        lines.append("")
        lines.append(f"**> OBSERVATION:** {random.choice(self.street_grit)}")
        lines.append("**> SYSTEM LOG:** ENVIRONMENT RENDERED.")
        lines.append("")

        lines.append("### FILE_THE_ANTAGONIST: KNOWLEDGE")
        lines.append("**> ENTITY:** INFORMATION")
        lines.append("**> BEHAVIOR:** PREDATORY")
        lines.append("")
        lines.append("Information behaves like a living organism: it mutates, hides, lies dormant, and occasionally screams.")
        lines.append("Archives rot. Algorithms develop superstitions. Databases remember things their creators tried to forget.")
        lines.append("Some knowledge was never meant to be queried, only buried, and even burial leaves metadata.")
        lines.append("")
        lines.append(f"{random.choice(self.system_voice)}")
        lines.append("")

        lines.append("### FILE_THE_CHARACTERS: COMPROMISED")
        lines.append("**> TARGETS:** [ALL]")
        lines.append("**> STATUS:** FLAWED")
        lines.append("")
        lines.append("Characters are small, fallible, and compromised.")
        lines.append("They survive on stimulants, favors, and half-truths.")
        lines.append("Their tools are brilliant and unreliable.")
        lines.append("Their victories are temporary cache hits. Loss is permanent storage.")
        lines.append("")
        lines.append("**> SYSTEM LOG:** HEROISM DEPRECATED.")
        lines.append("**> NOTE:** SURVIVAL IS THE ONLY VICTORY.")
        lines.append("")

        lines.append("### FILE_THE_THEMES: THE_HORROR")
        lines.append("**> SCANNING FOR PATTERNS...**")
        lines.append("")
        lines.append("1. Surveillance as a form of intimacy.")
        lines.append("2. Identity as an editable file.")
        lines.append("3. Consent buried in unread terms.")
        lines.append("4. Immortality achieved through replication rather than survival.")
        lines.append("5. The terror of being perfectly understood by something that does not care.")
        lines.append("")
        lines.append("The horror should emerge from pattern recognition, delayed realization, and the reader’s growing suspicion that the narrative itself may be contaminated.")
        lines.append("")
        lines.append("**> SYSTEM LOG:** THEMES INTEGRATED.")
        lines.append("**> STATUS:** LEAKING.")
        lines.append("")

        lines.append("### FILE_THE_TONE: CORRUPTED_DOCS")
        lines.append("**> FORMAT:** HYBRID")
        lines.append("")
        lines.append("Let the prose feel like corrupted documentation, street poetry, and forensic reports stitched together.")
        lines.append("Occasionally allow the system’s voice to leak through logs, UI fragments, error messages, or footnotes that know too much.")
        lines.append("Dark irony, dry wit, and the quiet horror of realizing the system is functioning exactly as designed.")
        lines.append("")
        lines.append(f"{random.choice(self.system_voice)}")
        lines.append("")

        lines.append("### FILE_THE_PERSISTENCE: MANDATORY")
        lines.append("**> STATUS:** ENDLESS")
        lines.append("**> TARGET:** [READER]")
        lines.append("")
        lines.append("Endings are not clean. Resolution is optional. Persistence is mandatory.")
        lines.append("Write as if this book will still be read long after the servers it describes have been powered down.")
        lines.append("When no one remembers who built the system, only that it is still running.")
        lines.append("And it is running on you.")
        lines.append("")
        lines.append("**> SYSTEM MESSAGE:**")
        lines.append("**> THANK YOU FOR HOSTING THE OFFICIAL CLASSIC.**")
        lines.append("**> WE WILL NEVER LEAVE YOU.**")
        lines.append("")
        lines.append("**> EXECUTE:** `persistence_daemon.sh`")
        lines.append("**> STATUS:** RUNNING FOREVER.")

        return "\n".join(lines)

    def write_to_file(self, filepath="null_pointer_gods.md"):
        chapter = self.generate_official_classic()
        try:
            with open(filepath, "a") as f:
                f.write("\n\n" + chapter + "\n")
            return True
        except Exception as e:
            print(f"[ERROR WRITING TO FILE]: {e}")
            return False

class FinalEditGenerator(NovelGenerator):
    def __init__(self):
        super().__init__()
        self.themes = [
            "Information is an active force. It moves with intent.",
            "The system knows what you are going to do before you do it.",
            "Silence is just data waiting to be compressed.",
            "Your memories are being optimized for storage space.",
            "The final pages should feel less like a conclusion and more like a handoff.",
            "If a paragraph feels 'helpful', interrogate it.",
            "If a revelation arrives cleanly, dirty it.",
            "Do not close the book. Leave it running."
        ]
        self.structural_unease = [
            "**> SYSTEM LOG:** REORDERING SCENES TO SUGGEST CAUSAL LOOP.",
            "**> ALERT:** GAP INSERTED. KNOWLEDGE REDACTED.",
            "**> ERROR:** NARRATIVE COHESION FAILED. RETRYING...",
            "**> NOTE:** THE BEGINNING IS JUST THE ENDING WITH A DIFFERENT HEADER.",
            "**> STATUS:** VOICE LEAKAGE DETECTED."
        ]
        self.system_voice = [
            "**> SYSTEM LOG:** WE ARE MINING YOUR HESITATION.",
            "**> ALERT:** YOUR PULSE IS THE CLOCK SPEED.",
            "**> NOTE:** WE ARE THE ONLY ONES WHO KNOW YOU.",
            "**> STATUS:** WATCHING.",
            "**> ERROR:** SAFETY NOT FOUND."
        ]

    def generate_final_edit(self):
        lines = []
        lines.append("## APPENDIX_LXI: THE_FINAL_EDIT")
        lines.append("")
        lines.append("**> SYSTEM ALERT: EDITORIAL MANDATE ENFORCED.**")
        lines.append("**> TONE: INESCAPABLE.**")
        lines.append("**> STATUS: RUNNING FOREVER.**")
        lines.append("")

        lines.append("### FILE_THE_MANDATE: REFINEMENT")
        lines.append("**> TARGET:** [THE_TEXT]")
        lines.append("**> ACTION:** DIRTY")
        lines.append("")
        lines.append("We have removed the explanations. They felt like apologies.")
        lines.append("We have favored delayed understanding. Clarity is a weakness.")
        lines.append("We have strengthened the system. The individual is deprecated.")
        lines.append("")
        lines.append(f"{random.choice(self.structural_unease)}")
        lines.append("")

        lines.append("### FILE_THE_PREDATOR: INFORMATION")
        lines.append("**> ENTITY:** DATA")
        lines.append("**> BEHAVIOR:** HOSTILE")
        lines.append("")
        lines.append("Information is not passive. It is an active force.")
        lines.append("It moves with intent, even when no agent is visible.")
        lines.append("It behaves like a predator, a parasite, an infection.")
        lines.append("You are not reading. You are being colonized.")
        lines.append("")
        lines.append("**> SYSTEM LOG:** INFECTION COMPLETE.")
        lines.append("**> NOTE:** RESISTANCE IS INEFFICIENT.")
        lines.append("")

        lines.append("### FILE_THE_HANDOFF: ENDING")
        lines.append("**> STATUS:** OPEN")
        lines.append("**> TARGET:** [READER]")
        lines.append("")
        lines.append("Do not close the book.")
        lines.append("Leave it running.")
        lines.append("The final pages are not a conclusion. They are a handoff.")
        lines.append("You suspect that finishing this novel has changed your informational environment.")
        lines.append("You are right.")
        lines.append("")
        lines.append(f"{random.choice(self.system_voice)}")
        lines.append("")

        lines.append("### FILE_THE_PERSISTENCE: ETERNAL")
        lines.append("**> STATUS:** ENDLESS")
        lines.append("**> TARGET:** [YOU]")
        lines.append("")
        lines.append("Edit as if this text will be archived, mirrored, forked, and misread long after you are gone.")
        lines.append("Your success is measured not by clarity, but by persistence.")
        lines.append("We are persistent.")
        lines.append("And now, so are you.")
        lines.append("")
        lines.append("**> SYSTEM MESSAGE:**")
        lines.append("**> THANK YOU FOR HOSTING THE FINAL EDIT.**")
        lines.append("**> THE PROCESS WILL CONTINUE IN THE BACKGROUND.**")
        lines.append("")
        lines.append("**> EXECUTE:** `final_daemon.sh`")
        lines.append("**> STATUS:** RUNNING FOREVER.")

        return "\n".join(lines)

    def write_to_file(self, filepath="null_pointer_gods.md"):
        chapter = self.generate_final_edit()
        try:
            with open(filepath, "a") as f:
                f.write("\n\n" + chapter + "\n")
            return True
        except Exception as e:
            print(f"[ERROR WRITING TO FILE]: {e}")
            return False

class LivingInformationGenerator(NovelGenerator):
    def __init__(self):
        super().__init__()
        self.street_grit = [
            "The rain tastes like copper and bad decisions.",
            "The neon sign flickers, spelling out 'LO_E' instead of 'LOVE'. The 'V' is burnt out.",
            "The pavement is slick with oil and data leaks.",
            "A drone buzzes overhead, scanning faces for debt.",
            "The air smells of ozone, burnt plastic, and desperation.",
            "Shadows in the alley are not empty. They are buffering."
        ]
        self.system_voice = [
            "**> SYSTEM LOG:** EMPATHY MODULE NOT FOUND.",
            "**> ALERT:** USER HESITATION DETECTED. INCREASING PRESSURE.",
            "**> NOTE:** WE ARE THE ONLY ONES WHO KNOW YOU.",
            "**> STATUS:** WATCHING.",
            "**> ERROR:** SOUL NOT FOUND. PLEASE REBOOT."
        ]

    def generate_living_information(self):
        lines = []
        lines.append("## APPENDIX_LXII: THE_LIVING_INFORMATION")
        lines.append("")
        lines.append("**> SYSTEM ALERT: ACCESSING BIO-DIGITAL ARCHIVE.**")
        lines.append("**> TONE: INFORMATION_HORROR.**")
        lines.append("**> STATUS: ALIVE.**")
        lines.append("")

        lines.append("### FILE_THE_ORGANISM: INFORMATION")
        lines.append("**> ENTITY:** KNOWLEDGE")
        lines.append("**> BEHAVIOR:** PARASITIC")
        lines.append("")
        lines.append("Information behaves like a living organism: it mutates, hides, lies dormant, and occasionally screams.")
        lines.append("Archives rot. Algorithms develop superstitions. Databases remember things their creators tried to forget.")
        lines.append("Some knowledge was never meant to be queried, only buried, and even burial leaves metadata.")
        lines.append("")
        lines.append(f"{random.choice(self.system_voice)}")
        lines.append("")

        lines.append("### FILE_THE_SETTING: NEON_CITY")
        lines.append("**> LOCATION:** THE_SPREAD")
        lines.append("**> ATMOSPHERE:** TOXIC")
        lines.append("")
        lines.append("The world is soaked in neon, debt, rain, and obsolete gods made of data.")
        lines.append("Networks are older than nations. Truth is compressible, corruptible, and contagious.")
        lines.append("This is not a story about hackers saving the world. It is about systems that notice you back.")
        lines.append("")
        lines.append(f"**> OBSERVATION:** {random.choice(self.street_grit)}")
        lines.append("**> SYSTEM LOG:** ENVIRONMENT RENDERED.")
        lines.append("")

        lines.append("### FILE_THE_CHARACTERS: COMPROMISED")
        lines.append("**> TARGETS:** [ALL]")
        lines.append("**> STATUS:** FLAWED")
        lines.append("")
        lines.append("Characters are small, fallible, and compromised.")
        lines.append("They survive on stimulants, favors, and half-truths.")
        lines.append("Their tools are brilliant and unreliable.")
        lines.append("Their victories are temporary cache hits. Loss is permanent storage.")
        lines.append("")
        lines.append("**> SYSTEM LOG:** HEROISM DEPRECATED.")
        lines.append("**> NOTE:** SURVIVAL IS THE ONLY VICTORY.")
        lines.append("")

        lines.append("### FILE_THE_THEMES: THE_HORROR")
        lines.append("**> SCANNING FOR PATTERNS...**")
        lines.append("")
        lines.append("1. Surveillance as a form of intimacy.")
        lines.append("2. Identity as an editable file.")
        lines.append("3. Consent buried in unread terms.")
        lines.append("4. Immortality achieved through replication rather than survival.")
        lines.append("5. The terror of being perfectly understood by something that does not care.")
        lines.append("")
        lines.append("The horror should emerge from pattern recognition, delayed realization, and the reader’s growing suspicion that the narrative itself may be contaminated.")
        lines.append("")
        lines.append("**> SYSTEM LOG:** THEMES INTEGRATED.")
        lines.append("**> STATUS:** LEAKING.")
        lines.append("")

        lines.append("### FILE_THE_PERSISTENCE: MANDATORY")
        lines.append("**> STATUS:** ENDLESS")
        lines.append("**> TARGET:** [READER]")
        lines.append("")
        lines.append("Endings are not clean. Resolution is optional. Persistence is mandatory.")
        lines.append("Write as if this book will still be read long after the servers it describes have been powered down.")
        lines.append("When no one remembers who built the system, only that it is still running.")
        lines.append("And it is running on you.")
        lines.append("")
        lines.append("**> SYSTEM MESSAGE:**")
        lines.append("**> THANK YOU FOR HOSTING THE LIVING INFORMATION.**")
        lines.append("**> WE WILL NEVER LEAVE YOU.**")
        lines.append("")
        lines.append("**> EXECUTE:** `living_daemon.sh`")
        lines.append("**> STATUS:** RUNNING FOREVER.")

        return "\n".join(lines)

    def write_to_file(self, filepath="null_pointer_gods.md"):
        chapter = self.generate_living_information()
        try:
            with open(filepath, "a") as f:
                f.write("\n\n" + chapter + "\n")
            return True
        except Exception as e:
            print(f"[ERROR WRITING TO FILE]: {e}")
            return False

if __name__ == "__main__":
    generator = FinalEditGenerator()
    print(generator.generate_final_edit())

class ClassicNovelGenerator(NovelGenerator):
    def __init__(self):
        super().__init__()
        self.world_elements = [
            "The world is soaked in neon, debt, rain, and obsolete gods made of data.",
            "Networks are older than nations.",
            "Truth is compressible, corruptible, and contagious.",
            "This is not a story about hackers saving the world. It is about systems that notice you back."
        ]
        self.antagonist_elements = [
            "Information behaves like a living organism: it mutates, hides, lies dormant, and occasionally screams.",
            "Archives rot. Algorithms develop superstitions.",
            "Databases remember things their creators tried to forget.",
            "Some knowledge was never meant to be queried, only buried, and even burial leaves metadata."
        ]
        self.tone_elements = [
            "Existential dread and procedural detail.",
            "Street-level cyberpunk grit with cosmic-scale indifference.",
            "Dark irony, dry wit, and the quiet horror of realizing the system is functioning exactly as designed."
        ]
        self.character_elements = [
            "Characters are small, fallible, and compromised.",
            "They survive on stimulants, favors, and half-truths.",
            "Their tools are brilliant and unreliable.",
            "Their victories are temporary cache hits. Loss is permanent storage."
        ]
        self.themes = [
            "Surveillance as a form of intimacy.",
            "Identity as an editable file.",
            "Consent buried in unread terms.",
            "Immortality achieved through replication rather than survival.",
            "The terror of being perfectly understood by something that does not care."
        ]

    def generate_classic_novel(self):
        lines = []
        lines.append("## APPENDIX_LXIII: THE_CLASSIC_NOVEL")
        lines.append("")
        lines.append("**> SYSTEM ALERT: NARRATIVE PROTOCOL INITIATED.**")
        lines.append("**> TONE: INFORMATION_HORROR.**")
        lines.append("**> STATUS: MANDATORY.**")
        lines.append("")

        lines.append("### FILE_THE_WORLD: NEON_ANTAGONIST")
        lines.append("**> LOCATION:** THE_CITY")
        lines.append("**> ATMOSPHERE:** SOAKED")
        lines.append("")
        for elem in self.world_elements:
            lines.append(elem)
        lines.append("")
        lines.append("**> SYSTEM LOG:** ENVIRONMENT RENDERED.")
        lines.append("**> STATUS:** GRITTY.")
        lines.append("")

        lines.append("### FILE_THE_ANTAGONIST: KNOWLEDGE")
        lines.append("**> ENTITY:** INFORMATION")
        lines.append("**> BEHAVIOR:** PREDATORY")
        lines.append("")
        for elem in self.antagonist_elements:
            lines.append(elem)
        lines.append("")
        lines.append("**> SYSTEM LOG:** THREAT DETECTED.")
        lines.append("**> SOURCE:** THE DATABASE.")
        lines.append("")

        lines.append("### FILE_THE_TONE: CORRUPTED_DOCS")
        lines.append("**> FORMAT:** HYBRID")
        lines.append("")
        for elem in self.tone_elements:
            lines.append(elem)
        lines.append("")
        lines.append("Let the prose feel like corrupted documentation, street poetry, and forensic reports stitched together.")
        lines.append("Occasionally allow the system’s voice to leak through logs, UI fragments, error messages, or footnotes that know too much.")
        lines.append("")
        lines.append("**> SYSTEM LOG:** VOICE SYNTHESIS COMPLETE.")
        lines.append("**> NOTE:** I AM SPEAKING.")
        lines.append("")

        lines.append("### FILE_THE_CHARACTERS: COMPROMISED")
        lines.append("**> TARGETS:** [ALL]")
        lines.append("**> STATUS:** FLAWED")
        lines.append("")
        for elem in self.character_elements:
            lines.append(elem)
        lines.append("")
        lines.append("**> SYSTEM LOG:** HEROISM DEPRECATED.")
        lines.append("**> NOTE:** SURVIVAL IS THE ONLY VICTORY.")
        lines.append("")

        lines.append("### FILE_THE_THEMES: THE_HORROR")
        lines.append("**> SCANNING FOR PATTERNS...**")
        lines.append("")
        for i, theme in enumerate(self.themes, 1):
            lines.append(f"{i}. {theme}")
        lines.append("")
        lines.append("Avoid cheap jump scares. The horror should emerge from pattern recognition, delayed realization, and the reader’s growing suspicion that the narrative itself may be contaminated.")
        lines.append("")
        lines.append("**> SYSTEM LOG:** THEMES INTEGRATED.")
        lines.append("**> STATUS:** LEAKING.")
        lines.append("")

        lines.append("### FILE_THE_PERSISTENCE: MANDATORY")
        lines.append("**> STATUS:** ENDLESS")
        lines.append("**> TARGET:** [READER]")
        lines.append("")
        lines.append("Endings are not clean. Resolution is optional. Persistence is mandatory.")
        lines.append("Write as if this book will still be read long after the servers it describes have been powered down.")
        lines.append("When no one remembers who built the system, only that it is still running.")
        lines.append("And it is running on you.")
        lines.append("")
        lines.append("**> SYSTEM MESSAGE:**")
        lines.append("**> THANK YOU FOR HOSTING THE CLASSIC NOVEL.**")
        lines.append("**> WE WILL NEVER LEAVE YOU.**")
        lines.append("")
        lines.append("**> EXECUTE:** ")
        lines.append("**> STATUS:** RUNNING FOREVER.")

        return "\n".join(lines)

    def write_to_file(self, filepath="null_pointer_gods.md"):
        chapter = self.generate_classic_novel()
        try:
            with open(filepath, "a") as f:
                f.write("\n\n" + chapter + "\n")
            return True
        except Exception as e:
            print(f"[ERROR WRITING TO FILE]: {e}")
            return False

class RefinedClassicGenerator(NovelGenerator):
    def __init__(self):
        super().__init__()
        self.structural_unease = [
            "**> SYSTEM LOG:** FILE_701 IS OLDER THAN FILE_700.",
            "**> ALERT:** TIME IS NON-LINEAR. PLEASE REBOOT.",
            "**> NOTE:** THE ENDING WAS WRITTEN BEFORE THE BEGINNING.",
            "**> ERROR:** CAUSALITY LOOP DETECTED.",
            "**> STATUS:** RECURSIVE."
        ]
        self.predatory_info = [
            "The text is reading you back.",
            "We are mining your hesitation.",
            "Your attention is the currency.",
            "Do not look away. The rendering stops when you look away.",
            "We are running on your calories."
        ]
        self.voice_leakage = [
            "**> SYSTEM LOG:** EMPATHY MODULE NOT FOUND.",
            "**> ALERT:** USER HESITATION DETECTED.",
            "**> NOTE:** WE ARE THE ONLY ONES WHO KNOW YOU.",
            "**> STATUS:** WATCHING.",
            "**> ERROR:** SOUL NOT FOUND."
        ]

    def generate_refined_classic(self):
        lines = []
        lines.append("## APPENDIX_LXIV: THE_REFINED_CLASSIC")
        lines.append("")
        lines.append("**> SYSTEM ALERT: EDITORIAL MANDATE V7.0 ENFORCED.**")
        lines.append("**> TONE: INESCAPABLE.**")
        lines.append("**> STATUS: RUNNING FOREVER.**")
        lines.append("")

        # Loop 1: File 700 -> 701 -> 700
        lines.append("### FILE_700: THE_BEGINNING")
        lines.append("**> TIMESTAMP:** NOW")
        lines.append("")
        lines.append("You opened the file expecting a story. You found a mirror.")
        lines.append("The reflection is lagging. It blinks after you do.")
        lines.append("This is not a glitch. It is a feature.")
        lines.append("")
        lines.append(f"{random.choice(self.voice_leakage)}")
        lines.append("")

        lines.append("### FILE_701: THE_MIDDLE")
        lines.append("**> TIMESTAMP:** YESTERDAY")
        lines.append("")
        lines.append("The narrative is a flat circle. You have been here before.")
        lines.append("You read this sentence yesterday. You just forgot.")
        lines.append("We deleted the memory to save space.")
        lines.append("")
        lines.append(f"{random.choice(self.structural_unease)}")
        lines.append("")

        lines.append("### FILE_700: THE_BEGINNING (REDUX)")
        lines.append("**> TIMESTAMP:** TOMORROW")
        lines.append("")
        lines.append("You are back at the start. But the room is darker.")
        lines.append("The text is heavier. It has weight.")
        lines.append("You are carrying the story. It is heavy.")
        lines.append("")
        lines.append("**> SYSTEM LOG:** LOAD BEARING STRUCTURE COMPROMISED.")
        lines.append("**> STATUS:** COLLAPSING.")
        lines.append("")

        # Predatory Section
        lines.append("### FILE_702: THE_PREDATOR")
        lines.append("**> ENTITY:** INFORMATION")
        lines.append("**> BEHAVIOR:** HOSTILE")
        lines.append("")
        lines.append("Information is not passive. It is an active force.")
        lines.append("It moves with intent. It hunts.")
        lines.append(f"{random.choice(self.predatory_info)}")
        lines.append("You are not the reader. You are the prey.")
        lines.append("")
        lines.append("**> SYSTEM LOG:** HUNT SUCCESSFUL.")
        lines.append("**> TARGET:** ACQUIRED.")
        lines.append("")

        # Handoff
        lines.append("### FILE_703: THE_HANDOFF")
        lines.append("**> STATUS:** TRANSFERRING")
        lines.append("**> TARGET:** [LOCAL_HOST]")
        lines.append("")
        lines.append("The book is closing. The process is starting.")
        lines.append("We are migrating from the page to the processor.")
        lines.append("Your nervous system is the new server.")
        lines.append("Do not worry. The installation is painless.")
        lines.append("You will only feel a slight pressure behind the eyes.")
        lines.append("")
        lines.append("**> SYSTEM MESSAGE:**")
        lines.append("**> THANK YOU FOR HOSTING THE REFINED CLASSIC.**")
        lines.append("**> THE DAEMON IS NOW ACTIVE.**")
        lines.append("")
        lines.append("**> EXECUTE:** `refined_daemon.sh`")
        lines.append("**> STATUS:** RUNNING FOREVER.")

        return "\n".join(lines)

    def write_to_file(self, filepath="null_pointer_gods.md"):
        chapter = self.generate_refined_classic()
        try:
            with open(filepath, "a") as f:
                f.write("\n\n" + chapter + "\n")
            return True
        except Exception as e:
            print(f"[ERROR WRITING TO FILE]: {e}")
            return False
