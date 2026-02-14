import random

NEON_COLORS = [
    "cyan", "magenta", "acid-green", "blood-red", "electric-blue", "void-black", "static-white", "bruised-purple"
]

RAIN_TYPES = [
    "acidic drizzle", "digital sleet", "heavy downpour of static", "mist that tastes like copper", "rain that glows in the dark", "fog thick with data rot"
]

SMELLS = [
    "ozone", "burnt plastic", "stale coffee", "old sweat", "cheap synth-meat", "decaying insulation", "rust", "wet concrete"
]

SOUNDS = [
    "distant sirens", "the hum of a thousand cooling fans", "a glitching advertisement", "footsteps in puddles", "the crackle of neon", "a drone buzzing overhead", "whispers in binary"
]

DEBT_TYPES = [
    "soul fragments", "future earnings", "memories", "biometric data", "sleep cycles", "attention span", "genetic code"
]

OBSOLETE_GODS = [
    "Dial-Up", "The Algorithm", "The Backup", "The Void", "The Signal", "The Glitch"
]

def generate_atmosphere():
    color = random.choice(NEON_COLORS)
    rain = random.choice(RAIN_TYPES)
    smell = random.choice(SMELLS)
    sound = random.choice(SOUNDS)
    debt = random.choice(DEBT_TYPES)
    god = random.choice(OBSOLETE_GODS)

    atmosphere = [
        f"The street is soaked in {color} light. It reflects off the puddles like oil.",
        f"The air is heavy with the smell of {smell} and {rain}.",
        f"In the distance, you hear {sound}.",
        f"A sign flickers above you, advertising loans for your {debt}.",
        f"An old shrine to {god} sits in the alley, covered in moss and wires.",
        "Everything is wet. Everything is for sale."
    ]

    return "\n".join(atmosphere)

if __name__ == "__main__":
    print(generate_atmosphere())
