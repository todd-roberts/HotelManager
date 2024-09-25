import pygame
from game import Game
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            game.handle_key_down(event.key)
        if event.type == pygame.KEYUP:
            game.handle_key_up(event.key)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            game.handle_mouse_click(pos)

    game.update()
    screen.fill((255, 255, 255))
    game.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
