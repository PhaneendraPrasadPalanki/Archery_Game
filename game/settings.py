import pygame

class Settings:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Settings")
        self.sound_on = True

    def open(self):
        while True:
            self.screen.fill((200, 200, 200))
            font = pygame.font.Font(None, 36)
            text = font.render(f"Sound: {'On' if self.sound_on else 'Off'}", True, (0, 0, 0))
            self.screen.blit(text, (150, 100))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.quit()
                        return

            pygame.display.update()
