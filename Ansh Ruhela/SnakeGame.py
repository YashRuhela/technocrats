import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake variables
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = (0, -1)  # Snake initially moves up
initial_speed = 5  # Initial snake speed
max_speed = 15  # Maximum allowed speed
speed_increment = 0.2  # Speed increment per eaten food

# Initialize the speed
snake_speed = initial_speed

# Food variables
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Game over flag
game_over = False

# Score
score = 0

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # Move the snake
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, new_head)

    # Check for collisions with the food
    if snake[0] == food:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        score += 1
        snake_speed = min(max_speed, snake_speed + speed_increment)

    else:
        snake.pop()

    # Check for collisions with the wall or itself
    if (
        snake[0][0] < 0
        or snake[0][0] >= GRID_WIDTH
        or snake[0][1] < 0
        or snake[0][1] >= GRID_HEIGHT
        or snake[0] in snake[1:]
    ):
        #game_over = True


        game_over = True

        # Display game over message and score
        font = pygame.font.Font(None, 48)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        play_again_text = font.render("Play Again? (Y/N)", True, (0, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
        screen.blit(score_text, (WIDTH // 2 - 50, HEIGHT // 2))
        screen.blit(play_again_text, (WIDTH // 2 - 120, HEIGHT // 2 + 50))
        pygame.display.update()

        # Wait for user input to play again or exit
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        # Play again
                        snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
                        snake_direction = (0, -1)
                        snake_speed = initial_speed
                        score = 0
                        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
                        game_over = False
                        waiting_for_input = False
                    elif event.key == pygame.K_n:
                        # Exit the game
                        game_over = True
                        waiting_for_input = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the food
    pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

    # Control game speed
    pygame.time.delay(int(1000 // snake_speed))

# Quit Pygame
pygame.quit()
sys.exit()
