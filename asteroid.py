import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity = None):
        super().__init__(x, y, radius)
        if velocity:
            self.velocity = velocity


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        groups = self.groups()

        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
            
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
            
        x, y = self.position
        asteroid1 = Asteroid(x, y, new_radius, new_velocity1 * 1.2)
        asteroid2 = Asteroid(x, y, new_radius, new_velocity2 * 1.2)

        for group in groups:
            group.add(asteroid1, asteroid2)


        