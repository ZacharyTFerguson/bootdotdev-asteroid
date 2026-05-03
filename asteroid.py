from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from logger import log_event
import random

import pygame


class Asteroid(CircleShape):
    def __init__(self,x,y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle_num = random.uniform(20,50)
        velocity_angle_one = self.velocity.rotate(angle_num)
        velocity_angle_two = self.velocity.rotate(-angle_num)
        smaller_asteroids_radius = self.radius - ASTEROID_MIN_RADIUS
        split_asteroid1 = Asteroid(self.position.x,self.position.y, smaller_asteroids_radius)
        split_asteroid1.velocity = velocity_angle_one * 1.2
        split_asteroid2 = Asteroid(self.position.x, self.position.y, smaller_asteroids_radius)
        split_asteroid2.velocity = velocity_angle_two * 1.2









