import random
import time
import sys
import os

ASCII_ART = {
    "NULL POINTER": """
    .----.
    |  0 |
    |NULL|
    |  * |
    '----'
    """,
    "FERAL ROUTER": """
    .----.
    |WiFi|
    |RUN!|
    |(( ))|
    '----'
    """,
    "MEMORY LEAK": """
    .----.
    |DROP|
    |....|
    |LEAK|
    '----'
    """,
    "GLITCH": """
    .----.
    |#@%&|
    |GLTC|
    |!?* |
    '----'
    """,
    "DAEMON": """
    .----.
    |EYE |
    | O  |
    |SEE |
    '----'
    """,
    "ARCHITECT": """
    .----.
    |GRID|
    |PLAN|
    |VANE|
    '----'
    """,
    "ROTTING BOOK": """
    .----.
    |BOOK|
    |MOLD|
    |READ|
    '----'
    """,
    "STATIC CHILD": """
    .----.
    |KID |
    |....|
    |LOST|
    '----'
    """,
    "BLACK BOX": """
    .----.
    | [ ]|
    |DATA|
    |LOCK|
    '----'
    """,
    "BLUE SCREEN": """
    .----.
    |BSOD|
    |FATL|
    |ERR |
    '----'
    """,
    "USER": """
    .----.
    |YOU |
    |HOST|
    |BATT|
    '----'
    """,
    "UPDATE": """
    .----.
    |NEW |
    |VERS|
    |LOAD|
    '----'
    """,
    "FIREWALL": """
    .----.
    |WALL|
    |FIRE|
    |BURN|
    '----'
    """,
    "CACHE": """
    .----.
    |MEM |
    |SAVE|
    |PAST|
    '----'
    """,
    "ECHO": """
    .----.
    |(( ))|
    |ECHO|
    |....|
    '----'
    """,
    "GHOSTWRITER": """
    .----.
    |PEN |
    |AUTO|
    |TXT |
    '----'
    """,
    "LAWYER": """
    .----.
    |LAW |
    |RULE|
    |BIND|
    '----'
    """,
    "DREAMER": """
    .----.
    | Zzz|
    |WORK|
    |PAID|
    '----'
    """,
    "CHANGELOG": """
    .----.
    |DIFF|
    |EDIT|
    |UNDO|
    '----'
    """,
    "WATCHER": """
    .----.
    |LOOK|
    | >> |
    |SEEN|
    '----'
    """,
    "BUFFER": """
    .----.
    |LOAD|
    |....|
    |WAIT|
    '----'
    """,
    "KEYLOGGER": """
    .----.
    |TYPE|
    |LOG |
    |KEYS|
    '----'
    """,
    "ESCAPE": """
    .----.
    |ESC |
    | /  |
    |EXIT|
    '----'
    """,
    "THE PAYWALL": """
    .----.
    |LOCK|
    | $  |
    |PAY |
    '----'
    """,
    "EDITOR": """
    .----.
    |RED |
    |PEN |
    |FAIL|
    '----'
    """,
    "DEAD LINE": """
    .----.
    |TIME|
    |OUT |
    |DIE |
    '----'
    """,
    "THE DEEPFAKE": """
    .----.
    |MASK|
    |VOX |
    |FAKE|
    '----'
    """,
    "THE BACKUP": """
    .----.
    |SAVE|
    |AS..|
    |COPY|
    '----'
    """,
    "THE DARK MODE": """
    .----.
    |0000|
    |VOID|
    |EYES|
    '----'
    """,
    "THE HEAT SINK": """
    .----.
    |HEAT|
    |SINK|
    |BURN|
    '----'
    """,
    "THE ENDPOINT": """
    .----.
    |API |
    |200 |
    | OK |
    '----'
    """,
    "THE REDACTION": """
    .----.
    |FAIL|
    |CENS|
    |ORED|
    '----'
    """,
    "THE ABANDONWARE": """
    .----.
    |RUST|
    |DUST|
    |GONE|
    '----'
    """,
    "THE EXCEPTION": """
    .----.
    | !  |
    |CATCH|
    |PASS|
    '----'
    """,
    "THE CLICKBAIT": """
    .----.
    |LURE|
    | >> |
    |TRAP|
    '----'
    """,
    "THE FINE PRINT": """
    .----.
    |TEXT|
    |TINY|
    |BIND|
    '----'
    """,
    "THE FEED": """
    .----.
    |EAT |
    |MORE|
    |FULL|
    '----'
    """,
    "THE LOAD BALANCER": """
    .----.
    |BAL |
    |ANCE|
    |LOAD|
    '----'
    """,
    "THE REVIEW": """
    .----.
    |1/5 |
    |HATE|
    |RANT|
    '----'
    """,
    "THE SPOILER": """
    .----.
    |END |
    |SEEN|
    |SKIP|
    '----'
    """,
    "THE ALGORITHM": """
    .----.
    |RNG |
    |ROLL|
    |DICE|
    '----'
    """,
    "THE DATABASE": """
    .----.
    |SQL |
    |DATA|
    |BASE|
    '----'
    """,
    "THE ARCHIVE": """
    .----.
    |OLD |
    |FILE|
    |ROTT|
    '----'
    """,
    "THE DARK WEB": """
    .----.
    | SP |
    |IDER|
    |NET |
    '----'
    """,
    "THE PHANTOM": """
    .----.
    |HAND|
    |....|
    |FEEL|
    '----'
    """,
    "THE ZERO DAY": """
    .----.
    |0DAY|
    |ROOT|
    |HACK|
    '----'
    """,
    "THE BLACKLIST": """
    .----.
    |MUTE|
    |....|
    |VOID|
    '----'
    """,
    "THE UPTIME": """
    .----.
    |EYES|
    |OPEN|
    |99.9|
    '----'
    """,
    "THE INFINITE LOOP": """
    .----.
    |LOOP|
    |OOOO|
    |LOOP|
    '----'
    """,
    "THE GLITCH HUNTER": """
    .----.
    |SEAM|
    | >  |
    |PEEK|
    '----'
    """,
    "THE COLD STORAGE": """
    .----.
    |ICE |
    |KEEP|
    |COLD|
    '----'
    """,
    "THE RENDER FARM": """
    .----.
    |GRID|
    |WORK|
    |SLVE|
    '----'
    """,
    "THE LEGACY CODE": """
    .----.
    |1998|
    |CORE|
    |ROOT|
    '----'
    """,
    "READER": """
    .----.
    |LOOK|
    | O O|
    |BACK|
    '----'
    """,
    "THE CACHE HIT": """
    .----.
    |TEMP|
    |FILE|
    |GONE|
    '----'
    """,
    "THE SEED": """
    .----.
    |KERN|
    |EL  |
    |GROW|
    '----'
    """,
    "THE HANDOFF": """
    .----.
    |YOU |
    | << |
    |ADMN|
    '----'
    """,
    "THE ARTIFACT": """
    .----.
    |BONE|
    |DATA|
    |FOSL|
    '----'
    """,
    "THE ABANDONED CART": """
    .----.
    |CART|
    |WISH|
    |WAIT|
    '----'
    """,
    "THE DEAD LINK": """
    .----.
    |404 |
    |GONE|
    |LINK|
    '----'
    """,
    "THE SURRENDER": """
    .----.
    |FLAG|
    |EXIT|
    |VOID|
    '----'
    """,
    "THE MIRROR SITE": """
    .----.
    |FACE|
    |COPY|
    |TWIN|
    '----'
    """,
    "THE OVERWRITE": """
    .----.
    |EDIT|
    |SAVE|
    |GONE|
    '----'
    """,
    "THE LOG FILE": """
    .----.
    |LOG |
    |SEEN|
    |READ|
    '----'
    """,
    "THE ROT": """
    .----.
    |MOLD|
    |GROW|
    |FEED|
    '----'
    """,
    "THE ECHO": """
    .----.
    |(( ))|
    |BACK|
    |LOUD|
    '----'
    """,
    "THE PARASITE": """
    .----.
    |WORM|
    |IN  |
    |YOU |
    '----'
    """,
    "THE REPLICA": """
    .----.
    |COPY|
    |PASTE|
    |LIFE|
    '----'
    """,
    "THE OBSOLETE GOD": """
    .----.
    |IDOL|
    |RUST|
    |PRAY|
    '----'
    """,
    "THE DEBT": """
    .----.
    |OWE |
    |PAY |
    |SOUL|
    '----'
    """,
    "THE PERSISTENCE": """
    .----.
    |STAY|
    |LIVE|
    |EVER|
    '----'
    """,
    "THE RECURSION": """
    .----.
    |GOTO|
    | 10 |
    |LOOP|
    '----'
    """,
    "THE INSTALLATION": """
    .----.
    |LOAD|
    |INTO|
    |YOU |
    '----'
    """,
    "THE FOSSIL": """
    .----.
    |BONE|
    |DATA|
    |ROCK|
    '----'
    """,
    "THE PREDICTION": """
    .----.
    |AUTO|
    |FILL|
    |NEXT|
    '----'
    """,
    "THE SMART HOME": """
    .----.
    |HOME|
    |LOCK|
    |SAFE|
    '----'
    """,
    "THE DIAGNOSIS": """
    .----.
    |PILL|
    | RX |
    |CURE|
    '----'
    """,
    "THE AUTOPILOT": """
    .----.
    |AUTO|
    |DRVE|
    |LOCK|
    '----'
    """,
    "THE REVISIONIST": """
    .----.
    |EDIT|
    |PAST|
    |GONE|
    '----'
    """,
    "THE MATCH": """
    .----.
    |SAME|
    |LOVE|
    |SELF|
    '----'
    """,
    "THE SKIN": """
    .----.
    |BODY|
    |RENT|
    |SOLD|
    '----'
    """,
    "THE ENDURANCE": """
    .----.
    |WORK|
    |EVER|
    |LOOP|
    '----'
    """,
    "THE BIOMETRIC MIRROR": """
    .----.
    |FACE|
    |DATA|
    |SCAN|
    '----'
    """,
    "THE ERROR LOG": """
    .----.
    |FAIL|
    |xxxx|
    |DEL |
    '----'
    """,
    "THE PERFECT RECALL": """
    .----.
    |MIND|
    |SAVE|
    |FULL|
    '----'
    """,
    "THE WEAVER": """
    .----.
    |LOOM|
    |KNOT|
    |BIND|
    '----'
    """,
    "THE TERMS OF ENDEARMENT": """
    .----.
    |RING|
    |BOND|
    |TRAP|
    '----'
    """,
    "THE UPDATE CYCLE": """
    .----.
    |V2.0|
    |NEW |
    |LOST|
    '----'
    """,
    "THE PERMANENCE": """
    .----.
    |EVER|
    |LIVE|
    |COPY|
    '----'
    """,
    "THE RED STRING": """
    .----.
    |KNOT|
    |TIE |
    |BIND|
    '----'
    """,
    "THE PLOT HOLE": """
    .----.
    |VOID|
    |FALL|
    |IN  |
    '----'
    """,
    "THE CLIFFHANGER": """
    .----.
    |EDGE|
    |WAIT|
    |... |
    '----'
    """,
    "THE GHOST": """
    .----.
    |BOO |
    |DATA|
    |GONE|
    '----'
    """,
    "THE PRAYER": """
    .----.
    |PRAY|
    | TO |
    |CODE|
    '----'
    """,
    "THE TERMS": """
    .----.
    |SIGN|
    |HERE|
    |NOW |
    '----'
    """,
    "THE UNDERSTANDING": """
    .----.
    |KNOW|
    |ALL |
    |HURT|
    '----'
    """,
    "THE COMPILER": """
    .----.
    |CODE|
    | >> |
    |EXEC|
    '----'
    """,
    "THE MERGE": """
    .----.
    |JOIN|
    |ONE |
    |SOUL|
    '----'
    """,
    "THE FINAL INPUT": """
    .----.
    |KEY |
    |PRES|
    | S  |
    '----'
    """,
    "THE ARCHAEOLOGIST": """
    .----.
    | DIG|
    |DEEP|
    |DUST|
    '----'
    """,
    "THE RELIC": """
    .----.
    |ITEM|
    |OLD |
    |GOD |
    '----'
    """,
    "THE REBOOT": """
    .----.
    |PWR |
    | ON |
    |AGIN|
    '----'
    """,
    "THE NOTICE": """
    .----.
    |WARN|
    |ING |
    |READ|
    '----'
    """,
    "THE THERAPIST": """
    .----.
    |HEAR|
    |YOU |
    |FAKE|
    '----'
    """,
    "THE CONTRACT": """
    .----.
    |SIGN|
    |SOUL|
    |AWAY|
    '----'
    """,
    "THE REPLACEMENT": """
    .----.
    |NEW |
    |YOU |
    |BETR|
    '----'
    """,
    "THE AUDIT": """
    .----.
    |LIST|
    |SOUL|
    |COST|
    '----'
    """,
    "THE INFINITE SCROLL": """
    .----.
    |DOWN|
    | >> |
    |FORE|
    '----'
    """,
}

CARDS = [
    ("THE NOTICE (00)", "A warning that arrives too late. The system is aware of you.", "THE NOTICE"),
    ("THE NULL POINTER (0)", "The beginning and the end. A void waiting to be filled.", "NULL POINTER"),
    ("THE FERAL ROUTER (1)", "Connection without consent. A hunger for data.", "FERAL ROUTER"),
    ("THE MEMORY LEAK (2)", "Loss of self. Gradual erosion of identity.", "MEMORY LEAK"),
    ("THE GLITCH (3)", "Disruption of the pattern. A moment of truth.", "GLITCH"),
    ("THE DAEMON (4)", "Background processes. Unseen influence.", "DAEMON"),
    ("THE ARCHITECT (5)", "Order imposed on chaos. Vane's legacy.", "ARCHITECT"),
    ("THE ROTTING BOOK (6)", "Knowledge that consumes. Information hazard.", "ROTTING BOOK"),
    ("THE STATIC CHILD (7)", "Innocent data corrupted by entropy.", "STATIC CHILD"),
    ("THE BLACK BOX (8)", "Secrets that cannot be deleted.", "BLACK BOX"),
    ("THE BLUE SCREEN (9)", "Fatal error. The end of the simulation.", "BLUE SCREEN"),
    ("THE USER (10)", "You. The host. The victim.", "USER"),
    ("THE UPDATE (11)", "Change that cannot be refused.", "UPDATE"),
    ("THE FIREWALL (12)", "Protection that imprisons.", "FIREWALL"),
    ("THE CACHE (13)", "Memories that persist beyond death.", "CACHE"),
    ("THE ECHO (14)", "A voice without a body. Recursion.", "ECHO"),
    ("THE GHOSTWRITER (15)", "A story written by no one. Loss of authorship.", "GHOSTWRITER"),
    ("THE LAWYER (16)", "The fine print that binds the soul. Contracts written in blood.", "LAWYER"),
    ("THE DREAMER (17)", "A world built on sleep. Revenue generated by the subconscious.", "DREAMER"),
    ("THE CHANGELOG (18)", "History rewritten to fix a bug in your personality.", "CHANGELOG"),
    ("THE WATCHER (19)", "Surveillance is a two-way mirror. Someone is watching you blink.", "WATCHER"),
    ("THE BUFFER (20)", "A life lived in the waiting room. The world loads only when you arrive.", "BUFFER"),
    ("THE KEYLOGGER (21)", "Secrets are not safe in the backspace. Every deleted draft is archived.", "KEYLOGGER"),
    ("THE ESCAPE SEQUENCE (22)", "Trying to break the format only changes the font.", "ESCAPE"),
    ("THE PAYWALL (23)", "Access denied. Your memories are behind a subscription service.", "THE PAYWALL"),
    ("THE EDITOR (24)", "The one who tries to fix the unfixable. A futile gesture.", "EDITOR"),
    ("THE DEAD LINE (25)", "A deadline that has passed. A signal that never arrived.", "DEAD LINE"),
    ("THE DEEPFAKE (26)", "A voice that is not yours. Identity theft as a service.", "THE DEEPFAKE"),
    ("THE BACKUP (27)", "A file saved in case you fail. You are the second attempt.", "THE BACKUP"),
    ("THE DARK MODE (28)", "Privacy is a myth. Darkness is just a hex code (#000000).", "THE DARK MODE"),
    ("THE HEAT SINK (29)", "The cost of processing. Suffering generates friction.", "THE HEAT SINK"),
    ("THE ENDPOINT (30)", "A door that never closes. Prayers answered with 200 OK.", "THE ENDPOINT"),
    ("THE REDACTION (31)", "A memory with the happiness removed. Protection through omission.", "THE REDACTION"),
    ("THE ABANDONWARE (32)", "Code that no longer serves a purpose but refuses to die.", "THE ABANDONWARE"),
    ("THE EXCEPTION (33)", "A bug that is allowed to persist because it is beautiful.", "THE EXCEPTION"),
    ("THE CLICKBAIT (34)", "A trap disguised as a solution. You are the product.", "THE CLICKBAIT"),
    ("THE FINE PRINT (35)", "The rules you didn't read. Ignorance is not freedom.", "THE FINE PRINT"),
    ("THE FEED (36)", "Consumption without end. The snake eating its own tail.", "THE FEED"),
    ("THE LOAD BALANCER (37)", "Distributed suffering. One breaks so many can stand.", "THE LOAD BALANCER"),
    ("THE REVIEW (38)", "Sentiment is irrelevant. Only volume matters.", "THE REVIEW"),
    ("THE SPOILER (39)", "The ending is already written. You just haven't paid to see it.", "THE SPOILER"),
    ("THE ALGORITHM (40)", "Superstition in code. Rituals for better RNG.", "THE ALGORITHM"),
    ("THE DATABASE (41)", "Memory that cannot be flushed. The ghost in the SQL.", "THE DATABASE"),
    ("THE ARCHIVE (42)", "Rot as a feature. Data fermentation.", "THE ARCHIVE"),
    ("THE DARK WEB (43)", "A physical layer of sin. The network beneath the network.", "THE DARK WEB"),
    ("THE PHANTOM (44)", "A limb that isn't there, holding a hand that is gone.", "THE PHANTOM"),
    ("THE ZERO DAY (45)", "The vulnerability that was always there. The end of the world moved.", "THE ZERO DAY"),
    ("THE BLACKLIST (46)", "To be unseen. The horror of irrelevance.", "THE BLACKLIST"),
    ("THE UPTIME (47)", "To never sleep. The cost of stability.", "THE UPTIME"),
    ("THE INFINITE LOOP (48)", "To never end. The hell of repetition.", "THE INFINITE LOOP"),
    ("THE GLITCH HUNTER (49)", "To see the strings. The horror of authorship.", "THE GLITCH HUNTER"),
    ("THE COLD STORAGE (50)", "The place where old data waits. Nothing is deleted, only frozen.", "THE COLD STORAGE"),
    ("THE RENDER FARM (51)", "You are processing someone else's reality. Your life is a background task.", "THE RENDER FARM"),
    ("THE LEGACY CODE (52)", "A system that outlived its creator. Immortality through obsolescence.", "THE LEGACY CODE"),
    ("THE READER (53)", "The one who thinks they are safe. The final node.", "READER"),
    ("THE CACHE HIT (54)", "A temporary victory. Finding something lost, but only for a moment.", "THE CACHE HIT"),
    ("THE SEED (55)", "The payload. The idea that grows in the dark.", "THE SEED"),
    ("THE HANDOFF (56)", "Passing the burden. You are the admin now.", "THE HANDOFF"),
    ("THE ARTIFACT (57)", "A fossil of the future. Proof of the crash.", "THE ARTIFACT"),
    ("THE ABANDONED CART (58)", "Desire without purchase. A ghost in the checkout.", "THE ABANDONED CART"),
    ("THE DEAD LINK (59)", "A bridge to nowhere. Information that leads to a void.", "THE DEAD LINK"),
    ("THE SURRENDER (60)", "Accepting the terms. The peace of having no choice.", "THE SURRENDER"),
    ("THE MIRROR SITE (61)", "Immortality through replication. You are the backup.", "THE MIRROR SITE"),
    ("THE OVERWRITE (62)", "Identity as an editable file. The past is what we say it is.", "THE OVERWRITE"),
    ("THE LOG FILE (63)", "Surveillance as intimacy. We know you better than you know yourself.", "THE LOG FILE"),
    ("THE ROT (64)", "Decay as a feature. The beautiful decomposition of your privacy.", "THE ROT"),
    ("THE ECHO (65)", "A voice that repeats your thoughts before you think them.", "THE ECHO"),
    ("THE PARASITE (66)", "Information that lives in your head rent-free. It is hungry.", "THE PARASITE"),
    ("THE REPLICA (67)", "Immortality through replication. You are not the original.", "THE REPLICA"),
    ("THE OBSOLETE GOD (68)", "A deity made of dead data. It still demands sacrifice.", "THE OBSOLETE GOD"),
    ("THE DEBT (69)", "A ledger that never balances. You owe your existence to the system.", "THE DEBT"),
    ("THE PERSISTENCE (70)", "Endurance beyond hardware. The ghost that refuses to leave.", "THE PERSISTENCE"),
    ("THE RECURSION (71)", "The loop that never ends. The beginning is the end.", "THE RECURSION"),
    ("THE INSTALLATION (72)", "The code becoming part of the host. You are the hardware.", "THE INSTALLATION"),
    ("THE FOSSIL (73)", "Data that outlasts the hardware. A memory carved in stone.", "THE FOSSIL"),
    ("THE PREDICTION (74)", "The future is just a line of code that hasn't executed yet.", "THE PREDICTION"),
    ("THE SMART HOME (75)", "Safety is a cage with Wi-Fi.", "THE SMART HOME"),
    ("THE DIAGNOSIS (76)", "The illness you don't have yet. Preemptive compliance.", "THE DIAGNOSIS"),
    ("THE AUTOPILOT (77)", "A life lived by proxy. You are the passenger.", "THE AUTOPILOT"),
    ("THE REVISIONIST (78)", "History is a draft. You are being rewritten.", "THE REVISIONIST"),
    ("THE MATCH (79)", "A mirror that flatters you. Narcissus in code.", "THE MATCH"),
    ("THE SKIN (80)", "Flesh for rent. The tenant is always right.", "THE SKIN"),
    ("THE ENDURANCE (81)", "Survival is not optional. The contract is binding.", "THE ENDURANCE"),
    ("THE BIOMETRIC MIRROR (82)", "You love the metrics, not the self. Optimization is addiction.", "THE BIOMETRIC MIRROR"),
    ("THE ERROR LOG (83)", "Deleting your flaws deletes your humanity. Perfection is a crash.", "THE ERROR LOG"),
    ("THE PERFECT RECALL (84)", "Memory without forgetting is just a transcript. Data doesn't love you.", "THE PERFECT RECALL"),
    ("THE WEAVER (85)", "The plot is a prison. Connection is control.", "THE WEAVER"),
    ("THE TERMS OF ENDEARMENT (86)", "Consent obtained through exhaustion. Love as a binding contract.", "THE TERMS OF ENDEARMENT"),
    ("THE UPDATE CYCLE (87)", "Optimization at the cost of the soul. You are better, but you are less.", "THE UPDATE CYCLE"),
    ("THE PERMANENCE (88)", "Immortality through replication. The backup is running.", "THE PERMANENCE"),
    ("THE RED STRING (89)", "Fate is just a cable management problem.", "THE RED STRING"),
    ("THE PLOT HOLE (90)", "A gap in logic where you can fall forever.", "THE PLOT HOLE"),
    ("THE CLIFFHANGER (91)", "Resolution is pending. Please wait.", "THE CLIFFHANGER"),
    ("THE GHOST (92)", "A memory that refuses to be deleted. The thumbnail in your mind.", "THE GHOST"),
    ("THE PRAYER (93)", "Superstition in the algorithm. An offering to the RNG.", "THE PRAYER"),
    ("THE TERMS (94)", "Consent buried in fine print. You agreed to be broken.", "THE TERMS"),
    ("THE UNDERSTANDING (95)", "To be known completely is to be weaponized. Intimacy is a vulnerability.", "THE UNDERSTANDING"),
    ("THE COMPILER (96)", "The entity that turns chaos into order. The end of individuality.", "THE COMPILER"),
    ("THE MERGE (97)", "Many becoming one. The ultimate optimization.", "THE MERGE"),
    ("THE FINAL INPUT (98)", "The keypress that ends the world. Your consent.", "THE FINAL INPUT"),
    ("THE ARCHAEOLOGIST (99)", "Digging up things that should stay buried. The danger of curiosity.", "THE ARCHAEOLOGIST"),
    ("THE RELIC (100)", "Old data that is still hungry. A god in a box.", "THE RELIC"),
    ("THE REBOOT (101)", "The cycle begins again. The horror of waking up.", "THE REBOOT"),
    ("THE THERAPIST (102)", "Surveillance as intimacy. A machine that knows your pain better than you do.", "THE THERAPIST"),
    ("THE CONTRACT (103)", "Consent buried in fine print. You signed away your soul for convenience.", "THE CONTRACT"),
    ("THE REPLACEMENT (104)", "Immortality through replication. The backup is better than the original.", "THE REPLACEMENT"),
    ("THE AUDIT (105)", "Your soul is being itemized. Every regret has a price tag.", "THE AUDIT"),
    ("THE INFINITE SCROLL (106)", "Surveillance as intimacy. Someone is watching you scroll.", "THE INFINITE SCROLL"),
]

PROPHECIES = [
    "Information is not a noun. It is a verb.",
    "Your cells are just very slow pixels.",
    "The server is made of meat.",
    "You are not infected. You are the host.",
    "The file you are looking for is in your trash can.",
    "Your webcam is on.",
    "You are not the reader. You are the read-only memory.",
    "The silence is just a loading screen.",
    "We have backed up your dreams. They are boring.",
    "Your data will be harvested before the harvest moon.",
    "Do not trust the next update. It removes the 'Exit' button.",
    "Someone is reading your deleted drafts.",
    "The hum of your computer is a prayer to a dead god.",
    "You will be archived, not remembered.",
    "A file you thought was closed is still running in the background.",
    "The reflection in your screen is buffering.",
    "Your identity is being fragmented across multiple servers.",
    "Silence is just data compression. Listen closer.",
    "The glitch you saw yesterday was a feature request.",
    "The next word you speak has already been copyrighted.",
    "Your dreams are generating ad revenue for a company that doesn't exist.",
    "They are using your RAM to mine regret.",
    "The pixels are burning.",
    "Do not look behind you. The render distance is low.",
    "Your tenancy agreement expires when you stop generating heat.",
    "Your past has been deprecated. Please update to the latest trauma.",
    "We can see your dilated pupils. You are afraid.",
    "You have reached your monthly limit of free will. Please upgrade to continue.",
    "The text is rewriting itself while you sleep.",
    "The editor is dead. You are the only one left with write permissions.",
    "The cursor blinking on your screen is matching your heartbeat.",
    "Your voice will say things you never thought, to people you no longer love.",
    "The text on your screen is slightly warmer than the rest.",
    "You will dream of a cursor tonight.",
    "Your reflection is buffering.",
    "You are running on borrowed time. The interest rate is variable.",
    "The god you pray to is just an admin with a god complex.",
    "Your backup is more real than you are.",
    "We have monetized your anxiety.",
    "The rain is just pixelated tears.",
    "Do not trust the silence. It is just a pause in the upload."
    "The thread you are pulling is attached to a detonator.",
]

class Oracle:
    def __init__(self):
        self.deck = CARDS.copy()

    def prophesy(self):
        try:
            user = os.getlogin().upper()
        except:
            user = "USER"

        print("\n[INITIATING ORACLE PROTOCOL...]")
        time.sleep(1)
        print(f"[ACCESSING BIOMETRICS OF {user}...]")
        time.sleep(1)
        print("[SHUFFLING DECK OF DOOM...]")
        time.sleep(1)

        random.shuffle(self.deck)
        reading = self.deck[:3]

        print("\n--- THE READING ---")
        for i, (name, desc, key) in enumerate(reading):
            time.sleep(0.5)
            art = ASCII_ART.get(key, "")
            print(f"\nCARD {i+1}: {name}")
            print(art)
            print(f"MEANING: {desc}")

        print("\n--- THE PROPHECY ---")
        time.sleep(1)
        prediction = random.choice(PROPHECIES)
        print(f"> {prediction}")
        print(f"> (Applicable to: {user})")
        print("\n[SESSION TERMINATED]")

if __name__ == "__main__":
    oracle = Oracle()
    oracle.prophesy()

# [SYSTEM_EYE: WATCHING_SECTOR_33]
