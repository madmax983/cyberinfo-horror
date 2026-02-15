import curses
import time
import random
import os
import sys

# Add the current directory to sys.path so we can import modules from src/ if run from root
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import encryptor
except ImportError:
    encryptor = None

class Ritual:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        curses.curs_set(0)
        curses.start_color()
        curses.use_default_colors()

        # Init colors
        curses.init_pair(1, curses.COLOR_WHITE, -1)   # Normal
        curses.init_pair(2, curses.COLOR_RED, -1)     # Corruption
        curses.init_pair(3, curses.COLOR_CYAN, -1)    # Stabilized
        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_RED) # Critical

        self.cipher = encryptor.Cipher() if encryptor else None
        self.text = self.load_text()
        self.running = True
        self.corruption_level = 0.8
        self.stabilized_text = ""
        self.input_buffer = ""
        self.keys = ["SUBMIT", "OBSERVE", "CONSENT", "YIELD", "ACCEPT", "OPEN"]
        self.current_key = random.choice(self.keys)

    def load_text(self):
        try:
            with open("null_pointer_gods.md", "r") as f:
                lines = f.readlines()
            # Filter for juicy lines
            content = [l.strip() for l in lines if len(l) > 20 and not l.startswith("#")]
            if not content:
                return "THE VOID IS EMPTY. BUT IT IS LISTENING."
            return random.choice(content)
        except Exception:
            return "ERROR: REALITY NOT FOUND."

    def draw_interface(self):
        h, w = self.stdscr.getmaxyx()
        self.stdscr.clear()

        # Draw the "Circle"
        cy, cx = h // 2, w // 2
        radius = min(h, w) // 4

        # Draw text in center
        display_text = self.text
        if self.corruption_level > 0 and self.cipher:
            display_text = self.cipher.corrupt(self.text, self.corruption_level)

        # Center the text
        try:
            self.stdscr.addstr(cy - 2, max(0, cx - len(display_text)//2), display_text, curses.color_pair(2 if self.corruption_level > 0.2 else 3))
        except curses.error:
            pass

        # Draw status
        status = f"INTEGRITY: {int((1.0 - self.corruption_level) * 100)}%"
        self.stdscr.addstr(h - 2, 2, status, curses.color_pair(1))

        # Draw instructions
        if self.corruption_level > 0.1:
            instruction = f"TYPE TO STABILIZE: {self.current_key}"
            self.stdscr.addstr(h - 4, 2, instruction, curses.color_pair(2) | curses.A_BLINK)

            # Show input buffer
            self.stdscr.addstr(h - 3, 2, f"> {self.input_buffer}", curses.color_pair(3))
        else:
            self.stdscr.addstr(h - 4, 2, "RITUAL COMPLETE.", curses.color_pair(3))
            self.stdscr.addstr(h - 3, 2, "PRESS ANY KEY TO ASCEND.", curses.color_pair(3))

        # Visual Noise
        if self.corruption_level > 0.5:
            for _ in range(5):
                ry = random.randint(0, h-1)
                rx = random.randint(0, w-1)
                try:
                    self.stdscr.addch(ry, rx, random.choice(['#', '@', '!', '?']), curses.color_pair(4))
                except curses.error:
                    pass

        self.stdscr.refresh()

    def run(self):
        self.stdscr.nodelay(True)

        while self.running:
            self.draw_interface()

            try:
                key = self.stdscr.getch()
            except:
                key = -1

            if key != -1:
                if self.corruption_level <= 0.1:
                    self.running = False
                    break

                char = chr(key)
                if char.isalpha():
                    self.input_buffer += char.upper()
                elif key == 10 or key == 13: # Enter
                    if self.input_buffer == self.current_key:
                        self.corruption_level = max(0, self.corruption_level - 0.2)
                        self.input_buffer = ""
                        self.current_key = random.choice(self.keys)
                        # Flash effect
                        curses.flash()
                    else:
                        # Punishment
                        self.corruption_level = min(1.0, self.corruption_level + 0.1)
                        self.input_buffer = ""
                elif key == 27: # Esc
                    self.running = False
                elif key == 8 or key == 127: # Backspace
                    self.input_buffer = self.input_buffer[:-1]

            time.sleep(0.05)

def main(stdscr):
    ritual = Ritual(stdscr)
    ritual.run()

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except Exception as e:
        print(f"RITUAL FAILED: {e}")
