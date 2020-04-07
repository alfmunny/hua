import sys
import time
import curses

class Window:
    COLOR_WHITE     = curses.COLOR_WHITE
    COLOR_BLACK     = curses.COLOR_BLACK
    COLOR_RED       = curses.COLOR_RED
    COLOR_BLUE      = curses.COLOR_BLUE
    COLOR_CYAN      = curses.COLOR_CYAN
    COLOR_GREEN     = curses.COLOR_GREEN	
    COLOR_MAGENTA   = curses.COLOR_MAGENTA
    COLOR_YELLOW    = curses.COLOR_YELLOW

    def __init__(self, stdsrc):
        self._w = stdsrc
        self.height, self.width = self._w.getmaxyx()
        curses.curs_set(0)
        self._init_colors()

    def _init_colors(self):
        B
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, self.COLOR_BLACK, self.COLOR_WHITE)

    def drawString(self, x, y, m, *args):
        self._w.addstr(x, y, m, *args)

    def clear(self):
        self._w.clear()

    def update(self):
        self._w.refresh()

    def wait(self):
        self._w.getch()

    @staticmethod
    def run(func):
        curses.wrapper(func)
