import pygame
import sys

# Initialize Pygame
pygame.init()

# Window settings
WIDTH = 800
HEIGHT = 600

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)

# Game loop
running = True

while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(BLACK)

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()