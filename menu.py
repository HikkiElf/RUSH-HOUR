import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox
from PIL import ImageTk, Image

def play():
    win.destroy()

def close():
    global level
    close = True
    level = 0
    win.destroy()
    return close

def clicked2(): 
    def on_closing(): 
        winHelp.destroy()

    winHelp = tk.Toplevel(win)
    winHelp.protocol("WM_DELETE_WINDOW", on_closing)
    winHelp.title('Help')
    winHelp.geometry('400x80+600+300')
    text = tk.Text(winHelp, width=50, bg='white',
                        fg='black', font=('Calibri', 12),
                        wrap=WORD, padx = 5, pady = 5)

    text.pack(fill=BOTH)
    help = open('help.txt', 'r', encoding='utf-8')
    s = help.read()
    text.insert(END, s)
    help.close()

def clicked3(): 
    def on_closing(): 
        winAbout.destroy()

    winAbout = tk.Toplevel(win)
    winAbout.protocol("WM_DELETE_WINDOW", on_closing)
    winAbout.title('About')
    winAbout.geometry('170x30+600+300')
    text = tk.Text(winAbout, width=50, bg='white',
                        fg='black', font=('Calibri', 12),
                        wrap=WORD, padx = 5, pady = 5)

    text.pack(fill=BOTH)
    about = open('about.txt', 'r', encoding='utf-8')
    s = about.read()
    text.insert(END, s)
    about.close()

win = tk.Tk()

win.title('RUSH HOUR')
win.geometry('300x480+550+250')
win.minsize(300, 400)
win.maxsize(700, 800)
win.resizable(True, True)

level = 1

button1 = tk.Button(win, text = 'play', bg='red', command = play).pack(ipadx = 132, ipady = 50)
button2 = tk.Button(win, text = 'rules', bg='#54FA9B', command = clicked2).pack(ipadx = 132, ipady = 50)
button3 = tk.Button(win, text = 'about', bg='#54FA9B', command = clicked3).pack(ipadx = 132, ipady = 50)
button4 = tk.Button(win, text = 'exit', bg='#54FA9B', command = close).pack(ipadx = 132, ipady = 50)

# label2 = tk.Label(win, textvariable = level_text)
# Btn_set = tk.Button(win, text = "set level", command = close).pack()
# for level in sorted(levels):
#     tk.Radiobutton(win, text = levels[level], variable = level_var, value = level, command = select_level).pack()
# label1.pack()
# label2.pack()

win.mainloop()