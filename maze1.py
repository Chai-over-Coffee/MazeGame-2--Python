import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
CELL_SIZE = 40
GRID_SIZE = WIDTH // CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

# Define maze grid (1 = path, 0 = wall)
maze = [
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
]

# Start and end points
start_pos = (0, 0)
end_pos = (9, 9)
player_pos = list(start_pos)
lives = 3

# Directions for movement
DIRECTIONS = {
    pygame.K_UP: (-1, 0),
    pygame.K_DOWN: (1, 0),
    pygame.K_LEFT: (0, -1),
    pygame.K_RIGHT: (0, 1),
}

# Function to draw grid and maze
def draw_grid():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            color = WHITE if maze[row][col] == 1 else BLACK
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, GREEN, (start_pos[1] * CELL_SIZE, start_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (end_pos[1] * CELL_SIZE, end_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to draw the player
def draw_player():
    pygame.draw.rect(screen, BLUE, (player_pos[1] * CELL_SIZE, player_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Main game loop
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and not game_over:
            if event.key in DIRECTIONS:
                move = DIRECTIONS[event.key]
                new_pos = [player_pos[0] + move[0], player_pos[1] + move[1]]

                # Check boundaries and walls
                if 0 <= new_pos[0] < GRID_SIZE and 0 <= new_pos[1] < GRID_SIZE:
                    if maze[new_pos[0]][new_pos[1]] == 1:
                        player_pos = new_pos
                    else:
                        lives -= 1
                        if lives == 0:
                            game_over = True

    # Clear the screen
    screen.fill(WHITE)

    # Draw the grid, maze, and player
    draw_grid()
    draw_player()

    # Display game over or win message
    font = pygame.font.Font(None, 36)
    if game_over:
        game_over_text = font.render("Game Over!", True, RED)
        screen.blit(game_over_text, (WIDTH // 3, HEIGHT // 2))
    elif player_pos == list(end_pos):
        win_text = font.render("You Win!", True, GREEN)
        screen.blit(win_text, (WIDTH // 3, HEIGHT // 2))
        game_over = True

    # Display lives remaining
    lives_text = font.render(f"Lives: {lives}", True, RED)
    screen.blit(lives_text, (10, 10))

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
