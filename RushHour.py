import tkinter as tk
from PIL import ImageTk, Image
import random



# draw game board
# 0 - empty,
# 1 - wall,
# 8 - key,
# 9 - lock
# other numbers - moveble blocks
def draw_board():
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
            
            elif board[row][col] == 8:
                key = canvas.create_rectangle(col * squareSize, row * squareSize,
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#D42421",
                                            outline="#8b5546")
            elif board[row][col] == 9:
                canvas.create_rectangle(col * squareSize, row * squareSize, # area blocks
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#ffffff",
                                            outline="#8b5546")
            else:
                canvas.create_rectangle(col * squareSize, row * squareSize, # area blocks
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#FFFF99",
                                            outline="#0F0326")
    

# Game settings
root = tk.Tk() # main window
root.title("Slide Blocks") # window name


# create board array
board = [[1, 1, 9, 1, 1, 1],
         [1, 0, 2, 2, 3, 1],
         [1, 0, 8, 0, 3, 1],
         [1, 0, 8, 0, 0, 1],
         [1, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1]]

squareSize = 100

canvas = tk.Canvas(root, width = len(board[0]) * squareSize, height = len(board) * squareSize, bg = "#808080") # create canvas
canvas.focus_set() # focus on canvas 
canvas.pack() # display canvas

draw_board()

root.mainloop()