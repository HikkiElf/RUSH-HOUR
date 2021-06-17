from tkinter import *
from PIL import ImageTk, Image

def win():

    root = Tk()
    root.geometry('500x400')
    canvas = Canvas(root,width=500,height=400)
    canvas.pack()
    pilImage = Image.open("unnamed1.jpeg")
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(250,200,image=image)
    root.mainloop()