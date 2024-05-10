from tkinter import *
from tkinter102 import MyGUI


# главное окно приложения
mainwin = Tk()
Label(mainwin, text=__name__).pack()

# окно диалога
popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGUI(popup).pack(side=RIGHT)


mainwin.mainloop()

