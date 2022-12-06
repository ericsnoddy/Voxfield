# std lib
import random
from math import pi, sin, cos

# local
from config import *


class Star:
    def __init__(self, app):
        self.win = app.win
        self.pos3d = self.get_pos3d()
        self.velocity = random.uniform(*VEL_RANGE)
        self.color = random.choice(COLORS)
        self.screen_pos = vec2(0, 0)
        self.size = 10

    
    def get_pos3d(self, scale_pos=35):
        angle = random.uniform(0, 2 * pi)  # [0, 2pi]
        radius = random.randrange(HEIGHT // 4, HEIGHT // 3) * scale_pos
        x = radius * sin(angle)
        y = radius * cos(angle)
        return vec3(x, y, Z_DIST)


    def update(self):
        # move star along z-axis by velocity
        self.pos3d.z -= self.velocity
        # reset star to random state when it gets close (< 1 unit on z-axis)
        # this is equivalent to destroying and re-creating the star
        self.pos3d = self.get_pos3d() if self.pos3d.z < 1 else self.pos3d
        # simple projection calculation 3d -> 2d; divide the z component and offset for center of screen
        self.screen_pos = (vec2(self.pos3d.x, self.pos3d.y) / self.pos3d.z) + CENTER
        # scaling ratio; trial and error
        self.size = (Z_DIST - self.pos3d.z) / (0.2 * self.pos3d.z)
        # rotate xy
        self.pos3d.xy = self.pos3d.xy.rotate(ROT_RATE)
        # mouse "navigation" - offset the center by mouse movement
        mouse_pos = CENTER - vec2(pg.mouse.get_pos())
        self.screen_pos += mouse_pos



    def draw(self):
        pg.draw.rect(self.win, self.color, (*self.screen_pos, self.size, self.size))
        # we want stars to get bigger as they draw closer; use ratio of starting distance
        self.size = Z_DIST / self.pos3d.z


class Starfield:
    def __init__(self, app):
        self.stars = [Star(app) for i in range(NUM_STARS)]


    def run(self):
        [star.update() for star in self.stars]
        # z-sorting so most distant stars are drawn first
        self.stars.sort(key=lambda star: star.pos3d.z, reverse=True)
        [star.draw() for star in self.stars]
