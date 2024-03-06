import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

player_speed = 10
paddle_w = 20
paddle_h = 80
paddle1_x = 15
paddle1_y = SCREEN_HEIGHT // 2 - paddle_h // 2

paddle2_x = SCREEN_WIDTH - 15 - paddle_w
paddle2_y = SCREEN_HEIGHT // 2 - paddle_h // 2

ball_speed_x = 5
ball_speed_y = 5

ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2

ball_radius = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

player1_score = 0
player2_score = 0
max_score = 10

font = pygame.font.Font(None, 48)

def reset_ball():
    return SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= player_speed

    if keys[pygame.K_DOWN] and paddle2_y < SCREEN_HEIGHT - paddle_h:
        paddle2_y += player_speed

    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= player_speed

    if keys[pygame.K_s] and paddle1_y < SCREEN_HEIGHT - paddle_h:
        paddle1_y += player_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_y <= 0 or ball_y >= SCREEN_HEIGHT:
        ball_speed_y = -ball_speed_y

    if ((paddle1_x < ball_x < paddle1_x + paddle_w and paddle1_y < ball_y < paddle1_y + paddle_h) or
        (paddle2_x < ball_x < paddle2_x + paddle_w and paddle2_y < ball_y < paddle2_y + paddle_h)
    ):
        ball_speed_x = -ball_speed_x

    if ball_x - ball_radius <= 0:
        player2_score += 1
        ball_x, ball_y = reset_ball()
    elif ball_x + ball_radius >= SCREEN_WIDTH:
        player1_score += 1
        ball_x, ball_y = reset_ball()

    if player1_score >= max_score or player2_score >= max_score:
        running = False

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [paddle1_x, paddle1_y, paddle_w, paddle_h])
    pygame.draw.rect(screen, WHITE, [paddle2_x, paddle2_y, paddle_w, paddle_h])
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), ball_radius)

    player1_text = font.render(f"Player 1: {player1_score}", True, WHITE)
    player2_text = font.render(f"Player 2: {player2_score}", True, WHITE)
    screen.blit(player1_text, (50, 20))
    screen.blit(player2_text, (SCREEN_WIDTH - 200, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

