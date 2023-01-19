import random
from enum import IntEnum

import pyxel


class Direction(IntEnum):
    Up = 0,
    Right = 1,
    Down = 2,
    Left = 3


SCALE = 10
WIDTH = 800 // SCALE
HEIGHT = 640 // SCALE


class Ant:
    def __init__(self, x = 0, y = 0, direction = Direction.UP):
        self.x = x
        self.y = y
        self.dir = direction

    def move_forward(self):
        offsets = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        self.x += offsets[self.dir][0]
        self.y += offsets[self.dir][1]

        self.x = self.x % WIDTH
        self.y = self.y % HEIGHT


class App:
    def __init__(self, bg=1, fg=11, no_of_ants=8) -> None:
        self.bg = bg
        self.fg = fg

        pyxel.init(WIDTH, HEIGHT, fps=60, title="Langton's Ant")

        self.grid = [[False for _ in range(pyxel.height)]
                     for _ in range(pyxel.width)]

        self.ants = [Ant(direction=random.randint(0, 3)) for _ in range(no_of_ants)]

        for idx, ant in enumerate(self.ants):
            ant.x = random.randint(0, pyxel.width - 1)
            ant.y = random.randint(0, pyxel.height - 1)
            self.grid[ant.x][ant.y] = True

        pyxel.cls(self.bg)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        for ant in self.ants:
            ant.dir += -1 if self.grid[ant.x][ant.y] else 1
            ant.dir = ant.dir % 4

            self.grid[ant.x][ant.y] = not self.grid[ant.x][ant.y]

            ant.move_forward()

    def draw(self) -> None:
        for ant in self.ants:
            color = self.fg if not self.grid[ant.x][ant.y] else self.bg
            pyxel.pset(ant.x, ant.y, color)


if __name__ == '__main__':
    App(bg=1, fg=7, no_of_ants=8)
