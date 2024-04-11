import pygame  # Import the pygame library for game development
import random  # Import the random module for generating random numbers
import sys     # Import the sys module for system-specific functions and variables

# Initialize pygame modules
pygame.init()
pygame.mixer.init()  # Initialize the mixer module for sound
fire = pygame.mixer.Sound('blaster-2-81267.mp3')  # Load the sound for firing
alien_dying = pygame.mixer.Sound('mixkit-negative-game-notification-249.wav')  # Load the sound for when an enemy dies
pygame.mixer.music.load('Travis Scott - Butterfly Effect.mp3')  # Load the background music
pygame.mixer.music.play(-1)  # Play the background music on loop

# Set the width and height of the game window
WIDTH, HEIGHT = 900, 700
# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Set the caption of the game window
pygame.display.set_caption("Monkey Invadors")

# Define some color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set the size of the player character
player_size = 50
# Load the image for the player character
player_img = pygame.image.load("player_fixed.png")
# Scale the player image to the desired size
player_img = pygame.transform.scale(player_img, (player_size, player_size))
# Set the initial position of the player character
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 70
# Set the speed of the player character
player_speed = 5
# Set the initial number of lives for the player
player_lives = 3

# Set the size of the enemy characters
enemy_size = 50
# Load the image for the enemy characters
enemy_img = pygame.image.load("monkey.png")
# Scale the enemy image to the desired size
enemy_img = pygame.transform.scale(enemy_img, (enemy_size, enemy_size))
# Set the number of enemies
num_enemies = 20
# Initialize a list to store the positions of the enemies
enemies = []

# Load the image for the player's bullets
bullet_img = pygame.image.load("bullet.png")
# Scale the bullet image to the desired size
bullet_img = pygame.transform.scale(bullet_img, (40, 120))
# Get the rectangle of the bullet image
bullet_rect = bullet_img.get_rect(center=(0, 0))
# Set the speed of the bullets
bullet_speed = 25
# Set the initial state of the bullet
bullet_state = "ready"

# Load the image for the enemy bullets
enemy_bullet_img = pygame.image.load("monkey_banana.png")
# Scale the enemy bullet image to the desired size
enemy_bullet_img = pygame.transform.scale(enemy_bullet_img, (20, 40))
# Set the speed of the enemy bullets
enemy_bullet_speed = 5

# Initialize variables for score and font
score_value = 0
font = pygame.font.Font(None, 32)
# Set the position of the score text
text_x = 10
text_y = 10

# Set variables for enemy shooting
enemy_shoot_timer = pygame.time.get_ticks()
enemy_shoot_interval = 2000
clock = pygame.time.Clock()
# Set the initial game state
game_over = False
running = True

# Initialize a list to store the positions of the enemy bullets
enemy_bullets = []

# Define a function to draw the player character
def player(x, y):
    screen.blit(player_img, (x, y))

# Define a function to draw an enemy character
def enemy(x, y):
    screen.blit(enemy_img, (x, y))

# Define a function to fire a bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    bullet_rect.midtop = (x, y)

# Define a function to check for collisions between objects
def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = ((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2) ** 0.5
    if distance < enemy_size / 2:
        return True
    else:
        return False

# Define a function to display the score
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, WHITE)
    screen.blit(score, (x, y))

# Define a function to display the number of lives
def show_lives(x, y, lives):
    lives_text = font.render("Lives : " + str(lives), True, WHITE)
    screen.blit(lives_text, (x, y))

# Define a function to display the game over screen
def show_game_over(score):
    game_over_font = pygame.font.Font("freesansbold.ttf", 64)
    game_over_text = game_over_font.render("Game Over", True, RED)
    screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))

    final_score_text = font.render("Final Score: " + str(score), True, WHITE)
    screen.blit(final_score_text, (WIDTH // 2 - 120, HEIGHT // 2 + 50))

    play_again_text = font.render("Play Again? (Y/N)", True, WHITE)
    screen.blit(play_again_text, (WIDTH // 2 - 150, HEIGHT // 2 + 100))

# Define a function to reset the game
def reset_game():
    global score_value, game_over, player_lives, enemies
    score_value = 0
    game_over = False
    player_lives = 3
    enemies.clear()
    spawn_enemies()

# Define a function to draw the enemy bullets
def draw_enemy_bullets():
    for bullet_pos in enemy_bullets:
        rotated_bullet_img = pygame.transform.rotate(enemy_bullet_img, bullet_pos[2])  # Rotate the bullet image
        new_rect = rotated_bullet_img.get_rect(center=enemy_bullet_img.get_rect(topleft=(bullet_pos[0], bullet_pos[1])).center)  # Adjust the bullet position after rotation
        screen.blit(rotated_bullet_img, new_rect.topleft)

# Define a function to move the enemy bullets
def move_enemy_bullets():
    for bullet_pos in enemy_bullets:
        bullet_pos[1] += enemy_bullet_speed
        bullet_pos[2] += 10  

# Define a function for the enemies to shoot
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

# Define a function to check for collisions between enemy bullets and the player
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

# Define a function to reset the player position
def reset_player_position():
    global player_x
    player_x = WIDTH // 2 - player_size // 2

# Define a function to spawn a single enemy
def spawn_enemy():
    global enemies
    enemy_x = random.randint(0, WIDTH - enemy_size)
    enemy_y = random.randint(50, 200)
    for existing_enemy in enemies:
        distance = ((existing_enemy[0] - enemy_x) ** 2 + (existing_enemy[1] - enemy_y) ** 2) ** 0.5
        if distance < enemy_size * 1.5:  
            return spawn_enemy()
    enemies.append([enemy_x, enemy_y])

# Define a function to spawn multiple enemies
def spawn_enemies():
    global enemies
    enemies.clear()
    for _ in range(num_enemies):
        spawn_enemy()

# Call the function to spawn enemies
spawn_enemies()

# Main game loop
while running:
    # Loop for gameplay
    while not game_over:
        # Fill the screen with a black background
        screen.fill(BLACK)

        # Event handling loop
        for event in pygame.event.get():
            # Check if the user wants to quit
            if event.type is pygame.QUIT:
                game_over = True
            # Check for key presses
            elif event.type == pygame.KEYDOWN:
                # Check if 'x' key is pressed to quit the game
                if event.key == pygame.K_x:
                    game_over = True
                # Check if 'y' key is pressed to play again
                elif event.key == pygame.K_y and game_over:
                    reset_game()
                # Check if 'n' key is pressed to quit the game
                elif event.key == pygame.K_n and game_over:
                    pygame.quit()
                    sys.exit()

        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_SPACE] and bullet_state == "ready":
            bullet_rect.midtop = (player_x + player_size // 2, player_y)
            fire_bullet(*bullet_rect.midtop)

        # Bound the player within the screen
        if player_x <= 0:
            player_x = 0
        elif player_x >= WIDTH - player_size:
            player_x = WIDTH - player_size

        # Handle enemy behavior
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

        # Handle bullet movement and collisions
        if bullet_state == "fire":
            screen.blit(bullet_img, bullet_rect)
            bullet_rect.y -= bullet_speed
            pygame.mixer.Sound.play(fire)
            if bullet_rect.y <= 0:
                bullet_state = "ready"

        # Enemy shooting logic
        current_time = pygame.time.get_ticks()
        if current_time - enemy_shoot_timer >= enemy_shoot_interval:
            enemy_shoot()
            enemy_shoot_timer = current_time

        move_enemy_bullets()
        check_bullet_collision()

        # Draw game elements on the screen
        player(player_x, player_y)
        show_score(text_x, text_y)
        show_lives(WIDTH - 150, text_y, player_lives)
        draw_enemy_bullets()

        # Update the display
        pygame.display.flip()
        clock.tick(60)

    # Loop for game over screen
    while game_over:
        # Event handling loop
        for event in pygame.event.get():
            # Check if the user wants to quit
            if event.type is pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Check for key presses
            elif event.type == pygame.KEYDOWN:
                # Check if 'y' key is pressed to play again
                if event.key == pygame.K_y:
                    reset_game()
                    game_over = False
                # Check if 'n' key is pressed to quit the game
                elif event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()

        # Fill the screen with a black background
        screen.fill(BLACK)
        # Display the game over screen
        show_game_over(score_value)
        # Update the display
        pygame.display.flip()
        clock.tick(60)

# Quit pygame and exit the program
pygame.quit()
sys.exit()