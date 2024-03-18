# Welcome to my Capstone Project. 
**Freddy Martinez Rosero**

For this project, I decided to design a small game of minesweeper. You can enter values for width, height, and the number of mines in play. Once you do, a board will be generated and you can begin the game. This game was developed using Python 3.10

The game begins by showing you the starting grid, which should look something like this:
       1    2    3    4    5  
1     [X]  [X]  [X]  [X]  [X]  
2     [X]  [X]  [X]  [X]  [X]  
3     [X]  [X]  [X]  [X]  [X]  
4     [X]  [X]  [X]  [X]  [X]  
5     [X]  [X]  [X]  [X]  [X]  

Which is then followed by the following prompt:
Make your guess. Please enter your coordinates in one of the following inputs:
 r c
 r c f
Where:
    r - row
    c - column
    f - flag, if you wish to flag/un-flag a square

This lets you choose what square you select to reveal. You can set as many flags as you wish, and any flags can be toggled by repeating the command. The game ends if you turn over a mine, and you win if you are able to turn over every square without hitting a mine.

To play this game, fork this repository and open your terminal. Make sure all files are in the same folder. To begin the game, run Minesweeper.py
