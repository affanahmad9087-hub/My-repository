import pygame
import random

# 1. INITIALIZATION
pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Prototype")
CLOCK = pygame.time.Clock()

# Physics & Game Constants
GRAVITY = 0.4
FLAP_STRENGTH = -7
PIPE_SPEED = 4
PIPE_GAP = 180
PIPE_FREQUENCY = 1500

SCORE_FONT = pygame.font.SysFont("Dubai", 50, bold=True)
INFO_FONT = pygame.font.SysFont("Dubai", 30)

# 2. FUNCTIONS
def spawn_pipe():
    gap_y = random.randint(200, HEIGHT - 200)
    bottom_rect = pygame.Rect(WIDTH, gap_y + (PIPE_GAP // 2), 60, HEIGHT)
    top_rect = pygame.Rect(WIDTH, 0, 60, gap_y - (PIPE_GAP // 2))
    return {"bottom": bottom_rect, "top": top_rect, "passed": False}

def reset_game():
    """Resets all variables for a new round."""
    return 100, HEIGHT // 2, 0, 0, [spawn_pipe()], pygame.time.get_ticks(), False

# 3. INITIAL VARIABLES
bird_x, bird_y, bird_vel, score, pipes, last_pipe_time, game_over = reset_game()
high_score = 0

# 4. MAIN GAME LOOP
running = True
while running:
    # --- A. EVENT HANDLING ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bird_vel = FLAP_STRENGTH
            
            # Restart the game if R is pressed after dying
            if event.key == pygame.K_r and game_over:
                bird_x, bird_y, bird_vel, score, pipes, last_pipe_time, game_over = reset_game()

            if event.key == pygame.K_ESCAPE and game_over:
                running = False

    # --- B. PHYSICS & LOGIC ---
    if not game_over:
        # Bird Movement
        bird_vel += GRAVITY
        bird_y += bird_vel

        # Pipe Spawning
        current_time = pygame.time.get_ticks()
        if current_time - last_pipe_time > PIPE_FREQUENCY:
            pipes.append(spawn_pipe())
            last_pipe_time = current_time

        # Pipe Movement and Scoring
        for p in pipes:
            p["bottom"].x -= PIPE_SPEED
            p["top"].x -= PIPE_SPEED

            if not p["passed"] and bird_x > p["bottom"].right:
                score += 1
                p["passed"] = True

        # Remove off-screen pipes
        if len(pipes) > 0 and pipes[0]["bottom"].right < 0:
            pipes.pop(0)

        # --- C. COLLISION DETECTION ---
        bird_rect = pygame.Rect(bird_x - 15, bird_y - 15, 30, 30)
        
        # Check pipes, ground, and ceiling
        hit_pipe = any(bird_rect.colliderect(p["bottom"]) or bird_rect.colliderect(p["top"]) for p in pipes)
        hit_bounds = bird_y > HEIGHT or bird_y < 0

        if hit_pipe or hit_bounds:
            game_over = True
            if score > high_score:
                high_score = score

    # --- D. DRAWING ---
    screen.fill((30, 30, 30))

    for p in pipes:
        pygame.draw.rect(screen, (0, 200, 0), p["bottom"])
        pygame.draw.rect(screen, (0, 200, 0), p["top"])

    pygame.draw.circle(screen, (255, 0, 0), (int(bird_x), int(bird_y)), 20)

    # UI Elements
    score_surf = SCORE_FONT.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_surf, (WIDTH // 2 - score_surf.get_width()//2, 50))

    if game_over:
        # Dim the screen slightly
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0,0))
        
        # Show Game Over Text
        msg = INFO_FONT.render(f"GAME OVER! High Score: {high_score}", True, (255, 255, 255))
        retry = INFO_FONT.render("Press 'R' to Restart and 'esc' to Exit", True, (200, 200, 200))
        screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - 20))
        screen.blit(retry, (WIDTH//2 - retry.get_width()//2, HEIGHT//2 + 30))

    pygame.display.flip()
    CLOCK.tick(60)

pygame.quit()