import pygame
from player import Player
from bird import Bird

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.background = pygame.image.load('assets/background.png').convert_alpha()
        self.background_rect = self.background.get_rect()
        self.background_rect.x = 0
        self.background_rect.y = pygame.display.get_surface().get_height() - (self.background.get_height() // 2 - 3)
        self.player = Player(self.background_rect.y)
        self.bird = Bird(self.player.rect.y)
        self.clock = pygame.time.Clock()

    def check_collision(self):
        if self.player.rect.colliderect(self.bird.rect):
            pygame.quit()
            print("Game Over")
            exit()