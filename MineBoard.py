from random import randint as r_int
from enum import auto, Enum
from Square import Square

'''
This class is in charge of maintaining the Minesweeper game board. it generates a playing board, 
which is then interpreted by the Cells board to display this board to the terminal.

To generate the board, it takes user input from the Minesweeper class.
The GameStatus class here is used to represent the state of the game at runtime.
'''


class GameStatus(Enum):
    PLAYING = auto()
    QUIT = auto()
    LOSE = auto()
    WIN = auto()


class MineBoard():
    def __init__(self, width, height, no_mines):
        self.width = width
        self.height = height
        self.mines = no_mines
        self.board = [[Square() for _ in range(self.width)]
                      for _ in range(self.height)]
        self.placeMines()
        self.status = GameStatus.PLAYING
        self.cellsLeftOpen = self.width * self.height - self.mines

    def __str__(self):
        res = []
        res.append(
            " "*5 + "".join(map(lambda x: "{:^5d}".format(x+1), range(self.width))))
        for i in range(self.height):
            string = "{:<6d}".format(i+1)
            for j in range(self.width):
                string += "[" + str(self.board[i][j].getValue()) + "]  "

            res.append(string)

        return "\n".join(res) + "\n"

    def placeMines(self):
        minesLeft = self.mines
        mineCoOrds = []
        while minesLeft != 0:
            r, c = r_int(0, self.width-1), r_int(0, self.height-1)
            if (r, c) in mineCoOrds:
                continue
            else:
                mineCoOrds.append((r, c))
                minesLeft -= 1
        for r, c in mineCoOrds:
            self.board[r][c].setMine()
            self.setAdjacentSquares(r, c)

    def setAdjacentSquares(self, row, col):
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if self.isSquareValid(r, c) and not self.isSquareMine(r, c):
                    self.board[r][c].incValue()

    def revealSquare(self, row, col):
        square = self.board[row][col]
        if not self.isSquareValid(row, col) or not self.isSquareHidden(row, col):
            return
        if square.getIsFlagged():
            square.toggleFlag()

        square.setRevealed()

    def playSquare(self, row, col):
        self.revealSquare(row, col)
        self.cellsLeftOpen -= 1
        if self.isSquareMine(row, col):
            self.status = GameStatus.LOSE
        elif self.cellsLeftOpen == 0:
            self.status = GameStatus.WIN

    def flagSquare(self, row, col):
        self.board[row][col].toggleFlag()

        return self.board[row][col]

    def isSquareFlagged(self, row, col):
        return self.board[row][col].getIsFlagged()

    def isSquareValid(self, row, col):
        return 0 <= row < self.height and 0 <= col < self.width

    def isSquareHidden(self, row, col):
        return self.board[row][col].isHidden()

    def isSquareMine(self, row, col):
        return self.board[row][col].isMine()

    def isPlaying(self):
        return self.status == GameStatus.PLAYING

    def stopPlaying(self):
        self.status = GameStatus.QUIT

    def showEndGrid(self):
        for row in range(self.width):
            for col in range(self.height):
                self.board[row][col].setRevealed()

    def victory(self):
        return self.status == GameStatus.WIN
