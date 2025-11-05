import pygame

from circleshape import CircleShape

from constants import ASTEROID_COLOR

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius) 
        self.x = x
        self.y = y
        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)