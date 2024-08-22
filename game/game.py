import pygame
import sys
from game.game_utils import Bow, Arrow, Target

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()  # Initialize the mixer for sound
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Archery Game")
        self.clock = pygame.time.Clock()
        self.bow = Bow()
        self.target = Target()
        self.arrows = pygame.sprite.Group()
        self.total_arrows = 10
        self.bow.set_speed(3)
        self.sound_on = True
        self.shoot_sound = pygame.mixer.Sound('assets/sound/arrow_shoot.mp3')
        self.score = 0

    def start(self):
        while True:
            self.handle_events()
            self.update_game()
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_x]:
            if self.total_arrows > 0:
                arrow = Arrow(self.bow.rect.centerx, self.bow.rect.top)
                self.arrows.add(arrow)
                self.total_arrows -= 1
                if self.sound_on:
                    self.shoot_sound.play()

        if self.total_arrows <= 0 and not self.arrows:
            self.game_over()

    def update_game(self):
        self.bow.update()
        for arrow in self.arrows:
            arrow.update()
            if arrow.rect.colliderect(self.target.rect):
                self.arrows.remove(arrow)
                arrow.rect.center = self.target.rect.center
                self.screen.blit(arrow.image, arrow.rect)
            
                # Update the score based on where the arrow hits the target
                score = self.target.get_score(arrow.rect)
                self.score += score

    def render(self):
        self.screen.fill((255, 255, 255))
        self.bow.draw(self.screen)
        self.target.draw(self.screen)
        for arrow in self.arrows:
            self.screen.blit(arrow.image, arrow.rect)
        
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {self.score}', True, (0, 0, 0))
        self.screen.blit(score_text, (650, 20))
        
        pygame.display.update()

    def game_over(self):
        font = pygame.font.Font(None, 74)
        text = font.render('Game Over', True, (255, 0, 0))
        text_rect = text.get_rect(center=(400, 300))
        self.screen.fill((255, 255, 255))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.start()
