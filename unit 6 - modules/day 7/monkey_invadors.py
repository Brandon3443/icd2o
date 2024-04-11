import pygame
import random
import sys

pygame.init()
pygame.mixer.init()
fire = pygame.mixer.Sound('blaster-2-81267.mp3')
alien_dying = pygame.mixer.Sound('mixkit-negative-game-notification-249.wav')
pygame.mixer.music.load('Travis Scott - Butterfly Effect.mp3')
pygame.mixer.music.play(-1)

WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monkey Invadors")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

player_size = 50
player_img = pygame.image.load("player_fixed.png")
player_img = pygame.transform.scale(player_img, (player_size, player_size))
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 70
player_speed = 5
player_lives = 3

enemy_size = 50
enemy_img = pygame.image.load("monkey.png")
enemy_img = pygame.transform.scale(enemy_img, (enemy_size, enemy_size))
num_enemies = 20
enemies = []

bullet_img = pygame.image.load("bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (40, 120))
bullet_rect = bullet_img.get_rect(center=(0, 0))
bullet_speed = 25
bullet_state = "ready"

enemy_bullet_img = pygame.image.load("monkey_banana.png")
enemy_bullet_img = pygame.transform.scale(enemy_bullet_img, (20, 40))
enemy_bullet_speed = 5

score_value = 0
font = pygame.font.Font(None, 32)
text_x = 10
text_y = 10

enemy_shoot_timer = pygame.time.get_ticks()
enemy_shoot_interval = 2000
clock = pygame.time.Clock()
game_over = False
running = True

enemy_bullets = []

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y):
    screen.blit(enemy_img, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    bullet_rect.midtop = (x, y)

def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = ((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2) ** 0.5
    if distance < enemy_size / 2:
        return True
    else:
        return False

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, WHITE)
    screen.blit(score, (x, y))

def show_lives(x, y, lives):
    lives_text = font.render("Lives : " + str(lives), True, WHITE)
    screen.blit(lives_text, (x, y))

def show_game_over(score):
    game_over_font = pygame.font.Font("freesansbold.ttf", 64)
    game_over_text = game_over_font.render("Game Over", True, RED)
    screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))

    final_score_text = font.render("Final Score: " + str(score), True, WHITE)
    screen.blit(final_score_text, (WIDTH // 2 - 120, HEIGHT // 2 + 50))

    play_again_text = font.render("Play Again? (Y/N)", True, WHITE)
    screen.blit(play_again_text, (WIDTH // 2 - 150, HEIGHT // 2 + 100))

def reset_game():
    global score_value, game_over, player_lives, enemies
    score_value = 0
    game_over = False
    player_lives = 3
    enemies.clear()
    spawn_enemies()

def draw_enemy_bullets():
    for bullet_pos in enemy_bullets:
        rotated_bullet_img = pygame.transform.rotate(enemy_bullet_img, bullet_pos[2])  # Rotate the bullet image
        new_rect = rotated_bullet_img.get_rect(center=enemy_bullet_img.get_rect(topleft=(bullet_pos[0], bullet_pos[1])).center)  # Adjust the bullet position after rotation
        screen.blit(rotated_bullet_img, new_rect.topleft)

def move_enemy_bullets():
    for bullet_pos in enemy_bullets:
        bullet_pos[1] += enemy_bullet_speed
        bullet_pos[2] += 10  

def enemy_shoot():
    global enemy_bullet_speed, enemy_shoot_interval, screen
    for enemy_pos in enemies:
        should_shoot = random.randint(0, 100)
        if should_shoot < 20:  
            enemy_bullet_x = enemy_pos[0] + enemy_size // 2
            enemy_bullet_y = enemy_pos[1] + enemy_size // 2
            enemy_bullets.append([enemy_bullet_x, enemy_bullet_y, 0])  

    if pygame.time.get_ticks() % 10000 == 0:
        enemy_bullet_speed += 2
        enemy_shoot_interval -= 500

        screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

def check_bullet_collision():
    global score_value, player_lives, game_over
    for bullet_pos in enemy_bullets:
        if bullet_pos[1] >= player_y and bullet_pos[1] <= player_y + player_size:
            if bullet_pos[0] >= player_x and bullet_pos[0] <= player_x + player_size:
                enemy_bullets.remove(bullet_pos)
                pygame.mixer.Sound.play(alien_dying)
                player_lives -= 1
                if player_lives <= 0:
                    game_over = True
                else:
                    reset_player_position()

def reset_player_position():
    global player_x
    player_x = WIDTH // 2 - player_size // 2

def spawn_enemy():
    global enemies
    enemy_x = random.randint(0, WIDTH - enemy_size)
    enemy_y = random.randint(50, 200)
    for existing_enemy in enemies:
        distance = ((existing_enemy[0] - enemy_x) ** 2 + (existing_enemy[1] - enemy_y) ** 2) ** 0.5
        if distance < enemy_size * 1.5:  
            return spawn_enemy()
    enemies.append([enemy_x, enemy_y])

def spawn_enemies():
    global enemies
    enemies.clear()
    for _ in range(num_enemies):
        spawn_enemy()

spawn_enemies()

while running:
    while not game_over:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    game_over = True
                elif event.key == pygame.K_y and game_over:
                    reset_game()
                elif event.key == pygame.K_n and game_over:
                    pygame.quit()
                    sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_SPACE] and bullet_state == "ready":
            bullet_rect.midtop = (player_x + player_size // 2, player_y)
            fire_bullet(*bullet_rect.midtop)

        if player_x <= 0:
            player_x = 0
        elif player_x >= WIDTH - player_size:
            player_x = WIDTH - player_size

        for enemy_pos in enemies:
            collision = isCollision(enemy_pos[0], enemy_pos[1], bullet_rect.x, bullet_rect.y)
            if collision:
                bullet_rect.y = 0
                bullet_state = "ready"
                score_value += 1
                enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
                enemy_pos[1] = random.randint(50, 200)
                pygame.mixer.Sound.play(alien_dying)
            enemy(*enemy_pos)

        if bullet_state == "fire":
            screen.blit(bullet_img, bullet_rect)
            bullet_rect.y -= bullet_speed
            pygame.mixer.Sound.play(fire)
            if bullet_rect.y <= 0:
                bullet_state = "ready"

        current_time = pygame.time.get_ticks()
        if current_time - enemy_shoot_timer >= enemy_shoot_interval:
            enemy_shoot()
            enemy_shoot_timer = current_time

        move_enemy_bullets()
        check_bullet_collision()

        player(player_x, player_y)
        show_score(text_x, text_y)
        show_lives(WIDTH - 150, text_y, player_lives)
        draw_enemy_bullets()

        pygame.display.flip()
        clock.tick(60)

    while game_over:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    reset_game()
                    game_over = False
                elif event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()

        screen.fill(BLACK)
        show_game_over(score_value)
        pygame.display.flip()
        clock.tick(60)

pygame.quit()
sys.exit()