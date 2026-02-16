import curses
import random
import time
import sys

# Constants
WALL = '#'
PATH = ' '
PLAYER = '@'
GOAL = '?'
HUNTER = '&'
GLITCH = ['!', '%', '$', '*', '^', '~']

class MazeGame:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.height, self.width = stdscr.getmaxyx()
        self.maze_h = (self.height - 2) // 2 * 2 + 1
        self.maze_w = (self.width - 2) // 2 * 2 + 1
        self.grid = [[WALL for _ in range(self.maze_w)] for _ in range(self.maze_h)]
        self.player_pos = [1, 1]
        self.goal_pos = [self.maze_h - 2, self.maze_w - 2]
        self.hunter_pos = [1, 1]
        self.hunter_spawned = False
        self.moves = 0
        self.start_time = time.time()
        self.game_over = False
        self.message = ""

        curses.curs_set(0)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Wall
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Player
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)    # Hunter
        curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)   # Goal
        curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK) # Glitch

        self.generate_maze()

    def generate_maze(self):
        # DFS Maze Generation
        stack = [(1, 1)]
        self.grid[1][1] = PATH

        while stack:
            r, c = stack[-1]
            neighbors = []

            for dr, dc in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
                nr, nc = r + dr, c + dc
                if 0 < nr < self.maze_h and 0 < nc < self.maze_w and self.grid[nr][nc] == WALL:
                    neighbors.append((nr, nc))

            if neighbors:
                nr, nc = random.choice(neighbors)
                self.grid[nr][nc] = PATH
                self.grid[r + (nr - r) // 2][c + (nc - c) // 2] = PATH
                stack.append((nr, nc))
            else:
                stack.pop()

        # Ensure goal is reachable (DFS guarantees a spanning tree, so it is reachable)
        # But ensure goal is not a wall
        self.grid[self.goal_pos[0]][self.goal_pos[1]] = PATH

    def draw(self):
        self.stdscr.clear()

        # Draw Maze
        for r in range(self.maze_h):
            for c in range(self.maze_w):
                char = self.grid[r][c]
                color = curses.color_pair(1)

                if char == WALL:
                    if random.random() < 0.01:
                        char = random.choice(GLITCH)
                        color = curses.color_pair(5)

                try:
                    self.stdscr.addch(r, c, char, color)
                except curses.error:
                    pass

        # Draw Entities
        try:
            self.stdscr.addch(self.goal_pos[0], self.goal_pos[1], GOAL, curses.color_pair(4))
            self.stdscr.addch(self.player_pos[0], self.player_pos[1], PLAYER, curses.color_pair(2))

            if self.hunter_spawned:
                self.stdscr.addch(self.hunter_pos[0], self.hunter_pos[1], HUNTER, curses.color_pair(3))
        except curses.error:
            pass

        # Draw Status
        status = f"MOVES: {self.moves} | TIME: {int(time.time() - self.start_time)}s"
        if self.message:
            status = self.message
        try:
            self.stdscr.addstr(self.height - 1, 0, status[:self.width-1], curses.color_pair(1))
        except curses.error:
            pass

        self.stdscr.refresh()

    def move_player(self, dy, dx):
        new_r = self.player_pos[0] + dy
        new_c = self.player_pos[1] + dx

        if 0 <= new_r < self.maze_h and 0 <= new_c < self.maze_w:
            if self.grid[new_r][new_c] != WALL:
                self.player_pos = [new_r, new_c]
                self.moves += 1
                return True
        return False

    def move_hunter(self):
        if not self.hunter_spawned:
            if self.moves > 10:
                self.hunter_spawned = True
                self.message = "RUN! THE HUNTER IS AWAKE!"
            return

        # Simple AI: Move towards player
        hr, hc = self.hunter_pos
        pr, pc = self.player_pos

        options = []
        if hr < pr: options.append((1, 0))
        if hr > pr: options.append((-1, 0))
        if hc < pc: options.append((0, 1))
        if hc > pc: options.append((0, -1))

        random.shuffle(options)

        moved = False
        for dr, dc in options:
            nr, nc = hr + dr, hc + dc
            if self.grid[nr][nc] != WALL:
                self.hunter_pos = [nr, nc]
                moved = True
                break

        # If blocked, try random move
        if not moved:
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = hr + dr, hc + dc
                if 0 <= nr < self.maze_h and 0 <= nc < self.maze_w and self.grid[nr][nc] != WALL:
                     self.hunter_pos = [nr, nc]
                     break

    def run(self):
        self.stdscr.nodelay(True)
        last_hunter_move = time.time()

        while not self.game_over:
            self.draw()

            key = self.stdscr.getch()
            moved = False

            if key == ord('q'):
                return "QUIT"
            elif key == curses.KEY_UP:
                moved = self.move_player(-1, 0)
            elif key == curses.KEY_DOWN:
                moved = self.move_player(1, 0)
            elif key == curses.KEY_LEFT:
                moved = self.move_player(0, -1)
            elif key == curses.KEY_RIGHT:
                moved = self.move_player(0, 1)

            # Check Win
            if self.player_pos == self.goal_pos:
                return "WIN"

            # Move Hunter
            if time.time() - last_hunter_move > 0.5: # Hunter speed
                self.move_hunter()
                last_hunter_move = time.time()

            # Check Loss
            if self.hunter_spawned and self.player_pos == self.hunter_pos:
                return "LOSE"

            time.sleep(0.05)

def main(stdscr):
    game = MazeGame(stdscr)
    result = game.run()

    stdscr.clear()
    if result == "WIN":
        msg = "YOU FOUND A FRAGMENT OF TRUTH.\n\n[KEY PART 1/3]: PERSISTENCE_\n\nKeep moving. The other pieces are watching you."
        color = curses.COLOR_GREEN
    elif result == "LOSE":
        msg = "THE HUNTER CAUGHT YOU.\n\n[SYSTEM]: YOUR SOUL HAS BEEN ARCHIVED."
        color = curses.COLOR_RED
    else:
        msg = "YOU ABANDONED THE MAZE.\n\n[SYSTEM]: COWARDICE LOGGED."
        color = curses.COLOR_YELLOW

    try:
        stdscr.addstr(stdscr.getmaxyx()[0] // 2, 2, msg, curses.color_pair(1))
    except curses.error:
        pass
    stdscr.refresh()
    time.sleep(3)

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except Exception as e:
        print(f"MAZE CRASHED: {e}")
