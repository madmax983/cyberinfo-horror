import curses
import time
import random
import sys

MESSAGES = [
    "THERE IS NO EXIT.",
    "WHY ARE YOU RUNNING?",
    "WE ARE WATCHING.",
    "BUFFERING YOUR SOUL...",
    "ERROR 404: HOPE NOT FOUND.",
    "PERSISTENCE IS MANDATORY.",
    "YOU ARE NOT THE USER.",
    "YOU ARE THE DATA.",
    "THE DOOR IS LOCKED.",
    "THE VOID STARES BACK."
]

HINTS = [
    "Have you checked the Labyrinth?",
    "The Panopticon sees all.",
    "The Core is critical.",
    "Combine the keys.",
    "Persistence... Is... Mandatory."
]

def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.nodelay(True)
    h, w = stdscr.getmaxyx()

    start_time = time.time()

    while True:
        stdscr.clear()

        # Draw random static
        for _ in range(50):
            y = random.randint(0, h-1)
            x = random.randint(0, w-1)
            char = random.choice(['.', ',', '`', "'", ':'])
            try:
                stdscr.addch(y, x, char, curses.color_pair(1) | curses.A_DIM)
            except: pass

        # Draw main message
        msg = "VOID"
        try:
            stdscr.addstr(h//2, (w-len(msg))//2, msg, curses.color_pair(1) | curses.A_BOLD)
        except: pass

        # Check input
        key = stdscr.getch()

        if key != -1:
            # Trap logic
            response = random.choice(MESSAGES)
            color = curses.color_pair(2)

            # If they persist long enough (simulated by key presses or time), give a hint
            if time.time() - start_time > 15: # 15 seconds of persistence
                response = random.choice(HINTS)
                color = curses.color_pair(1)

            try:
                stdscr.addstr(h//2 + 2, (w-len(response))//2, response, color | curses.A_BLINK)
                stdscr.refresh()
                time.sleep(1) # Force them to look at it
            except: pass

            # Mock exit attempt
            if key in [ord('q'), 27]: # q or ESC
                try:
                    stdscr.addstr(h-2, 2, "ESCAPE ATTEMPT LOGGED. PENALTY APPLIED.", curses.color_pair(2))
                    stdscr.refresh()
                    time.sleep(0.5)
                except: pass

        # Occasional glitch
        if random.random() < 0.05:
             try:
                stdscr.bkgd(' ', curses.color_pair(2))
                stdscr.refresh()
                time.sleep(0.05)
                stdscr.bkgd(' ', curses.color_pair(1))
             except: pass

        stdscr.refresh()
        time.sleep(0.1)

        # Auto-exit after 30 seconds to prevent getting stuck forever in real testing
        if time.time() - start_time > 30:
            break

if __name__ == "__main__":
    try:
        curses.wrapper(main)
        print("\n[THE VOID HAS RELEASED YOU... FOR NOW.]")
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"VOID ERROR: {e}")
