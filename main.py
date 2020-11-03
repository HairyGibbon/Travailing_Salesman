"""TODO:
Pause menu
Credits
Player Movement
"""

import pygame
import graph
import time
import random

# Initialise
pygame.init()

# Create Screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Clock
clock = pygame.time.Clock()

# Background
background = pygame.image.load("Map.png")

# Title and Icon
pygame.display.set_caption("Graph Game")
icon = pygame.image.load("big_ben.png")
pygame.display.set_icon(icon)

# Player Icon
player_width = 32
player_height = 32
player_image = pygame.image.load("person-walking.png")
player_image = pygame.transform.scale(player_image, (32, 32))

# Some Colours
black = (0, 0, 0)
green = (54, 186, 145)
d_green = (36, 124, 97)
b_green = (72, 248, 193)
blue = (0, 0, 150)
d_blue = (0, 0, 100)
b_blue = (0, 0, 200)
red = (150, 0, 0)
d_red = (100, 0, 0)
b_red = (200, 0, 0)

# Some Fonts
small_font = pygame.font.Font("freesansbold.ttf", 20)
large_font = pygame.font.Font("freesansbold.ttf", 100)

# Generating our Graph
A = graph.Graph()


# Player Function
def player(x, y):
    screen.blit(player_image, (x, y))


# Initialising the Title
title_surf = large_font.render("Graph Game", True, black)
title_rect = title_surf.get_rect()
title_rect.center = ((screen_width / 2), (screen_height / 2))


# Rectangular Button
def button_oblong(rect, text, dark_col, bright_col, command):

    button_surf = small_font.render(text, True, black)
    button_rect = button_surf.get_rect()
    button_rect.center = (rect[0] + rect[2] / 2, rect[1] + rect[3] / 2)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed(3)

    if rect[0] < mouse[0] < rect[0] + rect[2] and rect[1] < mouse[1] < rect[1] + rect[3]:
        pygame.draw.rect(screen, bright_col, rect)
        if click[0] == 1:
            command()
    else:
        pygame.draw.rect(screen, dark_col, rect)

    screen.blit(button_surf, button_rect)


# Circle button
def node_circle(centre, place, radius, dark_col, mid_col, bright_col):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed(3)

    if (centre[0] - mouse[0])**2 + (centre[1] - mouse[1])**2 < radius**2:
        pygame.draw.circle(screen, bright_col, centre, radius)
        if click[0] == 1:
            pygame.draw.circle(screen, dark_col, centre, radius)
            if A.get_pressed_num()[-1] != place and test_connection(A.get_pressed_num()[-1], place):
                A.set_pressed_num(place)
                A.set_pressed_coo(centre)
    else:
        pygame.draw.circle(screen, mid_col, centre, radius)


# Menu Screen
def game_menu():
    while True:
        for event in pygame.event.get():

            # Exiting
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(green)

        # Display Title
        screen.blit(title_surf, title_rect)

        # Display Working Buttons
        button_oblong((200, 450, 100, 50), "Start", blue, b_blue, game_loop)
        button_oblong((500, 450, 100, 50), "Credits", blue, b_blue, credit)

        pygame.display.update()

        clock.tick(60)  # 60 fps


# Fail Screen
def message(text):

    # Set up the Fail Message
    text_surf = large_font.render(text, True, black)
    text_rect = text_surf.get_rect()
    text_rect.center = ((screen_width / 2), (screen_height / 2))

    screen.blit(text_surf, text_rect)

    pygame.display.update()

    time.sleep(2)  # Can't do anything for two seconds

    A.init()

    game_loop()


# Credit Screen
def credit():
    pass


def score():
    score_surf = small_font.render("Distance: " + str(A.get_route_length()), True, black)
    score_rect = score_surf.get_rect()
    score_rect.topright = (800, 0)

    screen.blit(score_surf, score_rect)


def test_connection(p1, p2):
    for con in A.get_connections():
        if (con[0] == p1 and con[1] == p2) or (con[0] == p2 and con[1] == p1):
            return True
    return False


# Main Game Loop
def game_loop():

    # Generating Graph
    for num in range(random.randint(4, 10)):
        A.set_coordinates((random.randint(50, 550), random.randint(50, 550)))
        for p in range(len(A.get_coordinates()) - 1):
            if bool(random.getrandbits(1)):
                A.set_connections((p, num, random.randint(1, 10)))

    # Initialising the player position
    player_x = A.get_coordinates()[0][0] - player_width / 2
    player_y = A.get_coordinates()[0][1] - player_height - 10
    player_x_change = 0
    player_y_change = 0

    # Run Game
    while True:
        for event in pygame.event.get():

            # Exiting
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if len(set(A.get_pressed_num())) == len(A.get_coordinates()):
            message("Win")

        # Player Movement
        player_x += player_x_change
        player_y += player_y_change
        if A.get_pressed_coo():
            player_x = A.get_pressed_coo()[-1][0] - player_width / 2
            player_y = A.get_pressed_coo()[-1][1] - player_height - 10

        # Draw Background
        screen.fill(green)  # rgb colour
        screen.blit(background, (0, 0))

        # Draw Lines
        for con in A.get_connections():
            pygame.draw.line(screen, red, A.get_coordinates()[con[0]], A.get_coordinates()[con[1]], con[2])

        # Draw Circles
        for coo in A.get_coordinates():
            place = A.get_coordinates().index(coo)
            if A.get_pressed_num().count(place) == 0:
                node_circle(coo, place, 10, d_blue, blue, b_blue)
            else:
                node_circle(coo, place, 10, d_green, green, b_green)

        # Draw Figure
        player(player_x, player_y)

        # Draw Score
        score()

        pygame.display.update()

        clock.tick(60)  # 60 fps


game_menu()
