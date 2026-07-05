import pygame
import sys

# Initialize Pygame
pygame.init()

# Window settings
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Snake settings
BLOCK_SIZE = 20
snake_x = WIDTH // 2
snake_y = HEIGHT // 2

clock = pygame.time.Clock()

running = True

while running:

    # Handle events
    for event in pygame.event.get():

     if event.type == pygame.QUIT:
        running = False

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_LEFT:
            snake_x -= BLOCK_SIZE

        elif event.key == pygame.K_RIGHT:
            snake_x += BLOCK_SIZE

        elif event.key == pygame.K_UP:
            snake_y -= BLOCK_SIZE

        elif event.key == pygame.K_DOWN:
            snake_y += BLOCK_SIZE

    # Draw background
    screen.fill(BLACK)

    # Draw the snake block
    pygame.draw.rect(
        screen,
        GREEN,
        (snake_x, snake_y, BLOCK_SIZE, BLOCK_SIZE)
    )

    # Update display
    pygame.display.flip()

    # Limit FPS
    clock.tick(60)

pygame.quit()
sys.exit()