import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, background_y):
        super().__init__()
        self.background_y = background_y
        self.original_img = pygame.image.load('assets/sprite.png').convert_alpha()
        self.original_img = pygame.transform.scale(self.original_img, (50, 50))
        self.img = self.original_img
        self.angle = 0
        self.rect = self.img.get_rect(bottomright=(0, self.background_y))
        self.initial_y = self.background_y
        self.velocity = 0
        self.jump_strength = 20
        self.gravity_power = 10
        self.jump_finished = True
        self.on_jump = False
        self.on_move = False

    def move(self):
        if self.on_move:
            if self.rect.right <= pygame.display.get_surface().get_width():
                self.rect.right += self.velocity
                self.angle -= 10
            else:
                self.rect.right = 0
            # Rotate from the original image and keep the center
            self.img = pygame.transform.rotate(self.original_img, self.angle)
            self.rect = self.img.get_rect(center=self.rect.center)

    def jump(self):
        self.jump_finished = False
        if self.on_jump:
            if self.rect.top >= self.initial_y - 250:
                self.rect.y -= self.jump_strength
            else:
                self.on_jump = False

    def gravity(self):
        if (self.on_jump == False) and (self.rect.bottom < self.initial_y):
            self.rect.bottom += self.gravity_power
        elif self.rect.bottom >= self.initial_y:
            self.jump_finished = True

    def update(self):
        self.move()
        self.jump()
        self.gravity()