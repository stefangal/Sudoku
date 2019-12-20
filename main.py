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
        self.win_font = pygame.font.Font(None, 100)
        self.time_font = pygame.font.Font(None, 42)
        self.input_nr, self.pencilings_final, self.pencilings = "", [], dict()
        self.sudoku = SudokuArray()
        self.board = self.sudoku.board
        self.original_board = self.sudoku.original_board
        self.actual_cell = [15, 10, 50, 50]
        self.clicked = False
        self.delete = False

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
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    self.confirm = True
                if event.key == pygame.K_DELETE:
                    self.delete = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.clicked = True

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
                    cell_nr = [self.main_font.render(np_nr, True, BLACK), int(np_nr)]
                    self.screen.blit(cell_nr[0], (x+20, y+12))

    def draw(self):
        for y_idx, y in enumerate(range(10, H-100, 50)):
            for x_idx, x in enumerate(range(15, W-15, 50)):
                if self.clicked and self.original_board[y_idx][x_idx] == 0:
                        if pygame.Rect([x, y, 50, 50]).collidepoint(pygame.mouse.get_pos()):
                            pygame.draw.rect(self.screen, RED, [x, y, 50, 50] , 4)
                            self.actual_cell = [x, y, 50, 50]
                            self.clicked = False
                            self.input_nr = ""
                elif not self.clicked :
                    pygame.draw.rect(self.screen, RED, self.actual_cell , 4)

    def add_pencilmarking(self):
        if self.input_nr:
            penciling = self.corner_font.render(self.input_nr, True, LIGHTBLUE)

            penciling_pos = penciling.get_rect()
            penciling_pos.x = self.actual_cell[0]+3
            penciling_pos.y = self.actual_cell[1]+3
            self.pencilings[tuple((penciling_pos.x, penciling_pos.y))] = [penciling, self.input_nr]

        for k, v in self.pencilings.items():
            self.screen.blit(v[0], k)

        if self.confirm:
            for k, v in self.pencilings.items():
                if k[0]-3 == self.actual_cell[0] and k[1]-3 == self.actual_cell[1]:
                    row = (self.actual_cell[1]-10)//50
                    cell = (self.actual_cell[0]-15)//50
                    self.board[row][cell] = v[1]
                    self.input_nr = ""
                    self.confirm = False

        if self.delete:
            for k, v in self.pencilings.items():
                if k[0]-3 == self.actual_cell[0] and k[1]-3 == self.actual_cell[1]:
                    row = (self.actual_cell[1]-10)//50
                    cell = (self.actual_cell[0]-15)//50
                    self.board[row][cell] = 0
                    self.delete = False
            if tuple((self.actual_cell[0]+3, self.actual_cell[1]+3)) in self.pencilings:
                del self.pencilings[tuple((self.actual_cell[0]+3, self.actual_cell[1]+3))]

    def win(self):
        if self.sudoku.check():
            winner = self.win_font.render("SOLVED", True, RED)
            self.screen.blit(winner, (100, 200))
            #self.screen.lock()

    def game_loop(self):
        self.clock.tick(FPS)
        self.screen.fill(WHITE)
        self.board_layout()
        self.draw()
        self.add_pencilmarking()
        self.win()
        pygame.display.flip()

    def run(self):
        while True:
            self.game_loop()
            self.events()
        pygame.quit()


if __name__ == "__main__":
    board = Board()
    board.run()