
import pygame
import graph

# Initialise
pygame.init()

# Create Screen
screen = pygame.display.set_mode((800, 600))  # pixel size

# Title and Icon
pygame.display.set_caption("Epic Graph Game")
icon = pygame.image.load("big_ben.png")
pygame.display.set_icon(icon)

# Player Icon
player_image = pygame.image.load("person-walking.png")
player_x = 370
player_y = 480
player_x_change = 0
player_y_change = 0


# Player Function
def player(x, y):
    screen.blit(player_image, (x, y))


A = graph.Graph()

A.set_coordinates((100, 100), (100, 200), (200, 100), (200, 200))
A.set_connections((0, 1), (1, 2), (2, 0), (3, 2))
print(A.get_coordinates())

# Run Game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -1
            if event.key == pygame.K_RIGHT:
                player_x_change = 1
            if event.key == pygame.K_UP:
                player_y_change = -1
            if event.key == pygame.K_DOWN:
                player_y_change = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_y_change = 0

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

    # Fill Colour
    screen.fill((54, 186, 145))  # rgb colour

    # pygame.draw.line(screen, (0, 0, 0), (10, 30), (400, 500), 5)
    for con in A.get_connections():
        pygame.draw.line(screen, (150, 0, 0), A.get_coordinates()[con[0]], A.get_coordinates()[con[1]], 5)

    for coo in A.get_coordinates():
        pygame.draw.circle(screen, (0, 0, 150), coo, 10)

    player(player_x, player_y)
    pygame.display.update()
