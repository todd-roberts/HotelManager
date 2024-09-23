import pygame

# Initialize pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic and rendering code go here

    pygame.display.flip()

# Clean up
pygame.quit()
