import random
import sys
sys.path.append('C:\\Python312\\Lib\\site-packages')

import pygame

pygame.init()

# Set up the screen
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Circle Catcher")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define game variables
clock = pygame.time.Clock()

player_radius = 5
player_color = BLUE
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5

circles = []

# Function to create new circles
def create_circle():
    radius = random.randint(5, 20)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    x = random.randint(0, SCREEN_WIDTH - 2*radius)
    y = random.randint(0, SCREEN_HEIGHT - 2*radius)
    circle = {'rect': pygame.Rect(x, y, 2*radius, 2*radius), 'color': color, 'radius': radius}
    circles.append(circle)

for i in range(10):
    create_circle()

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(60)  # Set the frame rate to 60 frames per second

    for circle in circles:
        pygame.draw.circle(screen, circle['color'], circle['rect'].center, circle['radius'])

    # Move player circle with keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= player_speed
        player_x = max(player_x, player_radius)  # Ensure player does not move off the left edge
    if keys[pygame.K_d]:
        player_x += player_speed
        player_x = min(player_x, SCREEN_WIDTH - player_radius)  # Ensure player does not move off the right edge
    if keys[pygame.K_w]:
        player_y -= player_speed
        player_y = max(player_y, player_radius)  # Ensure player does not move off the top edge
    if keys[pygame.K_s]:
        player_y += player_speed
        player_y = min(player_y, SCREEN_HEIGHT - player_radius)  # Ensure player does not move off the bottom edge

    # Draw player circle
    pygame.draw.circle(screen, player_color, (player_x, player_y), player_radius)

    player_rect = pygame.Rect(player_x - player_radius, player_y - player_radius, 2 * player_radius, 2 * player_radius)

    for circle in circles:
            if player_rect.colliderect(circle['rect']):
                circles.remove(circle)
    
        # Refresh screen
    pygame.display.flip()

pygame.quit()
sys.exit()
