import pygame
import time
import random
import psycopg2

# Initialize database connection
def initialize_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="aliya1907",
            port="5432"
        )
        cur = conn.cursor()
        return conn, cur
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)

# Create table if not exists
def create_user_table(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS snake_scores (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE,
            user_score INTEGER DEFAULT 0
        )
    """)

# Update user score in database
def update_user_score(cur, conn, username, score):
    cur.execute("SELECT * FROM snake_scores WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        cur.execute("UPDATE snake_scores SET user_score = GREATEST(user_score, %s) WHERE username = %s", (score, username))
    else:
        cur.execute("INSERT INTO snake_scores (username, user_score) VALUES (%s, %s)", (username, score))
    conn.commit()

# Get user's current score
def get_user_score(cur, username):
    cur.execute("SELECT user_score FROM snake_scores WHERE username = %s", (username,))
    user_score = cur.fetchone()
    return user_score[0] if user_score else 0

# Show current user level
def show_user_level(username, cur, conn):
    score = get_user_score(cur, username)
    print(f"Welcome back, {username}! Your current level is {score // 10}.")
    return score

# Initialize database
conn, cur = initialize_db()
create_user_table(cur)

# Get username
username = input("Enter your username: ")
score = show_user_level(username, cur, conn)

# Game setup
pygame.init()
pygame.display.set_caption('Snake Game')
window_x, window_y = 700, 700
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Snake settings
snake_position = [100, 50]
snake_body = [[100, 50]]
fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True
direction = 'RIGHT'
change_to = direction
snake_speed = 10 + (score // 10)

# Show score on screen
def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f'Score: {score}', True, color)
    game_window.blit(score_surface, (10, 10))

# Game over function
def game_over():
    global score
    update_user_score(cur, conn, username, score)
    font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = font.render(f'Game Over! Your Score: {score}', True, red)
    game_over_rect = game_over_surface.get_rect(center=(window_x // 2, window_y // 2))
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Start game loop
def start_game():
    global snake_position, snake_body, fruit_position, fruit_spawn, direction, change_to, score, snake_speed
    start_font = pygame.font.SysFont('times new roman', 50)
    start_surface = start_font.render("Press 'S' to Start", True, green)
    game_window.fill(black)
    game_window.blit(start_surface, (window_x // 4, window_y // 2))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                return

start_game()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
    
    direction = change_to
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake growing and scoring
    snake_body.insert(0, list(snake_position))
    if snake_position == fruit_position:
        score += 1
        fruit_spawn = False
        snake_speed += 0.1
    else:
        snake_body.pop()
    
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True

    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Game over conditions
    if (snake_position[0] < 0 or snake_position[0] >= window_x or
            snake_position[1] < 0 or snake_position[1] >= window_y):
        game_over()
    for block in snake_body[1:]:
        if snake_position == block:
            game_over()

    show_score(white, 'times new roman', 20)
    pygame.display.update()
    fps.tick(snake_speed)
