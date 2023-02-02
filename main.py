# import pygame module in this program
import pygame as pg
from os import environ
from sys import platform as _sys_platform
import math

def platform():
    if 'ANDROID_ARGUMENT' in environ:
        return "android"
    elif _sys_platform in ('linux', 'linux2','linux3'):
        return "linux"
    elif _sys_platform in ('win32', 'cygwin'):
        return 'win'

class Cardioid:
    def __init__(self, app):
        self.app = app
        self.radius = 400
        self.num_lines = 200
        self.translate = self.app.screen.get_width() // 2, self.app.screen.get_height() // 2
        self.counter, self.inc = 0, 0.01

    def draw(self):
        time = pg.time.get_ticks()
        self.radius = 350 + 50 * abs(math.sin(time * 0.004) - 0.5)
        factor = 1 + 0.0001 * time

        for i in range(self.num_lines):
            theta = (2 * math.pi / self.num_lines) * i
            x1 = int(self.radius * math.cos(theta)) + self.translate[0]
            y1 = int(self.radius * math.sin(theta)) + self.translate[1]

            x2 = int(self.radius * math.cos(factor * theta)) + self.translate[0]
            y2 = int(self.radius * math.sin(factor * theta)) + self.translate[1]

            pg.draw.aaline(self.app.screen, (255,255,255), (x1, y1), (x2, y2))

class App:
    def __init__(self):
        self.screen = pg.display.set_mode([1600, 900])
        self.clock = pg.time.Clock()
        self.cardioid = Cardioid(self)

    def draw(self):
        self.screen.fill((0,0,0))
        self.cardioid.draw()
        pg.display.flip()

    def run(self):
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick(60)

if __name__ == '__main__':
    app = App()
    app.run()