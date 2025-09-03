import pygame
from game import Game

game = Game()

# pygame setup
pygame.init()

running = True

while running:
    # fill the screen with a color to wipe away anything from last frame
    game.screen.fill("white")

    # RENDER YOUR GAME HERE
    game.screen.blit(game.background, (game.background_rect.x, game.background_rect.y))
    game.screen.blit(game.player.img, (game.player.rect.x, game.player.rect.y))
    game.player.update()

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.player.on_jump = True

    # flip() the display to put your work on screen
    pygame.display.flip()

    game.clock.tick(60)  # limits FPS to 60

pygame.quit()