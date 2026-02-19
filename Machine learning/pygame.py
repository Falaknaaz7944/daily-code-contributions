import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Simple Pygame Window")

# Define colors (RGB values)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Drawing
    screen.fill(BLUE) # Fill the screen with blue

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
