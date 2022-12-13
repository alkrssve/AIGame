import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
 
# Set the width and height of the screen [width,height]
size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h))
 
pygame.display.set_caption("Crazy Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Define the variables
x_coord = 50
y_coord = 50
red_x_coord = 900
red_y_coord = 900
x_change = 0
y_change = 0
 
# Define the speed of the game
speed = 10
 
# Define the speed of the red circle
red_speed = 5

# Generate a random number
random_num = random.randint(0,100)

# create a simple font
font = pygame.font.SysFont("georgia", 72)

# set window caption
pygame.display.set_caption("Game Over Press 'r' to restart")

# create a text surface
text = font.render("Game Over! Press 'r' to Restart", True, (0, 0, 0))

# set the center of the text surface
textRect = text.get_rect()
textRect.center = (950, 450)

# Create a score variable
score = 0

score_text = font.render(f'Score: {score}', True, (0, 0, 0))

over = False

# create a list of obstacles
obstacles = []

# create obstacles and add them to the obstacles list
for i in range(15):
    x = random.randint(0,1600)
    y = random.randint(0,1200)
    obstacles.append(pygame.Rect(x, y, 50, 50))
 
# Create a loop to keep the game running
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r: 
                pygame.quit()
                pygame.init()
                screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h))
                clock = pygame.time.Clock()
                running = True
                speed = 10
                x_coord = 50
                y_coord = 50
                red_x_coord = 900
                red_y_coord = 900
                score = 0
                over = False
                # create a simple font
                font = pygame.font.SysFont("georgia", 72)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
        if event.type == pygame.QUIT:
            done = True
 
        # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_change = -speed
            elif event.key == pygame.K_RIGHT:
                x_change = speed
            elif event.key == pygame.K_UP:
                y_change = -speed
            elif event.key == pygame.K_DOWN:
                y_change = speed
 
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0
 
    # --- Game logic should go here
    # Move the object according to the speed vector.
    x_coord = x_coord + x_change
    y_coord = y_coord + y_change
 
    # Check if the ball is at the side of the screen
    if x_coord > size[0] - 25 or x_coord < 0:
        x_change = x_change * -1
 
    if y_coord > size[1] - 25 or y_coord < 0:
        y_change = y_change * -1
 
    # Generate a random number if the ball reaches a certain position
    if x_coord == random_num and y_coord == random_num:
        random_num = random.randint(0,100)
 
    # Move the red circle towards the player
    if x_coord > red_x_coord:
        red_x_coord += red_speed
    elif x_coord < red_x_coord:
        red_x_coord -= red_speed
    if y_coord > red_y_coord:
        red_y_coord += red_speed
    elif y_coord < red_y_coord:
        red_y_coord -= red_speed
 
    # --- Drawing code should go here

    if not over:
        # Increase the score by 1 every tick
        score += 1
        # Render the score
        score_text = font.render(f'Score: {score}', True, (0, 0, 0))
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
 
    # Draw the ball
    player = pygame.draw.circle(screen, BLACK, [x_coord, y_coord], 25)
    # Draw the red circle
    enemy = pygame.draw.circle(screen, RED, [red_x_coord, red_y_coord], 25)

    # draw the obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLACK, obstacle)

    # Render the score onto the screen
    screen.blit(score_text, (10, 10))
    
    # check if circless overlap
    if player.colliderect(enemy):
        # draw text surface
        screen.blit(text, textRect)
        speed = 0
        over = True
    for obstacle in obstacles:
        # check if circless overlap
        if player.colliderect(obstacle):
            x_coord = 0
            y_coord = 0

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()