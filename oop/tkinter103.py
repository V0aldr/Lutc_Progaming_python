from tkinter import *
from tkinter.messagebox import showinfo


def reply(name):
    showinfo(title='REPLY', message=f"Hello, {name}")

top = Tk()
top.title('ECHO')
# top.iconbitmap('py_blue.ico')
Label(top, text='ENTER your name ').pack()
ent = Entry(top)
ent.pack()
btn = Button(top, text='Submit', command=lambda : reply(ent.get()))
btn.pack()


top.mainloop()
