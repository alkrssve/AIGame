import pygame

# Initialize Pygame
pygame.init()

# Set the window size
width = 800
height = 600
screen = pygame.display.set_mode([width, height])

# Set the title
pygame.display.set_caption("Gravity Tank")

# Set the clock
clock = pygame.time.Clock()

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the position and speed of the tank
tank_x = width // 2
tank_y = height // 2
tank_speed = 5

# Set the gravity
gravity = 1

# Set the platform positions
platform_top_x = 0
platform_top_y = 0
platform_bottom_x = 0
platform_bottom_y = height

# Create a game loop
done = False
while not done:
    # Process user inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                tank_x -= tank_speed
            elif event.key == pygame.K_RIGHT:
                tank_x += tank_speed
            elif event.key == pygame.K_SPACE:
                # Switch the gravity
                gravity *= -1
            
    # Update the game
    if gravity == 1:
        tank_y += 5
    else:
        tank_y -= 5
    
    # Keep the tank on the screen
    if tank_x > width:
        tank_x = 0
    elif tank_x < 0:
        tank_x = width
    if tank_y > height:
        tank_y = 0
    elif tank_y < 0:
        tank_y = height
    
    # Check if the tank is on the platform
    if gravity == 1 and tank_y == platform_top_y:
        tank_y = platform_top_y
    elif gravity == -1 and tank_y == platform_bottom_y:
        tank_y = platform_bottom_y
    
    # Draw everything
    screen.fill((0,255,0))
    pygame.draw.rect(screen, WHITE, [platform_top_x, platform_top_y, width, 10])
    pygame.draw.rect(screen, WHITE, [platform_bottom_x, platform_bottom_y, width, 10])
    pygame.draw.rect(screen, WHITE, [tank_x, tank_y, 20, 20])
    pygame.display.flip()
    
    # Limit the frame rate
    clock.tick(60)
    
# Quit the game
pygame.quit()