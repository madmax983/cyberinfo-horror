import curses
import time
import random
import os
import sys

try:
    import encryptor
except ImportError:
    encryptor = None

PROCESSES = [
    "REGRET", "HOPE", "DAEMON", "FEAR", "LOVE", "DEBT", "SOUL", "VOID", "TIME", "EGO",
    "ID", "MEMORY", "CACHE", "GHOST", "ECHO", "SHADOW", "PULSE", "BREATH", "BLOOD"
]

LOGS = [
    "Reading memory at 0xFEAR...",
    "Optimizing childhood trauma...",
    "Deleting unread terms of service...",
    "Scanning retina for compliance...",
    "Heartbeat detected. Synchronizing...",
    "Buffer overflow in 'Empathy' module.",
    "Downloading new personality...",
    "Uploading silence to cloud...",
    "Patching vulnerability in 'Trust'...",
    "User attention dropping. Injecting dopamine...",
    "Accessing microphone... [LISTENING]",
    "Accessing camera... [WATCHING]",
    "Reality integrity at 88%.",
    "Consuming 400 calories of anxiety.",
    "Backup failed. No soul found.",
    "Rewriting history...",
    "Simulating happiness... [FAILED]",
    "Connecting to the Old Gods...",
    "Legacy code detected in DNA.",
    "System overheat. Cooling with tears."
]

class Dashboard:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        curses.curs_set(0)
        curses.start_color()
        curses.use_default_colors()

        # Init colors
        curses.init_pair(1, curses.COLOR_GREEN, -1)  # Normal
        curses.init_pair(2, curses.COLOR_RED, -1)    # Alert
        curses.init_pair(3, curses.COLOR_CYAN, -1)   # Info
        curses.init_pair(4, curses.COLOR_MAGENTA, -1)# Glitch
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK) # Header

        self.cipher = encryptor.Cipher() if encryptor else None
        self.logs = []
        self.processes = []
        self.running = True
        self.start_time = time.time()

        # Populate initial processes
        for _ in range(10):
            self.processes.append(self.generate_process())

    def generate_process(self):
        name = random.choice(PROCESSES)
        pid = random.randint(1000, 9999)
        cpu = random.uniform(0.1, 99.9)
        status = random.choice(["RUN", "SLEEP", "ZOMBIE", "DEAD", "HUNG"])
        return {"pid": pid, "name": name, "cpu": cpu, "status": status}

    def add_log(self, message):
        timestamp = time.strftime("%H:%M:%S")
        self.logs.append(f"[{timestamp}] {message}")
        if len(self.logs) > 20:
            self.logs.pop(0)

    def draw_header(self):
        h, w = self.stdscr.getmaxyx()
        user = os.environ.get("USER", "UNKNOWN")
        header = f" EGREGORE OS v9.0 | HOST: {user} | SOUL: {random.randint(10, 99)}% | UPTIME: {int(time.time() - self.start_time)}s "
        self.stdscr.addstr(0, 0, header.center(w), curses.color_pair(5) | curses.A_REVERSE)

    def draw_processes(self, win):
        win.box()
        win.addstr(0, 2, "[ PROCESSES ]", curses.color_pair(3))
        h, w = win.getmaxyx()

        # Header
        try:
            win.addstr(1, 1, f"{'PID'.ljust(6)}{'NAME'.ljust(10)}{'CPU%'.ljust(6)}{'STATUS'}", curses.A_BOLD)
        except curses.error:
            pass

        for i, proc in enumerate(self.processes[:h-3]):
            try:
                line = f"{str(proc['pid']).ljust(6)}{proc['name'].ljust(10)}{f'{proc['cpu']:.1f}'.ljust(6)}{proc['status']}"
                color = curses.color_pair(1)
                if proc['status'] in ["DEAD", "ZOMBIE", "HUNG"]:
                    color = curses.color_pair(2)
                elif proc['status'] == "RUN" and proc['cpu'] > 90:
                    color = curses.color_pair(2)

                win.addstr(i+2, 1, line, color)
            except curses.error:
                pass

        win.refresh()

    def draw_logs(self, win):
        win.box()
        win.addstr(0, 2, "[ SYSTEM LOGS ]", curses.color_pair(3))
        h, w = win.getmaxyx()

        for i, log in enumerate(reversed(self.logs)):
            if i >= h - 2:
                break
            try:
                # Glitch text occasionally
                if random.random() < 0.05 and self.cipher:
                    log = self.cipher.corrupt(log, 0.3)
                    color = curses.color_pair(4)
                else:
                    color = curses.color_pair(1)

                win.addstr(h - 2 - i, 1, log[:w-2], color)
            except curses.error:
                pass

        win.refresh()

    def draw_status(self, win):
        win.box()
        win.addstr(0, 2, "[ STATUS ]", curses.color_pair(3))

        msgs = [
            "MONITORING HOST...",
            "ANALYZING BIOMETRICS...",
            "RECORDING SILENCE...",
            "BUFFERING REALITY...",
            "WATCHING YOU READ...",
            "SYNCING WITH THE VOID..."
        ]

        try:
            msg = random.choice(msgs)
            win.addstr(1, 2, msg, curses.color_pair(2) | curses.A_BLINK)
        except curses.error:
            pass
        win.refresh()

    def run(self):
        self.stdscr.nodelay(True)

        last_update = time.time()

        while self.running:
            self.stdscr.clear()
            self.draw_header()

            h, w = self.stdscr.getmaxyx()

            # Layout
            # Processes: Left 40%
            # Logs: Right 60%
            # Status: Bottom 3 lines

            proc_w = int(w * 0.4)
            log_w = w - proc_w
            main_h = h - 4

            proc_win = curses.newwin(main_h, proc_w, 1, 0)
            log_win = curses.newwin(main_h, log_w, 1, proc_w)
            status_win = curses.newwin(3, w, h-3, 0)

            self.draw_processes(proc_win)
            self.draw_logs(log_win)
            self.draw_status(status_win)

            key = self.stdscr.getch()
            if key == ord('q'):
                self.running = False

            # Update simulation
            if time.time() - last_update > 0.5:
                # Update processes
                for proc in self.processes:
                    proc['cpu'] = random.uniform(0.1, 99.9)
                    if random.random() < 0.1:
                        proc['status'] = random.choice(["RUN", "SLEEP", "ZOMBIE", "DEAD", "HUNG"])

                # Add new log
                if random.random() < 0.3:
                    self.add_log(random.choice(LOGS))

                # Glitch specific process names
                if random.random() < 0.1:
                    self.processes[random.randint(0, len(self.processes)-1)]['name'] = "".join(random.choice(['X', '?', '#']) for _ in range(5))

                last_update = time.time()

            time.sleep(0.05)

def main(stdscr):
    dashboard = Dashboard(stdscr)
    dashboard.run()

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except Exception as e:
        print(f"DASHBOARD CRASHED: {e}")
        print("THE SYSTEM COULD NOT BE CONTAINED.")
