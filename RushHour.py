import tkinter as tk
from PIL import ImageTk, Image
import random



# draw game board
# 0 - empty,
# 1 - wall,
# 2 - key,
# 3 - lock
# other numbers - moveble blocks
def draw_board():
    global key
    key = [0] * len(board)
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                canvas.create_rectangle(col * squareSize, row * squareSize, # white cube
                                                col * squareSize + squareSize,
                                                row * squareSize + squareSize,
                                                fill="#55342b",
                                                outline="#8b5546")

            elif board[row][col] == 1:
                canvas.create_rectangle(col * squareSize, row * squareSize, # area blocks
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#000000")
            
            elif board[row][col] == 2:
                key[row] = canvas.create_rectangle(col * squareSize, row * squareSize,
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#D42421",
                                            outline="#8b5546")
            elif board[row][col] == 3:
                canvas.create_rectangle(col * squareSize, row * squareSize, # area blocks
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#ffffff",
                                            outline="#8b5546")
            else:
                tile[row][col] = canvas.create_rectangle(col * squareSize, row * squareSize, # area blocks
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#FFFF99",
                                            outline="#0F0326")


# moves blocks
def move(event):

    if event.keysym == "Up":
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 2 and (board[row - 1][col] not in range(3, 100)):
                    buff = board[row - 1][col]
                    board[row - 1][col] = board[row][col]
                    board[row][col] = buff
                    canvas.move(key[row], 0, -squareSize)
                    draw_board()
        for row in range(len(board)):
            for col in range(len(board[row])): 
                print(board[row][col], end=' ')
            print()
        print('\n')

    if event.keysym == "Down":
        for row in range(len(board) - 1, 0, -1):
            for col in range(len(board[row]) - 1, 0, -1):
                if board[row][col] == 2 and (board[row + 1][col] not in range(3, 100) and board[row + 1][col] != 1):
                    buff = board[row + 1][col]
                    board[row + 1][col] = board[row][col]
                    board[row][col] = buff
                    canvas.move(key[row], 0, squareSize)
                    draw_board()

        for row in range(len(board)):
            for col in range(len(board[row])): 
                print(board[row][col], end=' ')
            print()
        print('\n')



# Game settings
root = tk.Tk() # main window
root.title("Slide Blocks") # window name


# create board array
board = [[1, 1, 3, 1, 1, 1],
         [1, 0, 2, 5, 4, 1],
         [1, 0, 2, 5, 4, 1],
         [1, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1]]

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

canvas.bind('<Up>', move)
canvas.bind('<Down>', move)


root.mainloop()
# # register block selection for next moving
# def click(event):
#     print(event)
#     xCursor, yCursor = event.x, event.y # get cursor coordinates

#     xCursor = xCursor // squareSize # X cursor index
#     yCursor = yCursor // squareSize # Y cursor index

#     print(xCursor, yCursor, "\n")
#     for row in range(len(tile)):
#         for col in range(len(tile[row])):
#             print(canvas.coords(tile[row][col]), end=' ')
#         print()
#     print(canvas.coords(tile[1][2])[2])

#     for row in range(len(board)):
#         tileStatus[row] = "UNSELECT"
#         if (xCursor == canvas.coords(tile[row])[0] // squareSize) and (yCursor == canvas.coords(tile[row])[1] // squareSize):
#             tileStatus[row] = "SELECT"
#     for row in range(len(board)):
#         print(tileStatus[row])
    