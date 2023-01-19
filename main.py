import random
from enum import Enum, IntEnum

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
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.dir = direction

    def move_forward(self):
        match self.dir:
            case Direction.Up:
                self.y -= 1
            case Direction.Down:
                self.y += 1
            case Direction.Left:
                self.x -= 1
            case Direction.Right:
                self.x += 1

        if self.x > WIDTH - 1:
            self.x = 0
        elif self.x < 0:
            self.x = WIDTH - 1
        elif self.y > HEIGHT - 1:
            self.y = 0
        elif self.y < 0:
            self.y = HEIGHT - 1

    def turn_right(self):
        self.dir += 1
        if self.dir > Direction.Left:
            self.dir = Direction.Up

    def turn_left(self):
        self.dir -= 1
        if self.dir < Direction.Up:
            self.dir = Direction.Left


class App:
    def __init__(self, bg=1, fg=11, no_of_ants=8) -> None:
        self.bg = bg
        self.fg = fg
        pyxel.init(WIDTH, HEIGHT, fps=60, title="Langton's Ant")

        self.grid = [[False for _ in range(pyxel.height)]
                     for _ in range(pyxel.width)]

        self.ants = [Ant(0, 0, random.randint(0, 3)) for _ in range(no_of_ants)]
        for idx, ant in enumerate(self.ants):
            random_x = random.randint(0, pyxel.width - 1)
            random_y = random.randint(0, pyxel.height - 1)
            ant.x, ant.y = random_x, random_y
            self.grid[random_x][random_y] = True

        pyxel.cls(self.bg)
        pyxel.run(self.update, self.draw)

    def turn(self, ant):
        if not self.grid[ant.x][ant.y]:
            ant.turn_right()
        else:
            ant.turn_left()

        self.grid[ant.x][ant.y] = not self.grid[ant.x][ant.y]

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        for ant in self.ants:
            self.turn(ant)
            ant.move_forward()

    def draw(self) -> None:
        for ant in self.ants:
            if self.grid[ant.x][ant.y]:
                pyxel.pset(ant.x, ant.y, self.bg)
            else:
                pyxel.pset(ant.x, ant.y, self.fg)


if __name__ == '__main__':
    App(bg=1, fg=7, no_of_ants=8)
