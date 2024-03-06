import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 900
HEIGHT = 600
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Initialize paddles and ball
player_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)

# Set initial ball speed
ball_speed = [5, 5]

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= 5
    if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
        player_paddle.y += 5

    # Update ball position
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ball collision with paddles
    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed[0] = -ball_speed[0]

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Move opponent paddle towards the ball
    if ball_speed[0] > 0:
        if opponent_paddle.centery < ball.centery:
            opponent_paddle.y += 3
        elif opponent_paddle.centery > ball.centery:
            opponent_paddle.y -= 3

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, opponent_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Update the display
    pygame.display.flip()

    # Set the frames per second
    clock.tick(FPS)












keys = pygame.key.get_pressed()
if keys[pygame.K_UP]:
    paddle2_y -= player_speed
    paddle2_y = max(paddle2_y, paddle_h,paddle_w)  
if keys[pygame.K_DOWN]:
    paddle2_y += player_speed
    paddle2_y = max(paddle2_y, paddle_h,paddle_w)