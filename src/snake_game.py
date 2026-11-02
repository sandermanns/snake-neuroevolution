import pygame
import random

# ---------- Settings ----------
width, height = 600, 600   # Window size in pixels
block_size = 20            # Size of one grid square (snake segment / food)

teleport_walls = True      # True = snake wraps around the edges, False = walls kill you

# ---------- Initialize pygame ----------
pygame.init()
pygame.font.init()
score_font = pygame.font.SysFont("consolas", 20)
score = 0

# Colors (RGB)
snake_green = (172,225,175)
green = (0, 128, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Window and clock
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()   # Used to limit the frame rate

# ---------- Game state ----------
snake_pos = [[width // 2, height // 2]]   # List of [x, y] segments, head first
snake_speed = [0, block_size]             # [dx, dy] per frame, starts moving down


def generate_food():
    """Pick a random grid position that is not on top of the snake."""
    while True:
        x = random.randint(0, (width - block_size) // block_size) * block_size
        y = random.randint(0, (height - block_size) // block_size) * block_size
        food_pos = [x, y]
        if food_pos not in snake_pos:
            return food_pos


food_pos = generate_food()


def draw_objects():
    """Draw the snake, the food and the score."""
    win.fill((172,225,175))   # Clear the screen with black

    # Draw every snake segment
    for pos in snake_pos:
        pygame.draw.rect(win, green, pygame.Rect(pos[0], pos[1], block_size, block_size))

    # Draw the food
    # FIX: was pos[1] (leftover variable from the loop above), should be food_pos[1]
    pygame.draw.rect(win, red, pygame.Rect(food_pos[0], food_pos[1], block_size, block_size))

    # Draw the score in the top left corner
    score_text = score_font.render(f"Score: {score}", True, white)
    win.blit(score_text, (10, 10))


def update_snake():
    """Move the snake one step, handle wall wrapping, eating and growing."""
    global food_pos, score

    new_head = [snake_pos[0][0] + snake_speed[0],
                snake_pos[0][1] + snake_speed[1]]

    # If the head leaves the screen, wrap it to the opposite side
    if teleport_walls:
        if new_head[0] >= width:
            new_head[0] = 0
        elif new_head[0] < 0:
            new_head[0] = width - block_size
        if new_head[1] >= height:
            new_head[1] = 0           
        elif new_head[1] < 0:
            new_head[1] = height - block_size

    # FIX: everything below was indented under "if teleport_walls:",
    # so the snake only moved/ate when teleporting was on. Now it always runs.
    if new_head == food_pos:
        food_pos = generate_food()   # Eaten: new food, snake grows (no pop)
        score += 1
    else:
        snake_pos.pop()              # Not eaten: remove the tail so length stays the same

    snake_pos.insert(0, new_head)    # Add the new head at the front


def game_over():
    """Return True if the snake has died."""
    if teleport_walls:
        # Only dying by hitting yourself
        return snake_pos[0] in snake_pos[1:]
    else:
        # Hitting yourself OR leaving the screen
        return (snake_pos[0] in snake_pos[1:] or
                snake_pos[0][0] > width - block_size or
                snake_pos[0][0] < 0 or
                snake_pos[0][1] > height - block_size or
                snake_pos[0][1] < 0)


def game_over_screen():
    """Show the game over text and wait for R (restart) or Q (quit)."""
    win.fill((0, 0, 0))
    game_over_font = pygame.font.SysFont("consolas", 50)
    game_over_text = game_over_font.render(f"Game Over! Score: {score}", True, white)
    win.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2,
                              height // 2 - game_over_text.get_height() // 2))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    run()            # Replay the game
                    return
                elif event.key == pygame.K_q:
                    pygame.quit()    # Quit the game
                    return


def run():
    """Main game loop."""
    global snake_speed, snake_pos, food_pos, score

    # Reset the game state
    snake_pos = [[width // 2, height // 2]]
    snake_speed = [0, block_size]
    food_pos = generate_food()
    score = 0

    running = True
    while running:
        # --- Handle input (events) ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Each direction is ignored if it would reverse the snake into itself
                if event.key == pygame.K_w and snake_speed[1] != block_size:
                    snake_speed = [0, -block_size]
                elif event.key == pygame.K_s and snake_speed[1] != -block_size:
                    snake_speed = [0, block_size]
                elif event.key == pygame.K_a and snake_speed[0] != block_size:
                    snake_speed = [-block_size, 0]
                elif event.key == pygame.K_d and snake_speed[0] != -block_size:
                    snake_speed = [block_size, 0]

        # FIX: everything below was indented inside the event loop, so the game
        # only advanced when an event happened. Now it runs once per frame.
        if game_over():
            game_over_screen()
            return

        update_snake()
        draw_objects()
        pygame.display.update()
        clock.tick(10)   # Limit to 15 frames per second (controls snake speed)


if __name__ == '__main__':
    run()
    pygame.quit() 

                
        
        



