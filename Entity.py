""""
Entity class
"""

# Import dependencies
import pygame as pg
import numpy as np
from math import atan


class Entity:
    def __init__(self, pos, vel, acc):
        self.pos = np.array(pos, dtype=float)
        self.vel = np.array(vel, dtype=float)
        self.acc = np.array(acc, dtype=float)

    def draw(self, screen):
        pg.draw.circle(screen, (0, 0, 255), (int(self.pos[0]), int(self.pos[1])), 5)

    def apply_force(self, force):

        self.acc += force

    def update(self, dt):
        self.apply_force([0, 0.5])
        self.vel = self.vel + self.acc * dt / 1000
        self.pos = self.pos + self.vel * dt / 1000

    def get_direction_angle(self):
        theta = atan(self.vel[1] / self.vel[0])
        return theta
