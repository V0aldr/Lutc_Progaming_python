import random

from tkinter import *

fontsize = 30
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'cyan', 'purple']


def on_spam():
    popup = Toplevel()
    popup.geometry("150x20")
    color = random.choice(colors)
    Label(popup, text='PopUp!', bg='black', fg=color).pack(fill=BOTH)
    mainLabel.config(fg=color)


def on_flip():
    mainLabel.config(fg=random.choice(colors))
    main.after(250, on_flip)


def on_grow():
    global fontsize
    fontsize += 5
    mainLabel.config(font=('arial', fontsize, 'italic'))
    main.after(100, on_grow)


main = Tk()
# main.geometry('300x300+1000+75')

mainLabel = Label(main, text='GUI Fun!', relief=RAISED, borderwidth=3)
mainLabel.config(font=('arial', fontsize, 'italic'),
                 fg='cyan',
                 bg='navy')
mainLabel.pack(side=TOP, expand=YES, fill=BOTH) #side=TOP, expand=YES(or TRUE or True), fill=BOTH

Button(main, text='On Spam', command=on_spam).pack(fill=X)
Button(main, text='On Flip', command=on_flip).pack(fill=X)
Button(main, text='On Grow', command=on_grow).pack(fill=X)

main.mainloop()
