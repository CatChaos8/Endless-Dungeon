import pygame
import sys
import os
import time
# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Genius Battle")

# Choose the font to set up the text
# Load fonts from assets/fonts folder
fonts_dir = os.path.join(os.path.dirname(__file__), 'assets', 'fonts')
font_title = pygame.font.Font(os.path.join(fonts_dir, 'PressStart2P-Regular.ttf'), 20)
font_menu = pygame.font.Font(os.path.join(fonts_dir, 'PressStart2P-Regular.ttf'), 16)


def render_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Create the level count
level_count = int(1)    
level_count_str = str(level_count)

# Load player image
assets_dir = os.path.join(os.path.dirname(__file__), 'assets')

player_image = pygame.image.load(os.path.join(assets_dir, 'player.png'))
scale_factor = 10  # You can adjust this scale factor as needed
player_image = pygame.transform.scale(player_image, (player_image.get_width() * scale_factor, player_image.get_height() * scale_factor))

menu_image = pygame.image.load(os.path.join(assets_dir, 'menu.png'))
menu_scale_factor = 10
menu_image = pygame.transform.scale(menu_image, (menu_image.get_width() * menu_scale_factor, menu_image.get_height() * menu_scale_factor * 0.75)) #Short height

enemy1_image = pygame.image.load(os.path.join(assets_dir, 'enemy1.png'))
enemy1_scale_factor = 10
enemy1_image = pygame.transform.scale(enemy1_image, (enemy1_image.get_width() * enemy1_scale_factor, enemy1_image.get_height() * enemy1_scale_factor)) #Short height


arrow = pygame.image.load(os.path.join(assets_dir, 'arrow.png'))
arrow_scale_factor = 5
arrow = pygame.transform.scale(arrow, (arrow.get_width() * arrow_scale_factor, arrow.get_height() * arrow_scale_factor)) #Short height

# Get the dimensions of the scaled player image to center it
player_width, player_height = player_image.get_size() 

# Put player image at the bottom right
player_x = screen_width - player_width
player_y = screen_height - player_height - 150 #150 higher than bottom

#Base Stats:
max_health = int(15)
health = int(15)
health_percent = float(health/max_health)
melee_dmg = int(5)
crit_chance = float(0.1)
crit_amp = float(1.5)
poison_dmg = int(2)
heal_amount = int(1)


# Attack Descriptions and dammage
headshot_dmg = str(melee_dmg+7)
kick_dmg = str(melee_dmg+3)
toxic_dmg = str(poison_dmg+7)
rest_heal = str(heal_amount + 2)


headshot_description1 = str("Has 20% accuracy and deals ")
headshot_description2 = str(headshot_dmg + " damage when it hits.")

kick_description1 = str("Has 95% accuracy and deals ")
kick_description2 = str(kick_dmg +" damage when it hits.")

toxic_description1 = str("Has 70% accuracy and deals ")
toxic_description2 = str("toxic")
toxic_description3 = str("does " + toxic_dmg + " every turn for")
toxic_description4 = str("3 turns")

rest_description1 = str("Has a 70% chance to ")
rest_description2 = str("activate and heal the user")
rest_description3 = str("by "+ rest_heal +" health when used in")                        
rest_description4 = str("succession.")   
selected_action = 1

# Main game loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))  # WhiteBG
    # Menu box
    screen.blit(menu_image, (0, 300))
    #PLayer
    screen.blit(player_image, (525, 100))
    screen.blit(enemy1_image, (25, 25))
    
    render_text(level_count_str, font_title, (0, 0, 0), 760, 20)
    
    #Create the arrow and descreption
    
    if selected_action == 1: #Headshot
        
        screen.blit(arrow, (0, 470))
        arrow_location = (0,470)
        render_text(headshot_description1, font_menu, (255, 255, 255), 375, 500)
        render_text(headshot_description2, font_menu, (255, 255, 255), 375, 525)
        print(selected_action)
        
    elif selected_action == 2: #Toxic
       
        screen.blit(arrow, (195, 470))
        render_text(toxic_description1, font_menu, (255, 255, 255), 375, 475)
        render_text(toxic_description2, font_menu, (255, 255, 255), 375, 500)
        render_text(toxic_description3, font_menu, (255, 255, 255), 375, 525)
        render_text(toxic_description4, font_menu, (255, 255, 255), 375, 550)
        print(selected_action)
        
    elif selected_action == 3: #Kick

        screen.blit(arrow, (0, 535))
        render_text(kick_description1, font_menu, (255, 255, 255), 375, 500)
        render_text(kick_description2, font_menu, (255, 255, 255), 375, 525)
        print(selected_action)
        
    elif selected_action == 4: #Rest
        
        screen.blit(arrow, (195, 535))
        render_text(rest_description1, font_menu, (255, 255, 255), 375, 475)
        render_text(rest_description2, font_menu, (255, 255, 255), 375, 500)
        render_text(rest_description3, font_menu, (255, 255, 255), 375, 525)
        render_text(rest_description4, font_menu, (255, 255, 255), 375, 550)
        print(selected_action)


    #Write text
    render_text("Genius Battle", font_title, (0, 0, 0), 300, 100)
    render_text("1 Headshot", font_menu, (255, 255, 255), 30, 475) #Action 1
    render_text("3 Kick", font_menu, (255, 255, 255), 30, 540)     #Action 2
    render_text("2 Toxic", font_menu, (255, 255, 255), 230, 475)   #Action 3
    render_text("4 Rest", font_menu, (255, 255, 255), 230, 540)    #Action 4

    #Health Bar
    health_bar_length = 400*health_percent
    health_percent = float(health/max_health)
    health_fraction = str(health) + "/" + str(max_health)
    if health_percent > 1:
        health_percent = 1
    if health_percent <=0 :
        health_percent = 0
        health = 15
    health_color = ((255-(255*health_percent)),(255*health_percent),0)
    
    pygame.draw.rect(screen, health_color, (5, 397, health_bar_length, 25))

    pygame.display.flip()
    
    time.sleep(0.05)
    pressed_key = pygame.key.get_pressed()
    
    

    if pressed_key[pygame.K_1]:
        selected_action = 1
    elif pressed_key[pygame.K_2]:#s is pressed
        selected_action = 2
    elif pressed_key[pygame.K_3]:#a is pressed
        selected_action = 3
    elif pressed_key[pygame.K_4]:#d is pressed
        selected_action = 4
    if pressed_key[pygame.K_w]:
        if selected_action == 4:
            selected_action = 2
        elif selected_action == 3:
            selected_action = 1
        elif selected_action == 1:
            selected_action = 3
        elif selected_action == 2:
            selected_action = 4
    if pressed_key[pygame.K_s]:
        if selected_action == 4:
            selected_action = 2
        elif selected_action == 3:
            selected_action = 1
        elif selected_action == 1:
            selected_action = 3
        elif selected_action == 2:
            selected_action = 4
    if pressed_key[pygame.K_a]:
        if selected_action == 4:
            selected_action = 3
        elif selected_action == 3:
            selected_action = 4
        elif selected_action == 1:
            selected_action = 2
        elif selected_action == 2:
            selected_action = 1
    if pressed_key[pygame.K_d]:
        if selected_action == 4:
            selected_action = 3
        elif selected_action == 3:
            selected_action = 4
        elif selected_action == 1:
            selected_action = 2
        elif selected_action == 2:
            selected_action = 1
        







# Quit Pygame
pygame.quit()
sys.exit()
