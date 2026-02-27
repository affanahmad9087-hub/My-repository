import pygame
import random

# 1. INITIALIZATION
pygame.init()

# Set up display constants
WIDTH, HEIGHT = 960, 540
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multi-Ball Physics Engine")
clock = pygame.time.Clock()

# Physics Constants
GRAVITY = 0.5 
FRICTION = 0.99      # Slows horizontal movement slightly over time

# 2. CREATE MULTIPLE BALLS
# We store each ball as a dictionary inside a list.
balls = []
number_of_balls = 15

for i in range(number_of_balls):
    ball = {
        "x": random.randint(100, WIDTH - 100),    # Random start X
        "y": random.randint(50, 200),             # Random start Y
        "vel_x": random.uniform(-7, 7),           # Random horizontal speed
        "vel_y": random.uniform(0, 5),            # Random vertical speed
        "radius": random.randint(15, 35),         # Randomize sizes too!
        "color": (random.randint(50, 255),        # Random Red
                  random.randint(50, 255),        # Random Green
                  random.randint(50, 255)),
        "bounce_retain": random.uniform(0.6, 0.9)  # Random bounce retention (60% to 90%)
    }
    balls.append(ball)

# 3. MAIN GAME LOOP
running = True
while running:
    # A. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #check if a key was pressed down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for b in balls:
                    b["vel_x"] = random.uniform(-7, 7)  # Random horizontal speed
                    b["vel_y"] = -random.uniform(5, 10) # Random vertical speed (upwards)

            if event.key == pygame.K_ESCAPE:
                running = False

    # B. Drawing the Background
    screen.fill((30, 30, 30))  # Dark grey background
    
    # Draw static environment (Ground and Walls)
    # Ground
    pygame.draw.rect(screen, (0, 0, 255), (0, HEIGHT - 50, WIDTH, 50)) 
    # Left and Right Walls
    pygame.draw.rect(screen, (0, 0, 255), (0, 0, 50, HEIGHT)) 
    pygame.draw.rect(screen, (0, 0, 255), (WIDTH - 50, 0, 50, HEIGHT)) 

    # C. Physics and Drawing for each Ball
    for b in balls:
        # --- Apply Gravity and Movement ---
        b["vel_y"] += GRAVITY
        b["y"] += b["vel_y"]
        b["x"] += b["vel_x"]
        
        # --- Ground Collision ---
        # The ball hits the floor at (HEIGHT - 50). We factor in the ball's radius.
        if b["y"] > (HEIGHT - 50) - b["radius"]:
            b["y"] = (HEIGHT - 50) - b["radius"]
            b["vel_y"] = -b["vel_y"] * b["bounce_retain"]
            # Apply friction to horizontal movement only when touching the ground
            b["vel_x"] *= FRICTION

        # --- Wall Collisions (Left & Right) ---
        # Right wall starts at WIDTH - 50
        if b["x"] > (WIDTH - 50) - b["radius"]:
            b["x"] = (WIDTH - 50) - b["radius"]
            b["vel_x"] = -b["vel_x"] * b["bounce_retain"]

        # Left wall ends at 50
        if b["x"] < 50 + b["radius"]:
            b["x"] = 50 + b["radius"]
            b["vel_x"] = -b["vel_x"] * b["bounce_retain"]

        # --- Draw the Ball ---
        pygame.draw.circle(screen, b["color"], (int(b["x"]), int(b["y"])), b["radius"])

    # D. Refresh Display
    pygame.display.flip()
    clock.tick(60)  # Maintain 60 FPS

pygame.quit()