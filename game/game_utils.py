import pygame
import math

class Bow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/bow.jpg')
        self.image = pygame.transform.scale(self.image, (200, 150))  # Resize bow to width 100 and height 50
        self.rect = self.image.get_rect(center=(400, 550))
        self.speed = 3  # Default speed
        self.direction = 1

    def set_speed(self, speed):
        self.speed = speed

    def update(self):
        self.rect.x += self.speed * self.direction
        # Change direction when reaching the screen edges
        if self.rect.left < 0 or self.rect.right > 800:
            self.direction *= -1

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/arrow.jpg')
        self.image = pygame.transform.scale(self.image, (20, 60))  # Resize arrow to width 20 and height 60
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed
        # Optional: Remove the arrow if it moves off-screen
        if self.rect.bottom < 0:
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        try:
            self.image = pygame.image.load('assets/target.png')
            self.image = pygame.transform.scale(self.image, (100, 100))
        except pygame.error as e:
            print(f"Error loading target image: {e}")
        self.rect = self.image.get_rect(center=(400, 200))

    def get_score(self, hit_rect):
        target_center = pygame.math.Vector2(self.rect.center)
        hit_center = pygame.math.Vector2(hit_rect.center)
        distance = target_center.distance_to(hit_center)

        # Define scoring ranges
        if distance < 20:  # Adjust based on target size
            return 50  # Highest score
        elif distance < 40:
            return 30
        elif distance < 60:
            return 10
        else:
            return 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)
