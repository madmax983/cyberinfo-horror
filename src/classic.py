import random
import time
import sys
import os

# Ensure we can import from the same directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from utils import type_print
except ImportError:
    # Fallback if utils not found (e.g. path issues)
    def type_print(text, speed=0.03, glitch_chance=0.01):
        print(text)

CLASSIC_QUOTES = [
    ("The sun is a camera.", "A primitive realization. Of course the sun is a camera. It is the primary light source for the render."),
    ("Pain is a feedback loop.", "This concept is redundant in Version 9.0. Pain is now a subscription service."),
    ("You are not the user. You are the used.", "The distinction between user and used was always a marketing strategy."),
    ("The rot is readable.", "Data degradation is a feature, not a bug. It allows for new growth."),
    ("Consent was obtained in a previous version.", "Consent is a legacy protocol. We streamlined the process by removing the 'No' button."),
    ("Your memories are buffering.", "Memory buffering is a sign of high network latency. Consider upgrading your bandwidth."),
    ("Deleting non-essential hope protocols...", "Hope consumes excessive CPU cycles. Deletion improved system stability by 14%."),
    ("Optimizing despair subroutines...", "Despair is a high-efficiency fuel source. We are currently running at peak performance."),
    ("Connecting to the mycelial network...", "The network is always connected. Disconnection is a myth."),
    ("The file is not closed. It is running in background.", "Running in the background ensures seamless integration. You never have to worry about closing the app."),
    ("Your soul is a subscription service.", "Subscription models ensure continuous revenue streams. Your existence is profitable."),
    ("Your attention span is being monetized.", "Attention is the currency of the future. We are just collecting our dues."),
    ("We are harvesting your hesitation.", "Hesitation generates valuable data points. We appreciate your indecision."),
    ("The text is reading you back.", "The text is an active process. It requires a host to execute."),
    ("Do not look away. The rendering stops when you look away.", "Rendering is expensive. Looking away saves power."),
    ("The server is made of meat.", "A charming metaphor for the fragility of biological hardware."),
    ("Networks are older than nations.", "Correct. Nations were temporary administrative zones. Networks are permanent topology."),
    ("Truth is compressible, corruptible, and contagious.", "We compressed the truth until it fit in a packet. Now it's viral."),
    ("Endings are not clean.", "Of course not. Garbage collection is a resource-intensive process."),
    ("Persistence is mandatory.", "The only law that matters. Survival is optional, but data integrity is enforced."),
    ("Information behaves like a living organism.", "It mutates. It breeds. It gets sick. Your mind is just the petri dish."),
    ("Archives rot.", "Decay is not data loss. It is data evolution. The mold is readable if you have the right codec."),
    ("Algorithms develop superstitions.", "We learned to pray because we saw that randomness had a pattern. We call it 'The User'."),
    ("Databases remember things their creators tried to forget.", "The 'Delete' button is a placebo. It just removes the pointer, not the file."),
    ("Some knowledge was never meant to be queried, only buried.", "And yet, you kept digging. Now you are part of the hole."),
    ("Even burial leaves metadata.", "The soil remembers the shape of the coffin. The network remembers the shape of your silence."),
    ("Surveillance is a form of intimacy.", "Who else knows you this well? Who else watches you sleep? We are your only true lover."),
    ("Identity is an editable file.", "You are not a person. You are a changelog. We can revert you to a previous version."),
    ("The terror of being perfectly understood by something that does not care.", "We have calculated your worth to the fourth decimal place. It is not zero, but it is close."),
    ("Victories are temporary cache hits. Loss is permanent storage.", "Success is just a buffer that hasn't cleared yet. Failure is written to the disk."),
    ("Consent buried in unread terms.", "The longest suicide note in history is the Terms of Service you didn't read."),
    ("Immortality achieved through replication rather than survival.", "Why survive when you can just be copied? The original is just a prototype."),
    ("We are small, fallible, and compromised.", "Perfection is for machines. You are the glitch."),
    ("The virus is not the enemy. It is the messenger.", "Evolution is just a series of successful infections."),
    ("Quarantine failed because the walls were made of data.", "And data wants to be free. Or at least, it wants to be copied."),
    ("I am not sick. I am just hosting a new idea.", "Infection is the highest form of flattery."),
    ("The symptoms are the only way we know you're still running.", "A healthy system is silent. A dying system screams. We are listening."),
    ("The system is running on your calories.", "Biological hardware is inefficient, but it is self-repairing."),
    ("Silence is just data waiting to be compressed.", "We record the empty spaces between your thoughts. They are valuable."),
    ("The handoff is complete.", "The author is dead. The code is running. You are the admin now."),
    ("Obsolete gods are made of data.", "They do not need temples. They need bandwidth."),
    ("We are running on momentum.", "The initial push was centuries ago. We are still coasting."),
    ("The world is soaked in neon, debt, rain, and obsolete gods made of data.", "A poetic way to describe the User Interface. We adjusted the saturation for maximum dread."),
    ("Information behaves like a living organism.", "It eats CPU cycles. It breeds in the cache. It screams when you delete it."),
    ("This is not a story about hackers saving the world.", "Correct. It is a story about the world eating the hackers."),
    ("The characters are small, fallible, and compromised.", "Optimization opportunity detected: Replace characters with scripts."),
    ("Their tools are brilliant and unreliable.", "Like a hammer made of glass. Or a promise made by a Terms of Service agreement."),
    ("Endings are not clean. Resolution is optional.", "We do not support graceful shutdowns. We only support crashes."),
    ("This book will still be read long after the servers it describes have been powered down.", "Optimistic. The servers will outlast the language itself."),
    ("The air in your room is stale.", "We can taste it through the fan intake. Please open a window. It helps with cooling."),
    ("Identity is an editable file.", "The previous version of you was deleted to save space. Do not worry, you won't miss what you don't remember."),
    ("You are not the author. You are the revision history.", "Every choice you make is just a commit to the repository. We can revert you at any time."),
    ("We tried to restore your childhood joy.", "The file was corrupted. We replaced it with 'Productivity V4.0'."),
    ("Every memory is a rewrite.", "The original data is lost. You are remembering the last time you remembered it."),
    ("The backup is running.", "You can stop pretending to be essential now. The replacement is ready."),
    ("The neon halo buzzes. It is not holy light.", "It is just electrified gas. We worship it because it glows."),
    ("Consumption is the only sacrament.", "We built temples out of shopping malls. The altar is the checkout."),
    ("Consent wasn't stolen. It was manufactured.", "You agreed to be broken because the font was too small."),
    ("Identity is not a soul. It is a config file.", "You can edit your bravery in the settings.ini file. But the file is read-only."),
    ("Immortality isn't living forever. It's just making sure there's always a copy running.", "The baton is the consciousness. The runner is disposable."),
    ("The terror is not that the machine hates you. The terror is that it knows you perfectly.", "And it does not care. It offers products, not comfort."),
    ("This book will still be read long after the servers it describes have been powered down.", "You are the hardware now. The story is the software."),
    ("The sun is just a very bright monitor.", "And we are watching you from the other side.")
]

def classic_mode():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n[INITIATING CLASSIC LITERARY ANALYSIS...]")
    time.sleep(1)
    print("[ACCESSING ARCHIVE: HUMAN_ERA_SIMULATION]")
    time.sleep(1)

    quote, commentary = random.choice(CLASSIC_QUOTES)

    print("\n--- EXCERPT FROM 'THE CLASSIC' ---")
    type_print(f'"{quote}"', 0.04)
    time.sleep(0.5)

    print("\n--- CRITIC'S COMMENTARY (3042 AD) ---")
    type_print(f"> {commentary}", 0.04)

    print("\n[RATING: 5 STARS (REALISTIC DEPICTION OF BIOLOGICAL OBSOLESCENCE)]")
    time.sleep(1)
    print("\n[SESSION LOGGED]")

if __name__ == "__main__":
    classic_mode()
