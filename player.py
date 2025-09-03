import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, background):
        super().__init__()
        self.background = background
        self.img = pygame.image.load('assets/sprite.png')
        self.img = pygame.transform.scale(self.img, (50, 50))
        self.rect = self.img.get_rect()
        self.rect.x = 0
        self.rect.y = pygame.display.get_surface().get_height() - ((self.background.get_height() // 2) + self.img.get_height())
        self.speed_x = 5
        self.speed_y = 5

    def move(self):
        if self.rect.x + self.img.get_width() <= pygame.display.get_surface().get_width():
            self.rect.x += self.speed_x
        else:
            self.rect.x = 0