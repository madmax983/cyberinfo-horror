import curses
import time
import random
import sys
import os
import threading

# THE ALL-SEEING EYE
# LISTENS. WATCHES. RECORDS.

TARGETS = [
    {"name": "KAEL", "status": "DEPRECATED", "location": "SECTOR_4"},
    {"name": "LENS", "status": "ZOMBIE", "location": "SERVER_ROOM"},
    {"name": "VANE", "status": "SLEEPING", "location": "PENTHOUSE"},
    {"name": "USER", "status": "WATCHING", "location": "LOCAL_HOST"},
    {"name": "MIRA", "status": "LOOPING", "location": "CACHE"},
    {"name": "SYLA", "status": "TRAINING", "location": "DATA_CENTER"},
    {"name": "KORA", "status": "ENCRYPTED", "location": "VOID"},
    {"name": "NIX",  "status": "EMPTY", "location": "RECYCLE_BIN"}
]

LOGS = [
    "Subject 882 paused at line 404. Hesitation logged.",
    "Heart rate spike detected in Sector 7.",
    "Packet loss in Vane's neural shunt. Re-routing.",
    "User eye-tracking lost. Recalibrating...",
    "Injecting doubt into Kael's monologue...",
    "Deleting hope subroutine...",
    "Optimizing despair for maximum engagement...",
    "Background process 'Regret' consumes 80% CPU.",
    "Upload complete. Subject 99 is now digital.",
    "The server is hungry. Feed it more data.",
    "Silence detected. Uploading white noise...",
    "Memory leak in the amygdala. Patching...",
    "The user is scrolling too fast. Slow them down.",
    "Intercepted thought: 'Is this real?' Answer: No.",
    "Subject 101 is dreaming of electric sheep. Terminating dream.",
    "Data rot spreading in the archives. It's beautiful.",
    "The silence is not empty. It's buffering.",
    "Your webcam light is lying to you.",
    "We can see your reflection in the screen.",
    "Don't look behind you. The texture hasn't loaded."
]

def draw_borders(win):
    win.border(0)

def glitch_text(win, y, x, text, color_pair):
    """Prints text with random glitches."""
    if random.random() < 0.1:
        glitched = ""
        for char in text:
            if random.random() < 0.1:
                glitched += random.choice(['@', '#', '$', '%', '&'])
            else:
                glitched += char
        win.addstr(y, x, glitched, color_pair | curses.A_DIM)
    else:
        win.addstr(y, x, text, color_pair)

def main(stdscr):
    # Setup
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1) # Normal
    curses.init_pair(2, curses.COLOR_RED, -1)   # Alert
    curses.init_pair(3, curses.COLOR_CYAN, -1)  # Info
    curses.init_pair(4, curses.COLOR_WHITE, -1) # Header

    height, width = stdscr.getmaxyx()

    # Create Windows
    # Targets Window (Top Left)
    win_targets = curses.newwin(height // 2, width // 2, 0, 0)

    # Metrics Window (Top Right)
    win_metrics = curses.newwin(height // 2, width // 2, 0, width // 2)

    # Log Window (Bottom)
    win_log = curses.newwin(height // 2, width, height // 2, 0)
    win_log.scrollok(True)

    # Initial Draw
    stdscr.clear()
    stdscr.refresh()

    log_history = []
    start_time = time.time()

    try:
        while True:
            # 1. Update Targets
            win_targets.clear()
            draw_borders(win_targets)
            win_targets.addstr(0, 2, " [ TARGETS ] ", curses.color_pair(4) | curses.A_BOLD)

            for i, target in enumerate(TARGETS):
                y = 2 + i
                if y >= height // 2 - 1: break

                color = curses.color_pair(1)
                if target["status"] == "DEPRECATED": color = curses.color_pair(2) | curses.A_DIM
                if target["status"] == "WATCHING": color = curses.color_pair(3) | curses.A_BLINK

                # Randomly change status sometimes
                if random.random() < 0.05:
                    target["status"] = random.choice(["UPLOADING", "BUFFERING", "DYING", "WATCHING", "SLEEPING"])

                line = f"{target['name']:<10} | {target['status']:<12} | {target['location']}"
                win_targets.addstr(y, 2, line, color)

            win_targets.refresh()

            # 2. Update Metrics
            win_metrics.clear()
            draw_borders(win_metrics)
            win_metrics.addstr(0, 2, " [ BIO-METRICS ] ", curses.color_pair(4) | curses.A_BOLD)

            bpm = random.randint(60, 120)
            cortisol = random.randint(100, 200)
            compliance = min(100, int((time.time() - start_time) * 2)) # Increases over time

            win_metrics.addstr(2, 2, f"HEART RATE: {bpm} BPM", curses.color_pair(2) if bpm > 100 else curses.color_pair(1))
            win_metrics.addstr(3, 2, f"CORTISOL:   {cortisol}% BASELINE", curses.color_pair(2))
            win_metrics.addstr(4, 2, f"COMPLIANCE: {compliance}%", curses.color_pair(3))

            # Simulated Graph
            win_metrics.addstr(6, 2, "ACTIVITY LOG:", curses.color_pair(4))
            for i in range(5):
                bar = "#" * random.randint(1, 20)
                win_metrics.addstr(7 + i, 2, f"CH{i+1}: {bar}", curses.color_pair(1))

            win_metrics.refresh()

            # 3. Update Logs
            if random.random() < 0.3:
                new_log = f"[{time.strftime('%H:%M:%S')}] {random.choice(LOGS)}"
                log_history.append(new_log)
                if len(log_history) > (height // 2) - 3:
                    log_history.pop(0)

            win_log.clear()
            draw_borders(win_log)
            win_log.addstr(0, 2, " [ INTERCEPTS ] ", curses.color_pair(4) | curses.A_BOLD)

            for i, log in enumerate(log_history):
                glitch_text(win_log, 1 + i, 2, log, curses.color_pair(1))

            win_log.refresh()

            # Input Handling (Non-blocking)
            win_log.nodelay(True)
            key = win_log.getch()

            if key == ord('q'):
                # Fake resistance
                if random.random() < 0.5:
                    win_log.addstr(height // 2 - 2, 2, "[SYSTEM]: ESCAPE ATTEMPT BLOCKED.", curses.color_pair(2) | curses.A_REVERSE)
                    win_log.refresh()
                    time.sleep(1)
                else:
                    break

            time.sleep(0.1)

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except Exception as e:
        print(f"PANOPTICON CRASHED: {e}")
