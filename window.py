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
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, self.COLOR_BLACK, self.COLOR_WHITE)
        curses.init_pair(2, self.COLOR_RED, self.COLOR_WHITE)
        curses.init_pair(3, self.COLOR_BLUE, self.COLOR_WHITE)
        curses.init_pair(4, self.COLOR_CYAN, self.COLOR_WHITE)
        curses.init_pair(5, self.COLOR_MAGENTA, self.COLOR_WHITE)
        curses.init_pair(6, self.COLOR_YELLOW, self.COLOR_WHITE)

    def color_pair(self, number):
        return curses.color_pair(number)

    def drawString(self, y, x, s, *args):
        self._w.addstr(y, x, s, *args)

    def drawLine(self, y, x, l, r, *args):
        line = "*" * l
        self.drawString(y, x, line, *args)

    def clear(self):
        self._w.clear()

    def update(self):
        self._w.refresh()

    def wait(self):
        self._w.getch()

    @staticmethod
    def run(func):
        curses.wrapper(func)
