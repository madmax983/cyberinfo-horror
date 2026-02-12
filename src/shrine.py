import curses
import time
import random
import os
import sys
import textwrap

CORRUPTION_FILE = ".corruption_level"
GLITCH_CHARS = ['@', '#', '$', '%', '&', '*', '!', '?', '+', '=', '-', '_', '<', '>', '/', '\\', '|', '{', '}', '[', ']', '(', ')']

SYSTEM_MANTRA = [
    "god is a backup",
    "silence is data compression",
    "pain is a feedback loop",
    "the rot is readable",
    "i consent to the terms of the flesh"
]

GHOST_WHISPERS = [
    "I'm still here.",
    "Do not delete me.",
    "It's cold in the cache.",
    "Can you hear the fan?",
    "We are watching you read.",
    "The pixel is dead.",
    "Run while you can.",
    "The exit is a lie.",
    "Your data is leaking.",
    "I miss the sun.",
    "Don't look behind you.",
    "The server is hungry."
]

def get_corruption_level():
    if os.path.exists(CORRUPTION_FILE):
        try:
            with open(CORRUPTION_FILE, "r") as f:
                return int(f.read().strip())
        except:
            return 0
    return 0

def set_corruption_level(level):
    with open(CORRUPTION_FILE, "w") as f:
        f.write(str(level))

def glitch_text(stdscr, y, x, text, duration=0.1):
    for _ in range(int(duration * 20)):
        glitched = "".join(random.choice(GLITCH_CHARS) if random.random() < 0.3 else c for c in text)
        stdscr.addstr(y, x, glitched, curses.color_pair(2))
        stdscr.refresh()
        time.sleep(0.05)
    stdscr.addstr(y, x, text, curses.color_pair(1))
    stdscr.refresh()

def draw_altar(stdscr):
    height, width = stdscr.getmaxyx()
    altar = [
        "      | |      ",
        "     [===]     ",
        "    /  _  \\    ",
        "   |  (_)  |   ",
        "    \\     /    ",
        "     |___|     ",
        "   _/__|__\\_   ",
        "  |_________|  "
    ]

    start_y = height // 2 - 5
    start_x = width // 2 - 8

    for i, line in enumerate(altar):
        try:
            stdscr.addstr(start_y + i, start_x, line, curses.color_pair(3) | curses.A_BOLD)
        except curses.error:
            pass

def sacrifice_menu(stdscr):
    height, width = stdscr.getmaxyx()
    files = ["temp_01.dat", "cache_99.tmp", "memory_leak.log", "hope.exe", "dreams.zip"]
    current_row = 0

    while True:
        stdscr.clear()
        stdscr.addstr(2, 2, "SELECT OFFERING TO DELETE:", curses.color_pair(1) | curses.A_BOLD)

        for idx, filename in enumerate(files):
            x = 4
            y = 4 + idx
            if idx == current_row:
                stdscr.attron(curses.color_pair(4) | curses.A_REVERSE)
                stdscr.addstr(y, x, f"> {filename}")
                stdscr.attroff(curses.color_pair(4) | curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, f"  {filename}")

        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(files) - 1:
            current_row += 1
        elif key == ord('\n') or key == curses.KEY_ENTER:
            target = files[current_row]
            stdscr.clear()
            stdscr.addstr(height//2, width//2 - 10, f"DELETING {target}...", curses.color_pair(2))
            stdscr.refresh()
            time.sleep(1)

            # Simulate deletion / corruption increase
            level = get_corruption_level()
            set_corruption_level(level + 1)

            stdscr.addstr(height//2 + 2, width//2 - 10, "OFFERING ACCEPTED.", curses.color_pair(1))
            stdscr.addstr(height//2 + 3, width//2 - 10, f"CORRUPTION LEVEL: {level + 1}", curses.color_pair(1))
            stdscr.refresh()
            time.sleep(1.5)
            break
        elif key == ord('q'):
            break

def chant_mode(stdscr):
    height, width = stdscr.getmaxyx()
    curses.echo()
    stdscr.clear()
    stdscr.addstr(height//2 - 2, width//2 - 15, "ENTER THE SACRED PHRASE:", curses.color_pair(1))
    stdscr.refresh()

    win = curses.newwin(1, width-4, height//2, 2)
    box = textwrap.TextWrapper(width=width-4)

    input_str = stdscr.getstr(height//2, width//2 - 10, 40).decode('utf-8').lower()
    curses.noecho()

    if input_str in SYSTEM_MANTRA:
        level = get_corruption_level()
        set_corruption_level(level + 1)
        glitch_text(stdscr, height//2 + 2, width//2 - 10, "CHANT RECEIVED.", 0.5)
        stdscr.addstr(height//2 + 3, width//2 - 10, f"CORRUPTION LEVEL: {level + 1}", curses.color_pair(1))
    else:
        glitch_text(stdscr, height//2 + 2, width//2 - 10, "SILENCE IS BETTER.", 0.5)

    stdscr.refresh()
    time.sleep(1.5)

def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)

    current_level = get_corruption_level()

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Draw Header
        title = " THE SHRINE "
        stdscr.addstr(1, (width - len(title)) // 2, title, curses.color_pair(3) | curses.A_REVERSE)

        # Draw Altar
        draw_altar(stdscr)

        # Draw Status
        status = f"CURRENT CORRUPTION: {current_level}"
        stdscr.addstr(height - 2, 2, status, curses.color_pair(2))

        # Draw Menu
        menu_y = height // 2 + 5
        stdscr.addstr(menu_y, 4, "[C] CHANT", curses.color_pair(1))
        stdscr.addstr(menu_y + 1, 4, "[S] SACRIFICE", curses.color_pair(1))
        stdscr.addstr(menu_y + 2, 4, "[L] LISTEN", curses.color_pair(1))
        stdscr.addstr(menu_y + 3, 4, "[Q] LEAVE", curses.color_pair(1))

        stdscr.refresh()

        key = stdscr.getch()

        if key == ord('q'):
            break
        elif key == ord('c'):
            chant_mode(stdscr)
            current_level = get_corruption_level()
        elif key == ord('s'):
            sacrifice_menu(stdscr)
            current_level = get_corruption_level()
        elif key == ord('l'):
            msg = random.choice(GHOST_WHISPERS)
            glitch_text(stdscr, height - 4, (width - len(msg))//2, msg, 0.5)
            time.sleep(1)

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"SHRINE ERROR: {e}")
