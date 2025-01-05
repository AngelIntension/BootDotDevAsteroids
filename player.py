import pygame
from circleshape import *
from constants import *

WHITE = (255, 255, 255)

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.position = pygame.Vector2(x, y)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) * self.radius
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward
        b = self.position - forward - right
        c = self.position - forward + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED
        self.position += velocity * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
    