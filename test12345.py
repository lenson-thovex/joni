
import pygame
import time
import random




dis_width = 600
dis_height = 400




pygame.init()
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.update()
pygame.display.set_caption('Snake Game by Lenny and Joni')


blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (79, 186, 118)
white = (255, 255, 255)

snake_block = 10
clock = pygame.time.Clock()
snake_speed = 15


font_style = pygame.font.SysFont('comicsansms', 20, italic=True)
score_font = pygame.font.SysFont('comicsansms', 30)


def your_score(score, position, color):
    text = score_font.render("Your Score: " + str(score), True, color)
    dis.blit(text, position)


def message(msg, color):
    ms = font_style.render(msg, True, color)
    dis.blit(ms, [dis_width / 20, dis_height / 2])


def our_snake(snake_block, snake_list, color):
    for x in snake_list:
        pygame.draw.rect(dis, color, [x[0], x[1], snake_block, snake_block])


def cross_screen(x, y):
    return x >= dis_width or x < 0 or y >= dis_height < 0


def create_food():
    x = round(random.randrange(0, dis_width - snake_block) / 10) * 10
    y = round(random.randrange(0, dis_height - snake_block) / 10) * 10
    return x, y


def gameloop():
    game_close = False
    game_close2 = False
    game_over = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x2 = dis_width / 4
    y2 = dis_height / 4

    foodx, foody = create_food()

    snake_list = [[x1, y1]]
    snake_list2 = [[x2, y2]]
    snake_length = 1
    snake_length2 = 1

    while not game_over:
        has_changed = False
        has_changed2 = False
        while game_close or game_close2:
            dis.fill(black)
            message('You lost Nub! Press Q-Quit or C-Play Again', red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = False
                    if event.key == pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:

                #player 1 keyboard actions
                if event.key == pygame.K_LEFT:
                    x1 += -snake_block
                    has_changed = True
                elif event.key == pygame.K_RIGHT:
                    x1 += snake_block
                    has_changed = True
                elif event.key == pygame.K_UP:
                    y1 += -snake_block
                    has_changed = True
                elif event.key == pygame.K_DOWN:
                    y1 += snake_block
                    has_changed = True

                ##player 2 keyboard actions
                if event.key == pygame.K_a:
                    x2 += -snake_block
                    has_changed2 = True
                elif event.key == pygame.K_d:
                    x2 += snake_block
                    has_changed2 = True
                elif event.key == pygame.K_w:
                    y2 += -snake_block
                    has_changed2 = True
                elif event.key == pygame.K_s:
                    y2 += snake_block
                    has_changed2 = True

        game_close = cross_screen(x1, y1)
        game_close2 = cross_screen(x2, y2)

        dis.fill(black)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        if has_changed:
            snake_head = [x1, y1]
            snake_list += [snake_head]

            if len(snake_list) > snake_length:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            for x in snake_list2[:-1]:
                if x == snake_head:
                    game_close = True

        if has_changed2:
            snake_head2 = [x2, y2]
            snake_list2 += [snake_head2]

            if len(snake_list2) > snake_length2:
                del snake_list2[0]

            for x in snake_list[:-1]:
                if x == snake_head2:
                    game_close2 = True

            for x in snake_list2[:-1]:
                if x == snake_head2:
                    game_close = True

        our_snake(snake_block, snake_list, red)
        our_snake(snake_block, snake_list2, white)
        your_score(snake_length - 1, [0, 0], red)
        your_score(snake_length2 - 1, [dis_width - 200, 0], white)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx, foody = create_food()
            snake_length += 1

        if x2 == foodx and y2 == foody:
            foodx, foody = create_food()
            snake_length2 += 1

        clock.tick(snake_speed)

    message('You suck Dude', red)
    pygame.display.update()
    time.sleep(2)

    pygame.quit()
    quit()


gameloop()
