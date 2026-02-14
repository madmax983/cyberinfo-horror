import sys
import time
import random
import os

GLITCH_CHARS = ['@', '#', '$', '%', '&', '*', '!', '?', '+', '=', '-', '_', '<', '>', '/', '\\', '|', '{', '}', '[', ']', '(', ')']

def type_print(text, speed=0.03, glitch_chance=0.01):
    test_mode = os.environ.get("TEST_MODE") == "1"
    if test_mode:
        speed = 0
        glitch_chance = 0

    for char in text:
        if random.random() < glitch_chance:
            sys.stdout.write(random.choice(GLITCH_CHARS))
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        if not test_mode:
            time.sleep(speed + random.uniform(-0.01, 0.01))
    print("")
