
import pygame
import time
import random

class Snakegame:

    def __init__(self):
        self.dis_width = 600
        self.dis_height = 400


        pygame.init()
        self.dis = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.update()
        pygame.display.set_caption('Snake Game by Lenny and Joni')


        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.green = (79, 186, 118)
        self.white = (255, 255, 255)

        self.snake_block = 10
        self.clock = pygame.time.Clock()
        self.snake_speed = 15


        self.font_style = pygame.font.SysFont('comicsansms', 20, italic=True)
        self.score_font = pygame.font.SysFont('comicsansms', 30)


    def your_score(self, score, position, color):
        text = self.score_font.render("Your Score: " + str(score), True, color)
        self.dis.blit(text, position)


    def message(self, msg, color):
        ms = self.font_style.render(msg, True, color)
        self.dis.blit(ms, [self.dis_width / 20, self.dis_height / 2])


    def our_snake(self, snake_block, snake_list, color):
        for x in snake_list:
            pygame.draw.rect(self.dis, color, [x[0], x[1], self.snake_block, self.snake_block])


    def cross_screen(self, x, y):
        return x >= self.dis_width or x < 0 or y >= self.dis_height < 0


    def create_food(self):
        x = round(random.randrange(0, self.dis_width - self.snake_block) / 10) * 10
        y = round(random.randrange(0, self.dis_height - self.snake_block) / 10) * 10
        return x, y


    def gameloop(self):
        game_close = False
        game_close2 = False
        game_over = False

        x1 = self.dis_width / 2
        y1 = self.dis_height / 2

        x2 = self.dis_width / 4
        y2 = self.dis_height / 4

        foodx, foody = self.create_food()

        snake_list = [[x1, y1]]
        snake_list2 = [[x2, y2]]
        snake_length = 1
        snake_length2 = 1

        while not game_over:
            has_changed = False
            has_changed2 = False
            while game_close or game_close2:
                self.dis.fill(self.black)
                self.message('You lost Nub! Press Q-Quit or C-Play Again', self.red)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = False
                        if event.key == pygame.K_c:
                            self.gameloop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:

                    #player 1 keyboard actions
                    if event.key == pygame.K_LEFT:
                        x1 += -self.snake_block
                        has_changed = True
                    elif event.key == pygame.K_RIGHT:
                        x1 += self.snake_block
                        has_changed = True
                    elif event.key == pygame.K_UP:
                        y1 += -self.snake_block
                        has_changed = True
                    elif event.key == pygame.K_DOWN:
                        y1 += self.snake_block
                        has_changed = True

                    ##player 2 keyboard actions
                    if event.key == pygame.K_a:
                        x2 += -self.snake_block
                        has_changed2 = True
                    elif event.key == pygame.K_d:
                        x2 += self.snake_block
                        has_changed2 = True
                    elif event.key == pygame.K_w:
                        y2 += -self.snake_block
                        has_changed2 = True
                    elif event.key == pygame.K_s:
                        y2 += self.snake_block
                        has_changed2 = True

            game_close = self.cross_screen(x1, y1)
            game_close2 = self.cross_screen(x2, y2)

            self.dis.fill(self.black)
            pygame.draw.rect(self.dis, self.green, [foodx, foody, self.snake_block, self.snake_block])

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

            self.our_snake(self.snake_block, snake_list, self.red)
            self.our_snake(self.snake_block, snake_list2, self.white)
            self.your_score(snake_length - 1, [0, 0], self.red)
            self.your_score(snake_length2 - 1, [self.dis_width - 200, 0], self.white)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx, foody = self.create_food()
                snake_length += 1

            if x2 == foodx and y2 == foody:
                foodx, foody = self.create_food()
                snake_length2 += 1

            self.clock.tick(self.snake_speed)

        self.message('You suck Dude', self.red)
        pygame.display.update()
        time.sleep(2)

        pygame.quit()
        quit()

game = Snakegame()
game.gameloop()