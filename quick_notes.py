import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("Quick Notes")

frame = tkinter.Frame(window, bg="grey")
frame.pack()

#title box
title_frame = tkinter.LabelFrame(frame, text="Insert Your Title")
title_frame.grid(row=0, column=0, padx=20, pady=10)

user_input = tkinter.Entry(title_frame, width=80)
user_input.grid(row=0, column=0, columnspan=3)

#notes box
notes_frame = tkinter.LabelFrame(frame, text="Notes")
notes_frame.grid(row=1, column=0, padx=20, pady=10)

notes_input = tkinter.Entry(notes_frame, width=80)
notes_input.grid(row=0, column=0, columnspan=3, rowspan=2)

#submit box
submit_frame = tkinter.LabelFrame(frame)
submit_frame.grid(row=2, column=0, padx=20, pady=10)

def save_notes():
        filename = "save_note.txt"
        with open(filename, "a") as save:
            save.write(f"\ntitle = {user_input.get()}"
                       f"\nnotes = {notes_input.get()}\n")
        user_input.delete(0, END)
        notes_input.delete(0, END)

submit_button = tkinter.Button(submit_frame, text="Submit", width=15, 
                               command=save_notes)
submit_button.grid(row=0, column=1)

window.mainloop()