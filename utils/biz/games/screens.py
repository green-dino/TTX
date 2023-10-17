import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Bars")

# Bar properties
bars = []
BAR_WIDTH = 50
BAR_HEIGHT = 10
DEFAULT_BAR_COLOR = (255, 0, 0)

# Sliders
velocity_x_slider = pygame.Rect(50, 50, 200, 10)
velocity_y_slider = pygame.Rect(50, 70, 200, 10)

# Color selection buttons
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
color_buttons = [pygame.Rect(300 + i * 50, 50, 40, 20) for i in range(len(COLORS))]

# Add a new bar button
add_bar_button = pygame.Rect(50, 100, 100, 30)

# Delete the last bar button
delete_bar_button = pygame.Rect(200, 100, 100, 30)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            # Check if a color button was clicked
            for i, button in enumerate(color_buttons):
                if button.collidepoint(mouse_x, mouse_y):
                    bars[-1]["color"] = COLORS[i]
                    
            # Add a new bar
            if add_bar_button.collidepoint(mouse_x, mouse_y):
                new_bar = {
                    "x": random.randint(0, WIDTH - BAR_WIDTH),
                    "y": random.randint(0, HEIGHT - BAR_HEIGHT),
                    "velocity_x": 3,
                    "velocity_y": 3,
                    "color": DEFAULT_BAR_COLOR,
                }
                bars.append(new_bar)
                
            # Delete the last bar
            if delete_bar_button.collidepoint(mouse_x, mouse_y) and bars:
                bars.pop()

    # Check for slider input
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if velocity_x_slider.collidepoint(mouse_x, mouse_y):
            bars[-1]["velocity_x"] = (mouse_x - velocity_x_slider.left) / velocity_x_slider.width * 6 - 3
        elif velocity_y_slider.collidepoint(mouse_x, mouse_y):
            bars[-1]["velocity_y"] = (mouse_x - velocity_y_slider.left) / velocity_y_slider.width * 6 - 3

    # Move and bounce bars
    for bar in bars:
        bar["x"] += bar["velocity_x"]
        bar["y"] += bar["velocity_y"]

        if bar["x"] < 0 or bar["x"] + BAR_WIDTH > WIDTH:
            bar["velocity_x"] *= -1
        if bar["y"] < 0 or bar["y"] + BAR_HEIGHT > HEIGHT:
            bar["velocity_y"] *= -1

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw bars
    for bar in bars:
        pygame.draw.rect(screen, bar["color"], (bar["x"], bar["y"], BAR_WIDTH, BAR_HEIGHT))

    # Draw sliders
    pygame.draw.rect(screen, WHITE, velocity_x_slider)
    pygame.draw.rect(screen, WHITE, velocity_y_slider)

    # Draw color selection buttons
    for i, button in enumerate(color_buttons):
        pygame.draw.rect(screen, COLORS[i], button)

    # Add a new bar button
    pygame.draw.rect(screen, (0, 255, 0), add_bar_button)
    pygame.draw.rect(screen, WHITE, add_bar_button, 2)
    font = pygame.font.Font(None, 36)
    text = font.render("Add Bar", True, WHITE)
    screen.blit(text, (60, 105))

    # Delete the last bar button
    pygame.draw.rect(screen, (255, 0, 0), delete_bar_button)
    pygame.draw.rect(screen, WHITE, delete_bar_button, 2)
    text = font.render("Delete Bar", True, WHITE)
    screen.blit(text, (210, 105))

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    pygame.time.delay(10)

# Quit Pygame
pygame.quit()
