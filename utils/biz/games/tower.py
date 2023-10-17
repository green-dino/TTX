import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense")

# Player attributes
player_health = 10
player_score = 0

# Enemy attributes
enemies = []
enemy_speed = 1
enemy_spawn_interval = 100  # Lower values mean faster spawn
enemy_spawn_counter = 0

# Tower attributes
towers = []
tower_cost = 20

# Fonts
font = pygame.font.Font(None, 36)

def draw_text(text, x, y):
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))

def spawn_enemy():
    enemy = pygame.Rect(0, random.randint(50, HEIGHT - 50), 30, 30)
    enemies.append(enemy)

def draw_game():
    screen.fill((0, 0, 0))
    
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)
    
    for tower in towers:
        pygame.draw.rect(screen, GREEN, tower)
    
    draw_text(f"Health: {player_health}", 10, 10)
    draw_text(f"Score: {player_score}", 10, 50)
    
    pygame.display.flip()

def place_tower(x, y):
    if player_score >= tower_cost:
        if x < WIDTH - 50:  # Prevent placing towers on UI area
            tower = pygame.Rect(x, y, 20, 40)
            towers.append(tower)
            player_score -= tower_cost

def move_enemies():
    for enemy in enemies:
        enemy.x += enemy_speed

def check_collisions():
    for tower in towers:
        for enemy in enemies:
            if tower.colliderect(enemy):
                enemies.remove(enemy)
                player_score += 1

def remove_off_screen_enemies():
    global enemies
    enemies = [enemy for enemy in enemies if enemy.x < WIDTH]

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            place_tower(x, y)
    
    enemy_spawn_counter += 1
    if enemy_spawn_counter >= enemy_spawn_interval:
        spawn_enemy()
        enemy_spawn_counter = 0
    
    move_enemies()
    check_collisions()
    remove_off_screen_enemies()
    
    if player_health <= 0:
        pygame.quit()
        sys.exit()
    
    draw_game()
    
    clock.tick(60)
