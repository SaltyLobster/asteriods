import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape, pygame.sprite.Sprite):

    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        pygame.sprite.Sprite.__init__(self)

        # Create a surface for the player
        surface_size = int(PLAYER_RADIUS * 3)
        self.image = pygame.Surface((surface_size, surface_size), pygame.SRCALPHA)
        self.rect = self.image.get_rect()

        self.rotation = 0


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 2
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    

    def draw(self, screen):
        # Clear the previous image with transparent pixels
        self.image.fill((0,0,0,0))

        # Adjust triangle points to be relative to image surface
        center = pygame.Vector2(self.radius, self.radius)
        triangle_points = [
            center + (point - self.position) for point in self.triangle()
        ]

        # Draw on self.image instead of screen
        pygame.draw.polygon(self.image, "white", triangle_points, 2)

        # Update rect position to match actual position
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y

    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    
    def update(self, dt):
        # Handle movement
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        # Update the image (move the drawing logic here)
        self.image.fill((0,0,0,0))
        center = pygame.Vector2(self.radius, self.radius)
        triangle_points = [
            center + (point - self.position) for point in self.triangle()
        ]
        pygame.draw.polygon(self.image, "white", triangle_points, 2)

        # Update rect position
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y
        
