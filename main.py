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
    game.screen.blit(game.player.img, game.player.rect)
    game.screen.blit(game.bird.img, game.bird.rect)
    game.player.update()
    game.bird.update()
    game.check_collision()

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if game.player.jump_finished:
                    game.player.on_jump = True
            if event.key == pygame.K_RIGHT:
                game.player.velocity = 5
                game.player.on_move = True
            elif event.key == pygame.K_LEFT:
                game.player.velocity = -5
                game.player.on_move = True
        elif event.type == pygame.KEYUP:
            game.player.on_move = False
            game.player.speed = 0
    # flip() the display to put your work on screen
    pygame.display.flip()

    game.clock.tick(60)  # limits FPS to 60

pygame.quit()