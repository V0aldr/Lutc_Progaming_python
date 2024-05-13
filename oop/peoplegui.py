"""
Реализация графического интерфейса для просмотра и изменения экземпляров класса,
хранящихся в хранилище;
хранилище находится на том же компьютере, где выполняется сценарий в виде одного
или более локальных файлов.
"""

import shelve

from tkinter import *

from tkinter.messagebox import showerror

shelve_name = 'class_shelve'
field_names = ('name', 'age', 'pay', 'job')


def make_widgets():
    global entries
    window = Tk()
    window.title('People shelve')
    window.minsize(220, 160)
    form = Frame(window)
    form.pack(padx=10, pady=5)

    entries = {}
    for (ix, label) in enumerate(('key',) + field_names):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent

    Button(window, text='Fetch', command=fetch_record).pack(side=LEFT, padx=10, pady=5)
    Button(window, text='Update', command=update_record).pack(side=LEFT)
    Button(window, text='Quit', command=window.quit).pack(side=RIGHT, padx=10, pady=5)

    return window


def fetch_record():
    key = entries['key'].get().lower()
    try:
        record = db[key]  # извлечь запись по ключу, отобразить в форме
    except:
        showerror(title="ERROR", message='No suck key')
    else:
        for field in field_names:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))


def update_record():
    key = entries['key'].get().lower()
    if key in db:
        record = db[key]  # изменяется существующая запись
    else:
        from person_start import Person  # создать/сохранить новую запись
        record = Person(name='Unknown', job='Unknown')      #eval: строки должны
                                                            # заключаться в кавычки

    for field in field_names:
        setattr(record, field, eval(entries[field].get()))

    db[key] = record


if __name__ == '__main__':
    with shelve.open(shelve_name) as db:
        win = make_widgets()
        win.mainloop()
