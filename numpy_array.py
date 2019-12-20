import numpy as np
import random


class SudokuArray:
    def __init__(self):
        self.board = np.zeros((9,9), dtype=int)
        self.new_sudoku()
        self.play_board()

    def check_horizontal_move(self):
        # horizontal check
        result = []
        for row in self.board:
            if len(list(x for x in row if x != 0)) == len(set(list(x for x in row if x != 0))):
                result.append(True)
        if all(result):
            return True
        return False

    def check_vertical_move(self):
        # vertical check
        result = []
        for col in range(9):
            column = []
            for row in self.board:
                column.append(row[col])
            if len(list(x for x in column if x != 0)) == len(set(list(x for x in column if x != 0))):
                result.append(True)
        if all(result):
            return True
        return False

    def check_3by3(self):
        result = []
        for r in range(0, 9, 3):
            for d in range(0, 9, 3):
                box = []
                for nr in self.board[d:d+3]:
                    for col in nr[r:r+3]:
                        box.append(col)
                if len(list(x for x in box if x != 0)) == len(set(list(x for x in box if x != 0))):
                    result.append(True)
        if all(result):
            return True
        return False

    def check(self):
        if all([self.check_vertical_move(), self.check_horizontal_move(), self.check_3by3()]):
            return True
        return False


    def new_sudoku(self):
        rng_19 = [1,2,3,4,5,6,7,8,9]
        random.shuffle(rng_19)
        self.board[0] = rng_19
        self.board[1] = np.array(list(self.board[0][-3:]) + list(self.board[0][:6]))
        self.board[2] = np.array(list(self.board[1][-3:]) + list(self.board[1][:6]))

        self.board[3] = np.array(list(self.board[2][-1:]) + list(self.board[2][:8]))
        self.board[4] = np.array(list(self.board[3][-3:]) + list(self.board[3][:6]))
        self.board[5] = np.array(list(self.board[4][-3:]) + list(self.board[4][:6]))

        self.board[6] = np.array(list(self.board[5][-1:]) + list(self.board[5][:8]))
        self.board[7] = np.array(list(self.board[6][-3:]) + list(self.board[6][:6]))
        self.board[8] = np.array(list(self.board[7][-3:]) + list(self.board[7][:6]))

        # np.random.shuffle(self.board)
        # self.board = np.rot90(self.board)
        # np.random.shuffle(self.board)
        # self.board = np.rot90(self.board)
        # np.random.shuffle(self.board)
        self.board = np.rot90(self.board)

    def play_board(self):

        indexes = [0,1,2,3,4,5,6,7,8]
        idx = indexes
        for i in range(9):
            random.shuffle(idx)
            for x in idx[:4]:
                self.board[i][x] = 0
        return self.board

    def show(self):
        print(self.board)


# if __name__ == "__main__":
#     sudoku = SudokuArray()
#     sudoku.new_sudoku()
#     sudoku.show()
#     print(sudoku.check())
#     sudoku.play_board()
#     print()
#     sudoku.show()

#     print(sudoku.check())



