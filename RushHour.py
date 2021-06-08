import tkinter as tk
from PIL import ImageTk, Image
import random



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
                canvas.create_rectangle(col * squareSize, row * squareSize,
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#D42421",
                                            outline="#8b5546")
            elif board[row][col] == 3:
                canvas.create_rectangle(col * squareSize, row * squareSize, # area blocks
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#FFD700",
                                            outline="#8b5546")
        
            elif board[row][col] == selectedTile:
                canvas.create_rectangle(col * squareSize, row * squareSize, # area blocks
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#ffffff",
                                            outline="#8b5546", width = 5)
            else:
                canvas.create_rectangle(col * squareSize, row * squareSize,
                                            col * squareSize + squareSize,
                                            row * squareSize + squareSize,
                                            fill="#FFFF99",
                                            outline="#0F0326")


def winner():
        def on_closing():
            winWinner.destroy()

        winWinner = tk.Toplevel(root) 
        winWinner.protocol("WM_DELETE_WINDOW", on_closing)
        winWinner.title('You Win')
        winWinner.geometry('400x400+600+300')
        
        Mycanvas = tk.Canvas(winWinner,width=400,height=400)
        Mycanvas.pack()

        canvas_id = Mycanvas.create_text(180, 20, anchor="nw") 
        Mycanvas.itemconfig( canvas_id, text="You Win!") 

        pilImage = Image.open("unnamed1.jpeg")
        image = ImageTk.PhotoImage(pilImage)
        imagesprite = Mycanvas.create_image(200,200,image= image)
        winWinner.mainloop()


# moves blocks
def move(event):
    if selectedTileStatus == "VERTICAL":
        if event.keysym == "Up":
            for row in range(len(board)):
                for col in range(len(board[row])):
                    if board[row][col] == selectedTile and (board[row - 1][col] not in range(1, 100)):
                        buff = board[row - 1][col]
                        board[row - 1][col] = board[row][col]
                        board[row][col] = buff
                        draw_board()
                    elif board[row][col] == selectedTile and board[row - 1][col] == 3:
                        winner()
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
                        draw_board()
                    elif board[row][col] == selectedTile and board[row][col + 1] == 3:
                        winner()

        if event.keysym == "Left":
            for row in range(len(board)):
                for col in range(len(board[row])):
                    if board[row][col] == selectedTile and (board[row][col - 1] not in range(1, 100)):
                        buff = board[row][col - 1]
                        board[row][col - 1] = board[row][col]
                        board[row][col] = buff
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
    draw_board()




# Game settings
root = tk.Tk() # main window
root.title("Slide Blocks") # window name
xCursor = int
yCursor = int
selectedTile = int
selectedTileStatus = str

# create board array
board = [[1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 0, 4, 6, 0, 0, 1],
         [1, 0, 0, 4, 6, 0, 0, 1],
         [1, 2, 2, 4, 6, 0, 0, 3],
         [1, 0, 5, 5, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 1]]

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