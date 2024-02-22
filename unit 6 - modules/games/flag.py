import sys
import pygame
# Initialize Pygame
pygame.init()
# Set up the display
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("abe = super big boi")
# Define RGB colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
black = (0, 0, 0)
white = (255, 255, 255)
# Main loop
while True:
    screen.fill((255, 255, 255))  # Fill the screen with white color
    # Draw colored rectangles
    pygame.draw.rect(screen, black, (60, 48, 10, 150))  # Flagpole
    pygame.draw.rect(screen, blue, (70, 50, 100, 60))  # Flag
    pygame.draw.lines(screen, white, False, [(70, 75), (170, 50)], 4)  # Stripes
    pygame.draw.lines(screen, white, False, [(70, 110), (170, 80)], 4)  # Stripes
    
    # Update the display
    pygame.display.flip()
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        