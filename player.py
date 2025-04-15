import pygame
from constants import *
from circleshape import *


class Player(CircleShape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        return pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, clock):
        return PLAYER_TURN_SPEED * clock
    
    def update(self, clock):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation -= self.rotate(clock)

        if keys[pygame.K_d]:
            self.rotation += self.rotate(clock)