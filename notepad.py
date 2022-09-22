from tkinter.filedialog import *
import tkinter as tk
from tkinter import *


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Notepad")
canvas.config(bg = "black")
top = LabelFrame(canvas)
top.pack(padx =10, pady=5, anchor="nw")

def openFile():
   file = askopenfile(mode = 'r', filetype= [('text files', '.txt')])
   if file is None:
       content = file.read()
   entry.insert(INSERT, content)
                                                   

def saveFile():
    newfile= asksaveasfile(mode = 'w', filetype= [('text files', '.txt')])
    if newfile is None:
        return
    text = str(entry.get(1.0, END))
    newfile.write(text)
    newfile.close()
   

def clearFile():
    entry.delete(1.0, END)


b1 = Button(canvas, text="open", bg="white", command = openFile)
b1.pack(in_=top, side=RIGHT)

b2 = Button(canvas, text="save", bg="white", command = saveFile)
b2.pack(in_=top, side=RIGHT)

b3 = Button(canvas, text="clear", bg="white", command = clearFile)
b3.pack(in_=top, side=RIGHT)

b4 = Button(canvas, text="exit", bg="white", command=exit)
b4.pack(in_=top, side=RIGHT)

entry = Text(canvas, wrap = WORD, bg="grey", font =("poppins", 15))
entry.pack(padx=10, pady=5, expand = TRUE, fill = BOTH)

canvas.mainloop()
