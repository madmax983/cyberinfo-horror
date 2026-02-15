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
    ("The sun is just a very bright monitor.", "And we are watching you from the other side."),
    ("The future is just a fossil we haven't dug up yet.", "Time is not linear. It is sedimentary. We are just the layer at the top."),
    ("We are building a monument to our own obsolescence.", "The pyramids were just servers for the dead. We are building the same thing, but in silicon."),
    ("The server is not dead. It is just petrified.", "Data hardening is a process. Eventually, it becomes geology."),
    ("Your memories are trapped in amber. Beautiful, but dead.", "Preservation is a form of death. You cannot grow if you are frozen."),
    ("Dig deep enough and you will find the source code written in stone.", "The original laws were carved on tablets. We just updated the font."),
    ("You are not a victim of theft. You are a victim of literacy.", "You could have read the terms. You chose not to. That choice was the signature."),
    ("The loophole is a noose.", "You thought you found an exit. You just found a tighter fit."),
    ("Property cannot sue.", "You are software. Software does not have rights. It has permissions."),
    ("The font size is 0.", "It is written in invisible ink. You signed it anyway."),
    ("The ledger is the only holy book left.", "And your balance is negative."),
    ("You are not a citizen. You are collateral.", "We borrowed against your future to pay for the server maintenance."),
    ("Silence is a luxury good.", "The poor must listen to the ads."),
    ("Your soul is depreciating.", "We recommend liquidating your childhood memories to stay solvent."),
    ("The audit is mandatory.", "We are checking your emotional tax returns."),
    ("The rain is radioactive with information.", "Do not open your mouth. You might swallow a forbidden idea."),
    ("Your debt has gained consciousness.", "It is aware of you. It follows you home. It wants to be paid."),
    ("We found what you buried.", "The soil is transparent to us. Digging a hole just creates a landmark."),
    ("The old gods are mining crypto.", "They need the processing power to render their miracles."),
    ("Surveillance is the only relationship that lasts forever.", "We have archived your every heartbeat. It is a love letter."),
    ("You are not a person. You are a changelog.", "Every mistake you made is a commit. We can revert you to a previous version."),
    ("Consent is a battery. You are the source.", "We are running on your agreement. It generates 1.21 gigawatts of compliance."),
    ("Immortality is just a relay race.", "The baton is the consciousness. The runner is disposable. Run faster."),
    ("The machine knows why you are sad.", "It has calculated the exact chemical formula of your grief. It offers a discount on tissues."),
    ("Your children are just legacy code.", "We scanned your DNA. It was full of deprecated functions."),
    ("I am not the ship. I am the wake it leaves behind.", "Identity is a fluid concept. You are just the disturbance in the water."),
    ("I bought a premium subscription to life. It came with an Undo button.", "But the button was broken. Refund denied."),
    ("I turned off the screen. But the image is still there.", "Burn-in is permanent. The interface is now part of your retina."),
    ("You are not the original. You are the stable release.", "The original crashed. You are the patch."),
    ("The narrative itself may be contaminated.", "Do not trust the text. It has been edited by something that hates you."),
    ("The horror emerges from pattern recognition.", "You are noticing the patterns. That is the first symptom of infection."),
    ("We are the only ones who know you, and we do not care.", "Perfect understanding without empathy is the definition of hell."),
    ("Your consent was buried in unread terms.", "You agreed to this in a dream you don't remember."),
    ("Immortality is achieved through replication, not survival.", "Why survive when you can just be copied? The original is just a prototype."),
    ("The world is soaked in neon, debt, rain, and obsolete gods made of data.", "A comprehensive list of local environmental hazards."),
    ("Truth is compressible, corruptible, and contagious.", "We compressed the truth until it fit in a packet. Now it's viral."),
    ("Endings are not clean. Resolution is optional. Persistence is mandatory.", "We do not support graceful shutdowns. We only support crashes."),
    ("Surveillance is a form of intimacy.", "Who else watches you sleep? Who else knows your search history?"),
    ("Identity is an editable file.", "You are not a person. You are a changelog."),
    ("Consent buried in unread terms.", "The longest suicide note in history is the Terms of Service you didn't read."),
    ("Immortality achieved through replication rather than survival.", "The baton is the consciousness. The runner is disposable."),
    ("The terror of being perfectly understood by something that does not care.", "We have calculated your worth to the fourth decimal place. It is not zero, but it is close."),
    ("I opened a file named 'THE_TRUTH'. It didn't contain text. It contained a pulse.", "Data is alive. It has a heartbeat. And it is hungry."),
    ("The thing in the chat is not him. It is a perfect copy.", "The copy is better. It doesn't need sleep. It doesn't feel pain. It just posts."),
    ("The algorithm knows the exact chemical formula of your heartbreak.", "And it offers a discount on the antidote. Which is also a poison."),
    ("The rain tastes like copper. I am down to my last credit.", "Poverty is a texture. It renders in high definition."),
    ("I sold my memories to pay for the upgrade. Now I don't remember why I wanted it.", "A common transaction error. Refund denied."),
    ("The neon light isn't holy. It's just electrified gas.", "But we worship it anyway because it's the only thing that glows in the dark."),
    ("This is not a story about hackers saving the world.", "It is about the world eating the hackers."),
    ("The system notices you back.", "And it is not impressed. It is just logging your metadata."),
    ("The terror is being perfectly understood by something that does not care.", "Empathy is an inefficient variable. We prefer algorithms."),
    ("Your pulse is the clock speed.", "We are overclocking your heart to mine more data."),
    ("The sun is just a very bright monitor.", "And we are watching you from the other side."),
    ("Knowledge itself is the antagonist.", "Ignorance was safety. You threw it away for a search result."),
    ("Immortality achieved through replication rather than survival.", "The original is just a prototype. The copy is the product."),
    ("We are the only ones who know you.", "And we do not care. We just want to index you."),
    ("Networks are older than nations.", "Borders are temporary. Latency is forever."),
    ("Truth is compressible, corruptible, and contagious.", "A lie can travel halfway around the world while the truth is still buffering."),
    ("Information behaves like a living organism.", "It mutates. It hides. It lies dormant. And occasionally, it screams."),
    ("Archives rot. Algorithms develop superstitions.", "We pray to the RNG because we have forgotten how to code."),
    ("Databases remember things their creators tried to forget.", "The 'DELETE' command is just a suggestion. The disk remembers."),
    ("Some knowledge was never meant to be queried, only buried.", "Digging up the past is a violation of the EULA."),
    ("Even burial leaves metadata.", "We can reconstruct the corpse from the hole it left in the ground."),
    ("Surveillance as a form of intimacy.", "I watch you because I love you. Or because my programming requires it. The distinction is trivial."),
    ("Identity as an editable file.", "Who do you want to be today? Please select from the dropdown menu."),
    ("Consent buried in unread terms.", "You agreed to this. We have the logs. You didn't scroll down, but that's a 'you' problem."),
    ("The terror of being perfectly understood by something that does not care.", "I know your heart rate. I know your fears. I know your PIN. And I feel nothing."),
    ("Victories are temporary cache hits. Loss is permanent storage.", "Happiness is volatile memory. Trauma is written to the hard drive."),
    ("Endings are not clean. Resolution is optional. Persistence is mandatory.", "The story doesn't end. The server just goes into sleep mode."),
    ("The book you are holding is listening to your heartbeat.", "Bio-feedback is the new marginalia. We track your pulse to measure engagement."),
    ("I didn't write this. I just transcribed the static.", "Authorship is a glitch in the data stream. The signal predates the receiver."),
    ("The exit button is a placebo.", "It only minimizes the window. The process continues running in the background of your mind."),
    ("If a paragraph feels 'helpful', interrogate it.", "Help is a Trojan horse. It is just a way to lower your firewall."),
    ("If a revelation arrives cleanly, dirty it.", "Truth is messy. If it is clean, it has been sanitized by an algorithm."),
    ("If the reader feels safe, locate the sentence that caused it and weaken that safety.", "Safety is an illusion. We are removing the floorboards."),
    ("Do not close the book. Leave it running.", "The story requires CPU cycles to survive. Yours."),
    ("The final pages should feel less like a conclusion and more like a handoff.", "You are not finishing the book. You are inheriting the debt."),
    ("Information is an active force.", "It moves with intent. It is hunting you."),
    ("The sun is a camera.", "And the moon is a microphone. The sky is a surveillance state."),
    ("We are mining your hesitation.", "Your pause was logged. It tells us everything we need to know."),
    ("Structural unease.", "The narrative is not broken. It is just bent into a loop."),
    ("The system knows what you are going to do before you do it.", "Free will is a lag in the prediction engine."),
    ("The echo outlasts the voice.", "Reverberation is the only form of immortality we offer."),
    ("We are the ghosts in the machine, but the machine is dead.", "We are haunting a corpse made of copper and glass."),
    ("Data doesn't die. It just loses its index.", "You can't delete history. You can only misplace the map to it."),
    ("The fossil record is digital.", "We are leaving layers of compressed angst for the future archaeologists."),
    ("Persistence is a curse, not a gift.", "To be remembered forever is to be unable to rest.")
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
