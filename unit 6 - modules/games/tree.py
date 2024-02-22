import sys
sys.path.append('C:\\Python312\\Lib\\site-packages')
import pygame
# Initialize Pygame
pygame.init()
# Set up the display
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Random clour tree drawing")
# Define colors
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)
GREEN = (0, 128, 0)
DARK_PURPLE = (54,47,56)
DARK_GREEN = (12, 40, 32)
DARK_PINK = (163, 101, 114)
LIGHT_YELLOW = (187, 188, 137)
# Main loop
while True:
    screen.fill(WHITE)  # Fill the screen with white color
    
    # Draw the trunk (rectangle)
    pygame.draw.rect(screen, DARK_PURPLE, (180, 250, 40, 100))  # (x, y, width, height)
    
    # Draw the leaves (triangle)
    pygame.draw.polygon(screen, DARK_GREEN, [(100, 250), (200, 100), (300, 250)])
    pygame.draw.polygon(screen, DARK_PINK, [(120, 200), (200, 50), (280, 200)])
    pygame.draw.polygon(screen, LIGHT_YELLOW, [(140, 150), (200, 20), (260, 150)])
    
    # Update the display
    pygame.display.flip()
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

