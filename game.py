import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up the game
done = False
clock = pygame.time.Clock()

# Set up the player
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5

# Set up the enemy
enemy_x = random.randint(0, SCREEN_WIDTH)
enemy_y = random.randint(0, SCREEN_HEIGHT)
enemy_speed = 3

# Game loop
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Update the player position
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Update the enemy position
    if enemy_x > player_x:
        enemy_x -= enemy_speed
    else:
        enemy_x += enemy_speed
    if enemy_y > player_y:
        enemy_y -= enemy_speed
    else:
        enemy_y += enemy_speed

    # Draw the player and enemy
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (player_x, player_y), 10)
    pygame.draw.circle(screen, (0, 0, 255), (enemy_x, enemy_y), 10)

    # Update the screen
    pygame.display.flip()
    clock.tick(60)

# Clean up
pygame.quit()