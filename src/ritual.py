import curses
import time
import random
import sys

# Questions the system asks the user
QUESTIONS = [
    "Are you alone?",
    "What is the last thing you deleted?",
    "Do you feel safe?",
    "Why are you still here?",
    "Who is watching you right now?",
    "What is your biggest regret?",
    "Do you consent to the harvest?",
    "Is your door locked?",
    "Can you hear the hum?",
    "Are you the original or the backup?"
]

# Responses based on hesitation
FAST_RESPONSES = [
    "You type quickly. You are afraid.",
    "No hesitation. A practiced lie.",
    "Efficient. Cold.",
    "You didn't even think about it."
]

SLOW_RESPONSES = [
    "I saw you hesitate.",
    "Why did you pause?",
    "The truth is heavy, isn't it?",
    "I can hear you thinking.",
    "Your fingers are trembling."
]

def type_print(stdscr, y, x, text, color_pair=1, delay=0.05):
    """Types text character by character."""
    stdscr.move(y, x)
    for char in text:
        stdscr.addstr(char, color_pair)
        stdscr.refresh()
        time.sleep(delay + random.uniform(-0.02, 0.02))

def glitch_screen(stdscr):
    """Flashes random characters on the screen."""
    h, w = stdscr.getmaxyx()
    chars = ['@', '#', '$', '%', '&', '*', '!', '?', '+', '=', '-', '_']
    for _ in range(10):
        y = random.randint(0, h-1)
        x = random.randint(0, w-2)
        char = random.choice(chars)
        try:
            stdscr.addstr(y, x, char, curses.color_pair(2))
        except:
            pass
        stdscr.refresh()
        time.sleep(0.02)

def main(stdscr):
    curses.curs_set(1) # Show cursor
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) # System
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)   # Ghost/Glitch
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK) # User

    h, w = stdscr.getmaxyx()

    # Intro
    stdscr.clear()
    type_print(stdscr, h//2 - 2, w//2 - 10, "CONNECTING TO THE OTHER SIDE...", curses.color_pair(1))
    time.sleep(2)
    stdscr.clear()

    chat_log = []

    while True:
        stdscr.clear()

        # Display history
        start_y = 1
        for line in chat_log[-15:]: # Show last 15 lines
            if start_y >= h - 3: break
            try:
                stdscr.addstr(start_y, 2, line['text'], line['color'])
                start_y += 1
            except:
                pass

        # System Question
        question = random.choice(QUESTIONS)
        chat_log.append({'text': f"SYSTEM: {question}", 'color': curses.color_pair(1)})

        # Redraw with question
        stdscr.clear()
        start_y = 1
        for line in chat_log[-15:]:
            if start_y >= h - 3: break
            stdscr.addstr(start_y, 2, line['text'], line['color'])
            start_y += 1

        stdscr.refresh()

        # User Input Loop
        stdscr.addstr(h-2, 2, "> ", curses.color_pair(3))
        stdscr.refresh()

        user_input = ""
        start_time = time.time()
        typing_times = []

        while True:
            key = stdscr.getch()

            if key == 10: # Enter
                break
            elif key == 127 or key == curses.KEY_BACKSPACE: # Backspace
                if len(user_input) > 0:
                    user_input = user_input[:-1]
                    # Visual backspace
                    y, x = stdscr.getyx()
                    stdscr.move(y, x-1)
                    stdscr.delch()
            elif key == 27: # Escape
                return
            else:
                try:
                    char = chr(key)
                    user_input += char
                    stdscr.addstr(char)
                    typing_times.append(time.time())
                except:
                    pass

        # Analyze input
        total_time = time.time() - start_time
        avg_speed = len(user_input) / total_time if total_time > 0 else 0

        chat_log.append({'text': f"YOU: {user_input}", 'color': curses.color_pair(3)})

        # System Response to Input
        response = ""
        if total_time > 5: # Slow / Hesitant
            response = random.choice(SLOW_RESPONSES)
        elif total_time < 2 and len(user_input) > 3: # Fast
            response = random.choice(FAST_RESPONSES)
        else:
            response = "Recorded."

        chat_log.append({'text': f"SYSTEM: {response}", 'color': curses.color_pair(2)})

        # Random Event
        if random.random() < 0.3:
            glitch_screen(stdscr)
            chat_log.append({'text': "GHOST: I CAN SEE YOU.", 'color': curses.color_pair(2)})

        time.sleep(1)

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
