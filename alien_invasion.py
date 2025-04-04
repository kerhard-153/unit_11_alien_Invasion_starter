import sys
import pygame


class AlienInvasion:
    """Manage game assets and behaviors"""

    def __init__(self):
        
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (45, 50, 70)

        self.running = True

    def run_game(self):
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill(self.bg_color)
            pygame.display.flip()









if __name__ == '__main__':
    
    alien_inv = AlienInvasion()
    alien_inv.run_game()
