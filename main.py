import pygame
from pygame.locals import *
from pygame import *
from variables import *
from numpy_array import SudokuArray

class Base:
    def __init__(self, width = W, height = H, title = TITLE):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.confirm = False
        self.corner_font = pygame.font.Font(None, 26)
        self.main_font = pygame.font.Font(None, 42)
        self.time_font = pygame.font.Font(None, 42)
        self.counter = 1
        self.selected = False
        self.input_nr, self.pencilings_final, self.pencilings = "", [], dict()
        self.board = SudokuArray().board


class Board (Base):

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.input_nr = "1"
                if event.key == pygame.K_2:
                    self.input_nr = "2"
                if event.key == pygame.K_3:
                    self.input_nr = "3"
                if event.key == pygame.K_4:
                    self.input_nr = "4"
                if event.key == pygame.K_5:
                    self.input_nr = "5"
                if event.key == pygame.K_6:
                    self.input_nr = "6"
                if event.key == pygame.K_7:
                    self.input_nr = "7"
                if event.key == pygame.K_8:
                    self.input_nr = "8"
                if event.key == pygame.K_9:
                    self.input_nr = "9"
                if event.key == pygame.K_RETURN:
                    self.confirm = True

    def board_layout(self):
        pygame.draw.rect(self.screen, BLACK, [15, 10, 450, 450], 5)
        for y_idx, y in enumerate(range(10, H-100, 50)):
            for x_idx, x in enumerate(range(15, W-15, 50)):
                pygame.draw.rect(self.screen, GREY, [x, y, 50, 50], 1)
                if (x-15)%3 == 0 and x > 50:
                    pygame.draw.line(self.screen, BLACK, (x, 10), (x, 458), 5)
                if (y-10)%3 == 0 and y > 50:
                    pygame.draw.line(self.screen, BLACK, (15, y), (463, y), 5)
                np_nr = str(self.board[y_idx][x_idx])
                if np_nr != "0":
                    cell_nr = self.main_font.render(np_nr, True, BLACK)
                    self.screen.blit(cell_nr, (x+20, y+12))

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()

        for y in range(10, H-100, 50):
            for x in range(15, W-15, 50):
                if pygame.mouse.get_pressed()[0]:
                    self.counter += 1
                    self.selected = bool(self.counter % 2)

                if self.selected == False:
                    if pygame.Rect([x, y, 50, 50]).collidepoint(mouse_pos):
                            pygame.draw.rect(self.screen, RED, [x, y, 50, 50] , 4)
                            self.actual_cell = [x, y, 50, 50]
                if self.selected:
                    pygame.draw.rect(self.screen, RED, self.actual_cell , 4)
                    


    def add_pencilmarking(self):
        if self.input_nr:
            penciling = self.corner_font.render(self.input_nr, True, LIGHTBLUE)
            penciling_pos = penciling.get_rect()
            penciling_pos.x = self.actual_cell[0]+3
            penciling_pos.y = self.actual_cell[1]+3
            self.pencilings[tuple(penciling_pos)] = penciling
            self.input_nr = ""

        for k, v in self.pencilings.items():
            self.screen.blit(v, k)
        print(self.pencilings)

    # def confirm_pencilmarking(self):
    #     for y in range(10, H-100, 50):
    #         for x in range(15, W-15, 50):
    #             if


    def game_loop(self):
        self.clock.tick(FPS)
        self.screen.fill(WHITE)
        self.board_layout()
        self.draw()
        self.add_pencilmarking()
        pygame.display.flip()

    def run(self):
        while True:
            self.game_loop()
            self.events()

        pygame.quit()


if __name__ == "__main__":
    board = Board()
    board.run()