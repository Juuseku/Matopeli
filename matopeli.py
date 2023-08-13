import pygame
from sys import exit
import button
import random

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('SSSSnake')
clock = pygame.time.Clock()

# Button images
start_img = pygame.image.load('start_btn.png').convert_alpha()
try_again_img = pygame.image.load('try_again.png').convert_alpha()
# Main Menu background image
menu_image = pygame.image.load('snake_image.png').convert_alpha()
jungle = pygame.image.load('jungle.png')


def main_menu():
    # Create button instances
    start_button = button.Button(230, 150, start_img)

    # Menu loop
    while True:

        if start_button.draw(screen) == True:
            play_screen()

        screen.blit(jungle, (0, 0))
        start_button.draw(screen)
        screen.blit(menu_image, (130, 350))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # draw elements
        # update everything
        pygame.display.update()


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (0, 0, 128), [
                         x[0], x[1], snake_block, snake_block])


def message(msg, color, x, y):
    font_style = pygame.font.SysFont(None, 30)
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, (x, y))


def play_screen():

    snake_block = 10

    x1 = 400
    y1 = 370

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(240, 570) / 10) * 10
    food_y = round(random.randrange(110, 690) / 10) * 10

    game_over = False
    # Game loop
    while True:

        screen.blit(jungle, (0, 0))
        # Drawing the game area
        area_background = pygame.draw.rect(screen, (0, 0, 0),
                                           pygame.Rect(220, 90, 370, 620))
        area = pygame.draw.rect(screen, (255, 255, 255),
                                pygame.Rect(230, 100, 350, 600))

        # Drawing the snake
        snake = pygame.draw.rect(screen, (0, 0, 128),
                                 pygame.Rect(400, 370, 10, 10))
        # while not game_over:
        # Moving the snake
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -10
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = 10
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        x1_change = 0
                        y1_change = -10
                    elif event.key == pygame.K_DOWN:
                        x1_change = 0
                        y1_change = 10

            x1 += x1_change
            y1 += y1_change

            if x1 <= 230 or x1 >= 580:
                game_over = True
            if y1 <= 100 or y1 >= 700:
                game_over = True

            area = pygame.draw.rect(screen, (255, 255, 255),
                                    pygame.Rect(230, 100, 350, 600))
            pygame.draw.rect(screen, (255, 0, 0),
                             pygame.Rect(food_x, food_y, snake_block, snake_block))
            pygame.draw.rect(screen, (0, 0, 128),
                             pygame.Rect(x1, y1, snake_block, snake_block))
            snake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_over = True

            our_snake(snake_block, snake_list)

            # draw elements
            # update everything
            pygame.display.update()
            if x1 == food_x and y1 == food_y:
                food_x = round(random.randrange(240, 570) / 10) * 10
                food_y = round(random.randrange(110, 690) / 10) * 10
                length_of_snake += 1

            clock.tick(30)

        try_again()


def try_again():
    # Try again loop
    while True:

        try_again_button = button.Button(280, 300, try_again_img)
        if try_again_button.draw(screen) == True:
            play_screen()

        screen.blit(jungle, (0, 0))
        message("Kärmes törmäsi, harmin paikka! Yritä uudestaan",
                (255, 0, 0), 170, 270)

        try_again_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # draw elements
        # update everything
        pygame.display.update()


main_menu()
