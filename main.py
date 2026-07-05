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
BLOCK_SIZE = 40
snake_x = WIDTH // 2
snake_y = HEIGHT // 2

direction_x = 0
direction_y = 0

clock = pygame.time.Clock()

running = True

while running:

    # Handle events
    for event in pygame.event.get():

     if event.type == pygame.QUIT:
        running = False

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_LEFT:
            direction_x = -BLOCK_SIZE
            direction_y = 0

        elif event.key == pygame.K_RIGHT:
            direction_x = BLOCK_SIZE
            direction_y = 0

        elif event.key == pygame.K_UP:
            direction_x = 0
            direction_y = -BLOCK_SIZE

        elif event.key == pygame.K_DOWN:
            direction_x = 0
            direction_y = BLOCK_SIZE

    snake_x += direction_x
    snake_y += direction_y

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