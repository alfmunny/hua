from window import Window
import curses
import time

class Model:
    def figure1(self):
        return """
                      _~^~^~_
                  \) /  o o  \ (/
                    '_   -   _'
                    / '-----' \ """

    def figure2(self):
        return """
                  _~^~^~_
                 /  o o  \
                '_   -   _'
                \ '-----' / """

    def render(self):
        while True:
            print("%s"%self.figure, end='\r', flush=True3
            #print("this", end='\r', flush=True)
            time.sleep(2)
            print("%s"%self.figure2, end='\r', flush=True)
            #print("that", end='\r', flush=True)
            time.sleep(2)

class Object():
    def __init__():
        pass
    pass

class Environment():
    pass

class Animal(Model):
    pass

class Ground(Model):
    pass

class Crab(Animal):
    pass

class Human(Model):
    pass

def main(stdscr):
    win = Window(stdscr)
    m = Model()
    #win.drawString(0, 0, "*")
    win.drawLine(0, 0, 12, 0)
    win.update()
    win.wait()

Window.run(main)
