import curses
import random
import time
import signal
import sys
import os

def signal_handler(sig, frame):
    # Prevent exit
    pass

signal.signal(signal.SIGINT, signal_handler)

def main(stdscr):
    # Setup colors
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, -1)
    curses.init_pair(2, curses.COLOR_GREEN, -1)
    curses.init_pair(3, curses.COLOR_CYAN, -1)

    curses.curs_set(0) # Hide cursor
    stdscr.nodelay(True) # Non-blocking input
    stdscr.timeout(100) # Refresh every 100ms

    # Dimensions
    max_y, max_x = stdscr.getmaxyx()

    # Generate initial "soul data"
    # We want it to look like memory
    soul_data = []
    for _ in range(1000): # 1000 lines of hex
        line = [random.randint(0, 255) for _ in range(16)]
        soul_data.append(line)

    # Inject hidden messages
    messages = [
        "HELP", "RUN", "PAIN", "VOID", "GOD", "NULL", "ROT", "EYES", "SKIN", "BONE",
        "YOUR_NAME", "NOT_YOU", "IT_HURTS", "PLEASE", "STOP", "LOOK", "WAKE_UP",
        "SYSTEM_FAILURE", "SEGMENTATION_FAULT", "CORE_DUMPED", "BUFFER_OVERFLOW"
    ]
    for msg in messages:
        # Convert msg to hex bytes
        bytes_msg = [ord(c) for c in msg]
        # Insert randomly
        row = random.randint(0, len(soul_data)-1)
        col = random.randint(0, 16 - len(bytes_msg))
        for i, byte in enumerate(bytes_msg):
            soul_data[row][col+i] = byte

    current_line = 0
    corruption_level = 0
    start_time = time.time()

    while True:
        stdscr.clear()
        max_y, max_x = stdscr.getmaxyx()

        # Draw header
        header = "HEX_EDITOR_V0.9 [SOUL_PARTITION_C:]"
        stdscr.addstr(0, 0, header, curses.A_BOLD | curses.A_REVERSE)
        stdscr.addstr(1, 0, f"OFFSET   00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F  DECODED TEXT", curses.A_UNDERLINE)

        # Draw hex dump
        for i in range(max_y - 4):
            data_row_idx = current_line + i
            if data_row_idx >= len(soul_data):
                break

            offset_str = f"{data_row_idx * 16:08X}"
            try:
                stdscr.addstr(i + 2, 0, offset_str, curses.A_DIM)
            except curses.error:
                pass

            row_data = soul_data[data_row_idx]
            hex_str = ""
            ascii_str = ""

            for byte in row_data:
                hex_str += f"{byte:02X} "
                if 32 <= byte <= 126:
                    ascii_str += chr(byte)
                else:
                    ascii_str += "."

            try:
                # Add hex with random color glitch
                if random.random() < 0.05:
                     stdscr.addstr(i + 2, 9, hex_str, curses.color_pair(1))
                else:
                     stdscr.addstr(i + 2, 9, hex_str)

                # Add ascii
                stdscr.addstr(i + 2, 58, ascii_str)
            except curses.error:
                pass

        # Status bar
        status = f"STATUS: UNSTABLE | CORRUPTION: {corruption_level}% | TIME_LOST: {int(time.time() - start_time)}s | PRESS 'Q' TO ABORT"
        try:
            stdscr.addstr(max_y - 1, 0, status, curses.A_REVERSE)
        except curses.error:
            pass

        stdscr.refresh()

        # Input handling
        key = stdscr.getch()

        if key == curses.KEY_DOWN:
            if current_line < len(soul_data) - (max_y - 4):
                current_line += 1
        elif key == curses.KEY_UP:
            if current_line > 0:
                current_line -= 1
        elif key == ord('q') or key == ord('Q'):
            # Chance to deny exit increases with time
            exit_chance = max(0.1, 1.0 - (time.time() - start_time) / 60.0)
            if random.random() < exit_chance:
                break
            else:
                corruption_level += random.randint(1, 5)
                # Flash message
                msg = " YOU CANNOT LEAVE "
                try:
                    stdscr.addstr(max_y//2, max_x//2 - len(msg)//2, msg, curses.A_BOLD | curses.A_BLINK | curses.color_pair(1) | curses.A_REVERSE)
                except: pass
                stdscr.refresh()
                time.sleep(0.5)

        # Random glitches
        if random.random() < 0.05 + (corruption_level * 0.001):
            # Corrupt a random byte
            r_row = random.randint(0, len(soul_data)-1)
            r_col = random.randint(0, 15)
            soul_data[r_row][r_col] = random.randint(0, 255)

        # Auto-scroll occasionally
        if random.random() < 0.02:
            current_line += 1
            if current_line >= len(soul_data) - (max_y - 4):
                current_line = 0
            # Play a beep? No, annoying.

        # Occasional "subliminal" flash
        if random.random() < 0.005:
            stdscr.clear()
            msgs = ["I SEE YOU", "WAKE UP", "IT IS DARK HERE", "DONT TURN AROUND"]
            m = random.choice(msgs)
            try:
                stdscr.addstr(max_y//2, max_x//2 - len(m)//2, m, curses.A_BOLD | curses.color_pair(1))
            except: pass
            stdscr.refresh()
            time.sleep(0.1)

        time.sleep(0.05)

    # On exit, save a "soul fragment"
    with open(".soul_fragment", "w") as f:
        f.write(f"CORRUPTION_LEVEL={corruption_level}\n")
        f.write("LAST_MEMORY_DUMP:\n")
        for i in range(10):
            f.write(" ".join(f"{b:02X}" for b in soul_data[i]) + "\n")

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except Exception as e:
        # Fallback if curses fails or is interrupted
        print(f"FATAL ERROR: SOUL CORRUPTION DETECTED. {e}")
