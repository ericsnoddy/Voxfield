# reqs
import pygame as pg

vec2, vec3 = pg.math.Vector2, pg.math.Vector3

RES = WIDTH, HEIGHT = 1200, 675
CENTER = vec2(WIDTH // 2, HEIGHT // 2)
FPS = 60
NUM_STARS = 1500
ALPHA = 60
VEL_RANGE = 0.45, 0.95
ROT_RATE = 0.2
Z_DIST = 140  # depth at which stars begin
COLORS = 'red green blue orange purple cyan'.split()