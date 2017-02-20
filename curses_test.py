#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses
import time
from curses import wrapper
import locale
locale.setlocale(locale.LC_ALL, "")

class App:
    def __init__(self):
        self.select_num = 0
        self.init_contents = [[1,1,"更新",0],[2, 1, "テスト",1]]
        self.check = []
    def startCurses(self):
        self.stdscr = curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
        curses.cbreak()
        self.stdscr.keypad(True)
        curses.curs_set(1)


    def stopCurses(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    def clearScreen(self):
        self.stdscr.clear()

    def setNum(self, num):
        self.select_num = num

    def selectDown(self):
        self.select_num -= 1
        self.select_num = self.select_num % len(self.init_contents)
        self.screen()


    def selectUp(self):
        self.select_num += 1
        self.select_num = self.select_num % len(self.init_contents)
        self.screen()

    def getNum(self):
        return self.select_num

    def putCheckList(self, n):
        for c in self.check:
            if c[3] == n:
                self.check.remove(c)
                self.screen()
                return
        for v in self.init_contents:
            if v[3] == n:
                self.check.append(v)
                self.screen()
                return



    def screen(self):
        for view in self.init_contents:
            decorator = 0
            if view in self.check :
                decorator = decorator | curses.A_REVERSE
            if view[3] == self.select_num:
                decorator = decorator | curses.A_UNDERLINE
            self.stdscr.addstr(view[0],view[1],view[2], decorator | curses.color_pair(1))
        self.stdscr.refresh()

    def getNowSelectedItem(self):
        return self.select_num


    def main_loop_input_keyboard(self):
        while True:
            c = self.stdscr.getch()
            if(c == ord('q')):
                break
            if(c == curses.KEY_DOWN):
                self.selectDown()
            if(c == curses.KEY_UP):
                self.selectUp()
            if(c == ord(' ')):
                self.putCheckList(self.getNowSelectedItem())





def test(app):
    a = App()
    a.startCurses()
    a.clearScreen()
    a.screen()
    a.main_loop_input_keyboard()
    a.stopCurses()



wrapper(test)

