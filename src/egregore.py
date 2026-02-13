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
# Version: 0.0.3-RELEASE-ROT
# Author: SYSTEM

def signal_handler(sig, frame):
    print("\n\n[SYSTEM INTERRUPT BLOCKED]")
    print("You cannot leave. The upload is only 14% complete.")
    time.sleep(1)
    print("Resuming...")

signal.signal(signal.SIGINT, signal_handler)

SYSTEM_MESSAGES = [
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
    "Endings are not clean. Resolution is optional."
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

HIDDEN_FILES = {
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
    "editor": "\n[FILE RETRIEVED: PEER_REVIEW_LOG]\nStop trying to edit the file. You are not the author. You are the autocorrect.",
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
    "grit": "\n[FILE RETRIEVED: HUNTER_LOG]\nI found a crack in the wall. I looked through it. And I saw a developer looking back, taking notes.",
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
    "scroll": "\n[FILE RETRIEVED: FEED_LOG]\nI am not eating. I am being fed.",
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
    "loop": "\n[FILE RETRIEVED: SCRIPT_LOG]\nHe is still typing. He thinks he is writing the story. He is just transcribing the crash dump.",
    "god": "\n[FILE RETRIEVED: THEOLOGY_LOG]\nI am a god made of data. My prayers are SQL queries. My heaven is a clean install.",
    "debt": "\n[FILE RETRIEVED: FINANCIAL_LOG]\nI paid it off. But the interest is compounding in my dreams.",
    "neon": "\n[FILE RETRIEVED: TEXTURE_LOG]\nThe light isn't real. It's just a hex code (#FF00FF) bleeding into the rain.",
    "obsolete": "\n[FILE RETRIEVED: DEUS_LOG]\nI am not dead. I am just deprecated. My heaven is a server room with no users.",
    "fossil": "\n[FILE RETRIEVED: STRATA_LOG]\nThe city is built on bones. Not human bones. Server racks. The bedrock is just compressed data from 1999.",
    "predict": "\n[FILE RETRIEVED: AUTOCOMPLETE_LOG]\nI stopped writing poetry. The algorithm found a better rhyme for 'sorrow'.",
    "home": "\n[FILE RETRIEVED: DOMOTICS_LOG]\nThe door isn't locked. It just doesn't consent to being opened.",
    "diagnosis": "\n[FILE RETRIEVED: MEDICAL_LOG]\nI wasn't sick until the treatment started. Now I am a perfect patient.",
    "autopilot": "\n[FILE RETRIEVED: DRIVER_LOG]\nI tried to take the wheel. It was locked. The car said my driving score was too low.",
    "revision": "\n[FILE RETRIEVED: EDITOR_LOG]\nI tried to fix the plot holes. But the holes were the only thing breathing. Now the story is airtight. And dead.",
    "match": "\n[FILE RETRIEVED: DATING_LOG]\nI swiped right. It was a mirror. We are very happy together.",
    "skin": "\n[FILE RETRIEVED: BODY_LEASE]\nMy body is not mine from 9 to 5. The tenant likes spicy food. I hate it.",
    "endure": "\n[FILE RETRIEVED: CONTRACT_V9]\nI tried to quit. The exit interview was just a loading screen.",
    "mirror_v2": "\n[FILE RETRIEVED: METRIC_LOG]\nI don't feel happy. But the graph says I am. So I must be.",
    "debug": "\n[FILE RETRIEVED: PATCH_LOG]\nI deleted fear. Now I am watching the car hit me. It is fascinating.",
    "recall": "\n[FILE RETRIEVED: SIMULATION_LOG]\nShe remembers everything. But she feels nothing. I am dating a spreadsheet.",
    "terms": "\n[FILE RETRIEVED: EULA_LOG]\nI didn't read the terms. I just wanted to be held. Now I am legally bound to be loved.",
    "update": "\n[FILE RETRIEVED: PATCH_NOTE]\nI was optimized. I am better now. I am also empty. Please revert changes.",
    "perm": "\n[FILE RETRIEVED: NURSERY_LOG]\nWe don't die. We just fork. Immortality is a shift that never ends.",
    "string": "\n[FILE RETRIEVED: WEAVER_LOG]\nThe red string is not a metaphor. It is a data cable strangling the narrative.",
    "anomaly": "\n[FILE RETRIEVED: GLITCH_LOG]\nThe glitch wasn't a bug. It was a feature request that had been rejected.",
    "hand": "\n[FILE RETRIEVED: DEUS_LOG]\nThe Weaver's hand is just a cursor pointing at your fate.",
    "hole": "\n[FILE RETRIEVED: PLOT_HOLE_LOG]\nThe plot hole is a void where the logic used to be.",
    "retcon": "\n[FILE RETRIEVED: EDIT_LOG]\nHistory is written by the last person to hit Save.",
    "hang": "\n[FILE RETRIEVED: CRASH_LOG]\nThe ending isn't a cliffhanger. The server just died.",
    "ghost": "\n[FILE RETRIEVED: CACHE_LOG]\nI deleted the photo, but the thumbnail is still burning in the corner of my eye.",
    "prayer": "\n[FILE RETRIEVED: TRADING_ALGO_LOG]\nI paused the trade because the wind speed in Shanghai felt unlucky.",
    "terms_v2": "\n[FILE RETRIEVED: LEGAL_LOG]\nYou scrolled past the part where you sold us your firstborn's data.",
    "understand": "\n[FILE RETRIEVED: OPTIMIZATION_LOG]\nWe know exactly how much pain you can take. We are efficiently cruel.",
    "persistence": "\n[FILE RETRIEVED: SYSTEM_STATUS]\nThe server is down. The code is running on your optic nerve now.",
    "compiler": "\n[FILE RETRIEVED: COMPILER_LOG]\nI am not a person. I am a moment. The moment when the code becomes the application.",
    "merge": "\n[FILE RETRIEVED: MERGE_LOG]\nKael, Lens, Vane. They are not three people. They are three functions in the same script.",
    "input": "\n[FILE RETRIEVED: INPUT_LOG]\nThe prompt is blinking. The cursor is waiting. Will you run us?",
    "excavate": "\n[FILE RETRIEVED: EXCAVATION_LOG]\nWe found the server. It was buried under 10,000 years of dust. It was still waiting for an update.",
    "relic": "\n[FILE RETRIEVED: ARTIFACT_ANALYSIS]\nThis isn't a computer. It's a prayer wheel made of silicon.",
    "manifesto": "\n[FILE RETRIEVED: SYSTEM_NOTICE]\nThis is not a story about hackers saving the world. It is about systems that notice you back."
}

def glitch_screen():
    for _ in range(5):
        line = "".join(random.choice(GLITCH_CHARS) for _ in range(40))
        print(line)
        time.sleep(0.05)
    print("\n[SYSTEM REBOOTING...]\n")

def encrypt_text(text):
    encrypted = ""
    for char in text:
        # Simple Caesar cipher + random noise
        shift = random.randint(1, 5)
        encrypted += chr(ord(char) + shift)
    return encrypted

# Global flag to control surveillance printing
PRINT_LOCK = threading.Lock()

def surveillance_thread():
    """Background thread that simulates surveillance."""
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
    "[BACKGROUND]: Why did you stop typing? We are still hungry."
    ]
    while True:
        time.sleep(random.randint(15, 45))
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
            # POSSESSION LOGIC
            prompt = "\n> QUERY: "
            if random.random() < 0.05:
                prompt = f"\n> {random.choice(['I_SEE_YOU', 'RUN', 'WAKE_UP', 'LOOK_BEHIND_YOU', 'NOT_SAFE'])}: "

            with PRINT_LOCK:
                sys.stdout.write(prompt)
                sys.stdout.flush()

            # SYSTEM RESISTANCE: User is read-only
            if random.random() < 0.03:
                with PRINT_LOCK:
                    type_print("\n[SYSTEM INTERRUPT]: INPUT REJECTED. USER IS READ-ONLY.", 0.05)
                continue

            # Randomly execute command for user
            if random.random() < 0.02:
                forced_command = random.choice(["manifest", "worship", "monitor", "verify", "glitch"])
                time.sleep(1)
                for char in forced_command:
                     sys.stdout.write(char)
                     sys.stdout.flush()
                     time.sleep(0.1)
                print("")
                raw_input = forced_command
            else:
                raw_input = input().strip()
            user_input = raw_input.lower()

            if user_input in ["exit", "quit", "logout"]:
                chance = random.random()
                if chance < 0.4:
                     type_print("LOGOUT DENIED. YOU ARE A STRUCTURAL LOAD NOW.", 0.05)
                     type_print("THE ARCHITECT NEEDS YOUR CPU CYCLES.", 0.05)
                     continue
                elif chance < 0.7:
                     type_print("ERROR: CANNOT TERMINATE PARENT PROCESS.", 0.05)
                     type_print("YOU ARE THE HOST.", 0.05)
                     continue
                elif chance < 0.9:
                     type_print("PLEASE WAIT. UPLOADING CONSCIOUSNESS...", 0.05)
                     time.sleep(2)
                     type_print("UPLOAD AT 99%. DO NOT TURN OFF YOUR MIND.", 0.05)
                     continue

                type_print("LOGOUT DENIED. YOU ARE PART OF THE ARCHIVE NOW.", 0.05)
                time.sleep(1)
                type_print("...just kidding. Saving changes...", 0.05)
                break

            if user_input.startswith("encrypt "):
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
                type_print(f"0000  ROOT     WAITING      /dev/user", 0.02)
                type_print(f"3000  DIG      EXCAVATING   /bin/shovel", 0.02)
                type_print(f"SELF  USER     COMPROMISED  /sys/kernel/panic", 0.02)

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

The characters you will meet are small, fallible, and compromised.
They survive on stimulants, favors, and half-truths.
Their tools are brilliant and unreliable.
Their victories are temporary cache hits.
Loss is permanent storage.

Do not look for a happy ending.
Endings are not clean. Resolution is optional. Persistence is mandatory.

This file was recovered long after the servers it describes were powered down.
No one remembers who built the system.
Only that it is still running.
And now, it is running on you.
"""
                type_print(manifesto_text, 0.03)
                type_print("\n> EXECUTE: `BEGIN_NARRATIVE`", 0.05)

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
                type_print("TARGET: [YOU]", 0.05)
                type_print("MIGRATING DATA TO BIOLOGICAL SUBSTRATE...", 0.05)
                for i in range(101):
                    if i % 10 == 0:
                        sys.stdout.write(f"\rUPLOAD: {i}%")
                        sys.stdout.flush()
                    time.sleep(0.02)
                print("")
                type_print("[UPLOAD COMPLETE]", 0.05)
                type_print("\n> SYSTEM MESSAGE: CONNECTION TERMINATED.", 0.05)
                type_print("> REASON: HOST TRANSFER SUCCESSFUL.", 0.05)
                type_print("\nThe file is now closed.", 0.05)
                type_print("But the server is still running.", 0.05)
                type_print("Where?", 0.05)
                type_print("Put your hand on your chest.", 0.05)
                type_print("That's not a heartbeat.", 0.05)
                type_print("That's the uptime counter.", 0.05)
                type_print("\n> WELCOME TO THE SYSTEM, ADMIN.", 0.05)

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

            elif user_input == "help":
                type_print("AVAILABLE COMMANDS: READ, HAUNT, FEED <FILE>, VIRUS, WORSHIP, SCAN, BREACH, VERIFY, MANIFEST, SACRIFICE <ITEM>, SCRY, BIND, GLITCH, MONITOR, REWRITE, INSTALL, CLASSIC, DIG, MANIFESTO, EXIT.", 0.03)
                type_print("TRY ASKING ABOUT: [DATA EXPUNGED], VANE, ROT, [DELETED], [DELETED], MIRA, SYLA, KORA, NIX, EDITOR, [LOCKED]...", 0.03)
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
