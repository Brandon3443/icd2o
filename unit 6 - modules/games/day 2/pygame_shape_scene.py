import sys
sys.path.append('C:\\Python312\\Lib\\site-packages')
import pygame
# Initialize Pygame
pygame.init()
# Set up the display
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bear house")
# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
YELLOW = (255, 255, 0)
black = (0, 0, 0)
# Main loop
while True:
    screen.fill(WHITE)  # Fill the screen with white color
    
    # Draw the house body
    pygame.draw.rect(screen, BLUE, (150, 200, 200, 150))  # (x, y, width, height)
    
    # Draw the roof (triangle)
    pygame.draw.polygon(screen, black, [(150, 200), (250, 100), (350, 200)])
    
    # Draw the door
    pygame.draw.rect(screen, black, (225, 280, 50, 70))
    
    # Draw the windows
    pygame.draw.circle(screen, WHITE, (200, 230), 20)  # Window 1
    pygame.draw.circle(screen, WHITE, (300, 230), 20)  # Window 2
    
    # Update the display
    pygame.display.flip()
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

            