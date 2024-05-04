import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Battle Test")

# Choose the font to set up the text

font = pygame.font.Font(None, 36);

# Load player image
assets_dir = os.path.join(os.path.dirname(__file__), 'assets')
player_image = pygame.image.load(os.path.join(assets_dir, 'player.png'))

# Scale up the player image
scale_factor = 10  # You can adjust this scale factor as needed
player_image = pygame.transform.scale(player_image, (player_image.get_width() * scale_factor, player_image.get_height() * scale_factor))

menu_image = pygame.image.load(os.path.join(assets_dir, 'menu.png'))
menu_scale_factor = 2
menu_image = pygame.transform.scale(menu_image, (menu_image.get_width() * scale_factor, player_image.get_height() * scale_factor))
# Get the dimensions of the scaled player image
player_width, player_height = player_image.get_size()

# Position the player image at the bottom right
player_x = screen_width - player_width
player_y = screen_height - player_height

# Define box properties
box_width = 800
box_height = 150
box_x = screen_width - box_width
box_y = screen_height - box_height
box_move_up = False  # Flag to control box's movement

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the game

    # Draw everything
    screen.fill((255, 255, 255))  # Fill the screen with white
    # Draw your game elements here

    # Draw the scaled player image
    screen.blit(player_image, (player_x, player_y))

    # Draw the Menu box
    screen.blit(menu_image, (450, 0))

    pygame.display.flip()




# Quit Pygame
pygame.quit()
sys.exit()
