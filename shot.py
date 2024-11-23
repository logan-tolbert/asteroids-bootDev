from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, 0)
        
    def update(self,dt):
        self.position += self.velocity * dt
        
    def collision_check(self, circle_shape):
        distance = self.position.distance_to(circle_shape.position)
        return distance < self.radius + circle_shape.radius