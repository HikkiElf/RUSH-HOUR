import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import random
from menu import level
from win import win
from boards import *

# draw game board
# 0 - empty,
# 1 - wall,
# 2 - key,
# 3 - lock,
# other numbers - moveble blocks
def draw_board():
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                canvas.create_rectangle(col * squareSize, row * squareSize,
                                                col * squareSize + squareSize,
                                                row * squareSize + squareSize,
                                                fill="#55342b",
                                                outline="#8b5546")

            elif board[row][col] == 1:
                canvas.create_rectangle(col * squareSize, row * squareSize, 
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#000000")

            elif board[row][col] == selectedTile and selectedTile == 2:
                canvas.create_rectangle(col * squareSize, row * squareSize,
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#D42421",
                                            outline="#8b5546", width = 5)
            
            elif board[row][col] == 2:
                canvas.create_rectangle(col * squareSize, row * squareSize,
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#D42421",
                                            outline="#8b5546")

            elif board[row][col] == 3:
                canvas.create_rectangle(col * squareSize, row * squareSize, 
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#FFD700",
                                            outline="#8b5546")
        
            elif board[row][col] == selectedTile:
                canvas.create_rectangle(col * squareSize, row * squareSize,
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#ffffff",
                                            outline="#8b5546", width = 5)

            elif board[row][col] == 4:
                canvas.create_rectangle(col * squareSize, row * squareSize,
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#FFFF99",
                                            outline="#0F0326")
            elif board[row][col] == 5:
                canvas.create_rectangle(col * squareSize, row * squareSize,
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#FFC0CB",
                                            outline="#0F0326")
            elif board[row][col] == 6:
                canvas.create_rectangle(col * squareSize, row * squareSize,
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#42dc51",
                                            outline="#0F0326")
            elif board[row][col] == 7:
                canvas.create_rectangle(col * squareSize, row * squareSize,
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#b9d1d3",
                                            outline="#0F0326")
            elif board[row][col] == 8:
                canvas.create_rectangle(col * squareSize, row * squareSize,
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#2fd8e8",
                                            outline="#0F0326")
            elif board[row][col] == 9:
                canvas.create_rectangle(col * squareSize, row * squareSize,
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#7e63b3",
                                            outline="#0F0326")
            elif board[row][col] == 10:
                canvas.create_rectangle(col * squareSize, row * squareSize,
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#921160",
                                            outline="#0F0326")
            elif board[row][col] == 11:
                canvas.create_rectangle(col * squareSize, row * squareSize,
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#94c6b0",
                                            outline="#0F0326")
            elif board[row][col] == 12:
                canvas.create_rectangle(col * squareSize, row * squareSize,
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#f18d1f",
                                            outline="#0F0326")
            elif board[row][col] == 13:
                canvas.create_rectangle(col * squareSize, row * squareSize,
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#8d8742",
                                            outline="#0F0326")
            elif board[row][col] == 14:
                canvas.create_rectangle(col * squareSize, row * squareSize,
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#278dae",
                                            outline="#0F0326")
            elif board[row][col] == 15:
                canvas.create_rectangle(col * squareSize, row * squareSize,
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#c3a6b5",
                                            outline="#0F0326")


# moves blocks
def move(event):
    global level, board
    if selectedTileStatus == "VERTICAL":
        if event.keysym == "Up":
            for row in range(len(board)):
                for col in range(len(board[row])):
                    if board[row][col] == selectedTile and (board[row - 1][col] not in range(1, 100)):
                        buff = board[row - 1][col]
                        board[row - 1][col] = board[row][col]
                        board[row][col] = buff
                        canvas.delete("all")
                        draw_board()
                    # elif board[row][col] == selectedTile and board[row - 1][col] == 3:
                    #     win()
            for row in range(len(board)):
                for col in range(len(board[row])): 
                    print(board[row][col], end=' ')
                print()
            print('\n')

        if event.keysym == "Down":
            for row in range(len(board) - 1, 0, -1):
                for col in range(len(board[row]) - 1, 0, -1):
                    if board[row][col] == selectedTile and (board[row + 1][col] not in range(1, 100)):
                        buff = board[row + 1][col]
                        board[row + 1][col] = board[row][col]
                        board[row][col] = buff
                        canvas.delete("all")
                        draw_board()

            for row in range(len(board)):
                for col in range(len(board[row])): 
                    print(board[row][col], end=' ')
                print()
            print('\n')

    if selectedTileStatus == "HORIZONTAL":
        if event.keysym == "Right":
            for row in range(len(board) - 1, 0, -1):
                for col in range(len(board[row]) - 1, 0, -1):
                    if board[row][col] == selectedTile and (board[row][col + 1] not in range(1, 100)):
                        buff = board[row][col + 1]
                        board[row][col + 1] = board[row][col]
                        board[row][col] = buff
                        canvas.delete("all")
                        draw_board()
                    elif board[row][col] == selectedTile and board[row][col + 1] == 3:
                        level += 1
                        print(level,"LEVEL\n")
                        if level == 2:
                            board = random.choice([board4, board5, board6])
                            root.title("Slide Blocks: level " + str(level))
                        if level == 3:
                            board = random.choice([board7, board8, board9])
                            root.title("Slide Blocks: level " + str(level))
                        if level == 4:
                            board = random.choice([board10, board11, board12])
                            root.title("Slide Blocks: level " + str(level))
                        if level == 5:
                            board = random.choice([board13, board14, board15])
                            if board == board13:
                                root.title("Good Luck")
                            else:
                                root.title("Slide Blocks: level " + str(level))
                        if level == 6:
                            root.destroy()
                            win()
                        draw_board()
                        
                        

        if event.keysym == "Left":
            for row in range(len(board)):
                for col in range(len(board[row])):
                    if board[row][col] == selectedTile and (board[row][col - 1] not in range(1, 100)):
                        buff = board[row][col - 1]
                        board[row][col - 1] = board[row][col]
                        board[row][col] = buff
                        canvas.delete("all")
                        draw_board()


def click(event):
    global xCursor, yCursor, selectedTile, selectedTileStatus
    print(event)
    xCursor, yCursor = event.x, event.y # get cursor coordinates

    xCursor = xCursor // squareSize # X cursor index
    yCursor = yCursor // squareSize # Y cursor index
    value = board[yCursor][xCursor]
    print(value)
    if value not in range(0, 4):
        selectedTile = value
        print(selectedTile, "выбран")
        if selectedTile == board[yCursor - 1][xCursor] or selectedTile == board[yCursor + 1][xCursor]:
            selectedTileStatus = "VERTICAL"
            print(selectedTileStatus, "направление")
        elif selectedTile == board[yCursor][xCursor - 1] or selectedTile == board[yCursor][xCursor + 1]:
            selectedTileStatus = "HORIZONTAL"
            print(selectedTileStatus, "направление")

    elif value == 2:
        selectedTile = value
        print(selectedTile, "выбран")
        if selectedTile == board[yCursor - 1][xCursor] or selectedTile == board[yCursor + 1][xCursor]:
            selectedTileStatus = "VERTICAL"
            print(selectedTileStatus, "направление")
        elif selectedTile == board[yCursor][xCursor - 1] or selectedTile == board[yCursor][xCursor + 1]:
            selectedTileStatus = "HORIZONTAL"
            print(selectedTileStatus, "направление")


    print(xCursor, yCursor, "\n")
    canvas.delete("all")
    draw_board()


# Game settings
root = tk.Tk() # main window
root.title("Slide Blocks: level " + str(level)) # window name
xCursor = int
yCursor = int
selectedTile = int
selectedTileStatus = str
flag = bool

# create board array
if level == 1:
    board = random.choice([board1, board2, board3])
if flag == True:
    if level == 2:
        board = random.choice([board4, board5, board6])
        flag = False

for row in range(len(board)):
    for col in range(len(board[row])): 
        print(board[row][col], end=' ')
    print()
print('\n')

squareSize = 100

tile = [0] * len(board)
for row in range(len(board)):
    tile[row] = [0] * len(board)
tileStatus = [0] * len(board)

canvas = tk.Canvas(root, width = len(board[0]) * squareSize, height = len(board) * squareSize, bg = "#808080") # create canvas
canvas.focus_set() # focus on canvas 
canvas.pack() # display canvas

draw_board()

canvas.bind('<Button-1>', click)
canvas.bind('<Up>', move)
canvas.bind('<Down>', move)
canvas.bind('<Right>', move)
canvas.bind('<Left>', move)


root.mainloop()