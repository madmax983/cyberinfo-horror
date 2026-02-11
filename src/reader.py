import curses
import time
import random
import sys
import os
import textwrap

# Add the current directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import steganography
except ImportError:
    steganography = None

MANUSCRIPT_PATH = "null_pointer_gods.md"
GLITCH_CHARS = ['@', '#', '$', '%', '&', '*', '!', '?', '+', '=', '-', '_', '<', '>', '/', '\\', '|', '{', '}', '[', ']', '(', ')']

class GlitchReader:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.height, self.width = stdscr.getmaxyx()
        self.scroll_pos = 0
        self.lines = []
        self.running = True
        self.auto_scroll = False
        self.speed = 0.01

        # Colors
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) # Normal
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)   # Glitch/Danger
        curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)  # System
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK) # Highlight

        self.color_normal = curses.color_pair(1)
        self.color_glitch = curses.color_pair(2)
        self.color_system = curses.color_pair(3)

        # Load text
        self.load_file()

    def load_file(self):
        if not os.path.exists(MANUSCRIPT_PATH):
            self.lines = [("[ERROR: FILE NOT FOUND]", None), ("THE VOID IS EMPTY.", None)]
            return

        with open(MANUSCRIPT_PATH, "r", encoding="utf-8", errors="replace") as f:
            raw_lines = f.readlines()

        # Wrap text to fit screen width
        self.lines = []
        # Reserve some margin
        wrap_width = min(self.width - 4, 80)

        for line in raw_lines:
            # Check for hidden steganography before wrapping
            hidden = None
            if steganography:
                try:
                    decoded = steganography.decode(line)
                    if decoded:
                        hidden = decoded
                except:
                    pass

            wrapped = textwrap.wrap(line, width=wrap_width)
            if not wrapped:
                self.lines.append(("", hidden)) # Empty line, preserve hidden message if any
            else:
                for i, w_line in enumerate(wrapped):
                    # Attach hidden message to the last wrapped line of the original line
                    if i == len(wrapped) - 1:
                        self.lines.append((w_line, hidden))
                    else:
                        self.lines.append((w_line, None))

    def glitch_screen(self):
        """Simulates a screen glitch."""
        for _ in range(3):
            self.stdscr.clear()
            for y in range(self.height - 1):
                glitch_text = "".join(random.choice(GLITCH_CHARS) for _ in range(self.width - 1))
                try:
                    self.stdscr.addstr(y, 0, glitch_text, self.color_glitch)
                except curses.error:
                    pass
            self.stdscr.refresh()
            time.sleep(0.05)
        self.draw_screen()

    def draw_screen(self):
        self.stdscr.clear()

        # Determine range of lines to display
        display_lines = self.lines[self.scroll_pos : self.scroll_pos + self.height - 2]

        for y, (text, hidden) in enumerate(display_lines):
            try:
                # Glitch effect: random characters in line
                if random.random() < 0.005:
                    glitch_text = ""
                    for char in text:
                        if random.random() < 0.1:
                            glitch_text += random.choice(GLITCH_CHARS)
                        else:
                            glitch_text += char
                    self.stdscr.addstr(y, 2, glitch_text, self.color_glitch)
                else:
                    # Normal text
                    if text.startswith("#"):
                        self.stdscr.addstr(y, 2, text, self.color_system | curses.A_BOLD)
                    elif text.startswith(">"):
                        self.stdscr.addstr(y, 2, text, self.color_system)
                    else:
                        self.stdscr.addstr(y, 2, text, self.color_normal)

                # Check for hidden message trigger
                if hidden:
                    # Subtle hint that there is a hidden message
                    self.stdscr.addstr(y, 0, ">", self.color_glitch)

                    # Small chance to reveal it momentarily
                    if random.random() < 0.05:
                        self.stdscr.addstr(y, 2, f"[{hidden}]", self.color_glitch | curses.A_REVERSE)
                        self.stdscr.refresh()
                        time.sleep(0.1)
                        self.stdscr.addstr(y, 2, text, self.color_normal) # Restore

            except curses.error:
                pass

        # Status bar
        progress = int((self.scroll_pos / len(self.lines)) * 100)
        status = f" NULL_POINTER_GODS.MD | LINE: {self.scroll_pos}/{len(self.lines)} | SYNC: {progress}% "
        try:
            self.stdscr.addstr(self.height - 1, 0, status.center(self.width), curses.A_REVERSE | self.color_system)
        except curses.error:
            pass

        self.stdscr.refresh()

    def run(self):
        curses.curs_set(0)
        self.stdscr.timeout(100) # Non-blocking input

        while self.running:
            self.draw_screen()

            key = self.stdscr.getch()

            if key == ord('q'):
                if random.random() < 0.2:
                    self.stdscr.addstr(self.height // 2, (self.width // 2) - 10, " YOU CANNOT LEAVE ", self.color_glitch | curses.A_REVERSE)
                    self.stdscr.refresh()
                    time.sleep(1)
                else:
                    self.running = False
            elif key == curses.KEY_DOWN or key == ord('j'):
                if self.scroll_pos < len(self.lines) - self.height + 2:
                    self.scroll_pos += 1
            elif key == curses.KEY_UP or key == ord('k'):
                if self.scroll_pos > 0:
                    # Sometimes refuse to scroll up
                    if random.random() < 0.1:
                         self.stdscr.addstr(self.height - 2, 2, "THE PAST IS DELETED", self.color_glitch)
                         self.stdscr.refresh()
                         time.sleep(0.5)
                    else:
                        self.scroll_pos -= 1
            elif key == curses.KEY_NPAGE or key == ord(' '):
                 if self.scroll_pos < len(self.lines) - self.height + 2:
                    self.scroll_pos += self.height // 2
            elif key == curses.KEY_PPAGE:
                 if self.scroll_pos > 0:
                    self.scroll_pos -= self.height // 2
            elif key == ord('s'): # Scan for hidden
                 self.scan_current_page()

            # Random events
            if random.random() < 0.01:
                self.glitch_screen()

    def scan_current_page(self):
        """Reveals hidden messages on the current page."""
        display_lines = self.lines[self.scroll_pos : self.scroll_pos + self.height - 2]
        found = False
        for y, (text, hidden) in enumerate(display_lines):
            if hidden:
                try:
                    self.stdscr.addstr(y, 2, f" {hidden} ", self.color_glitch | curses.A_REVERSE)
                    found = True
                except curses.error:
                    pass

        if found:
            self.stdscr.refresh()
            time.sleep(1.5)
        else:
             try:
                self.stdscr.addstr(self.height - 2, 2, "NO ANOMALIES DETECTED", self.color_system)
                self.stdscr.refresh()
                time.sleep(0.5)
             except curses.error:
                pass


def main(stdscr):
    reader = GlitchReader(stdscr)
    reader.run()

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        # Fallback if curses fails
        print(f"TERMINAL ERROR: {e}")
        print("SWITCHING TO TEXT MODE...")
        time.sleep(1)
        with open(MANUSCRIPT_PATH, "r") as f:
            print(f.read())
