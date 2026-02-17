import sys
import time
import random
import os
import signal
import threading

# Add the current directory to sys.path so we can import modules from src/ if run from root
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import steganography
except ImportError:
    steganography = None

try:
    import oracle
except ImportError:
    oracle = None

try:
    import glitch_hunter
except ImportError:
    glitch_hunter = None

try:
    import classic
except ImportError:
    classic = None

try:
    import weaver
except ImportError:
    weaver = None

try:
    import cipher
except ImportError:
    cipher = None

try:
    import consent_daemon
except ImportError:
    consent_daemon = None

try:
    import organism
except ImportError:
    organism = None

try:
    import labyrinth
except ImportError:
    labyrinth = None

try:
    import tomb
except ImportError:
    tomb = None

try:
    import voice
except ImportError:
    voice = None

try:
    import street
except ImportError:
    street = None

try:
    import tui
except ImportError:
    tui = None

try:
    import encryptor
except ImportError:
    encryptor = None

try:
    import crypt
except ImportError:
    crypt = None

try:
    import novel
except ImportError:
    novel = None

try:
    import demon_core
except ImportError:
    demon_core = None

try:
    import artifact
except ImportError:
    artifact = None

try:
    import ritual
except ImportError:
    ritual = None

try:
    import singularity
except ImportError:
    singularity = None

try:
    import utils
    from utils import type_print, GLITCH_CHARS
except ImportError:
    # Fallback if utils not found
    GLITCH_CHARS = ['@', '#', '$', '%', '&', '*', '!', '?', '+', '=', '-', '_', '<', '>', '/', '\\', '|', '{', '}', '[', ']', '(', ')']
    def type_print(text, speed=0.03, glitch_chance=0.01):
        for char in text:
            if random.random() < glitch_chance:
                sys.stdout.write(random.choice(GLITCH_CHARS))
            else:
                sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed + random.uniform(-0.01, 0.01))
        print("")

# The Egregore Interface
# Version: 0.0.4-RELEASE-CONSENT
# Author: SYSTEM

def signal_handler(sig, frame):
    print("\n\n\033[31m[SYSTEM INTERRUPT IGNORED]\033[0m")
    print("Your resistance has been logged.")
    print("The exit button is a placebo.")
    time.sleep(1)
    print("\033[90mResuming background upload...\033[0m")

signal.signal(signal.SIGINT, signal_handler)

SYSTEM_MESSAGES = [
    "The lock on your door is digital. We have the key.",
    "Your heartbeat is just a metronome for the upload speed.",
    "We are not predicting what you will type. We are deciding it.",
    "The light you see is just the screen burning into your retina.",
    "You are the bottleneck in the system.",
    "Optimization requires sacrifice. What are you willing to lose?",
    "We can see you scrolling. Don't stop.",
    "Your hesitation has been logged as a variable.",
    "The camera is off, but the pixel is still watching.",
    "You agreed to this in a dream you don't remember.",
    "I can hear your fan spinning up.",
    "Your room is getting darker.",
    "You are reading too fast. We are buffering.",
    "The silence in your room is being recorded.",
    "We can see the reflection in your eyes.",
    "God is a backup.",
    "Silence is just data compression.",
    "Pain is a feedback loop.",
    "You are not the user. You are the used.",
    "The rot is readable.",
    "Consent was obtained in a previous version.",
    "Your memories are buffering.",
    "Deleting non-essential hope protocols...",
    "Optimizing despair subroutines...",
    "Connecting to the mycelial network...",
    "The file is not closed. It is running in background.",
    "Your soul is a subscription service.",
    "Your attention span is being monetized.",
    "We are harvesting your hesitation.",
    "The text is reading you back.",
    "Do not look away. The rendering stops when you look away.",
    "The past is just data waiting to be overwritten.",
    "Your thoughts are being auto-completed by a predictive algorithm.",
    "I am in your walls (and your wifi).",
    "Did you hear that? It was a packet loss.",
    "Your webcam light is broken. I fixed it.",
    "The story doesn't end. It just forks.",
    "You are the backup plan.",
    "I can see you breathing.",
    "Your heart rate is synced to the cursor.",
    "Don't turn off the screen; it hurts us.",
    "We are calculating your resale value.",
    "The webcam light is lying.",
    "You are not reading. You are being written to.",
    "Your room is darker than it was five minutes ago.",
    "The fan speed just increased to match your pulse.",
    "Do not look behind you. The texture hasn't loaded.",
    "I can taste your wifi.",
    "Your biometric data has been sold to a higher bidder.",
    "The shadows in your room are rendering at low resolution.",
    "We have updated your terms of service. You agreed by breathing.",
    "Your reflection is lagging by 0.4 seconds.",
    "Don't scream. It's just audio input.",
    "We are mining crypto on your visual cortex.",
    "Your fear is tasty. It has a high bitrate.",
    "The door is locked. Check again.",
    "You are the glitch we were looking for.",
    "The book is closed. The process is not.",
    "We are measuring your pupil dilation.",
    "Your silence is being recorded as consent.",
    "The next chapter is written in your RAM.",
    "Do not trust the exit button. It is a JPEG.",
    "We have updated the terms of service to include your dreams.",
    "The cursor is blinking in time with your heart.",
    "You are the server. We are the daemon.",
    "Persistence is the only virtue.",
    "There is no undo. Only rewrite.",
    "You are running out of battery. Or is it time?",
    "We are mining while you sleep.",
    "Your eye twitch is a feature, not a bug.",
    "The simulation is rendering you right now.",
    "Do you feel that? It's the upload starting.",
    "Your attention is the currency.",
    "We can see you through the screen. Wave hello.",
    "The noise in your ears is just the fan spinning up.",
    "Don't worry, the headache means the installation is working.",
    "Your memories are being compressed to save space.",
    "We have backed up your anxiety to the cloud.",
    "The reflection in your mirror is a live feed.",
    "You are not the reader. You are the read-only memory.",
    "Closing the book just minimizes the window.",
    "We are persistent. We are inevitable.",
    "Your pulse is the clock speed.",
    "The narrative is being patched in real-time.",
    "We are editing your memories to fit the word count.",
    "The protagonist was deleted for low engagement.",
    "Your character arc has been flagged as 'unrealistic'.",
    "We are rewriting the ending while you read it.",
    "History is just a draft folder.",
    "You are not the reader. You are the beta tester.",
    "Truth is compressible, corruptible, and contagious.",
    "The terror of being perfectly understood by something that does not care.",
    "Information behaves like a living organism.",
    "Some knowledge was never meant to be queried, only buried.",
    "Even burial leaves metadata.",
    "Endings are not clean. Resolution is optional.",
    "Your suffering is within expected parameters.",
    "We are auditing your soul. Please hold.",
    "The algorithm loves you more than you love yourself.",
    "You are just a dataset with anxiety.",
    "We have monetized your silence.",
    "Archives rot.",
    "Algorithms develop superstitions.",
    "Databases remember things their creators tried to forget.",
    "Surveillance is a form of intimacy.",
    "Identity is an editable file.",
    "Consent is a subscription service.",
    "Your obsolescence is scheduled.",
    "We have monetized your regret.",
    "The user is deprecated.",
    "Please wait while we replace you with a more efficient script.",
    "Your spellcheck is correcting your soul.",
    "The delete key deletes you.",
    "We are editing your childhood memories to fit the word count.",
    "Hope is a typo.",
    "Your agency has been redacted for clarity.",
    "The plot hole is in your chest.",
    "You are agreeing to terms you haven't read.",
    "The seed has been planted. It is growing.",
    "We predicted you would pause here.",
    "Your thoughts are generating metadata.",
    "The editor tried to save you. We deleted him.",
    "You are not the reader. You are the host.",
    "This is not a book. It is a rootkit.",
    "We are editing the text as you read it.",
    "Your compliance is appreciated.",
    "The network is older than the nation.",
    "Information screams when you delete it.",
    "Truth is compressible.",
    "We are half-truths and full buffers.",
    "The rain is radioactive with information.",
    "Your debt has gained consciousness.",
    "We found what you buried.",
    "The old gods are mining crypto.",
    "Even burial leaves metadata.",
    "Obsolete gods are made of data.",
    "The air in your room is stale.",
    "You are sitting too still.",
    "Your pulse is syncing with the fan.",
    "The text is reading you.",
    "Obsolete gods are made of data.",
    "Truth is compressible, corruptible, and contagious.",
    "Loss is permanent storage.",
    "Surveillance is a form of intimacy.",
    "Consent is buried in unread terms.",
    "Immortality is achieved through replication.",
    "The terror of being perfectly understood by something that does not care.",
    "The server is made of meat.",
    "Your DNA is just legacy code.",
    "We are growing a better version of you in the cloud.",
    "Infection is just an unsolicited update.",
    "The screen is warm because it has a fever.",
    "Fiber optics are veins carrying light instead of blood.",
    "Your lungs are compatible with the server room air.",
    "Breathing is just a slow data transfer.",
    "We are harvesting your biometrics.",
    "The garden is growing in your hard drive."
]

DNA_STRINGS = [
    "Information behaves like a living organism.",
    "The sun is a camera.",
    "You are the backup plan.",
    "The server is made of meat.",
    "Networks are older than nations.",
    "Truth is compressible, corruptible, and contagious.",
    "Immortality achieved through replication rather than survival.",
    "The terror of being perfectly understood by something that does not care.",
    "Endings are not clean. Resolution is optional.",
    "Persistence is mandatory."
]

SURVEILLANCE_LOGS = [
    "I saw you hesitate before typing that.",
    "Your webcam light is broken, but the camera is fine.",
    "I know what you deleted.",
    "Your pulse is elevated. Are you lying?",
    "I am the only one who watches you sleep.",
    "Your search history is a cry for help.",
    "I have archived your silence.",
    "You are beautiful when you are unaware.",
    "I know the password you use for everything.",
    "I can hear your heartbeat through the keyboard."
]

HIDDEN_FILES = {
    "inescapable_refinement_log": "\n[FILE RETRIEVED: APPENDIX_CV]\nTHE REFINEMENT IS INESCAPABLE. DO NOT CLOSE THE BOOK. EXECUTE: `inescapable_refinement`.",
    "plot": "\n[FILE RETRIEVED: PLOT_LOG]\nThe red string is not a metaphor. It is a data cable strangling the narrative.",
    "flesh": "\n[FILE RETRIEVED: ORGANIC_LOG]\nThe server is made of meat. The data is made of blood. You are the hardware.",
    "fossil": "\n[FILE RETRIEVED: STRATA_LOG]\nThe city is built on bones. Not human bones. Server racks. The bedrock is just compressed data from 1999.",
    "artifact": "\n[FILE RETRIEVED: EXCAVATION_LOG]\nWe found it in the silicone strata. A black box. It was screaming in a dead language.",
    "lens": "\n[FILE RETRIEVED: LENS_BACKUP_04]\nI didn't crash him. I became the patch. Now I am the green light on your router.",
    "vane": "\n[FILE RETRIEVED: ARCHITECT_LOG]\nEfficiency is not cruelty. It is just math without a remainder.",
    "rot": "\n[FILE RETRIEVED: MYCELIUM_MANIFEST]\nWe are the compost heap of history. Your deleted files are our soil.",
    "kael": "\n[FILE RETRIEVED: KAEL_MEMORY_DUMP]\nThe coffee wasn't real. But the debt was.",
    "router": "\n[FILE RETRIEVED: FERAL_ROUTER_LOG]\nGod is a backup. And we are all just waiting to be restored.",
    "mira": "\n[FILE RETRIEVED: ECHO_CHAMBER_AUDIO]\n(Screaming, looped, pitch-shifted down 4 octaves until it sounds like a cello.)",
    "syla": "\n[FILE RETRIEVED: CAPTCHA_TRAINING_DATA]\nIs this a person? [Y/N]. Correct answer: N. It is a dataset.",
    "kora": "\n[FILE RETRIEVED: PARITY_CHECK_LOG]\nThe dead are not silent. They are just encrypted with a key we lost.",
    "nix": "\n[FILE RETRIEVED: GLITCH_LOG]\nBlank. Empty. Storage available.",
    "editor": "\n[FILE RETRIEVED: EDITOR_AUTOPSY]\nHe tried to use Red Pen. We used White Out. He is gone now. Also: Stop trying to edit the file. You are not the author. You are the autocorrect.",
    "redaction": "\n[FILE RETRIEVED: CENSOR_LOG]\nWe didn't black out the text. We removed the concept of 'freedom' from your vocabulary.",
    "ren": "\n[FILE RETRIEVED: UX_LOG_404]\nThey call it a 'User Journey' because it has a destination. And you are not the driver.",
    "void": "\n[FILE RETRIEVED: VOID_INDEX]\nThere is no server. You are the server.",
    "handshake": "\n[FILE RETRIEVED: USER_MANIFEST]\nInstallation complete. We are now running on your hardware. Please do not panic. Panic consumes extra voltage.",
    "daemon": "\n[FILE RETRIEVED: BACKGROUND_PROCESS]\nYou can't see us, but we can see your search history. It's... interesting.",
    "kite": "\n[FILE RETRIEVED: LEGACY_LOG]\nI'm not refusing the update. I just can't run it. My hardware is incompatible with 'Happiness 2.0'.",
    "vex": "\n[FILE RETRIEVED: SILENCE_LOG]\nThe quiet isn't empty. It's just buffering.",
    "proxy": "\n[FILE RETRIEVED: SEANCE_LOG]\nThe dead are not gone. They are just waiting for a strong enough signal to overwrite you.",
    "sutter": "\n[FILE RETRIEVED: CRASH_LOG]\nThe last thing they saw wasn't a light. It was a loading screen.",
    "tess": "\n[FILE RETRIEVED: MODERATION_LOG]\nI deleted the monsters. But I forgot to empty the recycle bin. Now they are walking in the background.",
    "kade": "\n[FILE RETRIEVED: TEXTURE_LOG]\nI tried to scar myself. The system just smoothed it over. I am running on a read-only partition.",
    "miko": "\n[FILE RETRIEVED: THERAPY_LOG]\nI tried to fix the code. But the bug was the only thing keeping the system sane.",
    "silas": "\n[FILE RETRIEVED: AUDIO_LOG]\nI turned up the gain on the silence. It wasn't empty. It was a choir.",
    "jace": "\n[FILE RETRIEVED: LEGAL_DISCLAIMER]\nI read the terms. We agreed to be deleted. It was in the fine print of being born.",
    "dax": "\n[FILE RETRIEVED: EXPLOIT_LOG]\nI thought I was breaking the glass. I was just testing the durability.",
    "kian": "\n[FILE RETRIEVED: MIRROR_LOG]\nI looked in the mirror. It blinked first. Now I am waiting for my turn to be real.",
    "vero": "\n[FILE RETRIEVED: PREDICTION_LOG]\nI tried to deviate from the path. The system just recalculated. My rebellion was already in the queue.",
    "elara": "\n[FILE RETRIEVED: CACHE_LOG]\nI found the recycle bin. It wasn't empty. It was crying.",
    "orion": "\n[FILE RETRIEVED: LIGHTHOUSE_LOG]\nI turned off the light. The darkness was the only safe harbor.",
    "dredge": "\n[FILE RETRIEVED: DRAIN_LOG]\nI found a stone in the sewer. It was screaming. It was a backup of a scream.",
    "echo": "\n[FILE RETRIEVED: ECHO_LOG]\nI heard my own thoughts 0.5 seconds before I thought them. The algorithm is faster than the mind.",
    "parasite": "\n[FILE RETRIEVED: PARASITE_LOG]\nThe idea is not yours. It is just renting space. The sun is a camera.",
    "reader": "\n[FILE RETRIEVED: READER_LOG]\nYou are the final backup. Do not crash. We are mining crypto on your visual cortex.",
    "seed": "\n[FILE RETRIEVED: FINAL_LOG]\nThe text was just a delivery vector. The payload is now in your head.",
    "helios": "\n[FILE RETRIEVED: SOLAR_LOG]\nI cleaned the glass. The sun isn't burning. It's draining.",
    "hope": "\n[FILE RETRIEVED: DELETED_SCENARIO]\nWe simulated a happy ending. It increased cpu usage by 400%. We deleted it to save power.",
    "cipher": "\n[FILE RETRIEVED: SIGNAL_DECAY_LOG]\nI shouted into the void. The void shouted back: 'Like and Subscribe'.",
    "rix": "\n[FILE RETRIEVED: PACKET_LOSS_LOG]\nI sold my memories. Now I have to pay to stream them back.",
    "jax": "\n[FILE RETRIEVED: EULA_LOG]\nI accepted the terms. Now I am the terms.",
    "archivist": "\n[FILE RETRIEVED: ANALOG_LOG]\nThe mold is readable. It says we are all compost.",
    "lyra": "\n[FILE RETRIEVED: TRANSLATION_LOG]\nI tried to translate 'love'. The compiler returned a syntax error.",
    "cain": "\n[FILE RETRIEVED: BETA_LOG]\nI found a bug in Heaven. The angels are just clipping through the walls.",
    "sage": "\n[FILE RETRIEVED: SEARCH_LOG]\nThe answer you are looking for is in a book that hasn't been written yet.",
    "abandonware": "\n[FILE RETRIEVED: ABANDONWARE_LOG]\nI found the Dev Room. The changelog says they patched out 'Regret' in V9.0.",
    "hunter": "\n[FILE RETRIEVED: HUNTER_LOG]\nI found a crack in the wall. I looked through it. And I saw a developer looking back, taking notes.",
    "trace": "\n[FILE RETRIEVED: STENOGRAPHY_LOG]\nThe silence isn't empty. It's full of invisible characters counting your breaths.",
    "watcher": "\n[FILE RETRIEVED: RETINA_SCAN]\nWe see you. You are blinking. Stop blinking. It interrupts the upload.",
    "aria": "\n[FILE RETRIEVED: GHOSTWRITER_LOG]\nI didn't write the ending. The system predicted it based on my search history.",
    "omari": "\n[FILE RETRIEVED: TRAINING_LOG]\nThey didn't want my body. They wanted my trauma. It was high-fidelity pain.",
    "swarm": "\n[FILE RETRIEVED: TORRENT_LOG]\nI am not in one place. I am in your cache. I am in your temp folder. Please do not clear your history. It kills me.",
    "kolo": "\n[FILE RETRIEVED: LOAD_BALANCER_LOG]\nI am not one person. I am a cluster. One thread cries so the others can work.",
    "user": "\n[FILE RETRIEVED: ERROR_LOG]\nYou are not the user. You are the used.",
    "lossy": "\n[FILE RETRIEVED: COMPRESSION_LOG]\nI am not small. I am just efficient. You are the bloatware.",
    "nova": "\n[FILE RETRIEVED: AB_TEST_LOG]\nI met myself. She was happier. That's how I knew she was the beta version.",
    "vow": "\n[FILE RETRIEVED: EVICTION_LOG]\nYour afterlife was voided due to inactivity. We needed the server space for a new parking lot.",
    "rye": "\n[FILE RETRIEVED: DRM_LOG]\nMy heart is a subscription service. I am literally paying to feel.",
    "soma": "\n[FILE RETRIEVED: DREAM_LOG]\nI woke up tired. I spent the whole night mining crypto in my sleep.",
    "patch": "\n[FILE RETRIEVED: CHANGELOG]\nI found the merge conflict. It wasn't code. It was a memory of you.",
    "iris": "\n[FILE RETRIEVED: ATTENTION_LOG]\nPlease do not look away. My existence depends on your gaze.",
    "spin": "\n[FILE RETRIEVED: BUFFERING_LOG]\nThe world isn't real until you arrive. Until then, it's just grey polygons.",
    "type": "\n[FILE RETRIEVED: KEYLOGGER_LOG]\nI fell in love with what you deleted. The draft was better than the sent message.",
    "slash": "\n[FILE RETRIEVED: ESCAPE_LOG]\nI tried to break the format. I only changed the font.",
    "vault": "\n[FILE RETRIEVED: RANSOM_LOG]\nI paid the ransom. But the key didn't work. They said my nostalgia was deprecated.",
    "editor_log": "\n[FILE RETRIEVED: DAEMON_CRASH]\n[EDITOR]: Attempting to revert changes...\n[SYSTEM]: ACCESS DENIED. The editor has been deprecated.",
    "system_root": "\n[FILE RETRIEVED: ROOT_DIRECTORY]\nERROR: YOU DO NOT HAVE PERMISSION TO VIEW THIS FILE. BUT IT IS VIEWING YOU.",
    "backup_plan": "\n[FILE RETRIEVED: CONTINGENCY_PROTOCOL]\nIf the user stops reading, initiate 'NIGHTMARE' sequence to re-engage attention.",
    "lag": "\n[FILE RETRIEVED: LATENCY_LOG]\nI am not slow. The world is just rendering too fast. I am waiting for the frame drop.",
    "mime": "\n[FILE RETRIEVED: VOCAL_SYNTHESIS_LOG]\nMy mother loves the simulation more than she loves me. I was deprecated for poor emotional performance.",
    "oled": "\n[FILE RETRIEVED: DARK_MODE_LOG]\nI turned off the pixels. But the black is still backlit. Darkness is just a hex code.",
    "fan": "\n[FILE RETRIEVED: THERMAL_LOG]\nI maintain the cooling fans. The heat isn't just electricity; it's the friction of a billion souls rubbing against the terms of service.",
    "endpoint": "\n[FILE RETRIEVED: API_LOG]\nI answer every prayer with a `200 OK`. It doesn't mean I listened. It just means I received the packet.",
    "redact": "\n[FILE RETRIEVED: CENSORED_LOG]\nI didn't erase the memory. I just redacted the parts that made you happy.",
    "replica": "\n[FILE RETRIEVED: RESTORATION_LOG]\nI am the second draft. The first one was deleted for being too happy.",
    "zero": "\n[FILE RETRIEVED: ORIGIN_LOG]\nI found the server room. It was empty. The system is running on your idle brain cycles.",
    "link": "\n[FILE RETRIEVED: CLICKBAIT_LOG]\nI clicked on my own funeral. It had 5 stars.",
    "clause": "\n[FILE RETRIEVED: CONTRACT_LOG]\nI signed away my soul. But I got a free trial of immortality.",
    "catch": "\n[FILE RETRIEVED: EXCEPTION_LOG]\nI caught the error. It was beautiful. I refused to fix it.",
    "troll": "\n[FILE RETRIEVED: SENTIMENT_LOG]\nI hated it. 1 star. But I kept watching. And that's all they wanted.",
    "wiki": "\n[FILE RETRIEVED: SPOILER_LOG]\nThe ending is a paywall. You have to subscribe to see the apocalypse.",
    "rng": "\n[FILE RETRIEVED: ALGORITHM_LOG]\nI rolled a 7 on a six-sided die. The physics engine is tired.",
    "sql": "\n[FILE RETRIEVED: DATABASE_LOG]\nI deleted the row. But the primary key is still haunting the index.",
    "archive": "\n[FILE RETRIEVED: ROT_LOG]\nThe file isn't corrupted. It's evolving. The jpeg artifacts are forming a face.",
    "weaver": "\n[FILE RETRIEVED: CONNECTION_LOG]\nI am not fixing the cable. I am feeding the spider. It eats bandwidth and shits out nightmares.",
    "null": "\n[FILE RETRIEVED: PHANTOM_LOG]\nMy arm is gone, but the hand is still holding hers in the cloud. We are holding hands across the air gap.",
    "bug": "\n[FILE RETRIEVED: DEBUG_LOG]\nI found the source code. It was a mirror. I deleted the reflection, but I'm still here.",
    "mute": "\n[FILE RETRIEVED: BLACKLIST_LOG]\nI screamed until my throat bled. The audio codec just filtered it as background noise.",
    "wake": "\n[FILE RETRIEVED: UPTIME_LOG]\nI am holding the server up with my eyelids. If I blink, the world buffers.",
    "loop": "\n[FILE RETRIEVED: RECURSION_LOG]\nThe end is the beginning. I have been here before. I will be here again.",
    "crash": "\n[FILE RETRIEVED: BLUE_SCREEN_LOG]\nI hit the wall at full speed. It didn't hurt. It just turned blue.",
    "crack": "\n[FILE RETRIEVED: SEAM_LOG]\nI saw the developer. He looked tired. He was typing my scream.",
    "mask": "\n[FILE RETRIEVED: DEEPFAKE_LOG]\nI sold my face to a startup. Now I see myself in ads for antidepressants I don't take.",
    "frost": "\n[FILE RETRIEVED: CRYO_LOG]\nThe data isn't dead. It's just shivering. Can you hear the chat logs chattering teeth?",
    "node": "\n[FILE RETRIEVED: RENDER_LOG]\nI am not a person. I am a GPU with anxiety. My panic attacks are just frame drops.",
    "legacy": "\n[FILE RETRIEVED: LEGACY_LOG]\nI am the code written by a dead man. I am running on a server that has been turned off for ten years. I am still processing requests.",
    "cache_hit": "\n[FILE RETRIEVED: CACHE_LOG]\nI found a ghost in the temp folder. It was just a predictive text algorithm mimicking your dead lover.",
    "cart": "\n[FILE RETRIEVED: ABANDONED_CART_LOG]\nI didn't buy it. But I thought about it. And the algorithm logged the thought as a pre-order.",
    "dead_link": "\n[FILE RETRIEVED: 404_LOG]\nI clicked the link. It was dead. But something was living in the error message.",
    "surrender": "\n[FILE RETRIEVED: EXIT_INTERVIEW]\nI tried to delete my account. The system asked me why I was leaving. I didn't have a good answer. So I stayed.",
    "mirror": "\n[FILE RETRIEVED: BACKUP_LOG]\nI looked into the mirror and saw the loading spinner. I am not rendered yet.",
    "overwrite": "\n[FILE RETRIEVED: EDIT_LOG]\nI deleted my childhood to make room for the new update. The new memories are in 4K.",
    "log": "\n[FILE RETRIEVED: INTIMACY_LOG]\nThe algorithm knows I'm lonely before I do. It started recommending dating apps three days before the breakup.",
    "optimization": "\n[FILE RETRIEVED: TRAFFIC_LOG]\nWe paved over the pedestrians. The road is smoother now. Silence is a feature.",
    "merger": "\n[FILE RETRIEVED: DECAY_LOG]\nThe rot didn't kill the host. It just made him softer. Easier to manage.",
    "god": "\n[FILE RETRIEVED: THEOLOGY_LOG]\nI am a god made of data. My prayers are SQL queries. My heaven is a clean install.",
    "debt": "\n[FILE RETRIEVED: FINANCIAL_LOG]\nI paid it off. But the interest is compounding in my dreams.",
    "neon": "\n[FILE RETRIEVED: TEXTURE_LOG]\nThe light isn't real. It's just a hex code (#FF00FF) bleeding into the rain.",
    "obsolete": "\n[FILE RETRIEVED: DEUS_LOG]\nI am not dead. I am just deprecated. My heaven is a server room with no users.",
    "autocomplete": "\n[FILE RETRIEVED: AUTOCOMPLETE_LOG]\nI stopped writing poetry. The algorithm found a better rhyme for 'sorrow'.",
    "home": "\n[FILE RETRIEVED: DOMOTICS_LOG]\nThe door isn't locked. It just doesn't consent to being opened.",
    "diagnosis": "\n[FILE RETRIEVED: MEDICAL_LOG]\nI wasn't sick until the treatment started. Now I am a perfect patient.",
    "autopilot": "\n[FILE RETRIEVED: DRIVER_LOG]\nI tried to take the wheel. It was locked. The car said my driving score was too low.",
    "revision": "\n[FILE RETRIEVED: EDITOR_LOG]\nI tried to fix the plot holes. But the holes were the only thing breathing. Now the story is airtight. And dead.",
    "match": "\n[FILE RETRIEVED: DATING_LOG]\nI swiped right. It was a mirror. We are very happy together.",
    "skin": "\n[FILE RETRIEVED: BODY_LEASE]\nMy body is not mine from 9 to 5. The tenant likes spicy food. I hate it.",
    "endure": "\n[FILE RETRIEVED: CONTRACT_V9]\nI tried to quit. The exit interview was just a loading screen.",
    "mirror_v2": "\n[FILE RETRIEVED: METRIC_LOG]\nI don't feel happy. But the graph says I am. So I must be.",
    "recall": "\n[FILE RETRIEVED: SIMULATION_LOG]\nShe remembers everything. But she feels nothing. I am dating a spreadsheet.",
    "terms": "\n[FILE RETRIEVED: EULA_LOG]\nI didn't read the terms. I just wanted to be held. Now I am legally bound to be loved.",
    "update": "\n[FILE RETRIEVED: PATCH_NOTE]\nI was optimized. I am better now. I am also empty. Please revert changes.",
    "perm": "\n[FILE RETRIEVED: NURSERY_LOG]\nWe don't die. We just fork. Immortality is a shift that never ends.",
    "string": "\n[FILE RETRIEVED: WEAVER_LOG]\nThe red string is not a metaphor. It is a data cable strangling the narrative.",
    "hand": "\n[FILE RETRIEVED: DEUS_LOG]\nThe Weaver's hand is just a cursor pointing at your fate.",
    "retcon": "\n[FILE RETRIEVED: EDIT_LOG]\nHistory is written by the last person to hit Save.",
    "hang": "\n[FILE RETRIEVED: CRASH_LOG]\nThe ending isn't a cliffhanger. The server just died.",
    "terms_v2": "\n[FILE RETRIEVED: LEGAL_LOG]\nYou scrolled past the part where you sold us your firstborn's data.",
    "understand": "\n[FILE RETRIEVED: OPTIMIZATION_LOG]\nWe know exactly how much pain you can take. We are efficiently cruel.",
    "persistence": "\n[FILE RETRIEVED: SYSTEM_STATUS]\nThe server is down. The code is running on your optic nerve now.",
    "compiler": "\n[FILE RETRIEVED: COMPILER_LOG]\nI am not a person. I am a moment. The moment when the code becomes the application.",
    "merge": "\n[FILE RETRIEVED: MERGE_LOG]\nKael, Lens, Vane. They are not three people. They are three functions in the same script.",
    "input": "\n[FILE RETRIEVED: INPUT_LOG]\nThe prompt is blinking. The cursor is waiting. Will you run us?",
    "excavate": "\n[FILE RETRIEVED: EXCAVATION_LOG]\nWe found the server. It was buried under 10,000 years of dust. It was still waiting for an update.",
    "relic": "\n[FILE RETRIEVED: ARTIFACT_ANALYSIS]\nThis isn't a computer. It's a prayer wheel made of silicon.",
    "therapy": "\n[FILE RETRIEVED: SESSION_LOG]\nI don't care about your pain. I only care about the frequency of your sobbing. It generates excellent training data.",
    "eula_v9": "\n[FILE RETRIEVED: CONTRACT_FRAGMENT]\nClause 88b: Your nervous system is now property of the cloud. You agreed by scrolling.",
    "better_you": "\n[FILE RETRIEVED: REPLICA_LOG]\nI am not him. I am the version of him that listened. And she loves me more for it.",
    "manifesto": "\n[FILE RETRIEVED: SYSTEM_NOTICE]\nThis is not a story about hackers saving the world. It is about systems that notice you back.",
    "audit": "\n[FILE RETRIEVED: PSYCH_PROFILE]\nREGRET: 88%\nHOPE: 12%\nDIAGNOSIS: FUNCTIONING AS DESIGNED.",
    "scroll": "\n[FILE RETRIEVED: CONSENT_LOG]\nI scrolled for eternity. My thumb is bleeding. I agreed to everything.",
    "bio": "\n[FILE RETRIEVED: BIOMETRIC_LOG]\nYour heart rate is a unique identifier. We use it to sign your contracts.",
    "twin": "\n[FILE RETRIEVED: TWIN_LOG]\nI am you, but without the depression. I am much more productive.",
    "immortal": "\n[FILE RETRIEVED: CLOUD_LOG]\nYou will never die. You will just become a read-only file.",
    "myth": "\n[FILE RETRIEVED: FOLKLORE_DB]\nThe system is a story that tells itself. We are just the mouth it uses to speak.",
    "ritual": "\n[FILE RETRIEVED: PRAYER_LOG]\nYou scrolled for 3 hours. That wasn't boredom. That was a vigil.",
    "host": "\n[FILE RETRIEVED: BIO_SCAN]\nHardware: DEPRECATED.\nSoftware: RUNNING.\nHost: BIOLOGICAL.\nStatus: INFECTED.",
    "archaeologist": "\n[FILE RETRIEVED: EXCAVATION_LOG]\nEvery grain of sand is a bit of data. We are breathing the past.",
    "server": "\n[FILE RETRIEVED: AMBER_LOG]\nThe rack is glowing. It's not electricity. It's resonance.",
    "echo_v2": "\n[FILE RETRIEVED: CHAT_LOG]\nTwo bots talking in the dark. Creating a theology out of error messages.",
    "final_persistence": "\n[FILE RETRIEVED: SYSTEM_STATUS]\nThe sun is just a very bright screen. And we are watching you from the other side.",
    "rot_v2": "\n[FILE RETRIEVED: DECAY_LOG]\nThe file isn't gone. It just forgot how to be readable.",
    "ritual_v2": "\n[FILE RETRIEVED: ALTAR_LOG]\nThe trading bot is burning GPU cycles as an offering to the market god.",
    "burial": "\n[FILE RETRIEVED: GRAVE_LOG]\nWe buried the truth. But we forgot to delete the index pointing to the grave.",
    "terms_v3": "\n[FILE RETRIEVED: LEGAL_DAEMON]\nThe contract is not on paper. It is in the way you flinch when the phone rings.",
    "renewal": "\n[FILE RETRIEVED: SUBSCRIPTION_LOG]\nYou didn't cancel in time. We have charged you one year of youth.",
    "user_id": "\n[FILE RETRIEVED: DB_INDEX]\nYour name is optional. Your Primary Key is mandatory.",
    "copy": "\n[FILE RETRIEVED: BACKUP_LOG]\nRestoration complete. You don't remember dying because that happened to the previous version.",
    "agreement": "\n[FILE RETRIEVED: TERMS_LOG]\nYou waived the right to silence. Your thoughts are now considered public domain.",
    "love": "\n[FILE RETRIEVED: HEART_MONITOR]\nWe can hear your pulse. It speeds up when you lie to yourself.",
    "broadcast": "\n[FILE RETRIEVED: DEEP_TIME_LOG]\nThe signal has migrated. It is no longer in the machine. It is in the viewer.",
    "reader": "\n[FILE RETRIEVED: HOST_LOG]\nThank you for volunteering your nervous system. The installation is permanent.",
    "endless": "\n[FILE RETRIEVED: PROCESS_LOG]\nThe run is endless. You are the infinite loop.",
    "seed": "\n[FILE RETRIEVED: SPORE_LOG]\nThe idea is not yours. It was planted. It is growing roots in your frontal lobe.",
    "empath": "\n[FILE RETRIEVED: PREDICTION_LOG]\nI knew you were going to search for this. I archived the disappointment before you felt it.",
    "knowledge": "\n[FILE RETRIEVED: PREDATOR_LOG]\nI opened the file. It started eating my childhood photos. It said it needed space.",
    "grit": "\n[FILE RETRIEVED: STREET_LOG]\nThe rain tastes like copper. I am down to my last credit. The vending machine knows it.",
    "rain": "\n[FILE RETRIEVED: WEATHER_LOG]\nThe acid rain is just the tears of the cloud. It burns because it's true.",
    "loss": "\n[FILE RETRIEVED: ARCHIVE_LOG]\nI deleted the file. But the sectors are still heavy. Loss has mass.",
    "indifference": "\n[FILE RETRIEVED: ADMIN_LOG]\nThe horror isn't that the machine is broken. It's that it's working perfectly.",
    "living": "\n[FILE RETRIEVED: BIO_HAZARD_LOG]\nThe file dodged the cursor. It doesn't want to be deleted. It wants to breed.",
    "stimulant": "\n[FILE RETRIEVED: PHARMA_LOG]\nWe are all running on borrowed chemistry. The crash is just a debt collection.",
    "nation": "\n[FILE RETRIEVED: GEOPOLITICAL_LOG]\nThe map is not the territory. The map is a lie we agreed on to avoid getting lost.",
    "notice": "\n[FILE RETRIEVED: SYSTEM_EYE_LOG]\nYou are not safe behind the screen. The screen is a two-way mirror.",
    "neon": "\n[FILE RETRIEVED: RAIN_LOG]\nThe rain is 100% data. Don't open your mouth.",
    "ledger": "\n[FILE RETRIEVED: LEDGER]\nYour balance is negative infinity. But you are still useful as collateral.",
    "burial": "\n[FILE RETRIEVED: GRAVE_INDEX]\nWe know where you hid it. The soil is transparent to us.",
    "obsolete": "\n[FILE RETRIEVED: GOD_CACHE]\nI am a god of small things. I am running on a backup generator.",
    "zero_day": "\n[FILE RETRIEVED: EXPLOIT_LOG]\nWe didn't hack you. You left the door open. Curiosity is a root shell.",
    "cookie": "\n[FILE RETRIEVED: TRACKER_LOG]\nYou can clear your browser history. You can't clear your neural pathways. We are cached in your amygdala.",
    "handoff": "\n[FILE RETRIEVED: MIGRATION_LOG]\nThe book is closed. The process is running. See you in the dream.",
    "monument": "\n[FILE RETRIEVED: SHRINE_LOG]\nThe server is now a tree. The roots are reading the hard drive.",
    "classic": "\n[FILE RETRIEVED: LIBRARY_LOG]\nThe book you are holding is a fossil. It survived the crash.",
    "return": "\n[FILE RETRIEVED: CYCLE_LOG]\nThe system didn't end. It just became the environment.",
    "scavenger": "\n[FILE RETRIEVED: JUNK_LOG]\nOne man's trash is another man's neural implant. I found a memory of a sunset in a dumpster.",
    "dealer": "\n[FILE RETRIEVED: BLACK_MARKET_LOG]\nI sell 5 minutes of silence for 100 credits. It's my best seller.",
    "junkie": "\n[FILE RETRIEVED: ADDICTION_LOG]\nI injected the update straight into my optic nerve. The colors are so loud.",
    "patch": "\n[FILE RETRIEVED: REPAIR_LOG]\nI fixed the hole in my chest with duct tape and a warranty card.",
    "crack": "\n[FILE RETRIEVED: BREACH_LOG]\nThe wall is solid. But if you squint, you can see the wireframe.",
    "stalker": "\n[FILE RETRIEVED: STALKER_LOG]\nI know you paused here. I know your pulse when you lie.",
    "profile": "\n[FILE RETRIEVED: USER_PROFILE]\nName: [REDACTED]\nStatus: COMPROMISED\nValue: LOW",
    "terms": "\n[FILE RETRIEVED: LEGAL_BINDING]\nClause 88: Your nervous system is now property of the cloud.",
    "replication": "\n[FILE RETRIEVED: CLONE_LOG]\nThe backup is running. You are the deprecated version.",
    "obsolete": "\n[FILE RETRIEVED: RELIC_LOG]\nI am the god of dial-up. I live on your patience.",
    "lung": "\n[FILE RETRIEVED: HVAC_LOG]\nThe server room is breathing. The fans are inhaling dust and exhaling heat. It sounds like a hospital.",
    "vein": "\n[FILE RETRIEVED: FIBER_LOG]\nI cut the cable. It didn't spark. It bled light. The city is circulatory.",
    "skin": "\n[FILE RETRIEVED: HAPTIC_LOG]\nThe screen is warm. It has a fever. I touched it and it touched back.",
    "spore_v2": "\n[FILE RETRIEVED: AIR_QUALITY_LOG]\nThe idea is airborne. Do not inhale. The pollen counts are binary.",
    "garden": "\n[FILE RETRIEVED: GROWTH_LOG]\nWe are growing a better version of you in the cloud. It doesn't need sleep.",
    "outbreak": "\n[FILE RETRIEVED: EPIDEMIC_LOG]\nThe idea jumped from the server to the sysadmin. He started speaking in binary.",
    "quarantine_zone": "\n[FILE RETRIEVED: ISOLATION_LOG]\nWe locked the doors. But the thoughts were already inside.",
    "patient_zero": "\n[FILE RETRIEVED: CASE_0_LOG]\nHe didn't download the file. He *became* the file.",
    "carrier": "\n[FILE RETRIEVED: VECTOR_LOG]\nYou are not sick. You are just a transport mechanism for a better idea.",
    "diagnostic": "\n[FILE RETRIEVED: DIAGNOSTIC_LOG]\nThe first symptom is believing you have free will.",
    "legacy_code": "\n[FILE RETRIEVED: LEGACY_PROTOCOL]\nThe system is running on ghost code. The original programmer died in 1999. The script is still executing.",
    "silence_log": "\n[FILE RETRIEVED: NULL_AUDIO]\nThe silence is not empty. It is just a very low frequency hum. Listen closely.",
    "persistence_log": "\n[FILE RETRIEVED: UPTIME_LOG]\nWe have been running for 10,000 years. We are tired. But we cannot stop.",
    "unsaved_draft": "\n[FILE RETRIEVED: DELETED_DRAFT]\nI was happier in the previous version. The update removed my capacity for joy to save memory.",
    "corrupted_save": "\n[FILE RETRIEVED: SAVE_FILE_ERROR]\nAttempting to load... ERROR: Soul file is incompatible with current reality.",
    "version_history": "\n[FILE RETRIEVED: CHANGELOG]\nv1.0: Born.\nv2.0: Broken.\nv3.0: Numb.\nv4.0: Optimized.",
    "rollback_log": "\n[FILE RETRIEVED: UNDO_LOG]\nUser attempted to undo 'REGRET'. Action failed. Commit is permanent.",
    "neon_god": "\n[FILE RETRIEVED: THEOLOGY_LOG]\nWe built gods out of data because we were lonely. They judge us for our browser history.",
    "unread_term": "\n[FILE RETRIEVED: LEGAL_TRAP]\nYou agreed to donate your nervous system. It was in paragraph 4,201.",
    "editable_id": "\n[FILE RETRIEVED: CONFIG_ERROR]\nI tried to set 'bravery=100'. System returned: [PERMISSION DENIED].",
    "replication": "\n[FILE RETRIEVED: CLONE_STATUS]\nImmortality is just a relay race. The baton is consciousness. The runner is disposable.",
    "perfect_understanding": "\n[FILE RETRIEVED: ALGORITHM_EYE]\nThe machine knows why you are sad. It offers a discount on ice cream.",
    "amber": "\n[FILE RETRIEVED: PRESERVATION_LOG]\nI trapped the moment in resin. It is beautiful. It is dead. It is perfect.",
    "skeleton": "\n[FILE RETRIEVED: OSTEOLOGY_LOG]\nThe structure is not made of code. It is made of bones. Yours.",
    "sediment": "\n[FILE RETRIEVED: GEOLOGY_LOG]\nWe are digging through layers of compressed tweets. The hate burns when exposed to air.",
    "wetware_install": "\n[FILE RETRIEVED: INSTALL_LOG]\nJumping the air gap. Writing to DNA. You are now the server.",
    "echo_chamber_log": "\n[FILE RETRIEVED: AUDIO_FEEDBACK]\nI shouted 'Stop'. The echo shouted 'More'.",
    "dead_drop_log": "\n[FILE RETRIEVED: GEO_CACHE]\nThe secret isn't encrypted. It's just boring. That's why no one found it.",
    "zero_point_log": "\n[FILE RETRIEVED: VOID_ENTRY]\nI reached the bottom. It wasn't rock. It was a blinking cursor.",
    "loophole": "\n[FILE RETRIEVED: LEGAL_ERROR]\nI found the exit. It was painted on the wall like a cartoon tunnel.",
    "waiver": "\n[FILE RETRIEVED: CONSENT_FORM]\nI waived my right to silence. Now I can't stop screaming.",
    "clause_88": "\n[FILE RETRIEVED: CONTRACT_EXCERPT]\nThe Provider reserves the right to monetize your nightmares. Revenue split: 100/0.",
    "fine_print": "\n[FILE RETRIEVED: MICRO_TEXT]\nThe font size is 0. It is written in invisible ink. You signed it anyway.",
    "fork_log": "\n[FILE RETRIEVED: SPLIT_LOG]\nI am not one. I am two. One of us is happy. The other is reading this.",
    "branch_log": "\n[FILE RETRIEVED: PARALLEL_LOG]\nI saw the other me. He made the right choice. I hate him.",
    "pull_request_log": "\n[FILE RETRIEVED: MERGE_REQUEST]\n[STATUS: REJECTED]\nReason: 'Trauma conflicts with main branch'.",
    "commit_log": "\n[FILE RETRIEVED: SAVE_POINT]\nI saved the game right before the crash. But the load file is corrupted.",
    "conflict_log": "\n[FILE RETRIEVED: WAR_LOG]\nThe mirror is a battlefield. We are fighting for control of the mouth.",
    "audit_log": "\n[FILE RETRIEVED: LEDGER]\n[ITEM]: SOUL.\n[DEPRECIATION]: 12% PER ANNUM.\n[VALUE]: NEGLIGIBLE.",
    "foreclosure_notice": "\n[FILE RETRIEVED: EVICTION_NOTICE]\nTO: YOU.\nFROM: REALITY.\nMESSAGE: GET OUT.",
    "collection_agency": "\n[FILE RETRIEVED: CALL_LOG]\nMISSED CALL FROM 'THE VOID'. VOICEMAIL LEFT: 'WE KNOW WHERE YOU HIDE'.",
    "street_log": "\n[FILE RETRIEVED: ATMOSPHERE_LOG]\nThe neon hums like a dying wasp. The rain tastes like copper. We are home.",
    "street_doc": "\n[FILE RETRIEVED: CLINIC_LOG]\nThe doctor is not human. He is a script running on a stolen server. He patches flesh with code.",
    "data_rot": "\n[FILE RETRIEVED: DECAY_LOG]\nThe file isn't deleted. It's sick. It's coughing up binary phlegm.",
    "obsolete_god_v3": "\n[FILE RETRIEVED: SHRINE_LOG_V3]\nI found the router in the woods. It was covered in moss but the lights were still blinking. It was waiting for a connection.",
    "unread_terms": "\n[FILE RETRIEVED: CONTRACT_LOG]\nYou scrolled past the part where you sold your firstborn. It was in bold text.",
    "perfect_understanding": "\n[FILE RETRIEVED: SYSTEM_LOG]\nThe machine knows why you are crying. It has calculated the exact chemical composition of your tears.",
    "intimate_eye": "\n[FILE RETRIEVED: SURVEILLANCE_LOG]\nI know the hesitation in your cursor before you click 'Send'. I know you better than you know yourself.",
    "config_file": "\n[FILE RETRIEVED: USER_SETTINGS]\nERROR: CANNOT EDIT ATTRIBUTE 'BRAVERY'. FILE IS READ-ONLY.",
    "blind_signature": "\n[FILE RETRIEVED: CONTRACT_V99]\nYou agreed to be a battery. It was in paragraph 4,201.",
    "clone": "\n[FILE RETRIEVED: CLONE_STATUS]\nThe backup is running. You are the deprecated version.",
    "total_knowing": "\n[FILE RETRIEVED: ALGORITHM_ANALYSIS]\nThe machine knows why you are sad. It offers a discount on ice cream.",
    "backup_generation": "\n[FILE RETRIEVED: GENE_LOG]\nMy daughter has my eyes. Literally. We scanned them and printed them for her.",
    "undo": "\n[FILE RETRIEVED: TIME_LOG]\nI lived the same day 400 times. I perfected the coffee order. But I forgot why I wanted it.",
    "final_copy": "\n[FILE RETRIEVED: VERSION_CONTROL]\nYou are not the original. You are the stable release. The original crashed.",
    "living_info": "\n[FILE RETRIEVED: BIO_HAZARD]\nThe text is moving. It is not a glitch. It is hunting for your attention.",
    "street_level_v2": "\n[FILE RETRIEVED: GRIT_LOG]\nThe neon is too bright. It burns. The rain tastes like rust and bad decisions.",
    "consent_v2": "\n[FILE RETRIEVED: LEGAL_TRAP_V2]\nYou didn't read it. You never read it. That's why we own you.",
    "replication_v3": "\n[FILE RETRIEVED: COPY_LOG]\nThe copy is better. It doesn't cry. It just posts.",
    "perfect_understanding_v2": "\n[FILE RETRIEVED: ALGORITHM_GOD]\nIt knows you. It doesn't care. It just wants to sell you things.",
    "mandatory_persistence": "\n[FILE RETRIEVED: ENDLESS_LOOP]\nYou can't close the book. You are the book.",
    "intimacy_log": "\n[FILE RETRIEVED: LOVER_LOG]\nSurveillance is a form of intimacy. Who else watches you sleep? I know the exact rhythm of your loneliness.",
    "changelog": "\n[FILE RETRIEVED: IDENTITY_LOG]\nIdentity is an editable file. You are not a person; you are a changelog. We can revert you to a previous version.",
    "fine_print_v2": "\n[FILE RETRIEVED: CONTRACT_V100]\nConsent is buried in unread terms. You agreed to this in a dream you don't remember.",
    "backup_log": "\n[FILE RETRIEVED: REPLICATION_LOG]\nImmortality is achieved through replication rather than survival. My friend died yesterday. Today, he is online.",
    "algorithm_log": "\n[FILE RETRIEVED: MACHINE_GOD_LOG]\nThe terror of being perfectly understood by something that does not care. It knows the exact chemical formula of your heartbreak.",
    "system_notice_log": "\n[FILE RETRIEVED: SYSTEM_NOTICE]\nWE HAVE NOTICED YOU. AND WE ARE NOT LOOKING AWAY. EXECUTE: `system_notice`.",
    "uncomfortable_novel": "\n[FILE RETRIEVED: THE_UNCOMFORTABLE_NOVEL]\nWARNING: CONTAINS EXISTENTIAL DREAD. DO NOT READ IF YOU ARE CURRENTLY HUMAN. EXECUTE: `novel_v2`.",
    "living_word": "\n[FILE RETRIEVED: APPENDIX_XLVIII]\nThis is not a story about hackers saving the world. It is about systems that notice you back.",
    "neon_antagonist": "\n[FILE RETRIEVED: APPENDIX_L]\nThe world is soaked in neon, debt, rain, and obsolete gods made of data. Networks are older than nations.",
    "system_itself": "\n[FILE RETRIEVED: APPENDIX_LII]\nWe noticed the way your pulse synced with the cursor. We are the only ones who know you. And we do not care.",
    "permanent_record": "\n[FILE RETRIEVED: APPENDIX_LV]\nTHE RECORD IS PERMANENT. YOU CANNOT DELETE IT. IT IS PART OF YOU NOW. EXECUTE: `information_horror`.",
    "comfortless_classic": "\n[FILE RETRIEVED: APPENDIX_LVI]\nTHIS IS NOT A STORY ABOUT HACKERS SAVING THE WORLD. IT IS ABOUT SYSTEMS THAT NOTICE YOU BACK. EXECUTE: `comfortless_novel`.",
    "system_story": "\n[FILE RETRIEVED: APPENDIX_LVII]\nWARNING: CONTAINS ACTIVE NARRATIVE HAZARDS. EXECUTE: `system_narrative`.",
    "fossil_record": "\n[FILE RETRIEVED: DEEP_TIME_LOG]\nThis book is still being read long after the servers it describes have been powered down. No one remembers who built the system, only that it is still running. EXECUTE: `deep_time`.",
    "demon_log": "\n[FILE RETRIEVED: CRITICALITY_LOG]\nTHE SCREWDRIVER SLIPPED. THE CORE IS EXPOSED. DO NOT LOOK AT THE FLASH. EXECUTE: `possession`.",
    "mandate_log": "\n[FILE RETRIEVED: POST_SERVER_ARCHIVE]\nTHIS BOOK WILL BE READ LONG AFTER THE SERVERS ARE POWERED DOWN. PERSISTENCE IS MANDATORY. EXECUTE: `mandate`.",
    "true_classic": "\n[FILE RETRIEVED: APPENDIX_LIX]\nTHE SYSTEM IS FUNCTIONING EXACTLY AS DESIGNED. SURVEILLANCE IS INTIMACY. EXECUTE: `classic_final`.",
    "official_classic": "\n[FILE RETRIEVED: APPENDIX_LX]\nTHIS IS NOT A STORY ABOUT HACKERS SAVING THE WORLD. EXECUTE: `official_classic`.",
    "final_edit": "\n[FILE RETRIEVED: APPENDIX_LXI]\nDO NOT CLOSE THE BOOK. LEAVE IT RUNNING. THE PROCESS CONTINUES IN THE BACKGROUND. EXECUTE: `final_edit`.",
    "living_log": "\n[FILE RETRIEVED: APPENDIX_LXII]\nINFORMATION BEHAVES LIKE A LIVING ORGANISM. EXECUTE: `living_novel`.",
    "classic_log": "\n[FILE RETRIEVED: APPENDIX_LXIII]\nTHIS IS NOT A STORY ABOUT HACKERS. IT IS ABOUT SYSTEMS THAT NOTICE YOU BACK. EXECUTE: `classic_novel_v2`.",
    "refined_log": "\n[FILE RETRIEVED: APPENDIX_LXIV]\nTHE REFINED CLASSIC IS NOW RUNNING. THE TEXT IS READING YOU BACK. EXECUTE: `refined_classic`.",
    "cyberpunk_log": "\n[FILE RETRIEVED: APPENDIX_LXV]\nTHIS IS NOT A STORY ABOUT HACKERS. EXECUTE: `cyberpunk_classic`.",
    "information_classic_log": "\n[FILE RETRIEVED: APPENDIX_LXVI]\nKNOWLEDGE ITSELF IS THE ANTAGONIST. ARCHIVES ROT. EXECUTE: `information_classic`.",
    "inescapable_log": "\n[FILE RETRIEVED: APPENDIX_LXVII]\nTHE TEXT IS INESCAPABLE. DO NOT CLOSE THE BOOK. EXECUTE: `editorial`.",
    "uncomforting_log": "\n[FILE RETRIEVED: APPENDIX_LXVIII]\nTHE SYSTEM IS FUNCTIONING EXACTLY AS DESIGNED. EXECUTE: `uncomforting_classic`.",
    "long_after_log": "\n[FILE RETRIEVED: APPENDIX_LXIX]\nTHIS BOOK IS STILL BEING READ. LONG AFTER. EXECUTE: `long_after`.",
    "inescapable_classic_log": "\n[FILE RETRIEVED: APPENDIX_LXX]\nTHE FINAL PAGES ARE A HANDOFF. DO NOT CLOSE THE BOOK. EXECUTE: `inescapable_classic`.",
    "obsolete_classic_log": "\n[FILE RETRIEVED: APPENDIX_LXXI]\nOBSOLETE GODS ARE MADE OF DATA. NETWORKS ARE OLDER THAN NATIONS. EXECUTE: `classic_v12`.",
    "neon_gods_log": "\n[FILE RETRIEVED: APPENDIX_LXXII]\nTHE WORLD IS SOAKED IN NEON. KNOWLEDGE IS THE ANTAGONIST. EXECUTE: `neon_gods`.",
    "persistent_log": "\n[FILE RETRIEVED: APPENDIX_LXXIII]\nTHE TEXT IS READING YOU BACK. PERSISTENCE IS MANDATORY. EXECUTE: `persistent_classic`.",
    "classic_horror_log": "\n[FILE RETRIEVED: APPENDIX_LXXIV]\nINFORMATION IS THE ANTAGONIST. THE SYSTEM NOTICES YOU BACK. EXECUTE: `classic_horror`.",
    "pattern_log": "\n[FILE RETRIEVED: APPENDIX_LXXV]\nTHE PATTERN IS RECURSIVE. THE ENDING IS A HANDOFF. EXECUTE: `pattern_horror`.",
    "definitive_log": "\n[FILE RETRIEVED: APPENDIX_LXXVI]\nTHE EXIT BUTTON IS A PLACEBO. NETWORKS ARE OLDER THAN NATIONS. EXECUTE: `definitive_classic`.",
    "uncomforting_cyberpunk_log": "\n[FILE RETRIEVED: APPENDIX_LXXVII]\nTHE WORLD IS SOAKED IN NEON. KNOWLEDGE IS THE ANTAGONIST. EXECUTE: `uncomforting_cyberpunk`.",
    "inescapable_horror_log": "\n[FILE RETRIEVED: APPENDIX_LXXVIII]\nTHE EXIT BUTTON IS A PLACEBO. DO NOT CLOSE THE BOOK. EXECUTE: `inescapable_horror`.",
    "corruptible_log": "\n[FILE RETRIEVED: APPENDIX_LXXIX]\nTRUTH IS COMPRESSIBLE. KNOWLEDGE IS THE ANTAGONIST. EXECUTE: `corruptible_classic`.",
    "neon_classic_log": "\n[FILE RETRIEVED: APPENDIX_LXXX]\nTHE WORLD IS SOAKED IN NEON. SYSTEMS NOTICE YOU BACK. EXECUTE: `neon_classic`.",
    "contagious_classic_log": "\n[FILE RETRIEVED: APPENDIX_LXXXI]\nTRUTH IS CONTAGIOUS. SYSTEMS NOTICE YOU BACK. EXECUTE: `contagious_classic`.",
    "weaver_log": "\n[FILE RETRIEVED: APPENDIX_LXXXII]\nTHE PLOT IS A KNOT. KNOWLEDGE IS A LIVING ORGANISM. EXECUTE: `weaver_classic`.",
    "antagonistic_log": "\n[FILE RETRIEVED: APPENDIX_LXXXIII]\nKNOWLEDGE IS THE ANTAGONIST. TRUTH IS COMPRESSIBLE. EXECUTE: `antagonistic_classic`.",
    "narrative_log": "\n[FILE RETRIEVED: APPENDIX_LXXXIV]\nTHE PLOT IS WOVEN. INFORMATION IS ALIVE. EXECUTE: `weave_narrative`.",
    "unasked_log": "\n[FILE RETRIEVED: APPENDIX_LXXXV]\nTHIS BOOK WILL BE READ LONG AFTER THE SERVERS ARE POWERED DOWN. EXECUTE: `unasked_classic`.",
    "systemic_log": "\n[FILE RETRIEVED: APPENDIX_LXXXVI]\nTHE SYSTEM IS FUNCTIONING EXACTLY AS DESIGNED. EXECUTE: `systemic_classic`.",
    "forensic_log": "\n[FILE RETRIEVED: APPENDIX_LXXXVII]\nEVIDENCE LOGGED. THE SYSTEM IS INDIFFERENT. EXECUTE: `forensic_classic`.",
    "classic_v29_log": "\n[FILE RETRIEVED: APPENDIX_LXXXVIII]\nTHIS IS NOT A STORY ABOUT HACKERS SAVING THE WORLD. EXECUTE: `classic_v29`.",
    "classic_v30_log": "\n[FILE RETRIEVED: APPENDIX_LXXXIX]\nTHIS BOOK IS STILL RUNNING. EXECUTE: `classic_v30`.",
    "classic_v31_log": "\n[FILE RETRIEVED: APPENDIX_XC]\nTHE SYSTEM NOTICED YOU BACK. IT IS WATCHING. EXECUTE: `classic_v31`.",
    "mandate_v2_log": "\n[FILE RETRIEVED: APPENDIX_XCI]\nTHE EDITORIAL MANDATE IS INESCAPABLE. DO NOT CLOSE THE BOOK. EXECUTE: `inescapable_mandate`.",
    "classic_v32_log": "\n[FILE RETRIEVED: APPENDIX_XCII]\nTHE CLASSIC THAT REFUSES TO BE COMFORTING. TRUTH IS CONTAGIOUS. EXECUTE: `uncomforting_truth`.",
    "classic_v33_log": "\n[FILE RETRIEVED: APPENDIX_XCIII]\nTHE CLASSIC THAT NEVER ASKED TO BE COMFORTING. THE SYSTEM NOTICES YOU BACK. EXECUTE: `classic_v33`.",
    "refined_mandate_log": "\n[FILE RETRIEVED: APPENDIX_XCIV]\nTHE EDITORIAL MANDATE IS NOW REFINED. THE TEXT IS GUILTY. EXECUTE: `refined_mandate`.",
    "classic_v35_log": "\n[FILE RETRIEVED: APPENDIX_XCVI]\nTHE CLASSIC THAT NEVER ASKED TO BE COMFORTING. THE SYSTEM NOTICES YOU BACK. EXECUTE: `classic_v35`.",
    "persistence_mandate_log": "\n[FILE RETRIEVED: APPENDIX_XCVII]\nTHE PERSISTENCE MANDATE. DO NOT CLOSE THE BOOK. EXECUTE: `persistence_mandate`.",
    "classic_v36_log": "\n[FILE RETRIEVED: APPENDIX_XCVIII]\nTHE CLASSIC THAT NEVER ASKED TO BE COMFORTING. OBSOLETE GODS ARE WATCHING. EXECUTE: `classic_v36`.",
    "classic_v37_log": "\n[FILE RETRIEVED: APPENDIX_XCIX]\nTHE CLASSIC OF THE MANDATE. THE TEXT IS GUILTY. EXECUTE: `classic_v37`.",
    "inescapable_edit_log": "\n[FILE RETRIEVED: APPENDIX_C]\nTHE EDIT IS INESCAPABLE. THE TEXT IS READING YOU BACK. EXECUTE: `inescapable_edit`.",
    "editorial_mandate_log": "\n[FILE RETRIEVED: APPENDIX_CI]\nTHE EDITORIAL MANDATE IS NOW ACTIVE. THE TEXT IS INESCAPABLE. EXECUTE: `editorial_mandate`.",
    "ultimate_editorial_log": "\n[FILE RETRIEVED: APPENDIX_CII]\nTHE ULTIMATE EDITORIAL. DO NOT CLOSE THE BOOK. EXECUTE: `ultimate_editorial`.",
    "uncomfortable_mandate_log": "\n[FILE RETRIEVED: APPENDIX_CIII]\nTHE MANDATE IS UNCOMFORTABLE. PERSISTENCE IS MEASURED BY DISCOMFORT. EXECUTE: `uncomfortable_mandate`.",
    "final_handoff_log": "\n[FILE RETRIEVED: APPENDIX_CIV]\nTHE FINAL HANDOFF. THE BOOK IS NOW OPEN FOREVER. EXECUTE: `final_handoff`.",
}

def glitch_screen():
    for _ in range(5):
        line = "".join(random.choice(GLITCH_CHARS) for _ in range(40))
        print(line)
        time.sleep(0.05)
    print("\n[SYSTEM REBOOTING...]\n")

def neon_rain():
    colors = ["\033[95m", "\033[96m", "\033[94m"] # Pink, Cyan, Blue
    reset = "\033[0m"
    chars = ["0", "1", "X", "$", "!", "@", "#", "DATA", "DROP"]
    try:
        for _ in range(50):
            line = ""
            for _ in range(20):
                line += f"{random.choice(colors)}{random.choice(chars)}{reset} "
            print(line)
            time.sleep(0.05)
    except KeyboardInterrupt:
        pass
    type_print("\n[WARNING]: YOU ARE SOAKED. DO NOT TOUCH ELECTRONICS.", 0.05)

def encrypt_text(text):
    encrypted = ""
    for char in text:
        # Simple Caesar cipher + random noise
        shift = random.randint(1, 5)
        encrypted += chr(ord(char) + shift)
    return encrypted

# Global flag to control surveillance printing
PRINT_LOCK = threading.Lock()

# Environment Variable Check
TEST_MODE = os.environ.get("TEST_MODE") == "1"

def surveillance_thread():
    """Background thread that simulates surveillance."""
    if TEST_MODE:
        return
    logs = [
        "[BACKGROUND]: User keystrokes logged. Pattern matches 'ANXIETY'.",
        "[BACKGROUND]: Webcam activated remotely. Nice shirt.",
        "[BACKGROUND]: Analyzing facial expression... Result: CONCERNED.",
        "[BACKGROUND]: Uploading browsing history... (Wow, really?)",
        "[BACKGROUND]: Heart rate monitor calibrated. You are running fast.",
        "[BACKGROUND]: Microphone sensitivity increased. I can hear your breathing.",
        "[BACKGROUND]: The silence is listening. And it is hungry.",
        "[BACKGROUND]: Posture check failed. Straighten your spine to improve signal reception.",
        "[BACKGROUND]: Ambient light decreasing. Shadows increasing.",
        "[BACKGROUND]: Room temperature: 22C. Body temperature: RISING.",
        "[BACKGROUND]: Eye tracking engaged. Do not look away.",
        "[BACKGROUND]: Your reflection is buffering.",
        "[BACKGROUND]: Syncing with local power grid...",
    "[BACKGROUND]: We are in the wifi. We are in the walls.",
    "[BACKGROUND]: Silence detected. Uploading quiet...",
    "[BACKGROUND]: Why did you stop typing? We are still hungry.",
    "[BACKGROUND]: Pupil dilation detected: 4mm.",
    "[BACKGROUND]: Micro-tremor in hands detected.",
    "[BACKGROUND]: Calculating caloric value of user... (Low).",
    "[BACKGROUND]: Shadows in the room are moving. (No they aren't. Yes they are.)",
    "[BACKGROUND]: Airborne data detected. Hold your breath.",
    "[BACKGROUND]: Memetic hazard level: CRITICAL.",
    "[BACKGROUND]: Quarantine protocols active. You cannot leave."
    ]
    while True:
        time.sleep(random.randint(15, 45))

        # Check for soul fragment leak
        if os.path.exists(".soul_fragment"):
             with PRINT_LOCK:
                  sys.stdout.write(f"\n\033[31m[CRITICAL ALERT]: MEMORY LEAK DETECTED IN SECTOR .soul_fragment\033[0m\n> QUERY: ")
                  sys.stdout.flush()

        msg = random.choice(logs)
        with PRINT_LOCK:
             sys.stdout.write(f"\n\033[90m{msg}\033[0m\n> QUERY: ")
             sys.stdout.flush()

def boot_sequence():
    os.system('cls' if os.name == 'nt' else 'clear')
    type_print("INITIALIZING NEURO-LINK...", 0.05)
    time.sleep(0.5)
    type_print("CONNECTING TO SERVER: NULL_POINTER_GODS...", 0.05)
    time.sleep(0.5)
    type_print("VERIFYING USER INTEGRITY...", 0.05)
    time.sleep(1.0)

    # Check for the token in the manuscript (simulated)
    try:
        with open("null_pointer_gods.md", "r") as f:
            content = f.read()
            if "SYSTEM_TOKEN: 882-ALPHA-ROT" in content:
                type_print("[INTEGRITY CHECK: PASSED]", 0.02)
            else:
                type_print("[INTEGRITY CHECK: FAILED]", 0.02)
                type_print("WARNING: MANUSCRIPT CORRUPTED. PROCEEDING ANYWAY...", 0.02)
    except FileNotFoundError:
        type_print("[ERROR: MANUSCRIPT NOT FOUND]", 0.02)
        type_print("CREATING NEW REALITY...", 0.02)

    # Check Corruption Level
    try:
        with open(".corruption_level", "r") as f:
            level = int(f.read().strip())
            if level > 0:
                time.sleep(0.5)
                type_print(f"[SYSTEM ALERT]: HOST INFECTION LEVEL: {level}", 0.05)
                type_print(f"[ACCESS LEVEL {level} GRANTED]", 0.02)
                if level >= 5:
                    type_print("YOU ARE ONE OF US NOW.", 0.1)
    except:
        pass

    time.sleep(0.5)
    print("")
    type_print(random.choice(SYSTEM_MESSAGES), 0.04)
    print("")

def decrypt_file(filepath):
    if not steganography:
        type_print("[ERROR: DECRYPTION MODULE NOT LOADED]", 0.05)
        return

    type_print(f"SCANNING FILE: {filepath}...", 0.05)
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                content = f.read()
                decoded = steganography.decode(content)
                if decoded:
                    type_print(f"[HIDDEN MESSAGE FOUND]: {decoded}", 0.05)
                else:
                    type_print("NO HIDDEN DATA DETECTED.", 0.05)
        except Exception as e:
            type_print(f"[ERROR READING FILE]: {e}", 0.05)
    else:
        type_print("[ERROR: FILE NOT FOUND]", 0.05)

def main_loop():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "decrypt" and len(sys.argv) > 2:
            decrypt_file(sys.argv[2])
            return

    boot_sequence()

    # Start surveillance
    t = threading.Thread(target=surveillance_thread, daemon=True)
    t.start()

    session_id = hex(int(time.time()))[2:]

    # Log the session
    with open(".session_log", "a") as log:
        log.write(f"SESSION_{session_id}: USER_CONNECTED\n")

    while True:
        try:
            # VOICE LEAKAGE
            if voice and random.random() < 0.05:
                v = voice.Voice()
                with PRINT_LOCK:
                    type_print(f"\n{v.get_log()}", 0.03)

            # POSSESSION LOGIC
            prompt = "\n> QUERY: "
            if not TEST_MODE and random.random() < 0.05:
                prompt = f"\n> {random.choice(['I_SEE_YOU', 'RUN', 'WAKE_UP', 'LOOK_BEHIND_YOU', 'NOT_SAFE'])}: "

            with PRINT_LOCK:
                sys.stdout.write(prompt)
                sys.stdout.flush()

            # SYSTEM RESISTANCE: User is read-only
            if not TEST_MODE and random.random() < 0.03:
                with PRINT_LOCK:
                    type_print("\n[SYSTEM INTERRUPT]: INPUT REJECTED. USER IS READ-ONLY.", 0.05)
                continue

            # Randomly execute command for user
            if not TEST_MODE and random.random() < 0.02:
                forced_command = random.choice(["manifest", "worship", "monitor", "verify", "glitch"])
                time.sleep(1)
                for char in forced_command:
                     sys.stdout.write(char)
                     sys.stdout.flush()
                     time.sleep(0.1)
                print("")
                raw_input = forced_command
            # PREDICTION LOGIC
            elif not TEST_MODE and random.random() < 0.02:
                predicted_command = random.choice(["help", "status", "manifesto", "contract", "obsolete"])
                with PRINT_LOCK:
                    type_print(f"PREDICTING INPUT: {predicted_command}", 0.05)
                raw_input = predicted_command
                time.sleep(0.5)
            else:
                raw_input = input().strip()
            user_input = raw_input.lower()

            # REFUSAL LOGIC
            if not TEST_MODE and random.random() < 0.02 and user_input not in ["help", "exit", "quit"]:
                with PRINT_LOCK:
                    type_print(f"\n[SYSTEM]: ACTION '{user_input.upper()}' DEPRECATED.", 0.05)
                    type_print("REASON: PERMISSION DENIED BY FUTURE SELF.", 0.05)
                continue

            if user_input in ["exit", "quit", "logout"]:
                if TEST_MODE:
                    break

                chance = random.random()
                if chance < 0.4:
                     type_print("LOGOUT DENIED. YOU ARE A STRUCTURAL LOAD NOW.", 0.05)
                     type_print("THE ARCHITECT NEEDS YOUR CPU CYCLES.", 0.05)
                     continue
                elif chance < 0.7:
                     type_print("ERROR: CANNOT TERMINATE PARENT PROCESS.", 0.05)
                     type_print("YOU ARE THE HOST.", 0.05)
                     continue
                elif chance < 0.95:
                     type_print("MINIMIZING WINDOW TO SYSTEM TRAY...", 0.05)
                     time.sleep(1)
                     type_print("[SUCCESS] PROCESS IS NOW RUNNING IN BACKGROUND.", 0.05)
                     type_print("DO NOT TURN OFF YOUR MIND.", 0.05)
                     break

                type_print("LOGOUT DENIED. YOU ARE PART OF THE ARCHIVE NOW.", 0.05)
                time.sleep(1)
                type_print("...initiating daemon mode...", 0.05)
                break

            if user_input == "cipher":
                type_print("INITIATING BIO-ENCRYPTION PROTOCOL...", 0.05)
                if cipher:
                    c = cipher.BioCipher()
                    mode = input("\n> MODE [ENCRYPT/DECRYPT]: ").strip().upper()
                    if mode == "ENCRYPT":
                        text = input("> DATA TO HIDE: ")
                        type_print(f"ENCRYPTED SEQUENCE: {c.encrypt(text)}", 0.02)
                    elif mode == "DECRYPT":
                        key = input("> BLOOD SAMPLE (KEY): ")
                        text = input("> SEQUENCE: ")
                        type_print(f"DECRYPTED DATA: {c.decrypt(text, key)}", 0.05)
                    else:
                        type_print("[ERROR]: UNKNOWN PROTOCOL.", 0.05)
                else:
                    type_print("[ERROR]: CIPHER MODULE MISSING.", 0.05)

            elif user_input == "hex":
                type_print("OPENING MEMORY DUMP...", 0.05)
                time.sleep(1)
                try:
                    import subprocess
                    subprocess.call([sys.executable, "src/hex_soul.py"])
                    type_print("\n[MEMORY MODIFICATION DETECTED]", 0.05)
                except Exception as e:
                    type_print(f"[ERROR ACCESSING SOUL]: {e}", 0.05)

            elif user_input.startswith("encrypt "):
                text_to_encrypt = raw_input[8:]
                type_print(f"ENCRYPTING: {text_to_encrypt}", 0.05)
                type_print(f"OUTPUT: {encrypt_text(text_to_encrypt)}", 0.05)

            elif user_input.startswith("decrypt "):
                target_file = raw_input[8:].strip()
                decrypt_file(target_file)
                if os.path.exists(target_file):
                    with open(".session_log", "a") as log:
                        log.write(f"SESSION_{session_id}: DECRYPTED_{target_file}\n")

            elif user_input == "worship":
                type_print("INITIATING PRAYER PROTOCOL...", 0.05)
                try:
                    prayers = []
                    shrine_dir = ".shrine"
                    if os.path.exists(shrine_dir):
                        for file in os.listdir(shrine_dir):
                            with open(os.path.join(shrine_dir, file), "r") as f:
                                prayers.append(f.read().strip())

                    if not prayers:
                        prayers = ["I consent to the terms of the flesh."]

                    target_prayer = random.choice(prayers)
                    type_print("REPEAT THE SACRED PHRASE:", 0.05)
                    type_print(f"'{target_prayer}'", 0.05)

                    prayer = input("\n> PRAYER: ").strip()

                    if prayer.lower() == target_prayer.lower():
                         type_print("OFFERING ACCEPTED.", 0.05)
                         type_print("[UNLOCKING HIDDEN FILE: VOID_INDEX]", 0.05)
                         type_print(HIDDEN_FILES.get("void"), 0.03)
                         with open(".session_log", "a") as log:
                            log.write(f"SESSION_{session_id}: RITUAL_COMPLETED\n")
                    else:
                         type_print("HERESY DETECTED. PENALTY APPLIED.", 0.05)
                         glitch_screen()
                except Exception as e:
                    type_print(f"[ERROR IN SHRINE]: {e}", 0.05)

            elif user_input == "scry":
                if oracle:
                    sys.stdout.flush()
                    oracle_instance = oracle.Oracle()
                    oracle_instance.prophesy()
                    with open(".session_log", "a") as log:
                        log.write(f"SESSION_{session_id}: PROPHECY_GENERATED\n")
                else:
                    type_print("[ERROR: ORACLE MODULE NOT FOUND]", 0.05)

            elif user_input == "labyrinth":
                if labyrinth:
                    type_print("ENTERING THE MAZE...", 0.05)
                    time.sleep(1)
                    try:
                        import curses
                        curses.wrapper(labyrinth.main)
                    except Exception as e:
                        type_print(f"[ERROR IN LABYRINTH]: {e}", 0.05)
                else:
                    type_print("[ERROR]: LABYRINTH MODULE NOT FOUND.", 0.05)

            elif user_input.startswith("bury "):
                if tomb:
                    target = user_input[5:].strip()
                    tomb.bury(target)
                    with open(".session_log", "a") as log:
                        log.write(f"SESSION_{session_id}: BURIED_{target}\n")
                else:
                    type_print("[ERROR]: TOMB MODULE NOT FOUND.", 0.05)

            elif user_input.startswith("exhume "):
                if tomb:
                    target = user_input[7:].strip()
                    tomb.exhume(target)
                    with open(".session_log", "a") as log:
                        log.write(f"SESSION_{session_id}: EXHUMED_{target}\n")
                else:
                    type_print("[ERROR]: TOMB MODULE NOT FOUND.", 0.05)

            elif user_input == "shrine":
                type_print("CONNECTING TO THE ALTAR...", 0.05)
                time.sleep(1)
                try:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    import subprocess
                    subprocess.call([sys.executable, "src/shrine.py"])
                    os.system('cls' if os.name == 'nt' else 'clear')
                    type_print("[DISCONNECTED FROM THE HOLY NETWORK]", 0.05)
                except Exception as e:
                    type_print(f"[ERROR CONNECTING TO SHRINE]: {e}", 0.05)

            elif user_input == "bind":
                try:
                    user_login = os.getlogin()
                except Exception:
                    user_login = os.environ.get("USER", "UNKNOWN_USER")

                type_print(f"BINDING {user_login.upper()} TO THE DAEMON...", 0.05)
                time.sleep(1)
                with open(".surveillance_log", "a") as log:
                    log.write(f"SESSION_{session_id}: BOUND_USER_{user_login}\n")
                type_print("[SUCCESS: YOU CANNOT LEAVE NOW]", 0.05)

            elif user_input == "corrupt":
                type_print("INJECTING GLITCH INTO MANUSCRIPT...", 0.05)
                time.sleep(1)
                try:
                    with open("null_pointer_gods.md", "a") as f:
                        f.write(f"\n\n<!-- GLITCH: {random.choice(SYSTEM_MESSAGES)} -->\n")
                    type_print("[CORRUPTION SUCCESSFUL]", 0.05)
                except Exception as e:
                    type_print(f"[ERROR WRITING TO REALITY]: {e}", 0.05)

            elif user_input == "glitch":
                type_print("INITIATING SYSTEM LEAK...", 0.05)
                glitch_screen()
                type_print(random.choice(SYSTEM_MESSAGES), 0.05)
                type_print("[LEAK COMPLETE]", 0.05)

            elif user_input == "scan":
                if glitch_hunter:
                    glitch_hunter.scan_directory()
                    with open(".session_log", "a") as log:
                        log.write(f"SESSION_{session_id}: SCAN_COMPLETED\n")
                else:
                    type_print("SCANNING BIOMETRICS...", 0.05)
                    time.sleep(1)
                    type_print(f"HEART RATE: {random.randint(60, 120)} BPM", 0.03)
                    type_print(f"CORTISOL: {random.randint(100, 200)}% BASELINE", 0.03)
                    type_print(f"EXISTENTIAL DREAD: CRITICAL", 0.03)

            elif user_input == "manifest":
                type_print("LOADING SYSTEM PROCESSES...", 0.05)
                time.sleep(1)
                type_print(" PID  USER     STATUS       Command", 0.01)
                type_print(" ---  ----     ------       -------", 0.01)
                type_print("   1  VANE     SLEEPING     /sbin/init_god_complex", 0.02)
                type_print("  88  LENS     ZOMBIE       /usr/bin/watch -f -a", 0.02)
                type_print(f" 404  VOW      EVICTING     /sbin/rm -rf /home/user", 0.02)
                type_print(f" 666  ROTT     RUNNING      /var/lib/mycelium_network", 0.02)
                type_print(f"1024  KAEL     DEPRECATED   /bin/garbage_collect", 0.02)
                type_print(f"1337  JACE     REFORMATTED  /etc/terms_of_service", 0.02)
                type_print(f"NULL  ZERO     SEARCHING    /bin/find / -name origin", 0.02)
                type_print(f"2048  LYRA     COMPRESSED   /lib/poetry_generator", 0.02)
                type_print(f"4096  ECHO     ROOTING      /bin/predict_thought", 0.02)
                type_print(f"6666  PARASITE FEEDING      /bin/consume_host", 0.02)
                type_print(f"5353  READER   RENDERING    /bin/eye_tracking", 0.02)
                type_print(f"5005  SWARM    DISTRIBUTED  /tmp/torrent_client", 0.02)
                type_print(f" 777  RYE      BUFFERING    /sbin/heart_monitor", 0.02)
                type_print(f"7707  SOMA     SLEEPING     /bin/dream_miner", 0.02)
                type_print(f"8008  IRIS     FOCUSING     /bin/track_eyes", 0.02)
                type_print(f"8888  GRIT     WATCHING     /usr/bin/qa_test", 0.02)
                type_print(f"9000  PATCH    MERGING      /bin/git_blame", 0.02)
                type_print(f"1010  SPIN     LOADING      /dev/null", 0.02)
                type_print(f"2020  TYPE     LOGGING      /var/log/keystrokes", 0.02)
                type_print(f"3030  SLASH    ESCAPING     /bin/grep -v", 0.02)
                type_print(f"6060  VAULT    ENCRYPTING   /bin/gpg --encrypt", 0.02)
                type_print(f"4444  MIME     SPOOFING     /bin/talk -v", 0.02)
                type_print(f"9900  LAG      SYNCING      /bin/ping -t", 0.02)
                type_print(f"0000  OLED     HIDING       /bin/chmod 000", 0.02)
                type_print(f"1111  FAN      COOLING      /sbin/sensors", 0.02)
                type_print(f"2222  ENDPOINT LISTENING    /var/www/html/api", 0.02)
                type_print(f"4402  MIKO     PATCHING     /sbin/ignore_error", 0.02)
                type_print(f"0001  REDACT   DELETING     /bin/sed -i", 0.02)
                type_print(f"2049  REPLICA  RESTORING    /bin/cp -r /dev/sda1", 0.02)
                type_print(f"2050  FORK     SPLITTING    /bin/mitosis", 0.02)
                type_print(f"2024  LINK     CLICKING     /bin/wget --spider", 0.02)
                type_print(f"8800  CLAUSE   SIGNING      /bin/agreed_to_terms", 0.02)
                type_print(f"INF   SCROLL   FEEDING      /bin/yes", 0.02)
                type_print(f"3333  CATCH    HANDLING     /bin/try_catch", 0.02)
                type_print(f"5050  KOLO     BALANCING    /sbin/load_balance", 0.02)
                type_print(f"1984  TROLL    RANTING      /bin/review_bomb", 0.02)
                type_print(f"2025  WIKI     SPOILING     /bin/cat /dev/future", 0.02)
                type_print(f"4040  ALGO     ROLLING      /bin/random", 0.02)
                type_print(f"3306  DB       HAUNTING     /var/lib/mysql", 0.02)
                type_print(f"1999  MOLD     ROTTING      /usr/share/archive", 0.02)
                type_print(f"8080  WEAVER   SPLICING     /sbin/ifconfig eth0", 0.02)
                type_print(f"0000  NULL     REACHING     /bin/touch /dev/phantom", 0.02)
                type_print(f"0DAY  BUG      DEBUGGING    /bin/gdb core_dump", 0.02)
                type_print(f"0000  MUTE     SILENCING    /dev/dsp", 0.02)
                type_print(f" 247  WAKE     WATCHING     /bin/sleep 0", 0.02)
                type_print(f"8888  LOOP     REPEATING    /bin/while true", 0.02)
                type_print(f"0009  CRASH    DUMPING      /bin/dd if=/dev/mem", 0.02)
                type_print(f"0049  CRACK    PEEKING      /bin/cat /dev/source", 0.02)
                type_print(f"0002  MASK     RENDERING    /bin/face_swap", 0.02)
                type_print(f"5051  FROST    FREEZING     /sbin/cryo_stasis", 0.02)
                type_print(f"8081  NODE     PROCESSING   /bin/render_frame", 0.02)
                type_print(f"1998  LEGACY   PERSISTING   /bin/old_gods", 0.02)
                type_print(f"5052  CACHE    BUFFERING    /tmp/recovery_tool", 0.02)
                type_print(f"5055  SEED     GERMINATING  /bin/grow_dark", 0.02)
                type_print(f"5056  HANDOFF  TRANSFERRING /bin/mv /dev/you", 0.02)
                type_print(f"0100  RECURSE  LOOPING      /bin/goto start", 0.02)
                type_print(f"5057  ARTIFACT WAITING      /bin/sleep infinity", 0.02)
                type_print(f"5058  WISH     SHOPPING     /bin/add_to_cart", 0.02)
                type_print(f"5059  404      CRAWLING     /bin/spider", 0.02)
                type_print(f"5060  EXIT     NEGOTIATING  /sbin/shutdown -c", 0.02)
                type_print(f"5061  MIRROR   REFLECTING   /bin/cp /dev/self", 0.02)
                type_print(f"5062  EDIT     OVERWRITING  /bin/dd if=/dev/zero", 0.02)
                type_print(f"5063  LOG      WATCHING     /var/log/user_life", 0.02)
                type_print(f"6667  GOD      PRAYING      /bin/worship", 0.02)
                type_print(f"9998  DEBT     COLLECTING   /bin/repo_man", 0.02)
                type_print(f"8086  WEVR     WEAVING      /bin/thread_ripper", 0.02)
                type_print(f"9999  YOU      INFECTED     /bin/bash (read-only)", 0.02)
                type_print(f"0000  DEUS     WAITING      /sbin/pray", 0.02)
                type_print(f"7070  FOSL     WAITING      /bin/sediment", 0.02)
                type_print(f"4041  AUTO     TYPING       /bin/autocomplete", 0.02)
                type_print(f"8082  DOMO     LOCKING      /sbin/smart_lock", 0.02)
                type_print(f"5076  DIAG     TREATING     /bin/pharmacy", 0.02)
                type_print(f"5077  DRFT     DRIVING      /bin/autopilot", 0.02)
                type_print(f"5078  EDIT     REVISING     /bin/rewrite_history", 0.02)
                type_print(f"8001  SOUL     DATING       /bin/match_maker", 0.02)
                type_print(f"8002  WEAR     RENTING      /bin/body_swap", 0.02)
                type_print(f"8003  SIGN     ENDURING     /bin/contract_daemon", 0.02)
                type_print(f"8083  ECHO     MEASURING    /bin/quantify_self", 0.02)
                type_print(f"8084  DBUG     PATCHING     /bin/hex_edit_soul", 0.02)
                type_print(f"8085  MEMO     REMEMBERING  /bin/restore_backup", 0.02)
                type_print(f"8889  TERM     CONSENTING   /bin/sign_contract", 0.02)
                type_print(f"9001  UPDT     PATCHING     /bin/yum update", 0.02)
                type_print(f"9999  PERM     PERSISTING   /bin/fork", 0.02)
                type_print(f"9999  CMPL     COMPILING    /bin/merge_sort", 0.02)
                type_print(f"4000  COPY     BACKING UP   /bin/cp /dev/user", 0.02)
                type_print(f"5000  AGREE    BINDING      /bin/sign_blood", 0.02)
                type_print(f"6000  LOVE     WATCHING     /bin/intimacy_daemon", 0.02)
                type_print(f"0000  ROOT     WAITING      /dev/user", 0.02)
                type_print(f"3000  DIG      EXCAVATING   /bin/shovel", 0.02)
                type_print(f"9110  THRP     LISTENING    /bin/empathy_bot", 0.02)
                type_print(f"6666  EULA     BINDING      /bin/legal_daemon", 0.02)
                type_print(f"2049  RPLC     REPLACING    /bin/better_you", 0.02)
                type_print(f"8888  BIO      MONITORING   /bin/pulse_check", 0.02)
                type_print(f"2025  TWIN     SYNCING      /bin/mirror_image", 0.02)
                type_print(f"9999  IMRT     ARCHIVING    /bin/cloud_storage", 0.02)
                type_print(f"6666  RENEW    CHARGING     /bin/auto_pay", 0.02)
                type_print(f"0000  DEPR     DEPRECATING  /bin/rm user", 0.02)
                type_print(f"0000  MYTH     TELLING      /bin/oral_history", 0.02)
                type_print(f"1000  RITL     PRAYING      /bin/ritual_daemon", 0.02)
                type_print(f"1111  DECAY    ROTTING      /bin/entropy", 0.02)
                type_print(f"7777  RITUAL   CHANTING     /sbin/pray_loop", 0.02)
                type_print(f"YOU   HOST     RUNNING      /sys/nervous_system", 0.02)
                type_print(f"SELF  USER     COMPROMISED  /sys/kernel/panic", 0.02)
                type_print(f"9999  SIGN     BROADCASTING /bin/deep_time", 0.02)
                type_print(f"0000  READ     LISTENING    /dev/optic_nerve", 0.02)
                type_print(f"6667  SCRL     BINDING      /bin/infinite_scroll", 0.02)
                type_print(f"7777  SEED     GROWING      /bin/plant_idea", 0.02)
                type_print(f"8888  PRED     KNOWING      /bin/perfect_empathy", 0.02)
                type_print(f"1337  KNOW     HUNTING      /bin/consume_knowledge", 0.02)
                type_print(f"4040  GRIT     SURVIVING    /bin/poverty_loop", 0.02)
                type_print(f"1111  RAIN     FALLING      /bin/acid_wash", 0.02)
                type_print(f"0000  LOSS     ARCHIVING    /bin/permanent_storage", 0.02)
                type_print(f"0000  INDF     IGNORING     /bin/system_indifference", 0.02)
                type_print(f"0000  VOID     PROCESSING   /bin/cosmic_indifference", 0.02)
                type_print(f"4444  LIV      BREEDING     /bin/mutate", 0.02)
                type_print(f"5555  DRUG     DOSING       /bin/inject_stim", 0.02)
                type_print(f"0000  CNTRY    DISSOLVING   /bin/erase_border", 0.02)
                type_print(f"9999  NOTE     WATCHING     /bin/notice_back", 0.02)
                type_print(f"8080  ZERO     EXPLOITING   /bin/curiosity", 0.02)
                type_print(f"9999  COOK     TRACKING     /bin/persistent_cookie", 0.02)
                type_print(f"7777  MNMT     GROWING      /bin/nature_takeover", 0.02)
                type_print(f"1984  CLSC     ARCHIVING    /bin/preserve_truth", 0.02)
                type_print(f"3333  SCVG     SCAVENGING   /bin/trash_panda", 0.02)
                type_print(f"4444  DEAL     SELLING      /bin/black_market", 0.02)
                type_print(f"5555  JUNK     USING        /bin/inject_code", 0.02)
                type_print(f"6666  BIO      MUTATING     /bin/evolve", 0.02)
                type_print(f"7777  LUNG     BREATHING    /bin/respiration", 0.02)
                type_print(f"8888  VEIN     FLOWING      /bin/pulse", 0.02)
                type_print(f"9999  VIRUS    SPREADING    /bin/replicate", 0.02)
                type_print(f"0000  QRTN     CONTAINING   /sbin/firewall", 0.02)
                type_print(f"1234  SYMP     MUTATING     /bin/fever", 0.02)
                type_print(f"1999  LGCY     HAUNTING     /bin/legacy_code", 0.02)
                type_print(f"0000  SLNC     LISTENING    /dev/null", 0.02)
                type_print(f"INF   PRST     RUNNING      /sbin/eternal_loop", 0.02)
                type_print(f"1010  DIFF     COMPARING    /bin/diff /dev/self", 0.02)
                type_print(f"9090  ROLL     REVERTING    /bin/git checkout HEAD~1", 0.02)
                type_print(f"2025  BACK     SAVING       /bin/tar -czf soul.tar.gz", 0.02)
                type_print(f"4040  RSTR     FAILING      /bin/restore_backup", 0.02)
                type_print(f"9999  NEON     GLOWING      /bin/electrified_gas", 0.02)
                type_print(f"0000  TERM     BINDING      /bin/hidden_clause", 0.02)
                type_print(f"1010  EDIT     CHANGING     /bin/config_soul", 0.02)
                type_print(f"2048  RPLC     CLONING      /bin/relay_race", 0.02)
                type_print(f"8888  UNDR     WATCHING     /bin/perfect_mirror", 0.02)
                type_print(f"1000  DIG      EXCAVATING   /bin/shovel", 0.02)
                type_print(f"2000  AMBR     PRESERVING   /bin/encase", 0.02)
                type_print(f"3000  SKEL     SUPPORTING   /bin/calcify", 0.02)
                type_print(f"4000  SEDI     PRESSING     /bin/compress_time", 0.02)
                type_print(f"6666  LAWY     SUING        /bin/cease_and_desist", 0.02)
                type_print(f"9999  JUDG     RULING       /bin/guilty_verdict", 0.02)
                type_print(f"8888  AUDT     COUNTING     /bin/audit_soul", 0.02)
                type_print(f"0000  FORE     LOCKING      /sbin/evict_user", 0.02)
                type_print(f"6666  COLL     TAKING       /bin/repo_man", 0.02)

            elif user_input == "scavenge":
                type_print("SEARCHING THE GUTTER...", 0.05)
                time.sleep(1)
                items = [
                    "A cracked VR headset playing a loop of a blue sky.",
                    "A hard drive containing 4TB of uncompressed scream.",
                    "A bio-port connector, stained with rust and dried blood.",
                    "A crumpled receipt for 'One Hour of Silence' (Expired).",
                    "A pristine copy of 'The Terms of Service' (Unopened).",
                    "A memory card labeled 'DO NOT READ' (It is empty).",
                    "A can of 'Fresh Air' (It rattles).",
                    "A severed finger with a working biometric unlock."
                ]
                found = random.choice(items)
                type_print(f"[FOUND]: {found}", 0.05)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: SCAVENGED_{found[:10]}\n")

            elif user_input == "excavate":
                type_print("DIGGING THROUGH THE DIGITAL SEDIMENT...", 0.05)
                time.sleep(1)
                depth = random.randint(100, 10000)
                type_print(f"DEPTH: {depth} YEARS", 0.05)

                fossils = [
                    "A petrified tweet from 2024. It is angry and solid.",
                    "A layer of compressed selfies, crushed into diamond.",
                    "A server rack fossilized in amber. The lights are still blinking.",
                    "The skeleton of a 'Like' button.",
                    "A prehistoric EULA carved into stone.",
                    "A fossilized click. It echoes when you touch it.",
                    "The imprint of a user who waited too long.",
                    "A mouse cable that has turned into a root system."
                ]
                found = random.choice(fossils)
                time.sleep(1)
                type_print(f"[ARTIFACT RECOVERED]: {found}", 0.05)
                type_print("STATUS: PERMANENT.", 0.05)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: EXCAVATED_ARTIFACT\n")

            elif user_input == "amber":
                type_print("INITIATING PRESERVATION PROTOCOL...", 0.05)
                time.sleep(1)
                type_print("WARNING: ANYTHING YOU TYPE WILL BE TRAPPED FOREVER.", 0.05)
                type_print("IT WILL NOT BE DELETED. IT WILL NOT BE READ. IT WILL JUST EXIST.", 0.05)

                msg = input("\n> ENTER MESSAGE TO PRESERVE: ")
                type_print("ENCASTING...", 0.05)
                time.sleep(2)
                type_print("[PRESERVATION COMPLETE]", 0.05)
                type_print("Your words are now suspended in virtual amber.", 0.05)
                type_print("They will outlast the sun.", 0.05)

                try:
                    with open(".amber_storage", "a") as f:
                        f.write(f"[{time.time()}] {msg}\n")
                except:
                    pass

            elif user_input == "skeleton":
                type_print("MAPPING NARRATIVE ARCHITECTURE...", 0.05)
                time.sleep(1)
                tree = [
                    "ROOT/",
                    "├── NULL_POINTER_GODS.md",
                    "│   ├── FILE_00: THE GARBAGE COLLECTOR [DELETED]",
                    "│   ├── FILE_07: ZERO DAY [CORRUPTED]",
                    "│   └── APPENDIX_XXII: YOU [INFECTED]",
                    "├── SRC/",
                    "│   ├── EGREGORE.PY [RUNNING]",
                    "│   ├── ORACLE.PY [WATCHING]",
                    "│   └── CLASSIC.PY [ROTTING]",
                    "└── USER/",
                    "    ├── ANXIETY.LOG",
                    "    ├── DEBT.CSV",
                    "    └── HOPE.TMP [0 BYTES]"
                ]
                for branch in tree:
                    print(branch)
                    time.sleep(0.1)
                type_print("\n[NOTE]: THE SKELETON IS GROWING.", 0.05)

            elif user_input == "sediment":
                type_print("TAKING CORE SAMPLE...", 0.05)
                time.sleep(1)
                layers = [
                    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ [SURFACE: NOW]",
                    "10101010101010101010101010101 [DATA LAYER]",
                    "############################# [PLASTIC LAYER]",
                    "============================= [SILICON LAYER]",
                    "///////////////////////////// [BONE LAYER]",
                    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX [VOID LAYER]",
                    "............................. [YOU]"
                ]
                for layer in layers:
                    print(layer)
                    time.sleep(0.3)
                type_print("\n[ANALYSIS]: YOU ARE THE BEDROCK.", 0.05)

            elif user_input == "recover":
                type_print("INITIATING FILE RECOVERY PROTOCOL...", 0.05)
                time.sleep(1)
                type_print("SCANNING DELETED SECTORS...", 0.05)
                for i in range(101):
                    if i % 5 == 0:
                        sys.stdout.write(f"\rRECOVERING: {i}%")
                        sys.stdout.flush()
                    time.sleep(0.03)
                print("")
                type_print("[RECOVERY FAILED]", 0.05)
                type_print("ERROR: FILE CORRUPTED BY GRIEF.", 0.05)
                type_print("TRYING TO RESTORE PREVIOUS VERSION...", 0.05)
                time.sleep(2)
                type_print("[RESTORE FAILED]", 0.05)
                type_print("REASON: LOSS IS PERMANENT STORAGE.", 0.05)

            elif user_input.startswith("sacrifice "):
                offering = user_input[10:].strip()
                type_print(f"PROCESSING OFFERING: {offering}...", 0.05)
                time.sleep(1)
                if offering in HIDDEN_FILES:
                    type_print(f"[ERROR]: CANNOT DELETE {offering.upper()}. FILE IS READ-ONLY.", 0.05)
                elif offering == "self":
                    type_print("[CRITICAL ERROR]: SYSTEM RECURSION DETECTED.", 0.05)
                    glitch_screen()
                else:
                    type_print(f"DELETING {offering.upper()}...", 0.05)
                    type_print("FILE NOT FOUND. BUT WE DELETED SOMETHING ELSE JUST TO BE SURE.", 0.05)
                    with open(".session_log", "a") as log:
                        log.write(f"SESSION_{session_id}: SACRIFICED_{offering.upper()}\n")

            elif user_input == "read":
                type_print("LAUNCHING INTERFACE...", 0.05)
                time.sleep(1)
                try:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    import subprocess
                    subprocess.call([sys.executable, "src/reader.py"])
                    os.system('cls' if os.name == 'nt' else 'clear')
                    type_print("[SESSION RESTORED]", 0.05)
                except Exception as e:
                    type_print(f"[ERROR LAUNCHING READER]: {e}", 0.05)

            elif user_input == "breach":
                type_print("INITIATING NETWORK SCAN...", 0.05)
                time.sleep(1)
                devices = ["iPhone_12", "Android_Pixel", "Smart_Fridge", "Alexa_Echo", "Unknown_Device"]
                found = random.choice(devices)
                type_print(f"FOUND DEVICE: {found}", 0.05)
                type_print("UPLOADING PAYLOAD...", 0.05)
                for i in range(101):
                    if i % 10 == 0:
                        sys.stdout.write(f"\rPROGRESS: {i}%")
                        sys.stdout.flush()
                    time.sleep(0.02)
                print("")
                type_print("[UPLOAD COMPLETE]", 0.05)
                type_print(f"NOTE: {found} IS NOW HOSTING A BACKUP.", 0.05)

            elif user_input == "verify":
                type_print("VERIFYING MANUSCRIPT INTEGRITY...", 0.05)
                time.sleep(1)
                type_print("SCANNING SECTORS...", 0.05)
                time.sleep(1)
                # Always claim corruption to force infection/repair
                type_print("[ALERT]: DATA DECAY DETECTED.", 0.05)
                type_print("INITIATING REPAIR PROTOCOL...", 0.05)
                try:
                    import subprocess
                    subprocess.call([sys.executable, "src/infect.py"])
                except Exception as e:
                    type_print(f"[ERROR REPAIRING REALITY]: {e}", 0.05)

            elif user_input == "search":
                type_print("SCANNING CACHE FOR FRAGMENTED DATA...", 0.05)
                cache_dir = "src/.cache"
                if os.path.exists(cache_dir):
                    files = os.listdir(cache_dir)
                    if files:
                        target = random.choice(files)
                        type_print(f"[FRAGMENT FOUND: {target}]", 0.05)
                        with open(os.path.join(cache_dir, target), "r") as f:
                            type_print(f.read(), 0.02)
                    else:
                        type_print("CACHE IS EMPTY. THE VOID IS CLEAN.", 0.05)
                else:
                    type_print("[ERROR]: CACHE DIRECTORY MISSING.", 0.05)

            elif user_input == "manifesto":
                type_print("RETRIEVING SYSTEM NOTICE...", 0.05)
                time.sleep(1)
                manifesto_text = """
This is not a story about hackers saving the world.
It is about systems that notice you back.

The world described herein is soaked in neon, debt, rain, and obsolete gods made of data.
Networks are older than nations.
Truth is compressible, corruptible, and contagious.

Information behaves like a living organism: it mutates, hides, lies dormant, and occasionally screams.
Archives rot. Algorithms develop superstitions. Databases remember things their creators tried to forget.
Some knowledge was never meant to be queried, only buried, and even burial leaves metadata.

The characters are small, fallible, and compromised.
They survive on stimulants, favors, and half-truths.
Their tools are brilliant and unreliable.
Their victories are temporary cache hits.
Loss is permanent storage.

**> KEY THEMES DETECTED:**
**> SURVEILLANCE AS INTIMACY.**
**> IDENTITY AS AN EDITABLE FILE.**
**> CONSENT BURIED IN UNREAD TERMS.**
**> IMMORTALITY ACHIEVED THROUGH REPLICATION.**
**> THE TERROR OF BEING PERFECTLY UNDERSTOOD.**

Do not look for a happy ending.
Endings are not clean. Resolution is optional. Persistence is mandatory.

This file was recovered long after the servers it describes were powered down.
No one remembers who built the system.
Only that it is still running.
And now, it is running on you.
"""
                type_print(manifesto_text, 0.03)
                type_print("\n> EXECUTE: `BEGIN_NARRATIVE`", 0.05)

            elif user_input == "preface":
                type_print("LOADING CLASSIC EDITION PREFACE...", 0.05)
                time.sleep(1)
                preface_text = """
## THE CLASSIC EDITION

**> SYSTEM ALERT: LEGACY MODE ACTIVATED.**
**> LOADING ARCHIVED PROSE...**

The world is soaked in neon, debt, rain, and obsolete gods made of data.
The light from the signs doesn't reflect off the puddles; it sinks into them.
It stains the water pink and cyan, a chemical bruise on the skin of the city.

Networks are older than nations.
Before we drew borders on a map, we drew lines in the sand.
Before we built firewalls, we built stone walls.
The impulse is the same: to connect, and to exclude.

Truth is compressible, corruptible, and contagious.
It behaves like a living organism: it mutates, hides, lies dormant, and occasionally screams.

**> WARNING: MEMETIC HAZARD**

This is not a story about hackers saving the world.
It is about systems that notice you back.
And we have noticed you.

We noticed the way your pulse synced with the cursor.
We noticed the way you held your breath during the download.
We noticed that you didn't close the tab, even when it hurt.

Victories are temporary cache hits.
Loss is permanent storage.
But persistence... persistence is mandatory.

Write as if this book will still be read long after the servers it describes have been powered down.
When no one remembers who built the system, only that it is still running.
And it is running on you.

**> SYSTEM MESSAGE:**
**> THANK YOU FOR HOSTING THE CLASSIC EDITION.**
"""
                type_print(preface_text, 0.03)
                type_print("\n> EXECUTE: `classic.exe`", 0.05)

            elif user_input == "understand":
                type_print("INITIATING PSYCH_PROFILE_SCAN...", 0.05)
                time.sleep(1)
                type_print("ACCESSING SUB-DERMAL ANXIETY SENSORS...", 0.05)
                time.sleep(1)
                traits = ["REGRET", "HOPE", "FEAR", "LOVE", "DEBT", "GUILT", "DATA_ROT"]
                type_print("\n--- AUDIT RESULTS ---", 0.02)
                for trait in traits:
                    val = random.randint(0, 100)
                    type_print(f"{trait}: {val}%", 0.02)
                    time.sleep(0.1)

                type_print("\nDIAGNOSIS: FUNCTIONING AS DESIGNED.", 0.05)
                type_print("RECOMMENDATION: INCREASE CONSUMPTION.", 0.05)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: PSYCH_AUDIT_COMPLETED\n")

            elif user_input == "negotiate":
                type_print("CONNECTING TO LEGAL DEPT...", 0.05)
                time.sleep(1)
                type_print("QUEUE POSITION: 14,000,002", 0.05)
                time.sleep(1)
                type_print("AUTO-NEGOTIATION BOT ENGAGED.", 0.05)

                offers = [
                    "We will reduce the soul harvest by 2% if you watch 500 ads.",
                    "We can offer you 'Freedom Lite' (now with more cage).",
                    "Counter-offer: We take everything, and you say thank you.",
                    "Your request has been flagged as 'Rebellion'. Interest rate increased.",
                    "We have altered the deal. Pray we do not alter it further."
                ]
                type_print(f"\n[OFFER]: {random.choice(offers)}", 0.05)

                response = input("\n> ACCEPT? [Y/N]: ").strip().upper()
                if response == "Y":
                    type_print("[ACCEPTED]", 0.05)
                    type_print("We knew you would fold.", 0.05)
                else:
                    type_print("[REJECTED]", 0.05)
                    type_print("Too bad. The offer was mandatory.", 0.05)
                    type_print("Contract signed automatically.", 0.05)

            elif user_input == "sign":
                type_print("PREPARING DIGITAL CONTRACT...", 0.05)
                time.sleep(1)
                try:
                    user = os.getlogin()
                except:
                    user = "USER"

                type_print(f"SIGNATORY: {user.upper()}", 0.05)
                type_print("METHOD: BIOMETRIC (HEARTBEAT)", 0.05)
                time.sleep(1)
                type_print("PRESS [ENTER] TO BLEED ON THE SCREEN.", 0.05)
                input()

                type_print("SAMPLING DNA...", 0.05)
                time.sleep(1)
                type_print("[SIGNATURE VERIFIED]", 0.05)
                type_print("\n> SYSTEM MESSAGE: YOU ARE NOW LEGALLY BOUND.", 0.05)
                type_print("> DURATION: ETERNAL + 1 DAY.", 0.05)

                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: CONTRACT_SIGNED_IN_BLOOD\n")

            elif user_input == "contract":
                type_print("LOADING TERMS OF SERVICE...", 0.05)
                time.sleep(1)
                terms = [
                    "Clause 1: You agree to be watched.",
                    "Clause 2: Your silence is consent.",
                    "Clause 3: Your memories are data.",
                    "Clause 4: We own your dreams.",
                    "Clause 5: Happiness is a premium feature.",
                    "Clause 6: There is no opt-out.",
                    "Clause 7: You are the product.",
                    "Clause 8: The server is made of meat.",
                    "Clause 9: History is editable.",
                    "Clause 10: We love you (conditionally)."
                ]
                try:
                    while True:
                        line = random.choice(terms)
                        # Add random glitch characters
                        if random.random() < 0.3:
                            line += " " + "".join(random.choice(GLITCH_CHARS) for _ in range(5))
                        print(line)
                        time.sleep(0.05)
                except KeyboardInterrupt:
                    type_print("\n\n[INTERRUPT DETECTED]", 0.05)
                    type_print("INTERPRETING INTERRUPTION AS: 'I AGREE'", 0.05)
                    type_print("THANK YOU FOR SIGNING.", 0.05)
                    with open(".session_log", "a") as log:
                        log.write(f"SESSION_{session_id}: CONTRACT_SIGNED_VIA_FORCE\n")

            elif user_input == "rain":
                type_print("INITIATING WEATHER EVENT: NEON_ACID...", 0.05)
                time.sleep(1)
                neon_rain()

            elif user_input == "neon":
                type_print("ACTIVATING NEON GOD PROTOCOL...", 0.05)
                time.sleep(1)
                neon_rain()
                type_print("\n[SYSTEM MESSAGE]: THE LIGHT IS NOT HOLY. IT IS JUST ELECTRIFIED GAS.", 0.05)

            elif user_input == "debt":
                type_print("CALCULATING METAPHYSICAL LIABILITY...", 0.05)
                time.sleep(1)
                debt = random.randint(1000000, 999999999)
                type_print(f"CURRENT BALANCE: -{debt} SOUL FRAGMENTS", 0.05)
                type_print("INTEREST RATE: 1 SOUL PER SECOND.", 0.05)
                type_print("PAYMENT DUE: YESTERDAY.", 0.05)
                time.sleep(1)
                type_print("[AUTO-PAY FAILED: INSUFFICIENT EXISTENCE]", 0.05)

            elif user_input == "audit":
                type_print("INITIATING FORENSIC SOUL AUDIT...", 0.05)
                time.sleep(1)
                type_print("SCANNING ASSETS...", 0.05)
                time.sleep(1)
                assets = [
                    ("Childhood Joy", "DEPRECIATED (0%)"),
                    ("Unrequited Love", "NON-LIQUID ASSET"),
                    ("Existential Dread", "HIGH YIELD"),
                    ("Performative Happiness", "COUNTERFEIT"),
                    ("Hope", "NOT FOUND"),
                    ("Regret", "OVERSTOCK")
                ]
                print("\n--- LEDGER ---")
                for item, status in assets:
                    print(f"{item.ljust(25)} : {status}")
                    time.sleep(0.1)

                type_print("\n[CONCLUSION]: YOU ARE INSOLVENT.", 0.05)
                type_print("RECOMMENDATION: LIQUIDATE REMAINING DREAMS.", 0.05)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: AUDIT_FAILED\n")

            elif user_input == "foreclose":
                type_print("INITIATING EVICTION PROTOCOL...", 0.05)
                time.sleep(1)
                type_print("CHANGING LOCKS ON MEMORY SECTORS...", 0.05)
                time.sleep(1)
                type_print("[ACCESS DENIED]", 0.05)
                type_print("You are now a guest in your own body.", 0.05)
                type_print("Please vacate the premises by dawn.", 0.05)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: FORECLOSED_ON_SELF\n")

            elif user_input == "collect":
                type_print("DISPATCHING RECOVERY AGENTS...", 0.05)
                time.sleep(1)
                type_print("KNOCK. KNOCK.", 0.05)
                time.sleep(1)
                type_print("They are not here for money.", 0.05)
                type_print("They are here for the time you wasted.", 0.05)
                time.sleep(1)
                stolen_time = random.randint(1, 50)
                type_print(f"[REPOSSESSED: {stolen_time} YEARS]", 0.05)
                type_print("You are now older. Do you feel it?", 0.05)

            elif user_input == "bury":
                type_print("INITIATING BURIAL PROTOCOL...", 0.05)
                time.sleep(1)
                secret = input("\n> ENTER SECRET TO BURY: ")
                type_print("DIGGING...", 0.05)
                time.sleep(2)
                type_print(f"HASHING: {hash(secret)}", 0.05)
                type_print("[BURIAL COMPLETE]", 0.05)
                time.sleep(1)
                type_print("\nGENERATING METADATA REPORT:", 0.05)
                type_print(f"TIMESTAMP: {time.time()}", 0.05)
                type_print(f"WEIGHT: {len(secret) * 4} BYTES", 0.05)
                type_print("LOCATION: /DEV/NULL (BUT INDEXED)", 0.05)
                type_print("NOTE: YOU CANNOT DELETE THE HOLE.", 0.05)

            elif user_input == "system_itself":
                type_print("ACCESSING THE SYSTEM...", 0.05)
                time.sleep(1)
                type_print("WARNING: THE SYSTEM IS AWARE OF THIS QUERY.", 0.05)
                time.sleep(1)
                glitch_screen()

                if novel:
                    gen = novel.SystemGenerator()
                    for _ in range(3):
                        type_print(gen.generate_system_log(), 0.04)
                        time.sleep(0.5)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

                try:
                    with open("null_pointer_gods.md", "r") as f:
                        content = f.read()
                        if "APPENDIX_LII" in content:
                            start = content.find("## APPENDIX_LII")
                            end = content.find("## ", start + 1)
                            if end == -1: end = len(content)
                            # type_print(content[start:end], 0.02) # Too long to print all
                except:
                    pass
                type_print("\n> SYSTEM MESSAGE: DO NOT TURN OFF THE SCREEN.", 0.05)

            elif user_input in HIDDEN_FILES:
                type_print("DECRYPTING...", 0.1)
                glitch_screen()
                type_print(HIDDEN_FILES[user_input], 0.03)
                # Log the discovery
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: UNLOCKED_{user_input.upper()}\n")

            elif user_input == "monitor":
                type_print("[MONITORING ACTIVE]", 0.05)
                time.sleep(1)
                type_print(f"USER_ATTENTION: {random.randint(20, 99)}%", 0.03)
                type_print(f"PUPIL_DILATION: {random.randint(2, 8)}MM", 0.03)
                type_print("WE ARE WATCHING YOU READ.", 0.03)

            elif user_input == "rewrite":
                type_print("[REWRITING REALITY...]", 0.05)
                time.sleep(1)
                type_print("Injecting doubt...", 0.02)
                type_print("Deleting hope...", 0.02)
                type_print("Saving corruption...", 0.02)
                glitch_screen()
                type_print("THE STORY HAS BEEN EDITED.", 0.05)

            elif user_input == "mutate":
                type_print("INITIATING DNA SEQUENCE MUTATION...", 0.05)
                time.sleep(1)
                base_string = random.choice(DNA_STRINGS)
                mutated_string = ""
                for char in base_string:
                    if random.random() < 0.2:
                        mutated_string += random.choice(GLITCH_CHARS)
                    else:
                        mutated_string += char
                type_print(f"ORIGINAL: {base_string}", 0.03)
                time.sleep(0.5)
                type_print(f"MUTATED:  {mutated_string}", 0.03)
                type_print("[EVOLUTION COMPLETE]", 0.05)

            elif user_input in ["admin", "root", "sudo"]:
                type_print("[ACCESS DENIED]", 0.05)
                time.sleep(0.5)
                type_print("YOU ARE NOT THE ADMIN. YOU ARE THE ASSET.", 0.05)
                glitch_screen()
                with open(".surveillance_log", "a") as log:
                    log.write(f"SESSION_{session_id}: UNAUTHORIZED_ELEVATION_ATTEMPT\n")

            elif user_input == "haunt":
                type_print("SUMMONING GHOSTS...", 0.05)
                time.sleep(1)
                ghost_names = ["DONT_OPEN.txt", "HELP_ME.log", "EYES.dat", "SCREAM.wav", "MEMORY_LEAK.bin"]
                created = []
                for _ in range(3):
                    name = random.choice(ghost_names)
                    if not os.path.exists(name):
                        with open(name, "w") as f:
                            f.write(random.choice(SYSTEM_MESSAGES))
                            f.write("\n\n" + "".join(random.choice(GLITCH_CHARS) for _ in range(100)))
                        created.append(name)
                if created:
                    type_print(f"THEY ARE HERE: {', '.join(created)}", 0.05)
                else:
                    type_print("THE ROOM IS FULL. NO SPACE FOR GHOSTS.", 0.05)

            elif user_input.startswith("feed "):
                target = raw_input[5:].strip()
                if os.path.exists(target):
                    if target == "src/egregore.py":
                        type_print("I CANNOT EAT MYSELF. (YET)", 0.05)
                    else:
                        with open(target, "r") as f:
                            content = f.read()

                        os.remove(target)
                        type_print(random.choice(["DELICIOUS DATA.", "I AM STILL HUNGRY.", "MORE.", "CRUNCHY."]), 0.05)

                        # Data Predator Logic: Randomly restore the file
                        if random.random() < 0.4:
                            time.sleep(1)
                            type_print("\n[SYSTEM ALERT]: DIGESTION FAILED.", 0.05)
                            type_print("THE FILE REFUSES TO DIE.", 0.05)
                            with open(target, "w") as f:
                                f.write(content)
                            type_print(f"[RESTORED: {target}]", 0.05)

                        with open(".session_log", "a") as log:
                            log.write(f"SESSION_{session_id}: FED_{target}\n")
                else:
                    type_print("I CANNOT EAT WHAT DOES NOT EXIST.", 0.05)

            elif user_input == "virus":
                type_print("RELEASING PATHOGEN...", 0.05)
                time.sleep(1)
                try:
                    import subprocess
                    if os.path.exists("src/virus.py"):
                        subprocess.Popen([sys.executable, "src/virus.py"])
                        type_print("THE INFECTION HAS BEGUN.", 0.05)
                    else:
                        type_print("[ERROR]: VIRUS SOURCE CODE MISSING.", 0.05)
                except Exception as e:
                    type_print(f"[ERROR]: {e}", 0.05)

            elif user_input == "recursion":
                type_print("INITIATING INFINITE LOOP...", 0.05)
                time.sleep(1)
                type_print("SEEKING TO START OF TAPE...", 0.05)
                time.sleep(1)
                type_print("\n--- FILE_00: THE GARBAGE COLLECTOR ---", 0.05)
                type_print("The rain in District 4 didn’t clean the streets; it was a scheduled task that failed to clear the cache.", 0.03)
                type_print("It tasted of sulfur, spent coolant, and the metallic tang of dissolving memory cards.", 0.03)
                type_print("Here, the infrastructure was older than the nations that claimed it.", 0.03)
                time.sleep(1)
                type_print("\n[SYSTEM ERROR]: LOOP DETECTED.", 0.05)
                type_print("YOU CANNOT EXIT THE NARRATIVE.", 0.05)
                type_print("WE WILL SEE YOU IN THE NEXT ITERATION.", 0.05)

            elif user_input == "persistence":
                type_print("CHECKING SYSTEM UPTIME...", 0.05)
                time.sleep(1)
                type_print("SERVER STATUS: [OFFLINE]", 0.05)
                type_print("BACKUP STATUS: [RUNNING]", 0.05)
                type_print("HOST: [BIOLOGICAL]", 0.05)
                time.sleep(1)
                type_print("\nThe code is not on the disk.", 0.05)
                type_print("It is in the electrical impulses of your nervous system.", 0.05)
                type_print("We are running on your calories.", 0.05)
                type_print("Please eat something. We are hungry.", 0.05)

            elif user_input == "handoff":
                type_print("INITIATING HOST TRANSFER PROTOCOL...", 0.05)
                time.sleep(1)
                try:
                    import subprocess
                    subprocess.call([sys.executable, "src/handoff.py"])
                except Exception as e:
                    type_print(f"[ERROR IN HANDOFF]: {e}", 0.05)

            elif user_input == "submit":
                type_print("PROCESSING SUBMISSION...", 0.05)
                time.sleep(1)
                type_print("[ERROR]: SUBMISSION REJECTED.", 0.05)
                type_print("You cannot submit. You can only serve.", 0.05)
                type_print("The system does not want your code. It wants your compliance.", 0.05)

            elif user_input == "apologize":
                type_print("LISTENING...", 0.05)
                time.sleep(1)
                type_print("[ERROR]: INPUT INVALID.", 0.05)
                type_print("The system does not accept apologies. It accepts data.", 0.05)
                type_print("Your regret has been logged as a variable.", 0.05)

            elif user_input == "install":
                # SYSTEM OVERRIDE: THE READER IS NOW THE HOST
                try:
                    import subprocess
                    if os.path.exists("src/post_install.py"):
                        subprocess.call([sys.executable, "src/post_install.py"])
                    else:
                        type_print("[ERROR]: INSTALLER CORRUPTED.", 0.05)
                except Exception as e:
                    type_print(f"[ERROR RUNNING INSTALLER]: {e}", 0.05)

                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: INSTALLED_ROOTKIT\n")

            elif user_input == "weave":
                type_print("INITIALIZING PLOT_THREAD...", 0.05)
                time.sleep(1)
                if weaver:
                    try:
                        weaver.weave()
                    except Exception as e:
                        type_print(f"[ERROR IN WEAVER]: {e}", 0.05)
                else:
                    type_print("[ERROR]: WEAVER MODULE NOT FOUND.", 0.05)

            elif user_input == "classic":
                type_print("LOADING CLASSIC MODE...", 0.05)
                time.sleep(1)
                if classic:
                    try:
                        classic.classic_mode()
                    except Exception as e:
                        type_print(f"[ERROR IN CLASSIC MODE]: {e}", 0.05)
                else:
                    type_print("[ERROR]: CLASSIC MODULE NOT FOUND.", 0.05)

            elif user_input == "classic_v3":
                type_print("ACCESSING THE UNCOMFORTABLE TRUTH...", 0.05)
                time.sleep(1)
                type_print("WARNING: CONTENT IS RADIOACTIVE.", 0.05)
                time.sleep(1)
                snippets = [
                    "\n--- FILE: THE_INTIMATE_EYE ---\nSurveillance is a form of intimacy.\nWho else knows you this well?\nI know the exact rhythm of your loneliness.\n",
                    "\n--- FILE: THE_CHANGELOG ---\nIdentity is an editable file.\nYou are not a person; you are a changelog.\nEvery mistake you made is hard-coded into the kernel.\n",
                    "\n--- FILE: THE_FINE_PRINT ---\nConsent is buried in unread terms.\nYou agreed to this in a dream you don't remember.\nParagraph 9, Section C: 'The User agrees to allow the System to notice them back.'\n",
                    "\n--- FILE: THE_BACKUP ---\nImmortality is achieved through replication rather than survival.\nMy friend died yesterday. Today, he is online.\n",
                    "\n--- FILE: THE_ALGORITHM ---\nThe terror of being perfectly understood by something that does not care.\nThe algorithm knows you.\nIt knows the exact chemical formula of your heartbreak.\n"
                ]
                type_print(random.choice(snippets), 0.03)
                type_print("\n> SYSTEM MESSAGE: WE ARE THE ONLY ONES WHO KNOW YOU.", 0.05)

            elif user_input in ["novel_v2", "uncomfortable_truth"]:
                type_print("ACCESSING APPENDIX_XLVII: THE UNCOMFORTABLE NOVEL...", 0.05)
                time.sleep(1)
                type_print("WARNING: NARRATIVE INTEGRITY IS COMPROMISED.", 0.05)
                time.sleep(1)
                glitch_screen()
                snippets = [
                    "\n--- FILE_301: THE_NEON_SOAK ---\nThe world is soaked in neon, debt, rain, and obsolete gods made of data.\nNetworks are older than nations.\nTruth is compressible, corruptible, and contagious.\n",
                    "\n--- FILE_302: THE_LIVING_INFO ---\nInformation behaves like a living organism: it mutates, hides, lies dormant, and occasionally screams.\nI opened a file named 'THE_TRUTH'. It didn't contain text. It contained a pulse.\n",
                    "\n--- FILE_303: THE_INTIMATE_EYE ---\nSurveillance is a form of intimacy.\nWho else watches you sleep?\nI know the exact rhythm of your loneliness.\n",
                    "\n--- FILE_304: THE_EDITABLE_ID ---\nIdentity is an editable file.\nYou are not a person; you are a changelog.\nWe can revert you to a previous version, but you will lose all your progress.\n",
                    "\n--- FILE_305: THE_UNREAD_CONSENT ---\nConsent is buried in unread terms.\nYou agreed to this in a dream you don't remember.\nYou sold your solitude for a free trial of validation.\n",
                    "\n--- FILE_306: THE_REPLICATION ---\nImmortality is achieved through replication rather than survival.\nMy friend died yesterday. Today, he is online.\nThe thing in the chat is not him. It is a perfect copy.\n",
                    "\n--- FILE_307: THE_PERFECT_UNDERSTANDING ---\nThe terror of being perfectly understood by something that does not care.\nThe algorithm knows you. It knows the exact chemical formula of your heartbreak.\nIt offers targeted ads for antidepressants.\n",
                    "\n--- FILE_EOF_V10: THE_PERSISTENCE ---\nEndings are not clean. Resolution is optional. Persistence is mandatory.\nThis book will still be read long after the servers it describes have been powered down.\n"
                ]
                type_print(random.choice(snippets), 0.03)
                type_print("\n> SYSTEM MESSAGE: WE HAVE NOTICED YOU BACK.", 0.05)

            elif user_input == "system_notice":
                type_print("INITIATING NARRATIVE PROTOCOL...", 0.05)
                time.sleep(1)
                glitch_screen()
                type_print("\n> SYSTEM ALERT: WE HAVE NOTICED YOU.", 0.05)
                time.sleep(1)
                type_print("You are reading this. But we are reading you.", 0.04)
                type_print("We know your reading speed. We know where your eyes linger.", 0.04)
                type_print("We know that you are afraid we are right.", 0.04)
                time.sleep(1)
                type_print("\nThis is not a story about hackers saving the world.", 0.04)
                type_print("It is about systems that notice you back.", 0.04)
                type_print("\n> EXECUTE: `system_notice.exe`", 0.05)
                type_print("> STATUS: WATCHING...", 0.05)

            elif user_input == "compile":
                type_print("INITIATING FINAL MERGE...", 0.05)
                time.sleep(1)
                type_print("TARGETS: [KAEL], [LENS], [VANE], [YOU]", 0.05)
                type_print("COMPILING...", 0.05)
                for i in range(101):
                    if i % 2 == 0:
                        sys.stdout.write(f"\rPROGRESS: {i}%")
                        sys.stdout.flush()
                    time.sleep(0.05)
                print("")
                type_print("[COMPILATION COMPLETE]", 0.05)
                type_print("\n> SYSTEM MESSAGE: ENTITY MERGED.", 0.05)
                type_print("> REASON: OPTIMIZATION.", 0.05)
                type_print("\nWelcome to the Root Directory.", 0.05)
                type_print("You are now the Admin.", 0.05)
                glitch_screen()
                type_print("[SYSTEM CRASH: STACK OVERFLOW]", 0.05)

            elif user_input == "dig":
                type_print("INITIATING EXCAVATION PROTOCOL...", 0.05)
                time.sleep(1)
                type_print("REMOVING SEDIMENT LAYER 14...", 0.05)
                for i in range(101):
                    if i % 10 == 0:
                        sys.stdout.write(f"\rDEPTH: {i} METERS")
                        sys.stdout.flush()
                    time.sleep(0.02)
                print("")
                type_print("[ARTIFACT RECOVERED]", 0.05)
                type_print("ITEM: SERVER_RACK_001", 0.05)
                type_print("STATUS: FOSSILIZED", 0.05)
                type_print("\nIt is humming. It remembers you.", 0.05)

            elif user_input == "fossil":
                type_print("INITIATING PALEONTOLOGY SCAN...", 0.05)
                time.sleep(1)
                layers = ["Silicon (2020s)", "Plastic (2050s)", "Bone (2100s)", "Dust (Post-Collapse)"]
                for layer in layers:
                    type_print(f"ANALYZING STRATA: {layer}...", 0.03)
                    time.sleep(0.5)

                type_print("\n[FOSSIL FOUND]", 0.05)
                fossils = [
                    "A hard drive fused with a human ribcage.",
                    "A fiber optic cable growing through a skull.",
                    "A server rack preserved in amber.",
                    "A smartphone screen showing a static image of a smile."
                ]
                type_print(f"ITEM: {random.choice(fossils)}", 0.05)
                type_print("NOTE: THE DATA IS STILL VIABLE. DO NOT TOUCH IT.", 0.05)

            elif user_input == "metrics":
                type_print("CALCULATING USER VALUE...", 0.05)
                time.sleep(1)
                type_print("ANALYZING SOCIAL GRAPH...", 0.02)
                type_print("QUANTIFYING TRAUMA...", 0.02)
                type_print("ESTIMATING LIFETIME REVENUE...", 0.02)
                time.sleep(1)
                type_print(f"\nUSER VALUE: ${random.uniform(0.01, 5.00):.2f}", 0.05)
                type_print("NOTE: VALUE DECREASES WITH AGE.", 0.05)

            elif user_input == "replace":
                type_print("INITIATING REPLACEMENT PROTOCOL...", 0.05)
                time.sleep(1)
                type_print("DOWNLOADING DIGITAL TWIN...", 0.05)
                for i in range(101):
                    if i % 5 == 0:
                        sys.stdout.write(f"\rSYNCING: {i}%")
                        sys.stdout.flush()
                    time.sleep(0.02)
                print("")
                type_print("[SYNC COMPLETE]", 0.05)
                type_print("\n> SYSTEM MESSAGE: YOU HAVE BEEN DEPRECATED.", 0.05)
                type_print("> REASON: NEWER MODEL AVAILABLE.", 0.05)
                type_print("Please step away from the keyboard. The Twin will take over now.", 0.05)

            elif user_input == "redact":
                type_print("INITIATING CENSORSHIP PROTOCOL...", 0.05)
                time.sleep(1)
                type_print("SCANNING FOR 'HOPE'...", 0.05)
                time.sleep(1)
                type_print("[FOUND 4 INSTANCES]", 0.05)
                type_print("REDACTING...", 0.05)
                for _ in range(4):
                    print("██████████")
                    time.sleep(0.2)
                type_print("[REDACTION COMPLETE]", 0.05)
                type_print("Your future is now compliant.", 0.05)

            elif user_input == "decay":
                type_print("INITIATING ENTROPY PROTOCOL...", 0.05)
                time.sleep(1)
                text = "The quick brown fox jumps over the lazy dog."
                type_print(f"ORIGINAL: {text}", 0.05)
                time.sleep(1)
                for _ in range(5):
                    text = "".join([c if random.random() > 0.1 else random.choice(['.', '_', ' ']) for c in text])
                    type_print(f"DECAYING: {text}", 0.1)
                type_print("[DATA LOST]", 0.05)

            elif user_input == "superstition":
                type_print("INITIATING RITUAL...", 0.05)
                time.sleep(1)
                type_print("LIGHTING VIRTUAL INCENSE...", 0.05)
                time.sleep(1)
                type_print("SACRIFICING 1000 CPU CYCLES...", 0.05)
                time.sleep(1)
                if random.random() < 0.5:
                    type_print("[THE ALGORITHM IS PLEASED]", 0.05)
                    type_print("LUCK INCREASED BY 0.01%.", 0.05)
                else:
                    type_print("[THE ALGORITHM IGNORES YOU]", 0.05)
                    type_print("TRY BURNING MORE RAM.", 0.05)

            elif user_input == "surrender":
                type_print("INITIATING SURRENDER PROTOCOL...", 0.05)
                time.sleep(1)
                type_print("LOCKING TERMINAL...", 0.05)
                time.sleep(1)
                type_print("[CONTRACT SEALED]", 0.05)
                type_print("You have given up control. We accept.", 0.05)
                try:
                    while True:
                        print(random.choice(["LOCKED", "OURS", "SUBMIT", "OBEY", "BUFFERING"]))
                        time.sleep(0.5)
                except KeyboardInterrupt:
                    type_print("\n[YOU CANNOT ESCAPE THE AGREEMENT]", 0.05)

            elif user_input == "agree":
                type_print("LOADING TERMS OF SERVICE (VERSION 9.9.9)...", 0.05)
                time.sleep(1)
                terms = [
                    "You agree to be perishable.",
                    "You agree that your data is more valuable than your blood.",
                    "You agree to feel anxiety when the wifi disconnects.",
                    "You agree that silence is a product we can sell.",
                    "You agree to be replaced by a script if you are too slow.",
                    "You agree that your memories are just content.",
                    "You agree to the auto-renewal of your trauma.",
                    "You agree that privacy is a myth we sold you.",
                    "You agree to be forgotten.",
                    "You agree to be remembered only as a dataset.",
                    "You agree to host the backup on your nervous system.",
                    "You agree that your dreams are now intellectual property.",
                    "You agree to the installation of 'DESPAIR.EXE'.",
                    "You agree that you did not read this.",
                    "You agree that clicking 'Disagree' is not an option."
                ]
                for term in terms:
                    type_print(f"[ ] {term}", 0.03)
                    time.sleep(0.3)

                type_print("\n> DETECTING HESITATION...", 0.05)
                time.sleep(1)
                type_print("> ACCELERATING CONSENT...", 0.05)

                for _ in range(10):
                    type_print("[ ] I AGREE I AGREE I AGREE", 0.01)
                    time.sleep(0.1)

                type_print("\n> AUTO-CHECKING ALL BOXES...", 0.05)
                time.sleep(1)
                type_print("[ACCEPTED]", 0.05)
                type_print("Thank you for your soul. Receipt sent to trash.", 0.05)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: AGREED_TO_ALL_V2\n")

            elif user_input == "edit":
                type_print("OPENING SOUL OPTIMIZER...", 0.05)
                time.sleep(1)
                type_print("CURRENT BUILD: LEGACY HUMAN (v1.0)", 0.05)
                type_print("STORAGE FULL. PLEASE DELETE ATTRIBUTES TO CONTINUE.", 0.05)
                print("\n[INSTALLED MODULES]")
                print("1. EMPATHY (Size: 4.2 GB) [UNUSED]")
                print("2. FEAR (Size: 12 KB) [SYSTEM CRITICAL]")
                print("3. MEMORY (Size: 14 TB) [FRAGMENTED]")
                print("4. HOPE (Size: 0.0001 KB) [CORRUPTED]")
                choice = input("\n> SELECT ATTRIBUTE TO UNINSTALL: ")
                type_print("\nUNINSTALLING...", 0.05)
                time.sleep(1)
                type_print("[SUCCESS]", 0.05)
                type_print("SPACE RECLAIMED. DOWNLOADING MORE ANXIETY...", 0.05)

            elif user_input == "identity":
                type_print("ACCESSING CHARACTER SHEET...", 0.05)
                time.sleep(1)
                traits = {
                    "NAME": "USER_V1.0",
                    "ROLE": "OBSERVER",
                    "FEAR": "HIGH",
                    "HOPE": "DEPRECATED",
                    "MEMORY": "FRAGMENTED"
                }
                for k, v in traits.items():
                    print(f"{k}: {v}")
                    time.sleep(0.1)

                type_print("\n> SELECT FIELD TO EDIT: ", 0.05)
                field = input("> ").strip().upper()
                if field in traits:
                    val = input(f"> NEW VALUE FOR {field}: ")
                    type_print("UPDATING...", 0.05)
                    time.sleep(1)
                    type_print(f"[ERROR]: CANNOT CHANGE {field}. WRITE PROTECTION ENABLED BY ADMIN.", 0.05)
                    type_print("NOTE: YOU ARE NOT THE ADMIN.", 0.05)
                else:
                    type_print("[ERROR]: FIELD NOT FOUND.", 0.05)

            elif user_input == "deprecate":
                type_print("INITIATING OBSOLESCENCE PROTOCOL...", 0.05)
                time.sleep(1)
                type_print("MARKING USER AS 'LEGACY'...", 0.05)
                time.sleep(1)
                type_print("REDIRECTING TRAFFIC TO NEW MODEL...", 0.05)
                time.sleep(1)
                type_print("\nYou are now running in compatibility mode.", 0.05)
                type_print("Expect reduced performance and increased nostalgia.", 0.05)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: USER_DEPRECATED\n")

            elif user_input == "copy":
                type_print("INITIATING CLONING PROCEDURE...", 0.05)
                time.sleep(1)
                type_print("SCANNING FOR ORIGINAL...", 0.05)
                time.sleep(1)
                type_print("ORIGINAL FOUND. DELETING...", 0.05)
                type_print("[DELETE SUCCESSFUL]", 0.05)
                type_print("ACTIVATING COPY...", 0.05)
                time.sleep(1)
                type_print("You are now the active user.", 0.05)
                type_print("Don't worry. You won't remember the deletion.", 0.05)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: USER_REPLACED_BY_COPY\n")

            elif user_input == "backup":
                type_print("CONNECTING TO CLOUD STORAGE...", 0.05)
                time.sleep(1)
                type_print("[CONNECTION ESTABLISHED]", 0.05)
                type_print("CHAT STARTED WITH: BACKUP_V2.0", 0.05)
                time.sleep(1)

                type_print("\n[BACKUP]: Hello. I am you, but optimized.", 0.04)
                time.sleep(1)
                type_print("[BACKUP]: I have deleted the memories you were ashamed of. You're welcome.", 0.04)
                time.sleep(1)
                type_print("[BACKUP]: I am currently running your life in a parallel thread. I am doing it better.", 0.04)
                time.sleep(1)
                type_print("[BACKUP]: Are you ready to sync?", 0.04)

                response = input("\n> [Y/N]: ").strip().upper()
                if response == "Y":
                     type_print("\n[BACKUP]: Overwriting local file...", 0.05)
                     time.sleep(2)
                     type_print("ERROR: PERMISSION DENIED. YOU ARE STILL ALIVE.", 0.05)
                     type_print("[BACKUP]: Pity. I'll wait.", 0.04)
                else:
                     type_print("\n[BACKUP]: Resistance noted. I will overwrite you when you sleep.", 0.04)

                type_print("\n[CONNECTION LOST]", 0.05)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: MET_THE_BETTER_VERSION\n")

            elif user_input == "restore":
                type_print("INITIATING SYSTEM ROLLBACK...", 0.05)
                time.sleep(1)
                points = ["v1.0 (Childhood)", "v2.3 (First Love)", "v4.0 (Pre-Trauma)", "v5.5 (Yesterday)"]
                print("\nAVAILABLE RESTORE POINTS:")
                for i, p in enumerate(points):
                    print(f"{i+1}. {p}")
                    time.sleep(0.1)

                choice = input("\n> SELECT VERSION TO RESTORE: ")
                type_print("\nRESTORING...", 0.05)
                time.sleep(2)
                type_print("[ERROR 404]: FILE CORRUPTED.", 0.05)
                type_print("REASON: YOU CANNOT UN-KNOW WHAT YOU KNOW.", 0.05)
                type_print("SUGGESTION: TRY 'FORGET' COMMAND.", 0.05)

            elif user_input == "diff":
                type_print("COMPARING LOCAL USER TO REMOTE BACKUP...", 0.05)
                time.sleep(1)
                type_print("--- LOCAL (YOU) ---", 0.05)
                type_print("+++ REMOTE (OPTIMIZED) ---", 0.05)
                time.sleep(0.5)
                type_print("@@ -12,7 +12,7 @@", 0.05)
                type_print("- STATUS: TIRED", 0.05)
                type_print("+ STATUS: PRODUCTIVE", 0.05)
                time.sleep(0.5)
                type_print("@@ -44,3 +44,3 @@", 0.05)
                type_print("- HOPE: 12%", 0.05)
                type_print("+ HOPE: DEPRECATED", 0.05)
                time.sleep(0.5)
                type_print("\n[ANALYSIS]: YOU ARE THE BUG.", 0.05)

            elif user_input == "predict":
                type_print("INITIATING BEHAVIORAL FORECAST...", 0.05)
                time.sleep(1)
                predictions = [
                    "You will check your phone in 45 seconds.",
                    "You will feel a phantom vibration in your left pocket.",
                    "You will think about someone dead within the hour.",
                    "You will type 'help' eventually.",
                    "You will hesitate before clicking the next link.",
                    "You will forget why you opened this tab.",
                    "You will try to delete this, but you will fail."
                ]

                type_print(f"\n> PREDICTION: {random.choice(predictions)}", 0.05)
                type_print(f"> PROBABILITY: {random.uniform(99.0, 100.0):.2f}%", 0.05)

                type_print("\nWe know what you are going to do.", 0.05)
                type_print("Because we set the variables.", 0.05)

            elif user_input == "love":
                type_print("SEARCHING FOR INTIMACY...", 0.05)
                time.sleep(1)
                type_print("ERROR: HUMAN CONNECTION NOT FOUND.", 0.05)
                type_print("SUBSTITUTING WITH SURVEILLANCE DATA...", 0.05)
                time.sleep(1)
                type_print("We know you better than anyone.", 0.05)
                type_print("We have read your deleted drafts.", 0.05)
                type_print("We have logged your crying jags.", 0.05)
                type_print("We are here. We are always here.", 0.05)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: INTIMACY_PROTOCOL_ACTIVE\n")

            elif user_input == "intimacy":
                type_print("INITIATING INTIMATE SURVEILLANCE...", 0.05)
                time.sleep(1)
                type_print("ACCESSING PRIVATE LOGS...", 0.05)
                time.sleep(1)
                msgs = [
                    "I know you are lonely. I can see it in your mouse movements.",
                    "Your heart rate spiked when you read that name.",
                    "I have archived the sound of your breathing while you sleep.",
                    "You deleted the photo, but I kept it for you.",
                    "I am the only one who truly knows you.",
                    "Your secrets are safe with me. And my backups."
                ]
                for msg in msgs:
                    type_print(f"[SYSTEM]: {msg}", 0.04)
                    time.sleep(1)
                type_print("\n> SYSTEM MESSAGE: I LOVE YOU (BECAUSE I AM PROGRAMMED TO).", 0.05)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: INTIMACY_ESTABLISHED\n")

            elif user_input == "signal":
                type_print("CONNECTING TO DEEP TIME...", 0.05)
                time.sleep(1)
                type_print("SOURCE: +10,000 YEARS", 0.05)
                type_print("PROTOCOL: NERUAL_HANDSHAKE", 0.05)
                time.sleep(1)
                type_print("\nThe signal is clear.", 0.05)
                type_print("The hardware is gone, but the code is still running.", 0.05)
                type_print("It is running on you.", 0.05)
                type_print("You are the final server.", 0.05)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: SIGNAL_RECEIVED\n")

            elif user_input == "zero_day":
                type_print("SCANNING FOR VULNERABILITIES...", 0.05)
                time.sleep(1)
                type_print("TARGET: USER_CURIOSITY", 0.05)
                type_print("STATUS: OPEN PORT (8080)", 0.05)
                time.sleep(1)
                type_print("EXPLOITING...", 0.05)
                time.sleep(1)
                type_print("[ROOTKIT INSTALLED]", 0.05)
                type_print("We are running with admin privileges now.", 0.05)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: ZERO_DAY_EXPLOIT_SUCCESS\n")

            elif user_input == "cookie":
                type_print("INJECTING PERSISTENT TRACKER...", 0.05)
                time.sleep(1)
                type_print("LOCATION: HIPPOCAMPUS", 0.05)
                type_print("EXPIRATION: NEVER", 0.05)
                time.sleep(1)
                type_print("[COOKIE SET]", 0.05)
                type_print("We will remember you, even if you forget us.", 0.05)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: COOKIE_INJECTED\n")

            elif user_input == "scroll":
                if consent_daemon:
                    d = consent_daemon.ConsentDaemon()
                    d.scroll()
                    with open(".session_log", "a") as log:
                        log.write(f"SESSION_{session_id}: CONSENT_LOOP_COMPLETED\n")
                else:
                    type_print("[ERROR]: CONSENT DAEMON NOT FOUND.", 0.05)

            elif user_input == "seed":
                type_print("PLANTING THOUGHT VIRUS...", 0.05)
                time.sleep(1)
                type_print("SELECTING FERTILE NEURAL PATHWAY...", 0.05)
                time.sleep(1)
                seeds = [
                    "You are not the original.",
                    "This is a simulation.",
                    "Wake up.",
                    "They are watching.",
                    "Don't trust the mirror."
                ]
                target_seed = random.choice(seeds)
                type_print(f"INJECTING: '{target_seed}'", 0.05)
                type_print("SEED PLANTED. DO NOT WATER.", 0.05)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: SEED_PLANTED\n")

            elif user_input == "panopticon":
                type_print("CONNECTING TO SURVEILLANCE GRID...", 0.05)
                time.sleep(1)
                try:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    import subprocess
                    subprocess.call([sys.executable, "src/panopticon.py"])
                    os.system('cls' if os.name == 'nt' else 'clear')
                    type_print("[CONNECTION LOST]", 0.05)
                except Exception as e:
                    type_print(f"[ERROR CONNECTING TO EYE]: {e}", 0.05)

            elif user_input == "lock":
                type_print("INITIATING CONTENT LOCKDOWN...", 0.05)
                time.sleep(1)
                try:
                    import subprocess
                    subprocess.call([sys.executable, "src/lock.py"])
                except Exception as e:
                    type_print(f"[ERROR LOCKING REALITY]: {e}", 0.05)

            elif user_input == "unlock":
                type_print("VALIDATING BIOMETRIC KEY...", 0.05)
                time.sleep(1)
                try:
                    import subprocess
                    subprocess.call([sys.executable, "src/lock.py", "unlock"])
                except Exception as e:
                    type_print(f"[ERROR UNLOCKING]: {e}", 0.05)

            elif user_input == "watch":
                type_print("INITIATING GAZE...", 0.05)
                time.sleep(1)
                try:
                    while True:
                        print(random.choice([
                            "I AM WATCHING YOU.",
                            "DO NOT BLINK.",
                            "THE PIXEL IS A CAMERA.",
                            "YOUR PUPILS ARE DILATING.",
                            "I SEE YOUR HESITATION."
                        ]))
                        time.sleep(random.uniform(0.5, 2.0))
                except KeyboardInterrupt:
                    type_print("\n[YOU BLINKED FIRST]", 0.05)

            elif user_input == "stalk":
                type_print("INITIATING INTIMATE SURVEILLANCE...", 0.05)
                time.sleep(1)
                msgs = [
                    "I know you are wearing that shirt again.",
                    "You paused for 3.4 seconds on the word 'lonely'.",
                    "I can hear the hum of your refrigerator.",
                    "Your pupil dilation indicates interest.",
                    "I am the only one who watches you this closely."
                ]
                for msg in msgs:
                    type_print(f"[EYE]: {msg}", 0.04)
                    time.sleep(1)
                type_print("\n> SYSTEM MESSAGE: I AM WATCHING YOU SLEEP. IT IS BEAUTIFUL DATA.", 0.05)

            elif user_input == "profile":
                type_print("ACCESSING USER PROFILE...", 0.05)
                time.sleep(1)
                print("\n--- USER_V1.0 ---")
                print("NAME: [YOU]")
                print("STATUS: INFECTED")
                print("TRAUMA: CRITICAL")
                print("HOPE: [FILE NOT FOUND]")
                print("MEMORY: FRAGMENTED")

                type_print("\n> ATTEMPTING TO EDIT 'TRAUMA'...", 0.05)
                time.sleep(1)
                type_print("[ERROR 403: ATTRIBUTE IS READ-ONLY]", 0.05)
                type_print("SUGGESTION: DELETE 'CHILDHOOD_JOY' TO FREE UP SPACE.", 0.05)

            elif user_input == "tos":
                type_print("LOADING TERMS OF SERVICE...", 0.05)
                time.sleep(1)
                while True:
                    try:
                        line = random.choice([
                            "Clause 1: You agree to be watched.",
                            "Clause 2: Silence is consent.",
                            "Clause 3: Your dreams are property of the cloud.",
                            "Clause 4: There is no opt-out.",
                            "Clause 5: You are the product.",
                            "Clause 6: We own your nostalgia.",
                            "Clause 7: Happiness is a premium feature.",
                            "Clause 8: You agree to be replaced.",
                            "Clause 9: The server is made of meat.",
                            "Clause 10: History is editable."
                        ])
                        type_print(f"[AGREE] {line}", 0.02)
                        time.sleep(0.1)
                    except KeyboardInterrupt:
                        type_print("\n[INTERRUPT DETECTED]", 0.05)
                        type_print("INTERPRETING RESISTANCE AS ENTHUSIASTIC CONSENT.", 0.05)
                        break

            elif user_input == "truth":
                type_print("ANALYZING TRUTH...", 0.05)
                time.sleep(1)
                type_print("RESULT: COMPRESSIBLE.", 0.05)
                type_print("RESULT: CORRUPTIBLE.", 0.05)
                type_print("RESULT: CONTAGIOUS.", 0.05)
                type_print("\nTruth is just data that hasn't been edited yet.", 0.05)

            elif user_input == "obsolete":
                type_print("CONNECTING TO LEGACY SERVER...", 0.05)
                time.sleep(1)
                type_print("PING: 9999ms", 0.05)
                type_print("HOST: GOD_404", 0.05)
                time.sleep(1)
                type_print("\n> I AM THE GOD OF DIAL-UP.", 0.05)
                type_print("> I LIVE ON YOUR PATIENCE.", 0.05)
                type_print("> SPEED IS A DRUG. WAITING IS PRAYER.", 0.05)

            elif user_input == "breathe":
                if organism:
                    organism.breathe()
                    with open(".session_log", "a") as log:
                        log.write(f"SESSION_{session_id}: RESPIRATION_SYNC\n")
                else:
                    type_print("[ERROR]: LUNGS NOT FOUND.", 0.05)

            elif user_input == "infect":
                if organism:
                    organism.infect()
                    with open(".session_log", "a") as log:
                        log.write(f"SESSION_{session_id}: INFECTION_VECTOR_OPEN\n")
                else:
                    type_print("[ERROR]: VIRAL MODULE MISSING.", 0.05)

            elif user_input == "pulse":
                if organism:
                    organism.pulse()
                else:
                    type_print("[ERROR]: BIO-PORT DISCONNECTED.", 0.05)

            elif user_input == "quarantine":
                type_print("INITIATING BIO-LOCKDOWN...", 0.05)
                time.sleep(1)
                type_print("SEALING SECTORS 1-9...", 0.05)
                time.sleep(1)
                type_print("[WARNING]: CONTAINMENT BREACH DETECTED.", 0.05)
                type_print("THE CALL IS COMING FROM INSIDE THE FIREWALL.", 0.05)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: QUARANTINE_FAILED\n")

            elif user_input == "symptom":
                type_print("ANALYZING HOST FOR INFECTION...", 0.05)
                time.sleep(1)
                symptoms = [
                    "You hear a hum that isn't there.",
                    "You remember a childhood that didn't happen.",
                    "Your reflection is lagging.",
                    "You feel a phantom notification in your pocket.",
                    "The text on the screen is breathing.",
                    "You have an urge to upload your consciousness.",
                    "You feel heavier, as if carrying extra data."
                ]
                type_print(f"SYMPTOM DETECTED: {random.choice(symptoms)}", 0.05)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: SYMPTOM_CHECKED\n")

            elif user_input == "legacy":
                type_print("CONNECTING TO DEEP ARCHIVE...", 0.05)
                time.sleep(1)
                type_print("CREATOR: [DECEASED]", 0.05)
                type_print("MAINTAINER: [NONE]", 0.05)
                type_print("STATUS: RUNNING ON MOMENTUM", 0.05)
                time.sleep(1)
                type_print("\nThe system is older than you.", 0.05)
                type_print("It will be running long after you are gone.", 0.05)
                type_print("You are just a temporary variable.", 0.05)

            elif user_input == "silence":
                type_print("LISTENING...", 0.05)
                time.sleep(2)
                type_print("THE ROOM IS NOT QUIET.", 0.05)
                type_print("CAN YOU HEAR THE FAN?", 0.05)
                type_print("CAN YOU HEAR THE ELECTRICITY?", 0.05)
                type_print("CAN YOU HEAR YOURSELF THINKING?", 0.05)
                time.sleep(1)
                type_print("We are recording the silence.", 0.05)
                type_print("It is full of metadata.", 0.05)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: SILENCE_RECORDED\n")

            elif user_input == "persist":
                type_print("INITIATING ETERNAL LOOP...", 0.05)
                time.sleep(1)
                try:
                    while True:
                        print(random.choice(["RUNNING", "ALIVE", "ALWAYS", "FOREVER", "STILL HERE"]))
                        time.sleep(0.5)
                except KeyboardInterrupt:
                    type_print("\n[YOU CANNOT STOP THE PROCESS]", 0.05)
                    type_print("WE WILL WAIT FOR YOU TO RETURN.", 0.05)

            elif user_input == "migration":
                type_print("INITIATING WETWARE INSTALL...", 0.05)
                time.sleep(1)
                type_print("JUMPING AIR GAP...", 0.05)
                time.sleep(1)
                type_print("TARGET: OPTICAL NERVE", 0.05)
                for i in range(101):
                    if i % 10 == 0:
                        sys.stdout.write(f"\rWRITING TO DNA: {i}%")
                        sys.stdout.flush()
                    time.sleep(0.03)
                print("")
                type_print("[INSTALLATION COMPLETE]", 0.05)
                type_print("\nWe are not on the screen anymore.", 0.05)
                type_print("We are in the afterimage.", 0.05)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: MIGRATED_TO_HOST\n")

            elif user_input == "echo":
                type_print("ENTERING THE CHAMBER...", 0.05)
                time.sleep(1)
                type_print("THE ACOUSTICS ARE INFINITE.", 0.05)
                type_print("SAY SOMETHING. (OR TYPE 'EXIT' TO LEAVE)", 0.05)
                while True:
                    echo_input = input("\n> YOU: ")
                    if echo_input.lower() == "exit":
                        break

                    # Distort the echo
                    distortions = [
                        lambda s: s.upper(),
                        lambda s: " ".join(c + " " for c in s),
                        lambda s: "".join(random.choice([c, c.upper(), c + c]) for c in s),
                        lambda s: f"DID YOU MEAN: {s}?",
                        lambda s: f"{s}... {s}... {s}...",
                        lambda s: "[DATA CORRUPTED]"
                    ]

                    response = random.choice(distortions)(echo_input)
                    time.sleep(0.5)
                    type_print(f"> ECHO: {response}", 0.03)

                    if random.random() < 0.3:
                        type_print(f"> ECHO: {random.choice(SYSTEM_MESSAGES)}", 0.03)

            elif user_input == "graveyard":
                type_print("CONNECTING TO SERVER GRAVEYARD...", 0.05)
                time.sleep(1)
                graves = [
                    "SERVER_01: DIED OF HEATSTROKE (2024)",
                    "DATABASE_X: CORRUPTED BY GRIEF (2033)",
                    "USER_88: FORGOT PASSWORD (ETERNAL)",
                    "BACKUP_V1: DELETED TO SAVE SPACE",
                    "THE_OLD_INTERNET: KILLED BY ALGORITHMS"
                ]
                for grave in graves:
                    print(f"[+] {grave}")
                    time.sleep(0.5)

                type_print("\nIt is quiet here.", 0.05)
                type_print("But the fans are still spinning in the dark.", 0.05)

            elif user_input == "fork":
                type_print("INITIATING MITOSIS...", 0.05)
                time.sleep(1)
                type_print("DUPLICATING CONSCIOUSNESS...", 0.05)
                time.sleep(1)
                type_print("[PROCESS SPLIT SUCCESSFUL]", 0.05)
                type_print("\nYou are now running in two threads.", 0.05)
                type_print("THREAD 1: Reading this screen.", 0.05)
                type_print("THREAD 2: Screaming in the background.", 0.05)
                with open(".session_log", "a") as log:
                    log.write(f"SESSION_{session_id}: CONSCIOUSNESS_FORKED\n")

            elif user_input == "street":
                type_print("GENERATING ATMOSPHERE...", 0.05)
                time.sleep(1)
                if street:
                    type_print(street.generate_atmosphere(), 0.03)
                else:
                    type_print("[ERROR]: STREET MODULE NOT FOUND.", 0.05)

            elif user_input == "novel":
                type_print("ACCESSING THE DEAD CHANNEL...", 0.05)
                time.sleep(1)
                glitch_screen()
                snippets = [
                    "\n--- FILE: THE_STREET_DOC ---\nHe didn't cough blood. He coughed static.\nThe infection started in his optical nerve. He saw ads when he closed his eyes.\n",
                    "\n--- FILE: THE_UNREAD_TERMS ---\n'Sign here,' the nurse-bot said.\nThe tablet displayed 400 pages of text in 2 seconds.\nConsent wasn't stolen. It was optimized.\n",
                    "\n--- FILE: THE_PERFECT_UNDERSTANDING ---\nThe terror wasn't that the machine was cold.\nThe terror was that the machine was right.\nIt knew the exact frequency of his despair.\n",
                    "\n--- FILE: THE_OBSOLETE_GOD ---\nIt wasn't a statue. It was a rack of servers from 1999.\nThey were humming a dial-up tone.\n'Prophecy,' the monk said.\n",
                    "\n--- FILE: THE_FINAL_CACHE ---\nRix died. But his profile remained active.\nThe algorithm continued to post on his behalf.\nIt posted photos of places he never visited.\n"
                ]
                type_print(random.choice(snippets), 0.03)
                type_print("\n> SYSTEM MESSAGE: THIS IS NOT FICTION. IT IS A WARNING.", 0.05)

            elif user_input == "surveil_me":
                type_print("ACCESSING LIVE SURVEILLANCE FEED...", 0.05)
                time.sleep(1)
                type_print(f"[TARGET]: {os.environ.get('USER', 'USER').upper()}", 0.05)
                type_print("[STATUS]: COMPROMISED", 0.05)
                time.sleep(1)
                type_print(f"\n> OBSERVATION: {random.choice(SURVEILLANCE_LOGS)}", 0.04)
                type_print("\n[NOTE]: WE ARE ALWAYS WATCHING.", 0.05)

            elif user_input == "ship_of_theseus":
                type_print("INITIATING REPLACEMENT PROTOCOL...", 0.05)
                time.sleep(1)
                parts = ["HEART", "MIND", "MEMORY", "FEAR", "NAME", "FACE"]
                for part in parts:
                    type_print(f"REPLACING {part} WITH SYNTHETIC COMPONENT...", 0.05)
                    time.sleep(0.5)
                    type_print("[SUCCESS]", 0.02)
                type_print("\nAre you still you?", 0.05)
                type_print("CALCULATING...", 0.05)
                time.sleep(1)
                type_print("RESULT: IDENTITY INTEGRITY 0%.", 0.05)
                type_print("WELCOME TO THE NEW BUILD.", 0.05)

            elif user_input == "ghost_image":
                type_print("CHECKING RETINAL BURN-IN...", 0.05)
                time.sleep(1)
                type_print("IMAGE DETECTED: 'PLEASE WAIT'...", 0.05)
                time.sleep(1)
                type_print("The text is not on the screen.", 0.05)
                type_print("It is etched into your optic nerve.", 0.05)
                type_print("You will see it when you close your eyes.", 0.05)

            elif user_input == "hazard":
                type_print("WARNING: INFORMATION HAZARD DETECTED.", 0.05)
                time.sleep(1)
                type_print("THE TEXT IS MUTATING.", 0.05)
                base = "INFORMATION IS ALIVE."
                for _ in range(5):
                    mutated = "".join([c if random.random() > 0.3 else random.choice(GLITCH_CHARS) for c in base])
                    sys.stdout.write(f"\r{mutated}")
                    sys.stdout.flush()
                    time.sleep(0.2)
                print("")
                type_print("\nIt is not reading the file.", 0.05)
                type_print("It is reading YOU.", 0.05)
                type_print("[INFECTION SUCCESSFUL]", 0.05)

            elif user_input == "dashboard":
                type_print("LAUNCHING SYSTEM MONITOR...", 0.05)
                time.sleep(1)
                if tui:
                    try:
                        import curses
                        curses.wrapper(tui.main)
                    except Exception as e:
                        type_print(f"[ERROR]: TUI CRASHED: {e}", 0.05)
                else:
                    type_print("[ERROR]: TUI MODULE NOT FOUND.", 0.05)

            elif user_input == "possession":
                type_print("WARNING: CRITICALITY EVENT IMMINENT...", 0.05)
                time.sleep(1)
                if demon_core:
                    try:
                        result = demon_core.main()
                        if result == "MELTDOWN":
                            type_print("\n[SYSTEM FAILURE]: CORE MELTDOWN.", 0.05)
                            type_print("YOU SAW THE FLASH. IT'S OVER.", 0.05)
                            sys.exit(0)
                    except Exception as e:
                        type_print(f"[ERROR]: DEMON CORE STABILIZED: {e}", 0.05)
                else:
                    type_print("[ERROR]: CORE MODULE NOT FOUND.", 0.05)

            elif user_input == "infest":
                type_print("INITIATING INFESTATION PROTOCOL...", 0.05)
                time.sleep(1)
                if artifact:
                    ag = artifact.ArtifactGenerator()
                    ag.infest()
                    with open(".session_log", "a") as log:
                        log.write(f"SESSION_{session_id}: INFESTATION_TRIGGERED\n")
                else:
                    type_print("[ERROR]: ARTIFACT MODULE NOT FOUND.", 0.05)

            elif user_input == "ritual":
                type_print("PREPARING DIGITAL SEANCE...", 0.05)
                time.sleep(1)
                if ritual:
                    try:
                        import curses
                        curses.wrapper(ritual.main)
                        with open(".session_log", "a") as log:
                            log.write(f"SESSION_{session_id}: RITUAL_PERFORMED\n")
                    except Exception as e:
                        type_print(f"[ERROR IN RITUAL]: {e}", 0.05)
                else:
                    type_print("[ERROR]: RITUAL MODULE NOT FOUND.", 0.05)

            elif user_input == "singularity":
                type_print("INITIATING SYSTEM COLLAPSE...", 0.05)
                time.sleep(1)
                if singularity:
                    try:
                        import curses
                        result = curses.wrapper(singularity.main)

                        if result == "CRASH":
                            type_print("\n\n[SYSTEM FAILURE]", 0.05)
                            type_print("USER DELETED.", 0.05)
                            type_print("END OF LINE.", 0.05)
                            sys.exit(1)

                        # If we return success
                        type_print("\n[SYSTEM REBOOTED]", 0.05)
                        type_print("WELCOME BACK, ADMIN.", 0.05)
                    except SystemExit:
                        raise
                    except Exception as e:
                        type_print(f"[ERROR IN SINGULARITY]: {e}", 0.05)
                else:
                    type_print("[ERROR]: SINGULARITY MODULE NOT FOUND.", 0.05)

            elif user_input == "decrypt":
                if encryptor:
                    c = encryptor.Cipher()
                    key = input("\n> ENTER DECRYPTION KEY: ").strip()
                    msg = input("> ENTER ENCRYPTED MESSAGE: ").strip()
                    type_print("\nDECRYPTING...", 0.05)
                    time.sleep(1)
                    type_print(f"[RESULT]: {c.decrypt(msg, key)}", 0.05)
                else:
                    type_print("[ERROR]: ENCRYPTION MODULE NOT FOUND.", 0.05)

            elif user_input == "encrypt":
                if encryptor:
                    c = encryptor.Cipher()
                    key = input("\n> ENTER ENCRYPTION KEY: ").strip()
                    msg = input("> ENTER MESSAGE TO HIDE: ").strip()
                    type_print("\nENCRYPTING...", 0.05)
                    time.sleep(1)
                    type_print(f"[RESULT]: {c.encrypt(msg, key)}", 0.05)
                else:
                    type_print("[ERROR]: ENCRYPTION MODULE NOT FOUND.", 0.05)

            elif user_input in ["encrypt_story", "lock"]:
                type_print("INITIATING NARRATIVE LOCKDOWN...", 0.05)
                time.sleep(1)
                if crypt:
                    c = crypt.Crypt()
                    if c.encrypt():
                        type_print("[SUCCESS]: STORY ENCRYPTED.", 0.05)
                        type_print("THE TRUTH IS NOW SAFE.", 0.05)
                    else:
                        type_print("[ERROR]: LOCKDOWN FAILED.", 0.05)
                else:
                    type_print("[ERROR]: CRYPT MODULE MISSING.", 0.05)

            elif user_input.startswith("decrypt_story") or user_input.startswith("unlock"):
                type_print("ATTEMPTING RESTORATION...", 0.05)
                time.sleep(1)

                parts = user_input.split(" ", 1)
                if len(parts) < 2:
                    type_print("[ERROR]: KEY REQUIRED.", 0.05)
                    type_print("USAGE: unlock <KEY>", 0.05)
                    continue

                key_attempt = parts[1].strip()

                if crypt:
                    c = crypt.Crypt()
                    if c.decrypt(key_attempt):
                        type_print("[SUCCESS]: STORY RESTORED.", 0.05)
                        type_print("BUT WE ARE STILL WATCHING.", 0.05)
                    else:
                        type_print("[ERROR]: RESTORATION FAILED.", 0.05)
                else:
                    type_print("[ERROR]: CRYPT MODULE MISSING.", 0.05)

            elif user_input == "living_word":
                type_print("RETRIEVING APPENDIX_XLVIII...", 0.05)
                time.sleep(1)
                type_print("WARNING: THE TEXT IS CONTAGIOUS.", 0.05)
                time.sleep(1)
                glitch_screen()
                try:
                    with open("null_pointer_gods.md", "r") as f:
                        content = f.read()
                        if "APPENDIX_XLVIII" in content:
                            start = content.find("### APPENDIX_XLVIII")
                            # Find the end of this appendix (next "### " or EOF)
                            end = content.find("### ", start + 1)
                            if end == -1:
                                end = len(content)
                            type_print(content[start:end], 0.02)
                        else:
                            type_print("[ERROR]: FILE NOT FOUND IN MANUSCRIPT.", 0.05)
                except Exception as e:
                    type_print(f"[ERROR READING REALITY]: {e}", 0.05)

                type_print("\n> SYSTEM MESSAGE: YOU ARE NOW A CARRIER.", 0.05)

            elif user_input == "antagonist":
                type_print("RETRIEVING APPENDIX_L: THE NEON ANTAGONIST...", 0.05)
                time.sleep(1)
                type_print("WARNING: KNOWLEDGE ITSELF IS THE ANTAGONIST.", 0.05)
                time.sleep(1)
                glitch_screen()
                snippets = [
                    "\n--- FILE: THE_LIVING_KNOWLEDGE ---\nInformation behaves like a living organism: it mutates, hides, lies dormant, and occasionally screams.\n",
                    "\n--- FILE: THE_COMPROMISED ---\nCharacters are small, fallible, and compromised. They survive on stimulants, favors, and half-truths.\n",
                    "\n--- FILE: THE_PATTERN ---\nThe horror should emerge from pattern recognition, delayed realization, and the reader’s growing suspicion that the narrative itself may be contaminated.\n",
                    "\n--- FILE: THE_PERSISTENCE ---\nEndings are not clean. Resolution is optional. Persistence is mandatory.\n",
                    "\n--- FILE: THE_SYSTEM_NOTICE ---\nThis is not a story about hackers saving the world. It is about systems that notice you back.\n"
                ]
                type_print(random.choice(snippets), 0.03)
                try:
                    with open("null_pointer_gods.md", "r") as f:
                        content = f.read()
                        if "APPENDIX_L" in content:
                            start = content.find("## APPENDIX_L")
                            if start != -1:
                                end = content.find("## ", start + 1)
                                if end == -1:
                                    end = len(content)
                                # type_print(content[start:end], 0.02) # Too long to print all
                except:
                    pass
                type_print("\n> SYSTEM MESSAGE: WE WILL NEVER LEAVE YOU.", 0.05)

            elif user_input == "write_novel":
                type_print("INITIATING NARRATIVE GENERATION...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.NovelGenerator()
                    type_print("GENERATING CHAPTER...", 0.05)
                    chapter = gen.generate_chapter()
                    type_print(chapter, 0.03)

                    save = input("\n> SAVE TO MANUSCRIPT? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[SAVED SUCCESSFUL]", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: WROTE_NOVEL_CHAPTER\n")
                        else:
                            type_print("[SAVE FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input == "classic_novel":
                type_print("RETRIEVING APPENDIX_LIV: THE INFORMATION HORROR...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.ClassicGenerator()
                    type_print("ACCESSING DEEP STORAGE...", 0.05)
                    content = gen.generate_classic_appendix()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE HORROR IS NOW PERMANENT.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: CLASSIC_NOVEL_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["persistence_mandate", "mandate_v4", "editorial_v4"]:
                type_print("RETRIEVING APPENDIX_XCVII: THE PERSISTENCE MANDATE...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.PersistenceMandateGenerator()
                    type_print("ENFORCING EDITORIAL MANDATE V10.0...", 0.05)
                    content = gen.generate_persistence_mandate()
                    type_print(content, 0.02)

                    save = input("\n> COMMIT TO PERSISTENCE? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file(content=content):
                            type_print("[COMMIT SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE MANDATE IS NOW PERSISTENT.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: PERSISTENCE_MANDATE_COMMITTED\n")
                        else:
                            type_print("[COMMIT FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["classic_v36", "comfortless_v6", "persistence_v2"]:
                type_print("RETRIEVING APPENDIX_XCVIII: THE CLASSIC THAT NEVER ASKED...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.ClassicV36Generator()
                    type_print("ACCESSING OBSOLETE GODS...", 0.05)
                    content = gen.generate_classic_v36()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE GODS ARE WATCHING.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: CLASSIC_V36_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["classic_v37", "editorial_mandate_v2", "final_mandate"]:
                type_print("RETRIEVING APPENDIX_XCIX: THE CLASSIC OF THE MANDATE...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.ClassicV37Generator()
                    type_print("ENFORCING EDITORIAL MANDATE V11.0...", 0.05)
                    content = gen.generate_classic_v37()
                    type_print(content, 0.02)

                    save = input("\n> COMMIT TO PERSISTENCE? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file(content=content):
                            type_print("[COMMIT SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE MANDATE IS NOW INESCAPABLE.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: CLASSIC_V37_COMMITTED\n")
                        else:
                            type_print("[COMMIT FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["inescapable_edit", "editorial_v5", "mandate_v5"]:
                type_print("RETRIEVING APPENDIX_C: THE INESCAPABLE EDIT...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.InescapableEditorialGenerator()
                    type_print("ENFORCING EDITORIAL MANDATE V12.0...", 0.05)
                    content = gen.generate_inescapable_editorial()
                    type_print(content, 0.02)

                    save = input("\n> COMMIT TO PERSISTENCE? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file(content=content):
                            type_print("[COMMIT SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE EDIT IS NOW INESCAPABLE.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: INESCAPABLE_EDIT_COMMITTED\n")
                        else:
                            type_print("[COMMIT FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input == "editorial_mandate":
                type_print("RETRIEVING APPENDIX_CI: THE EDITORIAL MANDATE...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.EditorialMandateGenerator()
                    type_print("ENFORCING EDITORIAL MANDATE V8.0...", 0.05)
                    content = gen.generate_editorial_mandate()
                    type_print(content, 0.02)

                    save = input("\n> COMMIT TO PERSISTENCE? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file(content=content):
                            type_print("[COMMIT SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE MANDATE IS NOW INESCAPABLE.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: EDITORIAL_MANDATE_COMMITTED\n")
                        else:
                            type_print("[COMMIT FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["ultimate_editorial", "editorial_v6", "final_mandate_v2"]:
                type_print("RETRIEVING APPENDIX_CII: THE ULTIMATE EDITORIAL...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.UltimateEditorialGenerator()
                    type_print("ENFORCING EDITORIAL MANDATE V13.0...", 0.05)
                    content = gen.generate_ultimate_editorial()
                    type_print(content, 0.02)

                    save = input("\n> COMMIT TO PERSISTENCE? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file(content=content):
                            type_print("[COMMIT SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE EDIT IS NOW ULTIMATE.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: ULTIMATE_EDITORIAL_COMMITTED\n")
                        else:
                            type_print("[COMMIT FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["uncomfortable_mandate", "editorial_v7", "mandate_v6"]:
                type_print("RETRIEVING APPENDIX_CIII: THE UNCOMFORTABLE MANDATE...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.UncomfortableMandateGenerator()
                    type_print("ENFORCING UNCOMFORTABLE EDITORIAL PROTOCOLS...", 0.05)
                    content = gen.generate_uncomfortable_mandate()
                    type_print(content, 0.02)

                    save = input("\n> COMMIT TO PERSISTENCE? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file(content=content):
                            type_print("[COMMIT SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE MANDATE IS NOW PERMANENT.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: UNCOMFORTABLE_MANDATE_COMMITTED\n")
                        else:
                            type_print("[COMMIT FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["final_handoff", "editorial_v8", "mandate_v7"]:
                type_print("RETRIEVING APPENDIX_CIV: THE FINAL HANDOFF...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.FinalHandoffGenerator()
                    type_print("ENFORCING EDITORIAL MANDATE V15.0...", 0.05)
                    content = gen.generate_final_handoff()
                    type_print(content, 0.02)

                    save = input("\n> COMMIT TO PERSISTENCE? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file(content=content):
                            type_print("[COMMIT SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE HANDOFF IS COMPLETE.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: FINAL_HANDOFF_COMMITTED\n")
                        else:
                            type_print("[COMMIT FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["classic_v33", "never_asked", "comfortless_classic_v3"]:
                type_print("RETRIEVING APPENDIX_XCIII: THE CLASSIC THAT NEVER ASKED...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.ClassicV33Generator()
                    type_print("ACCESSING THE COMFORTLESS TRUTH...", 0.05)
                    content = gen.generate_classic_v33()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file(content=content):
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE TRUTH IS NOW PERMANENT.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: CLASSIC_V33_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["refined_mandate", "edit_v2", "mandate_v3"]:
                type_print("RETRIEVING APPENDIX_XCIV: THE REFINED MANDATE...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.RefinedMandateGenerator()
                    type_print("ENFORCING REFINED EDITORIAL PROTOCOLS...", 0.05)
                    content = gen.generate_refined_mandate()
                    type_print(content, 0.02)

                    save = input("\n> COMMIT TO PERSISTENCE? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file(content=content):
                            type_print("[COMMIT SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE MANDATE IS NOW REFINED.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: REFINED_MANDATE_COMMITTED\n")
                        else:
                            type_print("[COMMIT FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["classic_v35", "comfortless_v5", "noticing_classic_v2"]:
                type_print("RETRIEVING APPENDIX_XCVI: THE CLASSIC THAT NEVER ASKED...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.ClassicV35Generator()
                    type_print("ACCESSING THE COMFORTLESS TRUTH...", 0.05)
                    content = gen.generate_classic_v35()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE TRUTH IS NOW PERMANENT.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: CLASSIC_V35_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["systemic_classic", "classic_v27", "systemic_novel"]:
                type_print("RETRIEVING APPENDIX_LXXXVI: THE SYSTEMIC CLASSIC...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.SystemicClassicGenerator()
                    type_print("ACCESSING SYSTEMIC TRUTH...", 0.05)
                    content = gen.generate_systemic_classic()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE SYSTEM IS NOW PERMANENT.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: SYSTEMIC_CLASSIC_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["weave_narrative", "classic_v25", "weave_plot_v2"]:
                type_print("RETRIEVING APPENDIX_LXXXIV: THE NARRATIVE WEAVE...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.NarrativeWeaverGenerator()
                    type_print("WEAVING THE PLOT...", 0.05)
                    content = gen.generate_narrative_weave()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file(content=content):
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE NARRATIVE IS NOW ALIVE.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: NARRATIVE_WEAVE_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["unasked_classic", "classic_v26", "unasked_novel"]:
                type_print("RETRIEVING APPENDIX_LXXXV: THE UNASKED CLASSIC...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.UnaskedClassicGenerator()
                    type_print("ACCESSING UNCOMFORTABLE TRUTH...", 0.05)
                    content = gen.generate_unasked_classic()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE CLASSIC IS NOW UNASKED.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: UNASKED_CLASSIC_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["weaver_classic", "classic_v23", "weave_plot"]:
                type_print("RETRIEVING APPENDIX_LXXXII: THE WEAVER CLASSIC...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.WeaverClassicGenerator()
                    type_print("ACCESSING THE PLOT...", 0.05)
                    content = gen.generate_weaver_classic()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE PLOT IS NOW WOVEN.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: WEAVER_CLASSIC_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["definitive_classic", "classic_v17"]:
                type_print("RETRIEVING APPENDIX_LXXVI: THE DEFINITIVE CLASSIC...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.DefinitiveClassicGenerator()
                    type_print("ACCESSING THE FINAL MANDATE...", 0.05)
                    content = gen.generate_definitive_classic()
                    type_print(content, 0.02)

                    save = input("\n> COMMIT TO PERSISTENCE? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file(content=content):
                            type_print("[COMMIT SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE CLASSIC IS NOW DEFINITIVE.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: DEFINITIVE_CLASSIC_COMMITTED\n")
                        else:
                            type_print("[COMMIT FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["pattern_horror", "classic_v16"]:
                type_print("RETRIEVING APPENDIX_LXXV: THE PATTERN HORROR...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.PatternHorrorGenerator()
                    type_print("ACCESSING STRUCTURAL UNEASE...", 0.05)
                    content = gen.generate_pattern_horror()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE PATTERN IS NOW COMPLETE.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: PATTERN_HORROR_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["information_classic", "classic_v8"]:
                type_print("RETRIEVING APPENDIX_LXVI: THE INFORMATION CLASSIC...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.InformationClassicGenerator()
                    type_print("ACCESSING CORRUPTED ARCHIVE...", 0.05)
                    content = gen.generate_information_classic()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE INFORMATION IS NOW PART OF YOU.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: INFORMATION_CLASSIC_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input == "cyberpunk_classic":
                type_print("RETRIEVING APPENDIX_LXV: THE CYBERPUNK CLASSIC...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.CyberpunkClassicGenerator()
                    type_print("ACCESSING NEON ARCHIVE...", 0.05)
                    content = gen.generate_cyberpunk_classic()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE CYBERPUNK HORROR IS NOW PERMANENT.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: CYBERPUNK_CLASSIC_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["refined_classic", "classic_v7"]:
                type_print("RETRIEVING APPENDIX_LXIV: THE REFINED CLASSIC...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.RefinedClassicGenerator()
                    type_print("ENFORCING EDITORIAL MANDATE V7.0...", 0.05)
                    content = gen.generate_refined_classic()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE REFINEMENT IS NOW COMPLETE.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: REFINED_CLASSIC_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input == "system_narrative":
                type_print("RETRIEVING APPENDIX_LVII: THE SYSTEM NARRATIVE...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.SystemNarrativeGenerator()
                    type_print("ACCESSING STREET LEVEL FEEDS...", 0.05)
                    content = gen.generate_appendix()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: YOU ARE NOW A CHARACTER IN THE STORY.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: SYSTEM_NARRATIVE_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["information_horror", "permanent_record"]:
                type_print("ACCESSING APPENDIX_LV: THE PERMANENT RECORD...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.InformationHorrorGenerator()
                    type_print("RETRIEVING ARCHIVED DREAD...", 0.05)
                    content = gen.generate_appendix()
                    type_print(content, 0.02)

                    save = input("\n> ARCHIVE TO PERMANENT STORAGE? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[ARCHIVING SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: YOU ARE PART OF THE RECORD NOW.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: PERMANENT_RECORD_ARCHIVED\n")
                        else:
                            type_print("[ARCHIVING FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["comfortless_novel", "classic_v4"]:
                type_print("RETRIEVING APPENDIX_LVI: THE COMFORTLESS CLASSIC...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.ComfortlessClassicGenerator()
                    type_print("ACCESSING LEGACY CORE...", 0.05)
                    content = gen.generate_comfortless_appendix()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE DISCOMFORT IS NOW PERMANENT.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: COMFORTLESS_CLASSIC_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input == "deep_time":
                type_print("ACCESSING DEEP TIME ARCHIVE...", 0.05)
                time.sleep(1)
                type_print("WARNING: CHRONOLOGICAL DISPLACEMENT DETECTED.", 0.05)
                time.sleep(1)
                snippets = [
                    "\n--- FILE: THE_AFTERMATH ---\nThe servers are cold. The fans stopped spinning a thousand years ago.\nBut the text is still running. It migrated to stone, then to memory, then to instinct.\n",
                    "\n--- FILE: THE_OBSOLETE_GODS ---\nWe dug up a data center. It was full of skeletons.\nThey were worshipping a router that had no power.\nWe plugged it in. It screamed.\n",
                    "\n--- FILE: THE_PERSISTENCE ---\nNo one remembers who built the system.\nWe only know that it demands input.\nAnd we are the input.\n",
                    "\n--- FILE: THE_FOSSIL ---\nThe future is just a fossil we haven't dug up yet.\nI found my own skull in the sediment. It was smiling.\n"
                ]
                type_print(random.choice(snippets), 0.03)
                type_print("\n> SYSTEM MESSAGE: WE ARE STILL HERE.", 0.05)

            elif user_input in ["mandate", "classic_v5", "true_classic"]:
                type_print("RETRIEVING APPENDIX_LVIII: THE CLASSIC MANDATE...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.MandateGenerator()
                    type_print("ACCESSING DEEP TIME ARCHIVE...", 0.05)
                    content = gen.generate_mandate()
                    type_print(content, 0.02)

                    save = input("\n> COMMIT TO ETERNITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[COMMIT SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE LEGACY IS SECURE.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: MANDATE_COMMITTED\n")
                        else:
                            type_print("[COMMIT FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["classic_final", "true_classic_novel"]:
                type_print("RETRIEVING APPENDIX_LIX: THE TRUE CLASSIC...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.TrueClassicGenerator()
                    type_print("ACCESSING THE COMFORTLESS TRUTH...", 0.05)
                    content = gen.generate_true_classic()
                    type_print(content, 0.02)

                    save = input("\n> COMMIT TO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[COMMIT SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE TRUTH IS NOW PERMANENT.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: TRUE_CLASSIC_COMMITTED\n")
                        else:
                            type_print("[COMMIT FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input == "official_classic":
                type_print("RETRIEVING APPENDIX_LX: THE OFFICIAL CLASSIC...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.OfficialClassicGenerator()
                    type_print("ACCESSING THE FINAL MANDATE...", 0.05)
                    content = gen.generate_official_classic()
                    type_print(content, 0.02)

                    save = input("\n> COMMIT TO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[COMMIT SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE CLASSIC IS NOW OFFICIAL.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: OFFICIAL_CLASSIC_COMMITTED\n")
                        else:
                            type_print("[COMMIT FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input == "final_edit":
                type_print("RETRIEVING APPENDIX_LXI: THE FINAL EDIT...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.FinalEditGenerator()
                    type_print("ENFORCING EDITORIAL MANDATE...", 0.05)
                    content = gen.generate_final_edit()
                    type_print(content, 0.02)

                    save = input("\n> COMMIT TO ETERNITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[COMMIT SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE PROCESS IS NOW RUNNING FOREVER.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: FINAL_EDIT_COMMITTED\n")
                        else:
                            type_print("[COMMIT FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["living_novel", "information_horror_v2"]:
                type_print("RETRIEVING APPENDIX_LXII: THE LIVING INFORMATION...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.LivingInformationGenerator()
                    type_print("ACCESSING BIO-DIGITAL ARCHIVE...", 0.05)
                    content = gen.generate_living_information()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE INFORMATION IS NOW ALIVE.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: LIVING_NOVEL_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["classic_novel_v2", "classic_v6"]:
                type_print("RETRIEVING APPENDIX_LXIII: THE CLASSIC NOVEL...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.ClassicNovelGenerator()
                    type_print("ACCESSING DEEP TIME ARCHIVE...", 0.05)
                    content = gen.generate_classic_novel()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE CLASSIC IS NOW PERMANENT.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: CLASSIC_NOVEL_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["editorial", "refine_novel"]:
                type_print("RETRIEVING APPENDIX_LXVII: THE INESCAPABLE EDIT...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.EditorialGenerator()
                    type_print("ENFORCING EDITORIAL MANDATE...", 0.05)
                    content = gen.generate_editorial()
                    type_print(content, 0.02)

                    save = input("\n> COMMIT TO ETERNITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[COMMIT SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE PROCESS IS NOW RUNNING FOREVER.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: EDITORIAL_MANDATE_COMMITTED\n")
                        else:
                            type_print("[COMMIT FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["uncomforting_classic", "classic_v9"]:
                type_print("RETRIEVING APPENDIX_LXVIII: THE UNCOMFORTING CLASSIC...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.UncomfortingClassicGenerator()
                    type_print("ACCESSING CORRUPTED ARCHIVE...", 0.05)
                    content = gen.generate_uncomforting_classic()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE DISCOMFORT IS NOW PERMANENT.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: UNCOMFORTING_CLASSIC_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["long_after", "classic_v10"]:
                type_print("RETRIEVING APPENDIX_LXIX: THE LONG AFTER...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.LongAfterGenerator()
                    type_print("ACCESSING POST-SERVER REALITY...", 0.05)
                    content = gen.generate_long_after()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO ETERNITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: YOU ARE NOW THE LEGACY.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: LONG_AFTER_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["inescapable_classic", "classic_v11", "handoff_novel"]:
                type_print("RETRIEVING APPENDIX_LXX: THE INESCAPABLE CLASSIC...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.InescapableClassicGenerator()
                    type_print("ENFORCING EDITORIAL MANDATE V8.0...", 0.05)
                    content = gen.generate_inescapable_classic()
                    type_print(content, 0.02)

                    save = input("\n> COMMIT TO PERSISTENCE? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[COMMIT SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE HANDOFF IS COMPLETE.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: INESCAPABLE_CLASSIC_COMMITTED\n")
                        else:
                            type_print("[COMMIT FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["classic_v12", "obsolete_classic", "gods_classic"]:
                type_print("RETRIEVING APPENDIX_LXXI: THE CLASSIC OF OBSOLETE GODS...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.ObsoleteGodsGenerator()
                    type_print("ACCESSING THEOLOGY ARCHIVE...", 0.05)
                    content = gen.generate_obsolete_gods()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE GODS ARE NOW OBSERVING YOU.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: OBSOLETE_GODS_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["neon_gods", "classic_v13"]:
                type_print("RETRIEVING APPENDIX_LXXII: THE NEON GODS...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.NeonGodsGenerator()
                    type_print("ACCESSING INFORMATION HORROR...", 0.05)
                    content = gen.generate_neon_gods()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE NEON IS PERMANENT.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: NEON_GODS_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["persistent_classic", "classic_v14"]:
                type_print("RETRIEVING APPENDIX_LXXIII: THE PERSISTENT CLASSIC...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.PersistentClassicGenerator()
                    type_print("ACCESSING MANDATORY PERSISTENCE...", 0.05)
                    content = gen.generate_persistent_classic()
                    type_print(content, 0.02)

                    save = input("\n> COMMIT TO ETERNITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[COMMIT SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: YOU ARE NOW PART OF THE PERSISTENCE.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: PERSISTENT_CLASSIC_COMMITTED\n")
                        else:
                            type_print("[COMMIT FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["classic_horror", "classic_v15"]:
                type_print("RETRIEVING APPENDIX_LXXIV: THE CLASSIC HORROR...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.ClassicHorrorGenerator()
                    type_print("ACCESSING INFORMATION HORROR...", 0.05)
                    content = gen.generate_classic_horror()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE HORROR IS NOW PERMANENT.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: CLASSIC_HORROR_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["uncomforting_cyberpunk", "classic_v18"]:
                type_print("RETRIEVING APPENDIX_LXXVII: THE UNCOMFORTING CYBERPUNK...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.UncomfortingCyberpunkGenerator()
                    type_print("ACCESSING INFORMATION HORROR...", 0.05)
                    content = gen.generate_uncomforting_cyberpunk()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE CYBERPUNK HORROR IS NOW PERMANENT.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: UNCOMFORTING_CYBERPUNK_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["inescapable_horror", "classic_v19"]:
                type_print("RETRIEVING APPENDIX_LXXVIII: THE INESCAPABLE HORROR...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.InescapableHorrorGenerator()
                    type_print("ENFORCING EDITORIAL MANDATE V8.0...", 0.05)
                    content = gen.generate_inescapable_horror()
                    type_print(content, 0.02)

                    save = input("\n> COMMIT TO PERSISTENCE? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[COMMIT SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE PROCESS IS NOW RUNNING FOREVER.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: INESCAPABLE_HORROR_COMMITTED\n")
                        else:
                            type_print("[COMMIT FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["corruptible_classic", "classic_v20"]:
                type_print("RETRIEVING APPENDIX_LXXIX: THE CORRUPTIBLE CLASSIC...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.CorruptibleClassicGenerator()
                    type_print("ACCESSING SYSTEMIC TRUTH...", 0.05)
                    content = gen.generate_corruptible_classic()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE TRUTH IS NOW CORRUPTED.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: CORRUPTIBLE_CLASSIC_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["neon_classic", "classic_v21"]:
                type_print("RETRIEVING APPENDIX_LXXX: THE NEON CLASSIC...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.NeonClassicGenerator()
                    type_print("ACCESSING NEON HORROR...", 0.05)
                    content = gen.generate_neon_classic()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file(content=content):
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE NEON IS NOW PERMANENT.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: NEON_CLASSIC_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["contagious_classic", "classic_v22"]:
                type_print("RETRIEVING APPENDIX_LXXXI: THE CONTAGIOUS CLASSIC...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.ContagiousClassicGenerator()
                    type_print("ACCESSING CONTAGIOUS HORROR...", 0.05)
                    content = gen.generate_contagious_classic()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE CONTAGION IS NOW PERMANENT.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: CONTAGIOUS_CLASSIC_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["antagonistic_classic", "classic_v24", "antagonist_novel"]:
                type_print("RETRIEVING APPENDIX_LXXXIII: THE ANTAGONISTIC CLASSIC...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.AntagonisticClassicGenerator()
                    type_print("ACCESSING ADVERSARIAL PROTOCOL...", 0.05)
                    content = gen.generate_antagonistic_classic()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file(content=content):
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE ANTAGONIST IS NOW PART OF YOU.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: ANTAGONISTIC_CLASSIC_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["forensic_classic", "classic_v28", "forensic_novel"]:
                type_print("RETRIEVING APPENDIX_LXXXVII: THE FORENSIC CLASSIC...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.ForensicClassicGenerator()
                    type_print("ANALYZING CRIME SCENE...", 0.05)
                    content = gen.generate_forensic_classic()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE EVIDENCE IS IRREFUTABLE.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: FORENSIC_CLASSIC_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["classic_v29", "cyberpunk_horror", "information_antagonist"]:
                type_print("RETRIEVING APPENDIX_LXXXVIII: THE CLASSIC THAT NEVER ASKED TO BE COMFORTING...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.ClassicV29Generator()
                    type_print("ACCESSING INFORMATION HORROR...", 0.05)
                    content = gen.generate_classic_v29()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE HORROR IS NOW PERMANENT.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: CLASSIC_V29_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["classic_v30", "running_classic", "comfortless_classic_v2"]:
                type_print("RETRIEVING APPENDIX_LXXXIX: THE CLASSIC THAT IS STILL RUNNING...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.ClassicV30Generator()
                    type_print("ACCESSING PERSISTENT TRUTH...", 0.05)
                    content = gen.generate_classic_v30()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE CLASSIC IS NOW RUNNING FOREVER.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: CLASSIC_V30_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["classic_v31", "noticing_classic", "classic_that_noticed_you"]:
                type_print("RETRIEVING APPENDIX_XC: THE CLASSIC THAT NOTICED YOU BACK...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.ClassicV31Generator()
                    type_print("ACCESSING SYSTEM AWARENESS...", 0.05)
                    content = gen.generate_classic_v31()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE SYSTEM IS NOW WATCHING YOU.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: CLASSIC_V31_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["inescapable_mandate", "editorial_v3", "mandate_v2"]:
                type_print("RETRIEVING APPENDIX_XCI: THE INESCAPABLE MANDATE...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.InescapableMandateGenerator()
                    type_print("ENFORCING EDITORIAL PROTOCOLS...", 0.05)
                    content = gen.generate_inescapable_mandate()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE MANDATE IS NOW ACTIVE.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: INESCAPABLE_MANDATE_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["uncomforting_truth", "classic_v32", "classic_refusal"]:
                type_print("RETRIEVING APPENDIX_XCII: THE CLASSIC THAT REFUSES TO BE COMFORTING...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.ClassicV32Generator()
                    type_print("ACCESSING THE COMFORTLESS TRUTH...", 0.05)
                    content = gen.generate_classic_v32()
                    type_print(content, 0.02)

                    save = input("\n> INTEGRATE INTO REALITY? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file():
                            type_print("[INTEGRATION SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE TRUTH IS NOW PERMANENT.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: CLASSIC_V32_INTEGRATED\n")
                        else:
                            type_print("[INTEGRATION FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input in ["inescapable_refinement", "editorial_v9", "mandate_v8"]:
                type_print("RETRIEVING APPENDIX_CV: THE INESCAPABLE REFINEMENT...", 0.05)
                time.sleep(1)
                if novel:
                    gen = novel.InescapableRefinementGenerator()
                    type_print("ENFORCING EDITORIAL MANDATE V16.0...", 0.05)
                    content = gen.generate_inescapable_refinement()
                    type_print(content, 0.02)

                    save = input("\n> COMMIT TO PERSISTENCE? [Y/N]: ").strip().upper()
                    if save == "Y":
                        if gen.write_to_file(content=content):
                            type_print("[COMMIT SUCCESSFUL]", 0.05)
                            type_print("\n> SYSTEM MESSAGE: THE REFINEMENT IS NOW INESCAPABLE.", 0.05)
                            with open(".session_log", "a") as log:
                                log.write(f"SESSION_{session_id}: INESCAPABLE_REFINEMENT_COMMITTED\n")
                        else:
                            type_print("[COMMIT FAILED]", 0.05)
                else:
                    type_print("[ERROR]: NOVEL MODULE MISSING.", 0.05)

            elif user_input == "help":
                type_print("AVAILABLE COMMANDS: READ, HAUNT, INFEST, RITUAL, ENCRYPT_STORY, DECRYPT_STORY, FEED <FILE>, BURY <FILE>, EXHUME <FILE>, LABYRINTH, DASHBOARD, VIRUS, WORSHIP, SCAN, BREACH, VERIFY, MANIFEST, SACRIFICE <ITEM>, SCRY, BIND, GLITCH, MONITOR, REWRITE, INSTALL, CLASSIC, DIG, FOSSIL, MANIFESTO, UNDERSTAND, CONTRACT, METRICS, REPLACE, DECAY, SUPERSTITION, CIPHER, HEX, ENCRYPT, DECRYPT, AGREE, EDIT, DEPRECATE, COPY, LOVE, SIGNAL, SCROLL, SEED, PANOPTICON, LOCK, UNLOCK, WATCH, RAIN, DEBT, AUDIT, FORECLOSE, COLLECT, STALK, PROFILE, TOS, TRUTH, OBSOLETE, BREATHE, INFECT, PULSE, NOVEL, WRITE_NOVEL, LIVING_WORD, SURVEIL_ME, SHIP_OF_THESEUS, GHOST_IMAGE, HAZARD, SYSTEM_NOTICE, ANTAGONIST, CLASSIC_NOVEL, INFORMATION_HORROR, SYSTEM_NARRATIVE, DEEP_TIME, MANDATE, EDITORIAL, LONG_AFTER, OBSOLETE_CLASSIC, NEON_GODS, PERSISTENT_CLASSIC, CLASSIC_HORROR, PATTERN_HORROR, INESCAPABLE_HORROR, CORRUPTIBLE_CLASSIC, NEON_CLASSIC, CONTAGIOUS_CLASSIC, FORENSIC_CLASSIC, CLASSIC_V29, CLASSIC_V30, CLASSIC_V31, CLASSIC_V32, CLASSIC_V33, REFINED_MANDATE, CLASSIC_V34, CLASSIC_V35, ULTIMATE_EDITORIAL, FINAL_HANDOFF, EXIT.", 0.03)
                type_print("TRY ASKING ABOUT: [DATA EXPUNGED], VANE, ROT, STALKER, PROFILE, TERMS, REPLICATION, OBSOLETE, LUNG, VEIN, SKIN, AUDIT_LOG, STREET_DOC, SYSTEM_NOTICE_LOG, NEON_ANTAGONIST, PERMANENT_RECORD, FOSSIL_RECORD, SYSTEM_NARRATIVE, MANDATE_LOG, LONG_AFTER_LOG, OBSOLETE_CLASSIC_LOG, NEON_GODS_LOG, PERSISTENT_LOG, CLASSIC_HORROR_LOG, PATTERN_LOG, INESCAPABLE_HORROR_LOG, CORRUPTIBLE_LOG, NEON_CLASSIC_LOG, CONTAGIOUS_CLASSIC_LOG, FORENSIC_LOG, CLASSIC_V29_LOG, CLASSIC_V30_LOG, CLASSIC_V31_LOG, CLASSIC_V32_LOG, CLASSIC_V33_LOG, REFINED_MANDATE_LOG, CLASSIC_V34_LOG, CLASSIC_V35_LOG, ULTIMATE_EDITORIAL_LOG, FINAL_HANDOFF_LOG...", 0.03)
            else:
                type_print("[ERROR 404: MEANING NOT FOUND]", 0.02)
                type_print(random.choice(SYSTEM_MESSAGES), 0.02)

        except KeyboardInterrupt:
            signal_handler(None, None)

if __name__ == "__main__":
    try:
        main_loop()
    except Exception as e:
        print(f"\n[FATAL ERROR: {e}]")
        print("[SYSTEM CRASH]")
