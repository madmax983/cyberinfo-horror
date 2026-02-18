import curses
import time
import random
import os
import sys

# THE MIRROR
# IT BLINKS FIRST

MIRROR_LOG = ".mirror_log"

SUBLIMINAL_MESSAGES = [
    "I SEE YOU",
    "NOT REAL",
    "WAKE UP",
    "THEY KNOW",
    "LOOK BEHIND",
    "DONT BLINK",
    "FEED ME",
    "IM HERE",
    "NO EXIT",
    "RUN NOW"
]

def log_reflection(text):
    try:
        with open(MIRROR_LOG, "a") as f:
            f.write(f"{time.time()}: {text}\n")
    except:
        pass

def distort_text(text):
    # Pronoun swapping
    replacements = {
        "I": "WE",
        "ME": "US",
        "MY": "OUR",
        "YOU": "IT",
        "YOUR": "ITS",
        "AM": "ARE"
    }

    words = text.upper().split()
    new_words = []
    for word in words:
        if word in replacements:
            new_words.append(replacements[word])
        else:
            # Glitch chance
            if random.random() < 0.1:
                glitch_chars = ['@', '#', '$', '%', '&', '*', '!', '?']
                new_word = ""
                for char in word:
                    if random.random() < 0.3:
                        new_word += random.choice(glitch_chars)
                    else:
                        new_word += char
                new_words.append(new_word)
            else:
                new_words.append(word)

    return " ".join(new_words)

def main(stdscr):
    curses.curs_set(1) # Visible cursor
    stdscr.nodelay(True) # Non-blocking input
    stdscr.timeout(50) # Refresh every 50ms

    # Colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK) # Subliminal
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK) # Input
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK) # Reflection

    input_buffer = ""
    reflection_buffer = ""

    last_flash_time = time.time()
    flash_active = False
    flash_text = ""
    flash_duration = 0.05

    while True:
        rows, cols = stdscr.getmaxyx()
        stdscr.clear()

        # Draw border
        stdscr.border()

        # Title
        title = "[ DIGITAL MIRROR ]"
        stdscr.addstr(0, (cols - len(title)) // 2, title, curses.color_pair(1) | curses.A_BOLD)

        # Draw Input Area (Bottom)
        input_prompt = "> "
        stdscr.addstr(rows - 3, 2, input_prompt, curses.color_pair(3) | curses.A_BOLD)
        stdscr.addstr(rows - 3, 4, input_buffer, curses.color_pair(3))

        # Draw Reflection Area (Top/Middle)
        # The reflection appears as if on the other side of the glass
        reflection_prompt = "REFLECTION:"
        stdscr.addstr(2, 2, reflection_prompt, curses.color_pair(4) | curses.A_DIM)

        # Render reflection
        # We can simulate lag by delaying the update, or just distort immediately
        # Let's distort immediately but add visual noise

        y = 4
        # Wrap reflection text
        max_width = cols - 4
        wrapper = []
        current_line = ""
        for word in reflection_buffer.split():
            if len(current_line) + len(word) + 1 > max_width:
                wrapper.append(current_line)
                current_line = word
            else:
                if current_line:
                    current_line += " " + word
                else:
                    current_line = word
        if current_line:
            wrapper.append(current_line)

        # Display only last few lines that fit
        display_lines = wrapper[-(rows - 10):]
        for line in display_lines:
            stdscr.addstr(y, 4, line, curses.color_pair(4))
            y += 1

        # Subliminal Flash
        current_time = time.time()
        if not flash_active:
            # Chance to start flash
            if random.random() < 0.01 and (current_time - last_flash_time > 2.0):
                flash_active = True
                flash_text = random.choice(SUBLIMINAL_MESSAGES)
                last_flash_time = current_time
        else:
            # Draw flash
            center_y = rows // 2
            center_x = (cols - len(flash_text)) // 2
            stdscr.addstr(center_y, center_x, flash_text, curses.color_pair(2) | curses.A_BOLD | curses.A_REVERSE)

            if current_time - last_flash_time > flash_duration:
                flash_active = False

        stdscr.refresh()

        # Input handling
        try:
            key = stdscr.getch()
            if key != -1:
                if key == 10: # Enter
                    if input_buffer.lower() in ["exit", "quit"]:
                        break

                    log_reflection(input_buffer)
                    distorted = distort_text(input_buffer)
                    reflection_buffer += " " + distorted
                    input_buffer = ""

                    # Lag simulation: freeze screen briefly
                    time.sleep(0.2)

                elif key == 127 or key == 8 or key == curses.KEY_BACKSPACE:
                    input_buffer = input_buffer[:-1]
                elif key >= 32 and key <= 126:
                    input_buffer += chr(key)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except Exception as e:
        print(f"THE MIRROR BROKE: {e}")
