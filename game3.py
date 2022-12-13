import pygame
import random

pygame.init()

# Set window size and title, and frame rate
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption('My Complex Game')
FPS = 60

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Clock used to update game events and frames
clock = pygame.time.Clock() 

# Create player
player_width = 50
player_height = 50
playerX = win_width/2 - player_width/2
playerY = win_height - player_height
playerX_change = 0

# Create enemies
enemy_width = 50
enemy_height = 50
enemyX = random.randint(0, win_width - enemy_width)
enemyY = 0
enemyX_change = 0.3
enemyY_change = 5

# Create powerups
powerup_width = 30
powerup_height = 30
powerupX = random.randint(0, win_width - powerup_width)
powerupY = 0
powerupX_change = 0.2
powerupY_change = 3

# Score
score = 0

# Create player and enemies
playerImg = pygame.image.load('player.png')
enemyImg = pygame.image.load('obstacle.png')
powerupImg = pygame.image.load('player.png')

def player(x,y):
    win.blit(playerImg, (x,y))

def enemy(x,y):
    win.blit(enemyImg, (x,y))

def powerup(x,y):
    win.blit(powerupImg, (x,y))

def show_score(score):
    font = pygame.font.SysFont('comicsans', 20)
    score_text = font.render("Score: " + str(score), True, BLACK)
    win.blit(score_text, (10,10))

# Main loop
run = True
while run:
    clock.tick(FPS)

    # Quit game if quit button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Keystroke logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and playerX > 0:
        playerX_change = -3
    elif keys[pygame.K_RIGHT] and playerX < win_width - player_width:
        playerX_change = 3
    else:
        playerX_change = 0

    # Update player position
    playerX += playerX_change

    # Update enemy position
    enemyX += enemyX_change
    if enemyX <= 0 or enemyX >= win_width - enemy_width:
        enemyX_change *= -1
    enemyY += enemyY_change

    # Update powerup position
    powerupX += powerupX_change
    if powerupX <= 0 or powerupX >= win_width - powerup_width:
        powerupX_change *= -1
    powerupY += powerupY_change

    # Collision logic
    if playerX < enemyX + enemy_width and playerX + player_width > enemyX and playerY < enemyY + enemy_height and playerY + player_height > enemyY:
        score += 1
        enemyX = random.randint(0, win_width - enemy_width)
        enemyY = 0

    if playerX < powerupX + powerup_width and playerX + player_width > powerupX and playerY < powerupY + powerup_height and playerY + player_height > powerupY:
        score += 5
        powerupX = random.randint(0, win_width - powerup_width)
        powerupY = 0

    # Fill background
    win.fill(WHITE)
    # Draw player and enemy
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    powerup(powerupX,powerupY)
    # Show score
    show_score(score)
    # Update game window
    pygame.display.update()

# Quit game
pygame.quit()