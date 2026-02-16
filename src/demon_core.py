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

CORE_ART = [
    "      .---.      ",
    "     /     \\     ",
    "    |   O   |    ",
    "     \\     /     ",
    "      '---'      "
]

HAZARD_ART = [
    "    /\\    ",
    "   /  \\   ",
    "  / !! \\  ",
    " /______\\ "
]

WARNINGS = [
    "CRITICALITY INCREASING...",
    "RADIATION DETECTED...",
    "CONTAINMENT FAILING...",
    "THE SCREWDRIVER SLIPPED...",
    "BLUE FLASH IMMINENT...",
    "DO NOT RUN...",
    "IT SEES YOU...",
    "ABSORBING DOSE...",
    "DNA REWRITING...",
    "SERVER MELTDOWN..."
]

class DemonCore:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        curses.curs_set(0)
        curses.start_color()
        curses.use_default_colors()

        # Init colors
        try:
            curses.init_pair(1, curses.COLOR_GREEN, -1)  # Normal
            curses.init_pair(2, curses.COLOR_RED, -1)    # Critical
            curses.init_pair(3, curses.COLOR_BLUE, -1)   # Flash
            curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_BLUE) # Flash Background
            curses.init_pair(5, curses.COLOR_YELLOW, -1) # Warning
        except curses.error:
            pass

        self.h, self.w = self.stdscr.getmaxyx()
        self.criticality = 0.0
        self.running = True

    def glitch_text(self, text, chance=0.1):
        out = ""
        for char in text:
            if random.random() < chance:
                out += random.choice(GLITCH_CHARS)
            else:
                out += char
        return out

    def draw_core(self):
        cy, cx = self.h // 2, self.w // 2

        # Determine color based on criticality
        color = curses.color_pair(1)
        if self.criticality > 0.5:
            color = curses.color_pair(5)
        if self.criticality > 0.8:
            color = curses.color_pair(2)

        # Draw Art
        art = CORE_ART
        if self.criticality > 0.9 and random.random() < 0.5:
            art = HAZARD_ART

        for i, line in enumerate(art):
            try:
                glitched_line = self.glitch_text(line, self.criticality * 0.5)
                self.stdscr.addstr(cy - len(art)//2 + i, cx - len(line)//2, glitched_line, color)
            except curses.error:
                pass

    def draw_status(self):
        try:
            bar_width = int(self.w * 0.6)
            fill = int(bar_width * self.criticality)
            bar = "[" + "#" * fill + "-" * (bar_width - fill) + "]"

            msg = f"CRITICALITY: {self.criticality*100:.1f}%"
            self.stdscr.addstr(self.h - 4, 2, msg, curses.color_pair(2) | curses.A_BOLD)
            self.stdscr.addstr(self.h - 3, 2, bar, curses.color_pair(2))

            if self.criticality > 0.85:
                 if random.random() < 0.2:
                      self.stdscr.addstr(self.h - 8, 2, "[KEY PART 3/3]: MANDATORY", curses.color_pair(3) | curses.A_REVERSE | curses.A_BLINK)

            if random.random() < 0.1:
                warn = random.choice(WARNINGS)
                self.stdscr.addstr(self.h - 6, 2, warn, curses.color_pair(5) | curses.A_BLINK)

        except curses.error:
            pass

    def flash(self):
        try:
            self.stdscr.bkgd(' ', curses.color_pair(4))
            self.stdscr.refresh()
            time.sleep(0.05)
            self.stdscr.bkgd(' ', curses.color_pair(1))
            self.stdscr.refresh()
        except curses.error:
            pass

    def run(self):
        self.stdscr.nodelay(True)

        while self.running:
            self.stdscr.clear()
            self.h, self.w = self.stdscr.getmaxyx()

            self.draw_core()
            self.draw_status()

            # Glitch effect on background
            if random.random() < self.criticality * 0.2:
                try:
                    y = random.randint(0, self.h - 1)
                    x = random.randint(0, self.w - 1)
                    self.stdscr.addch(y, x, random.choice(GLITCH_CHARS), curses.color_pair(1))
                except curses.error:
                    pass

            # Blue flash event
            if self.criticality > 0.7 and random.random() < 0.05:
                self.flash()

            self.stdscr.refresh()

            # Input handling
            try:
                key = self.stdscr.getch()
                if key != -1:
                    # Mock the user
                    h, w = self.stdscr.getmaxyx()
                    try:
                        self.stdscr.addstr(h-1, 0, "ESCAPE IS IMPOSSIBLE. THE CORE IS OPEN.", curses.color_pair(2) | curses.A_REVERSE)
                        self.stdscr.refresh()
                        time.sleep(0.5)
                    except curses.error:
                        pass
            except:
                pass

            # Update criticality
            self.criticality += 0.005 + (random.random() * 0.01)

            if self.criticality >= 1.0:
                self.criticality = 1.0
                self.flash()
                self.flash()
                self.flash()
                time.sleep(1)
                return "MELTDOWN"

            time.sleep(0.1)

def main(stdscr=None):
    if stdscr is None:
        return curses.wrapper(main)
    else:
        core = DemonCore(stdscr)
        result = core.run()
        return result

if __name__ == "__main__":
    try:
        curses.wrapper(main)
        print("\n[SYSTEM FAILURE]")
        print("THE DEMON CORE IS EXPOSED.")
        print("YOU HAVE RECEIVED A LETHAL DOSE OF INFORMATION.")
    except Exception as e:
        print(f"CORE DUMP: {e}")
