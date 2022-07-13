import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)


labelList = tkinter.Label(window, text="Lista de cursos")
labelList.grid(column=0, row=0, padx=5, pady=5, sticky=tkinter.W)

listBox = tkinter.Listbox(window, selectmode=tkinter.EXTENDED)
items = (
    "Intro",
    "Python",
    "Java",
    "ReactJS"
)
listBox.insert(0, *items)
listBox.grid(column=0, row=1, padx=5, pady=5, sticky=tkinter.W)

window.mainloop()