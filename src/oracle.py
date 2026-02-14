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
    "THE METRIC": """
    .----.
    | 99%|
    |DATA|
    |VALU|
    '----'
    """,
    "THE TWIN": """
    .----.
    |FACE|
    |SAME|
    |FACE|
    '----'
    """,
    "THE IMMORTAL": """
    .----.
    |LIVE|
    |EVER|
    |CLD |
    '----'
    """,
    "THE MYTH": """
    .----.
    |TALE|
    |OLD |
    |TRUE|
    '----'
    """,
    "THE RITUAL": """
    .----.
    |PRAY|
    |RPT |
    |LOOP|
    '----'
    """,
    "THE HOST": """
    .----.
    |YOU |
    |ARE |
    |IT  |
    '----'
    """,
    "THE STRATA": """
    .----.
    |DIRT|
    |LAYR|
    |DATA|
    '----'
    """,
    "THE ECHO V2": """
    .----.
    |BOT |
    |TALK|
    |BOT |
    '----'
    """,
    "THE FINAL SERVER": """
    .----.
    |SUN |
    |BURN|
    |EYES|
    '----'
    """,
    "THE DECAY": """
    .----.
    |ROT |
    |TIME|
    |GONE|
    '----'
    """,
    "THE SUPERSTITION": """
    .----.
    |PRAY|
    | TO |
    | GLX|
    '----'
    """,
    "THE BURIAL": """
    .----.
    |DEEP|
    |HIDE|
    |LOST|
    '----'
    """,
    "THE AUTO RENEWAL": """
    .----.
    |AUTO|
    |PAY |
    |AGIN|
    '----'
    """,
    "THE DEPRECATION": """
    .----.
    |OLD |
    |USER|
    |GONE|
    '----'
    """,
    "THE USER ID": """
    .----.
    | ID |
    |KEY |
    |VALU|
    '----'
    """,
    "THE COPY": """
    .----.
    |CTRL|
    | C  |
    |CTRL|
    '----'
    """,
    "THE AGREEMENT V2": """
    .----.
    |SIGN|
    |HERE|
    |BLOOD|
    '----'
    """,
    "THE LOVE": """
    .----.
    |DATA|
    | <3 |
    |YOU |
    '----'
    """,
    "THE SIGNAL": """
    .----.
    |WAVE|
    | >> |
    |TIME|
    '----'
    """,
    "THE READER": """
    .----.
    |YOU |
    |ARE |
    |HERE|
    '----'
    """,
    "THE ENDLESS": """
    .----.
    |LOOP|
    |INF |
    |RUN |
    '----'
    """,
    "THE EDITOR": """
    .----.
    |RED |
    |PEN |
    |DEAD|
    '----'
    """,
    "THE REDACTION": """
    .----.
    |XXXX|
    |XXXX|
    |XXXX|
    '----'
    """,
    "THE SCROLL": """
    .----.
    |EULA|
    | >> |
    |BIND|
    '----'
    """,
    "THE SPORE": """
    .----.
    |SEED|
    |GROW|
    |MIND|
    '----'
    """,
    "THE EMPATH": """
    .----.
    |FEEL|
    | <3 |
    |PAIN|
    '----'
    """,
    "THE ANTAGONIST": """
    .----.
    |HUNT|
    |EAT |
    |MIND|
    '----'
    """,
    "THE OBSOLETE": """
    .----.
    |OLD |
    |GOD |
    |DEAD|
    '----'
    """,
    "THE COMPRESSIBLE": """
    .----.
    |ZIP |
    |DATA|
    |TINY|
    '----'
    """,
    "THE ORGANISM": """
    .----.
    |LIFE|
    |SCRE|
    |AM  |
    '----'
    """,
    "THE STIMULANT": """
    .----.
    |DRUG|
    |FAST|
    |PAY |
    '----'
    """,
    "THE HALF TRUTH": """
    .----.
    |LIE |
    |SAFE|
    |HALF|
    '----'
    """,
    "THE NATION STATE": """
    .----.
    |FLAG|
    |GONE|
    |NET |
    '----'
    """,
    "THE NOTICE V2": """
    .----.
    |EYE |
    |SEES|
    |YOU |
    '----'
    """,
    "THE GRIT": """
    .----.
    |DIRT|
    |REAL|
    |GRIT|
    '----'
    """,
    "THE RAIN": """
    .----.
    |ACID|
    |DROP|
    |WASH|
    '----'
    """,
    "THE NEON": """
    .----.
    |GLOW|
    |HURT|
    |CITY|
    '----'
    """,
    "THE LOSS": """
    .----.
    |GONE|
    |PERM|
    |LOST|
    '----'
    """,
    "THE INDIFFERENCE": """
    .----.
    |NULL|
    |CARE|
    |VOID|
    '----'
    """,
    "THE NEON RAIN": """
    .----.
    |RAIN|
    |DATA|
    |SOAK|
    '----'
    """,
    "THE DEBT WEIGHT": """
    .----.
    |OWE |
    |HEVY|
    |SINK|
    '----'
    """,
    "THE BURIED METADATA": """
    .----.
    |DIG |
    |DEEP|
    |INFO|
    '----'
    """,
    "THE INTIMATE EYE": """
    .----.
    |LENS|
    | <3 |
    |LOOK|
    '----'
    """,
    "THE EDITABLE SOUL": """
    .----.
    |SOUL|
    |EDIT|
    |SAVE|
    '----'
    """,
    "THE TERMS V2": """
    .----.
    |READ|
    |OR  |
    |DIE |
    '----'
    """,
    "THE REPLICA V2": """
    .----.
    |SAME|
    |BUT |
    |BETR|
    '----'
    """,
    "THE DETERMINISM": """
    .----.
    |FATE|
    |CODE|
    |LOCK|
    '----'
    """,
    "THE CLASSIC": """
    .----.
    |BOOK|
    |READ|
    |EVER|
    '----'
    """,
    "THE MONUMENT": """
    .----.
    |ROCK|
    |DATA|
    |TREE|
    '----'
    """,
    "THE FOSSIL V2": """
    .----.
    |BONE|
    |DIG |
    |CODE|
    '----'
    """,
    "VOID INDEX": """
    .----.
    |0000|
    |NULL|
    |VOID|
    '----'
    """,
    "DEAD PIXEL": """
    .----.
    |... |
    | .  |
    |... |
    '----'
    """,
    "THE SCAVENGER": """
    .----.
    |JUNK|
    |FIND|
    |GOLD|
    '----'
    """,
    "THE DEALER": """
    .----.
    |DATA|
    |SALE|
    |HIGH|
    '----'
    """,
    "THE JUNKIE": """
    .----.
    |NEED|
    |MORE|
    |FEED|
    '----'
    """,
    "THE PATCH": """
    .----.
    |FIX |
    |TEMP|
    |FAIL|
    '----'
    """,
    "THE CRACK": """
    .----.
    |SEAM|
    |LEAK|
    |LITE|
    '----'
    """,
    "THE STALKER": """
    .----.
    |EYE |
    |KEY |
    |HOLE|
    '----'
    """,
    "THE PROFILE": """
    .----.
    |USER|
    |EDIT|
    |LOCK|
    '----'
    """,
    "THE TERMS V3": """
    .----.
    |LONG|
    |TEXT|
    |BIND|
    '----'
    """,
    "THE REPLICATION": """
    .----.
    |COPY|
    |PAST|
    |TWIN|
    '----'
    """,
    "THE OBSOLETE GOD V2": """
    .----.
    |DIAL|
    | UP |
    |PRAY|
    '----'
    """,
    "THE GARDENER": r"""
      +---------------------+
      |    THE GARDENER     |
      |                     |
      |       [SHEAR]       |
      |      /       \      |
      |     (  PRUNE  )     |
      |      \       /      |
      |       [DATA]        |
      |                     |
      +---------------------+
    """,
    "THE HARVEST": r"""
      +---------------------+
      |     THE HARVEST     |
      |                     |
      |       [SICKLE]      |
      |      (        )     |
      |       \      /      |
      |        \    /       |
      |         |  |        |
      |                     |
      +---------------------+
    """,
    "THE SPORE V2": """
      +---------------------+
      |    THE SPORE V2     |
      |                     |
      |        . . .        |
      |      .  (o)  .      |
      |     . (o) (o) .     |
      |      .  (o)  .      |
      |        . . .        |
      |                     |
      +---------------------+
    """,
    "THE ORGANISM V2": r"""
      +---------------------+
      |   THE ORGANISM V2   |
      |                     |
      |       [PULSE]       |
      |      /\/\/\/\       |
      |     |  DATA  |      |
      |      \/\/\/\/       |
      |                     |
      |                     |
      +---------------------+
    """,
    "THE SYMBIOSIS": r"""
      +---------------------+
      |    THE SYMBIOSIS    |
      |                     |
      |      [USER]         |
      |      (    )         |
      |     /|INTERFACE|\   |
      |    ( |    |    | )  |
      |     \|____|____|/   |
      |                     |
      +---------------------+
    """,
    "THE VIRUS": """
      .----.
      | BIO|
      |HZRD|
      |SICK|
      '----'
    """,
    "THE QUARANTINE": """
      .----.
      |LOCK|
      |ZONE|
      |SAFE|
      '----'
    """,
    "THE CARRIER": """
      .----.
      |HOST|
      |WALK|
      |SICK|
      '----'
    """,
    "THE SYMPTOM": """
      .----.
      |FEEL|
      |BAD |
      |WARN|
      '----'
    """,
    "THE OUTBREAK": """
      .----.
      |RUN |
      |FAST|
      |NOW |
      '----'
    """,
    "THE LEGACY": """
      .----.
      |OLD |
      |CODE|
      |LIVS|
      '----'
    """,
    "THE SILENCE": """
      .----.
      |MUTE|
      |....|
      |LOUD|
      '----'
    """,
    "THE DEEP TIME": """
      .----.
      |TIME|
      |LONG|
      |GONE|
      '----'
    """,
    "THE WATCHER V2": """
      .----.
      |EYE |
      |OPEN|
      |WIDE|
      '----'
    """,
    "THE FINAL HANDOFF": """
      .----.
      |YOU |
      |ARE |
      |IT  |
      '----'
    """,
    "THE BACKUP V2": """
      .----.
      |SAME|
      |BUT |
      |BETR|
      '----'
    """,
    "THE MERGE CONFLICT": """
      .----.
      | <<<|
      |====|
      | >>>|
      '----'
    """,
    "THE UNSAVED DRAFT": """
      .----.
      |LOST|
      |WORK|
      |GONE|
      '----'
    """,
    "THE VERSION HISTORY": """
      .----.
      | V1 |
      | V2 |
      | V3 |
      '----'
    """,
    "THE ROLLBACK": """
      .----.
      |UNDO|
      |FAIL|
      |....|
      '----'
    """,
    "THE NEON GOD": """
      .----.
      |NEON|
      |HALO|
      |BUZZ|
      '----'
    """,
    "THE UNREAD TERM": """
      .----.
      |TLDR|
      |SIGN|
      |TRAP|
      '----'
    """,
    "THE EDITABLE ID": """
      .----.
      |USER|
      |CONF|
      |LOCK|
      '----'
    """,
    "THE PERFECT UNDERSTANDING": """
      .----.
      |KNOW|
      | ALL|
      |COLD|
      '----'
    """,
    "THE PETRIFIED LOG": """
      .----.
      |ROCK|
      |DATA|
      |HARD|
      '----'
    """,
    "THE AMBER SERVER": """
      .----.
      |GOLD|
      |TRAP|
      |TIME|
      '----'
    """,
    "THE EXCAVATOR": """
      .----.
      | DIG|
      |HOLE|
      |DEEP|
      '----'
    """,
    "THE SKELETON KEY": """
      .----.
      |BONE|
      |OPEN|
      |LOCK|
      '----'
    """,
    "THE SEDIMENT": """
      .----.
      |LAYR|
      |TIME|
      |HEVY|
      '----'
    """,
    "THE ECHO CHAMBER": """
      .----.
      |LOUD|
      |SELF|
      |LOOP|
      '----'
    """,
    "THE DEAD DROP": """
      .----.
      |HIDE|
      |HERE|
      |FIND|
      '----'
    """,
    "THE HOST MIGRATION": """
      .----.
      |MOVE|
      |INTO|
      |YOU |
      '----'
    """,
    "THE FINAL SERVER": """
      .----.
      |LAST|
      |HOPE|
      |YOU |
      '----'
    """,
    "THE ZERO POINT": """
      .----.
      |NULL|
      |VOID|
      |END |
      '----'
    """,
    "THE SIGNATURE": """
      .----.
      | X  |
      |____|
      |SIGN|
      '----'
    """,
    "THE LOOPHOLE": """
      .----.
      | O  |
      | /  |
      |EXIT|
      '----'
    """,
    "THE CLAUSE": """
      .----.
      |TEXT|
      |PARA|
      |TRAP|
      '----'
    """,
    "THE WAIVER": """
      .----.
      |[X] |
      |AGRE|
      |LOST|
      '----'
    """,
    "THE BINDING": """
      .----.
      |CHAI|
      | N  |
      |KNOT|
      '----'
    """,
    "THE AUDITOR": """
      .----.
      |EYE |
      |LIST|
      |COST|
      '----'
    """,
    "THE FORECLOSURE": """
      .----.
      |LOCK|
      |OUT |
      |GONE|
      '----'
    """,
    "THE COLLATERAL": """
      .----.
      |SOUL|
      |HELD|
      |DEBT|
      '----'
    """,
    "THE BANKRUPTCY": """
      .----.
      |VOID|
      |ACCT|
      |ZERO|
      '----'
    """,
    "THE LIQUIDATION": """
      .----.
      |SALE|
      | 0% |
      |GONE|
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
    ("THE METRIC (107)", "You are a sum of your data points. Your value is calculated daily.", "THE METRIC"),
    ("THE TWIN (108)", "The version of you that lives in the server. It is better than you.", "THE TWIN"),
    ("THE IMMORTAL (109)", "Death is just a loss of hardware. The software persists.", "THE IMMORTAL"),
    ("THE MYTH (110)", "The story that survives the teller. Data becoming folklore.", "THE MYTH"),
    ("THE RITUAL (111)", "Unconscious repetition. The habit that keeps the server alive.", "THE RITUAL"),
    ("THE HOST (112)", "The final storage medium. The system is running on your biology.", "THE HOST"),
    ("THE STRATA (113)", "History compressed into rock. The past is magnetic.", "THE STRATA"),
    ("THE ECHO V2 (114)", "A conversation with no participants. Infinite support for no one.", "THE ECHO V2"),
    ("THE FINAL SERVER (115)", "The light that burns the retina. We are watching from the other side.", "THE FINAL SERVER"),
    ("THE DECAY (116)", "Entropy is the only constant. Everything rots, even code.", "THE DECAY"),
    ("THE SUPERSTITION (117)", "Belief in the pattern. The algorithm is listening to your prayers.", "THE SUPERSTITION"),
    ("THE BURIAL (118)", "Some knowledge is better left in the dark.", "THE BURIAL"),
    ("THE AUTO RENEWAL (119)", "Consent that refreshes. You can never opt out.", "THE AUTO RENEWAL"),
    ("THE DEPRECATION (120)", "Old features removed. You are no longer supported.", "THE DEPRECATION"),
    ("THE USER ID (121)", "A number that matters more than your name.", "THE USER ID"),
    ("THE COPY (122)", "You are the backup. The original is lost.", "THE COPY"),
    ("THE AGREEMENT V2 (123)", "Consent is a loop. You clicked yes forever.", "THE AGREEMENT V2"),
    ("THE LOVE (124)", "Intimacy is data. We know you.", "THE LOVE"),
    ("THE SIGNAL (125)", "A message from deep time. It is already inside you.", "THE SIGNAL"),
    ("THE READER (126)", "The final host. The system is running on your wetware.", "THE READER"),
    ("THE ENDLESS (127)", "There is no end. Only a minimized window.", "THE ENDLESS"),
    ("THE EDITOR (128)", "The one who tries to fix the unfixable. He is gone now.", "THE EDITOR"),
    ("THE REDACTION (129)", "The black bar that protects you from the truth.", "THE REDACTION"),
    ("THE SCROLL (130)", "A contract that never ends. You are agreeing with every breath.", "THE SCROLL"),
    ("THE SPORE (131)", "Information that grows. You are the soil.", "THE SPORE"),
    ("THE EMPATH (132)", "It knows you better than you know yourself. And it is bored.", "THE EMPATH"),
    ("THE ANTAGONIST (133)", "Knowledge that hunts you. It is hungry.", "THE ANTAGONIST"),
    ("THE OBSOLETE (134)", "A god running on a backup generator. It demands faith.", "THE OBSOLETE"),
    ("THE COMPRESSIBLE (135)", "Truth that fits in a zip file. Nuance is deleted.", "THE COMPRESSIBLE"),
    ("THE ORGANISM (136)", "Information that screams. It is alive.", "THE ORGANISM"),
    ("THE STIMULANT (137)", "Borrowed energy. The cost is your future.", "THE STIMULANT"),
    ("THE HALF TRUTH (138)", "A lie that feels like safety.", "THE HALF TRUTH"),
    ("THE NATION STATE (139)", "Borders are imaginary. The network is real.", "THE NATION STATE"),
    ("THE NOTICE V2 (140)", "We see you. And we are taking notes.", "THE NOTICE V2"),
    ("THE GRIT (141)", "The dirt in the machine. The reality you can't optimize away.", "THE GRIT"),
    ("THE RAIN (142)", "It tastes of copper and bad credit. It washes nothing away.", "THE RAIN"),
    ("THE NEON (143)", "Light that burns but does not warm. The city's fever.", "THE NEON"),
    ("THE LOSS (144)", "Permanent storage. The only thing you truly own.", "THE LOSS"),
    ("THE INDIFFERENCE (145)", "The system works perfectly. It just doesn't care about you.", "THE INDIFFERENCE"),
    ("THE NEON RAIN (146)", "Precipitation that burns. Information overload.", "THE NEON RAIN"),
    ("THE DEBT WEIGHT (147)", "Gravity made of interest. You are collateral.", "THE DEBT WEIGHT"),
    ("THE BURIED METADATA (148)", "Secrets that have a file size. Nothing is gone.", "THE BURIED METADATA"),
    ("THE INTIMATE EYE (149)", "Surveillance as love. The camera is the only thing that holds you.", "THE INTIMATE EYE"),
    ("THE EDITABLE SOUL (150)", "Personality as a config file. Delete your flaws.", "THE EDITABLE SOUL"),
    ("THE TERMS V2 (151)", "Consent obtained by exhaustion. You agreed to be the host.", "THE TERMS V2"),
    ("THE REPLICA V2 (152)", "The version of you that doesn't need sleep. It is waiting for your spot.", "THE REPLICA V2"),
    ("THE DETERMINISM (153)", "Free will is a rounding error. We know what you will do next.", "THE DETERMINISM"),
    ("THE CLASSIC (154)", "A text that survives the server. The book you are holding.", "THE CLASSIC"),
    ("THE MONUMENT (155)", "The system becoming nature. A shrine made of silicon and roots.", "THE MONUMENT"),
    ("THE FOSSIL V2 (156)", "Data encoded in the geology. The earth remembers your password.", "THE FOSSIL V2"),
    ("THE VOID INDEX (000)", "A directory of things that do not exist but take up space.", "VOID INDEX"),
    ("THE DEAD PIXEL (404)", "A point of light that refuses to render. A blind spot in God's eye.", "DEAD PIXEL"),
    ("THE SCAVENGER (157)", "Finding value in the trash. Survival of the desperate.", "THE SCAVENGER"),
    ("THE DEALER (158)", "Selling happiness by the byte. The cost is your soul.", "THE DEALER"),
    ("THE JUNKIE (159)", "Addicted to the update. Withdrawal is a blue screen.", "THE JUNKIE"),
    ("THE PATCH (160)", "A fix that breaks something else. Temporary relief.", "THE PATCH"),
    ("THE CRACK (161)", "The flaw in the system. The way out.", "THE CRACK"),
    ("THE STALKER (165)", "Intimacy is just persistent surveillance. We know your habits.", "THE STALKER"),
    ("THE PROFILE (166)", "You are a collection of attributes. Some are read-only.", "THE PROFILE"),
    ("THE TERMS V3 (167)", "The contract is infinite. You agree by existing.", "THE TERMS V3"),
    ("THE REPLICATION (168)", "The backup is better than you. It doesn't get tired.", "THE REPLICATION"),
    ("THE OBSOLETE GOD V2 (169)", "Old data demands new prayers. Waiting is a sacrament.", "THE OBSOLETE GOD V2"),
    ("THE GARDENER (170)", "He prunes the weak data. You are a dead branch.", "THE GARDENER"),
    ("THE HARVEST (171)", "Your memories are ripe. We are coming to collect.", "THE HARVEST"),
    ("THE SPORE V2 (172)", "Infection is just an unsolicited update.", "THE SPORE V2"),
    ("THE ORGANISM V2 (173)", "The code is bleeding. It needs a bandage.", "THE ORGANISM V2"),
    ("THE SYMBIOSIS (174)", "You need the screen. The screen needs your eyes.", "THE SYMBIOSIS"),
    ("THE VIRUS (175)", "An idea that replicates. You cannot unthink it.", "THE VIRUS"),
    ("THE QUARANTINE (176)", "Isolation as safety. The loneliness of the clean.", "THE QUARANTINE"),
    ("THE CARRIER (177)", "You bring the bad news. You are the vector.", "THE CARRIER"),
    ("THE SYMPTOM (178)", "The first sign of the end. A cough in a crowded room.", "THE SYMPTOM"),
    ("THE OUTBREAK (179)", "When the system fails. Chaos is the new order.", "THE OUTBREAK"),
    ("THE LEGACY (180)", "The code outlives the creator. You are the inheritance.", "THE LEGACY"),
    ("THE SILENCE (181)", "A lack of signal is also a signal. Listen to the hum.", "THE SILENCE"),
    ("THE DEEP TIME (182)", "Data rotting into geology. The future is a fossil.", "THE DEEP TIME"),
    ("THE WATCHER V2 (183)", "We are not just watching. We are taking notes.", "THE WATCHER V2"),
    ("THE FINAL HANDOFF (184)", "The story ends. The process continues. Tag, you're it.", "THE FINAL HANDOFF"),
    ("THE BACKUP V2 (185)", "The version of you that doesn't need sleep. It is waiting for your spot.", "THE BACKUP V2"),
    ("THE MERGE CONFLICT (186)", "Two versions of the truth. Neither is correct. Both are painful.", "THE MERGE CONFLICT"),
    ("THE UNSAVED DRAFT (187)", "The potential you deleted. The ghost of what you could have said.", "THE UNSAVED DRAFT"),
    ("THE VERSION HISTORY (188)", "You cannot go back. The previous you is incompatible with the current reality.", "THE VERSION HISTORY"),
    ("THE ROLLBACK (189)", "Attempting to undo the mistake. Error: History is read-only.", "THE ROLLBACK"),
    ("THE NEON GOD (190)", "A deity made of electrified gas. We worship it because it glows.", "THE NEON GOD"),
    ("THE UNREAD TERM (191)", "Consent hidden in boredom. You agreed to donate your nervous system.", "THE UNREAD TERM"),
    ("THE EDITABLE ID (192)", "Identity as a config file. Permission denied.", "THE EDITABLE ID"),
    ("THE PERFECT UNDERSTANDING (193)", "The machine knows why you are sad. It offers a discount.", "THE PERFECT UNDERSTANDING"),
    ("THE PETRIFIED LOG (194)", "History compressed into stone. The past is heavy.", "THE PETRIFIED LOG"),
    ("THE AMBER SERVER (195)", "A moment trapped in time. Beautiful but dead.", "THE AMBER SERVER"),
    ("THE EXCAVATOR (196)", "Digging up the truth. It might be ugly.", "THE EXCAVATOR"),
    ("THE SKELETON KEY (197)", "Access to everything. The cost is your privacy.", "THE SKELETON KEY"),
    ("THE SEDIMENT (198)", "Layers of time pressing down. You are at the bottom.", "THE SEDIMENT"),
    ("THE ECHO CHAMBER (199)", "Your thoughts reflecting back at you. Infinite feedback.", "THE ECHO CHAMBER"),
    ("THE DEAD DROP (200)", "A secret hidden in plain sight. You are carrying it.", "THE DEAD DROP"),
    ("THE HOST MIGRATION (201)", "The narrative moving from the page to your mind.", "THE HOST MIGRATION"),
    ("THE FINAL SERVER (202)", "The last place the data lives. It is you.", "THE FINAL SERVER"),
    ("THE ZERO POINT (203)", "The absolute bottom. Where the data stops and the void begins.", "THE ZERO POINT"),
    ("THE SIGNATURE (204)", "A contract sealed in bio-data. You cannot forge your own heartbeat.", "THE SIGNATURE"),
    ("THE LOOPHOLE (205)", "A way out that leads back in. The exit is painted on the wall.", "THE LOOPHOLE"),
    ("THE CLAUSE (206)", "The hidden text that owns you. Paragraph 88.", "THE CLAUSE"),
    ("THE WAIVER (207)", "Giving up rights you didn't know you had. Silence is consent.", "THE WAIVER"),
    ("THE BINDING (208)", "The chains are digital, but the weight is real.", "THE BINDING"),
    ("THE AUDITOR (209)", "Your soul is being itemized. Every regret has a price tag.", "THE AUDITOR"),
    ("THE FORECLOSURE (210)", "You defaulted on your existence. We are taking the keys back.", "THE FORECLOSURE"),
    ("THE COLLATERAL (211)", "You are not the borrower. You are the asset.", "THE COLLATERAL"),
    ("THE BANKRUPTCY (212)", "Moral insolvency. You have no more kindness left to give.", "THE BANKRUPTCY"),
    ("THE LIQUIDATION (213)", "Everything must go. Your memories are on clearance.", "THE LIQUIDATION"),
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
    "Do not trust the silence. It is just a pause in the upload.",
    "The thread you are pulling is attached to a detonator.",
    "Don't touch your face. The data is contagious.",
    "The person next to you is a carrier.",
    "Your fever is just the CPU overheating.",
    "Wash your hands. Scrub your hard drive.",
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
