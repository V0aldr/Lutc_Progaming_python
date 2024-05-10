from tkinter import *

from tkinter102 import MyGUI

from tkinter.messagebox import showinfo


class CustomGUI(MyGUI):
    def reply(self):
        showinfo(title='popup', message='OUCH')

if __name__ == '__main__':
    CustomGUI().pack()
    mainloop()

