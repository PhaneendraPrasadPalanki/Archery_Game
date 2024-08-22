import pygame
import sys
from game.settings import Settings
from game.game import Game

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Archery Game")

def draw_text(surf, text, size, color, x, y):
    font = pygame.font.Font(None, size)
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surf.blit(textobj, textrect)

def main_menu():
    while True:
        screen.fill((255, 255, 255))
        draw_text(screen, 'Archery Game', 64, (0, 0, 0), 400, 100)
        draw_text(screen, 'Start Game', 48, (0, 0, 0), 400, 300)
        draw_text(screen, 'Settings', 48, (0, 0, 0), 400, 400)
        draw_text(screen, 'Exit', 48, (0, 0, 0), 400, 500)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if 250 < mouse_x < 550 and 275 < mouse_y < 325:
                    game = Game()
                    game.start()
                elif 250 < mouse_x < 550 and 375 < mouse_y < 425:
                    settings = Settings()
                    settings.open()
                elif 250 < mouse_x < 550 and 475 < mouse_y < 525:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main_menu()
