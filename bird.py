import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, background_y):
        super().__init__()
        self.background_y = background_y
        self.original_img = pygame.image.load('assets/Bird.png').convert_alpha()
        self.original_img = pygame.transform.scale(self.original_img, (50, 50))
        self.img = self.original_img
        self.rect = self.img.get_rect(bottomright=(pygame.display.get_surface().get_width(), self.background_y + 30))
        self.speed_x = 5

    def move(self):
        if self.rect.right >= 0:
            self.rect.right -= self.speed_x
        else:
            self.rect.left = pygame.display.get_surface().get_width()

    def update(self):
        self.move()