import circleshape
import pygame
from constants import SHOT_RADIUS, LINE_WIDTH, PLAYER_SHOOT_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MAX_RADIUS

class Shot(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt