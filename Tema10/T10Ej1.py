import tkinter
from tkinter import ttk


def reboot(event):
    selected.set(None)
    selectedOption.config(text="")


def selectoption():
    text = "Se ha seleccionado {}".format(selected.get())
    selectedOption.config(text=text)


window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

selected = tkinter.StringVar()
selected.set(None)
rb1 = tkinter.Radiobutton(window, text="Intro", value="Intro", variable=selected, command=selectoption)
rb2 = tkinter.Radiobutton(window, text="Python", value="Python", variable=selected, command=selectoption)
rb3 = tkinter.Radiobutton(window, text="ReactJS", value="ReactJS", variable=selected, command=selectoption)

rb1.grid(column=0, row=0, padx=5, pady=5, sticky=tkinter.W)
rb2.grid(column=0, row=1, padx=5, pady=5, sticky=tkinter.W)
rb3.grid(column=0, row=2, padx=5, pady=5, sticky=tkinter.W)
selectedOption = tkinter.Label(window)
selectedOption.grid(column=0, row=4, padx=5, pady=5, sticky=tkinter.W)

reboot_button = ttk.Button(window, text="Reiniciar")
reboot_button.grid(column=1, row=5, sticky=tkinter.E, padx=5, pady=5)
reboot_button.bind('<Button-1>', reboot)
window.mainloop()

