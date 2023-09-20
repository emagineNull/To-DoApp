# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import *


def callback():
    global E1
    string = E1.get()
    T1.insert(END, "● " + string + '\n')


tasklist = []
top = Tk()


L1 = Label(top, text="Task: ")
E1 = Entry(top, bd=5)
T1 = Text(top, height=30, width=40)


MyButton1 = Button(top, text="Submit", bg="light gray", width=10,
                   command=lambda: callback())
MyButton1.grid(row=1, column=1)


T1.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)
E1.grid(row=0, column=1)
L1.grid(row=0)

top.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
