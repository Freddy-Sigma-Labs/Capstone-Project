from re import compile
from MineBoard import MineBoard

gameStartInputMessage = '''Make your guess. Please enter your coordinates in one of the following inputs:\n r c\n r c f
Where:
    r - row
    c - column
    f - flag, if you wish to flag/un-flag a square'''

# take user input and return a tuple: width, height, number of mines


def getBoardGenerationInputs():
    while True:
        try:
            width = int(input("Please enter the grid width: "))
            height = int(input("Please enter the grid height: "))
            no_mines = int(input("Please enter the number of mines: "))
            if no_mines > width * height:
                raise ValueError
            break
        except ValueError:
            pass
    return width, height, no_mines


# TODO check if passing gameboard is legal -_-
def getUserCommand(gameBoard):
    userInputEX = compile("[1-9] [1-9]( f)?")
    print(gameStartInputMessage)
    while True:
        try:
            userInput = input().lower()
            if userInputEX.fullmatch(userInput) is None:
                raise Exception
            userInput = userInput.split(" ")
            row, col = int(userInput[0]) - 1, int(userInput[1]) - 1
            if not gameBoard.isSquareValid(row, col):
                raise ValueError
            if len(userInput) == 3:
                return row, col, userInput[2]
            else:
                return row, col, None
        except ValueError:
            print("Make sure your selection is within the bounds of the board.")
        except:
            print("Please check your input matches the format described.")


def main():
    gameSetupInputs = getBoardGenerationInputs()
    gameBoard = MineBoard(
        gameSetupInputs[0], gameSetupInputs[1], gameSetupInputs[2])
    while gameBoard.isPlaying():
        # TODO implement gameBoard.displayGrid()
        print(gameBoard)
        row, col, isFlagged = getUserCommand(gameBoard)
        if isFlagged:
            gameBoard.flagSquare(row, col)
            pass
        else:
            gameBoard.playSquare(row, col)

        print(gameBoard)

        if gameBoard.isPlaying():
            keepPlaying = input(
                "if you would like to stop here, press q: ").lower().strip()
            if keepPlaying == 'q':
                gameBoard.stopPlaying()

    gameBoard.showEndGrid()
    print(gameBoard)

    if gameBoard.victory():
        print("----- YOU HAVE WON -----")
    else:
        print("----- GAME OVER -----")


if __name__ == "__main__":
    main()
