import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            split_angle = random.uniform(20, 50)
            split_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, split_radius)
            asteroid1.velocity = self.velocity.rotate(split_angle)
            asteroid2 = Asteroid(self.position.x, self.position.y, split_radius)
            asteroid2.velocity = self.velocity.rotate(-split_angle)
    