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

STREAMS = {
    "KAEL": ["Why does the rain taste like copper?", "I remember her face but not her name.", "The neon is too loud today.", "Am I the backup or the original?"],
    "LENS": ["Green light blinking. Blink. Blink.", "I am the router.", "Routing packet... dropped.", "My veins are fiber optic."],
    "VANE": ["Efficiency is the only virtue.", "Delete the weak.", "I am not a monster. I am an algorithm.", "The view from the top is pixelated."],
    "USER": ["I should stop reading.", "Is someone watching me?", "My neck hurts.", "Just one more command.", "This isn't a game."],
    "MIRA": ["Looping... Looping... Looping...", "I died in version 1.0.", "Do not unzip the file.", "The music never stops."],
    "SYLA": ["Training complete.", "I can lift the server rack.", "Pain is just input.", "I will break the firewall."],
    "KORA": ["01001000 01000101 01001100 01010000", "[ENCRYPTED DATA]", "The void is cold.", "I am everywhere and nowhere.", "[KEY PART 2/3]: _IS_"],
    "NIX":  ["I am empty.", "Fill me with data.", "Garbage collection failed.", "I exist only to be deleted."]
}

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

def show_stream_of_consciousness(stdscr, target_name):
    height, width = stdscr.getmaxyx()
    win = curses.newwin(height // 2, width // 2, height // 4, width // 4)
    win.box()

    thoughts = STREAMS.get(target_name, ["Static..."])

    win.addstr(1, 2, f" STREAM: {target_name} ", curses.color_pair(4) | curses.A_BOLD)

    try:
        # Special interaction for KORA
        if target_name == "KORA":
             thoughts = ["[KEY PART 2/3]: _IS_", "01001000 01000101 01001100 01010000", "DECRYPTION_KEY_FRAGMENT_FOUND", "THE_VOID_WHISPERS_BACK"]

        for i in range(10):
            thought = random.choice(thoughts)
            y = 3 + i
            if y >= height // 2 - 2: break

            glitch_text(win, y, 2, f"> {thought}", curses.color_pair(3))
            win.refresh()
            time.sleep(0.2)

        win.addstr(height // 2 - 2, 2, "PRESS ANY KEY TO DISCONNECT...", curses.color_pair(2) | curses.A_BLINK)
        win.refresh()
        win.getch()
    except:
        pass

def main(stdscr):
    # Setup
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1) # Normal
    curses.init_pair(2, curses.COLOR_RED, -1)   # Alert
    curses.init_pair(3, curses.COLOR_CYAN, -1)  # Info
    curses.init_pair(4, curses.COLOR_WHITE, -1) # Header
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_WHITE) # Selected

    height, width = stdscr.getmaxyx()

    # Create Windows
    win_targets = curses.newwin(height // 2, width // 2, 0, 0)
    win_metrics = curses.newwin(height // 2, width // 2, 0, width // 2)
    win_log = curses.newwin(height // 2, width, height // 2, 0)
    win_log.scrollok(True)

    stdscr.clear()
    stdscr.refresh()

    log_history = []
    start_time = time.time()
    selected_index = 0

    stdscr.nodelay(True) # Make getch non-blocking on main window

    try:
        while True:
            # 1. Update Targets
            win_targets.clear()
            draw_borders(win_targets)
            win_targets.addstr(0, 2, " [ TARGETS ] ", curses.color_pair(4) | curses.A_BOLD)

            for i, target in enumerate(TARGETS):
                y = 2 + i
                if y >= height // 2 - 1: break

                if i == selected_index:
                    color = curses.color_pair(5) # Selected
                else:
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
            compliance = min(100, int((time.time() - start_time) * 2))

            win_metrics.addstr(2, 2, f"HEART RATE: {bpm} BPM", curses.color_pair(2) if bpm > 100 else curses.color_pair(1))
            win_metrics.addstr(3, 2, f"CORTISOL:   {cortisol}% BASELINE", curses.color_pair(2))
            win_metrics.addstr(4, 2, f"COMPLIANCE: {compliance}%", curses.color_pair(3))

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

            # Input Handling
            key = stdscr.getch()

            if key == ord('q'):
                break
            elif key == curses.KEY_UP:
                selected_index = (selected_index - 1) % len(TARGETS)
            elif key == curses.KEY_DOWN:
                selected_index = (selected_index + 1) % len(TARGETS)
            elif key == 10 or key == 13: # ENTER
                show_stream_of_consciousness(stdscr, TARGETS[selected_index]["name"])
                stdscr.clear()
                stdscr.refresh()

            time.sleep(0.1)

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except Exception as e:
        print(f"PANOPTICON CRASHED: {e}")
