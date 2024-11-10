import pygame
import time
import random

pygame.init()

# Frame settings
window_width = 600
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
first_background_color = (173, 216, 230)
second_background_color = (240, 240, 240)

# Snake & food settings
snake_block = 10
snake_speed = 12

# Fonts
font_style = pygame.font.SysFont(None, 35)


# Score function
def show_score(score):
    value = font_style.render("Score: " + str(score), True, black)
    window.blit(value, [0, 0])


# Snake initialization
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], snake_block, snake_block])


# End game message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [window_width / 6, window_height / 3])

# Background drawing
def draw_background():
        for y in range(0, window_height, snake_block):
            for x in range(0, window_width, snake_block):
                if (x // snake_block + y // snake_block) % 2 == 0:
                    color = first_background_color
                else:
                    color = second_background_color
                pygame.draw.rect(window, color, [x, y, snake_block, snake_block])


# Main game function
def game_loop():
    game_over = False
    game_close = False

    x1 = window_width / 2
    y1 = window_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Food position - random coordinates
    foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0

    # Game loop
    clock = pygame.time.Clock()
    while not game_over:

        while game_close:
            window.fill(white)
            message("Game Over! Press Q-Quit or C-Play Again", red)
            show_score(length_of_snake - 1)
            pygame.display.update()

            # Events after game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
                        return

        # Handling control events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # Snake position update
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(white)

        #draw_background()

        pygame.draw.rect(window, green, [foodx, foody, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        show_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            length_of_snake += 1
            # Nowe jedzenie nie pojawi się na ciele węża
            while [foodx, foody] in snake_list:
                foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0

        clock.tick(snake_speed)

    pygame.quit()
    quit()


# Start the game
game_loop()
