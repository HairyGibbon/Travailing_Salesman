"""TODO:
Add background image of London
Make it so the player can select the path
Make the guy go along the lines
Add High score system
Add Sam's google travelling salesman algorithm
Add pause menu with credits
"""

import pygame
import graph
import time

# Initialise
pygame.init()

# Create Screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))  # pixel size

# Clock
clock = pygame.time.Clock()

# Background
background = pygame.image.load("Map.png")

# Title and Icon
pygame.display.set_caption("Epic Graph Game")
icon = pygame.image.load("big_ben.png")
pygame.display.set_icon(icon)

# Player Icon
player_image = pygame.image.load("person-walking.png")


# Player Function
def player(x, y):
    screen.blit(player_image, (x, y))


# Menu Screen
def game_menu():
    pass


# Fail Screen

def fail_message(text):
    large_font = pygame.font.Font("freesansbold.ttf", 100)
    text_surf = large_font.render(text, True, (0, 0, 0))
    text_rect = text_surf.get_rect()
    text_rect.center = ((screen_width / 2), (screen_height / 2))

    screen.blit(text_surf, text_rect)

    pygame.display.update()

    time.sleep(2)


# Generating our Graph
A = graph.Graph()

A.set_coordinates((100, 100), (100, 200), (200, 100), (200, 200))
A.set_connections((0, 1, 1), (1, 2, 2), (2, 0, 4), (3, 2, 8))
print(A.get_coordinates())


def game_loop():

    player_x = 370
    player_y = 480
    player_x_change = 0
    player_y_change = 0

    # Run Game
    while True:
        for event in pygame.event.get():

            # Exiting
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Keystrokes
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -5
                if event.key == pygame.K_RIGHT:
                    player_x_change = 5
                if event.key == pygame.K_UP:
                    player_y_change = -5
                if event.key == pygame.K_DOWN:
                    player_y_change = 5
                # Fail Message
                if event.key == pygame.K_f:
                    fail_message("Fail")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_y_change = 0

        # Player Movement
        player_x += player_x_change
        player_y += player_y_change

        if player_x <= 0:
            player_x = 0
        elif player_x >= 736:
            player_x = 736

        if player_y <= 0:
            player_y = 0
        elif player_y >= 536:
            player_y = 536

        # Background
        screen.fill((54, 186, 145))  # rgb colour
        screen.blit(background, (0, 0))

        # Draw Lines
        for con in A.get_connections():
            pygame.draw.line(screen, (150, 0, 0), A.get_coordinates()[con[0]], A.get_coordinates()[con[1]], con[2])

        # Draw Circles
        for coo in A.get_coordinates():
            pygame.draw.circle(screen, (0, 0, 150), coo, 10)

        player(player_x, player_y)
        pygame.display.update()

        clock.tick(60)


game_loop()
