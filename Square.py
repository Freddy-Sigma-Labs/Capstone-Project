from enum import Enum, auto


class SquareStatus(Enum):
    HIDDEN = auto()
    REVEALED = auto()


class Square():
    # TODO implement object that stores the state of each individual square
    def __init__(self):
        self.value = 0
        self.status = SquareStatus.HIDDEN
        self.isFlagged = False

    def incValue(self):
        if self.value is None:
            self.value = 0
        self.value += 1

    def setMine(self):
        self.value = "M"

    def getValue(self):
        if self.status == SquareStatus.REVEALED:
            return self.value
        elif self.status == SquareStatus.HIDDEN:
            return "F" if self.isFlagged else "X"

    def getStatus(self):
        return self.status

    def isMine(self):
        return self.value == "M"

    def getIsFlagged(self):
        return self.isFlagged

    def isHidden(self):
        return self.status == SquareStatus.HIDDEN

    def isRevealed(self):
        return self.status == SquareStatus.REVEALED

    def toggleFlag(self):
        if self.isFlagged:
            self.status = SquareStatus.HIDDEN
            self.isFlagged = False
        elif not self.status == SquareStatus.REVEALED:
            self.isFlagged = True

    def setRevealed(self):
        self.status = SquareStatus.REVEALED
