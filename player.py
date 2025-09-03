import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, background):
        super().__init__()
        self.background = background
        self.img = pygame.image.load('assets/sprite.png')
        self.img = pygame.transform.scale(self.img, (50, 50))
        self.rect = self.img.get_rect()
        self.rect.x = 0
        self.initial_y = pygame.display.get_surface().get_height() - ((self.background.get_height() // 2) + self.img.get_height())
        self.rect.y = self.initial_y
        self.speed_x = 5
        self.speed_y = 5
        self.jump_strength = 8
        self.gravity_power = 5
        self.on_jump = False

    def move(self):
        if self.rect.x + self.img.get_width() <= pygame.display.get_surface().get_width():
            self.rect.x += self.speed_x
        else:
            self.rect.x = 0

    def jump(self):
        if self.on_jump:
            if self.rect.y >= self.initial_y - 150:
                self.speed_x = 9
                self.rect.y -= self.jump_strength
            else:
                self.speed_x = 5
                self.on_jump = False

    def gravity(self):
        if (self.on_jump == False) and (self.rect.y < self.initial_y):
            self.rect.y += self.gravity_power

    def update(self):
        self.move()
        self.jump()
        self.gravity()