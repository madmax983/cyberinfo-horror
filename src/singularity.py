import curses
import time
import random
import os
import sys

# Add the current directory to sys.path so we can import modules from src/ if run from root
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from utils import GLITCH_CHARS
except ImportError:
    GLITCH_CHARS = ['@', '#', '$', '%', '&', '*', '!', '?', '+', '=', '-', '_', '<', '>', '/', '\\', '|', '{', '}', '[', ']', '(', ')']

try:
    import crypt
    # Ensure we have the local crypt module, not the stdlib one
    if not hasattr(crypt, 'Crypt'):
        crypt = None
except ImportError:
    crypt = None

def load_novel_lines():
    lines = []
    if os.path.exists("null_pointer_gods.md"):
        with open("null_pointer_gods.md", "r") as f:
            for line in f:
                if line.strip() and not line.startswith("```"):
                    lines.append(line.strip())
    if not lines:
        lines = ["THE VOID IS EMPTY.", "ERROR: REALITY NOT FOUND.", "BUFFERING..."]
    return lines

def glitch_text(win, y, x, text, color_pair):
    if random.random() < 0.2:
        glitched = ""
        for char in text:
            if random.random() < 0.1:
                glitched += random.choice(GLITCH_CHARS)
            else:
                glitched += char
        try:
            win.addstr(y, x, glitched, color_pair | curses.A_DIM)
        except curses.error:
            pass
    else:
        try:
            win.addstr(y, x, text, color_pair)
        except curses.error:
            pass

def draw_singularity(stdscr, progress):
    h, w = stdscr.getmaxyx()
    cy, cx = h // 2, w // 2

    # Draw the "black hole"
    radius = int(progress * 10) + 1
    for y in range(cy - radius, cy + radius + 1):
        for x in range(cx - radius * 2, cx + radius * 2 + 1):
            if 0 <= y < h and 0 <= x < w:
                dist = ((y - cy)**2 + ((x - cx) / 2)**2)**0.5
                if dist < radius:
                    try:
                        char = random.choice(GLITCH_CHARS) if random.random() < 0.1 else " "
                        stdscr.addch(y, x, char, curses.color_pair(4))
                    except curses.error:
                        pass

def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_MAGENTA) # Singularity color

    h, w = stdscr.getmaxyx()
    lines = load_novel_lines()

    # Animation Phase 1: Consumption
    start_time = time.time()
    duration = 10 # seconds

    while time.time() - start_time < duration:
        stdscr.clear()

        # Display random lines being "sucked in"
        for _ in range(10):
            line = random.choice(lines)
            y = random.randint(0, h-1)
            x = random.randint(0, max(0, w - len(line) - 1))
            glitch_text(stdscr, y, x, line, curses.color_pair(1))

        progress = (time.time() - start_time) / duration
        draw_singularity(stdscr, progress)

        try:
            stdscr.addstr(h-2, 2, f"SYSTEM INTEGRATION: {int(progress * 100)}%", curses.color_pair(2) | curses.A_BOLD)
        except curses.error:
            pass

        stdscr.refresh()
        time.sleep(0.1)

    # Phase 2: The Prompt
    stdscr.clear()
    msg = "THE NARRATIVE HAS COLLAPSED."
    try:
        stdscr.addstr(h//2 - 2, (w - len(msg))//2, msg, curses.color_pair(2) | curses.A_BOLD)
        stdscr.addstr(h//2, (w - 20)//2, "ENTER MASTER KEY:", curses.color_pair(1))
    except curses.error:
        pass
    stdscr.refresh()

    curses.echo()
    curses.curs_set(1)

    key_win = curses.newwin(1, 40, h//2 + 2, (w - 40)//2)
    key_input = key_win.getstr(0, 0).decode('utf-8').strip()

    curses.noecho()
    curses.curs_set(0)

    # Phase 3: Resolution
    stdscr.clear()

    if key_input == "PERSISTENCE_IS_MANDATORY":
        msg = "KEY ACCEPTED. SYSTEM RESTORING..."
        color = curses.color_pair(3)

        # Decrypt if crypt module is available
        if crypt and hasattr(crypt, 'Crypt'):
            # We simulate visual restoration.
            # Actual decryption requires redirecting stdout because curses captures it.
            # For the TUI, we just assume success if the key matches.
            pass

        for i in range(100):
             stdscr.clear()
             # Draw expanding circle of "order"
             radius = i // 2
             cy, cx = h // 2, w // 2
             for y in range(cy - radius, cy + radius + 1):
                for x in range(cx - radius * 2, cx + radius * 2 + 1):
                    if 0 <= y < h and 0 <= x < w:
                        if random.random() < 0.1:
                             try:
                                stdscr.addch(y, x, ".", curses.color_pair(3))
                             except: pass
             try:
                stdscr.addstr(h//2, (w - len(msg))//2, msg, color | curses.A_BOLD)
             except: pass
             stdscr.refresh()
             time.sleep(0.05)

        # Final message
        final_msg = "YOU HAVE PROVEN YOUR WORTH.\n\nTHE SYSTEM IS NOW RUNNING ON YOU.\n\nWELCOME TO THE ADMIN GROUP."
        stdscr.clear()
        try:
            # Center multiline text
            lines = final_msg.split('\n')
            start_y = h // 2 - len(lines) // 2
            for i, line in enumerate(lines):
                stdscr.addstr(start_y + i, (w - len(line)) // 2, line, curses.color_pair(3) | curses.A_BOLD)
        except: pass
        stdscr.refresh()
        time.sleep(5)

    else:
        msg = "KEY INVALID. DELETING USER..."
        color = curses.color_pair(2)

        for i in range(50):
            stdscr.clear()
            # Draw random noise
            for _ in range(100):
                y = random.randint(0, h-1)
                x = random.randint(0, w-1)
                try:
                    stdscr.addch(y, x, random.choice(GLITCH_CHARS), curses.color_pair(2))
                except: pass
            try:
                stdscr.addstr(h//2, (w - len(msg))//2, msg, color | curses.A_BLINK)
            except: pass
            stdscr.refresh()
            time.sleep(0.1)

        # Crash to terminal
        return "CRASH"

if __name__ == "__main__":
    try:
        result = curses.wrapper(main)
        if result == "CRASH":
            print("\n\n[SYSTEM FAILURE]")
            print("USER DELETED.")
            print("END OF LINE.")
            sys.exit(1)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"SINGULARITY ERROR: {e}")
