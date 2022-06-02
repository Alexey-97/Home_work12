import os 
from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk, Image

a = os.listdir('images')
root = Tk()
root.geometry('600x600')
root.title("Галерея")
root.resizable(0,0)

curr_img = 0
def setForward():
    try:
        global curr_img
        if curr_img < len(a):
            curr_img = curr_img + 1
            pach = "images/" + str(a[curr_img])
            img["file"] = pach
    except IndexError:
        mb.showinfo("Предупреждение", "Картинки кончились")

def setBack():
    try:
        global curr_img
        if str(curr_img) <= a[0]:
            curr_img = curr_img - 1
            pach = "images/" + str(a[curr_img])
            img["file"] = pach
    except IndexError:
        mb.showinfo("Предупреждение", "Картинки кончились")


img = PhotoImage(file= 'images/'+ a[0])
lbl_img = Label(image=img)
lbl_img.pack(side=TOP)

btn_forward = Button(text = "Вперёд ", font = "Calibre 14",background='green',command=setForward)
btn_forward.place(x = 350 ,y = 500)

btn_forwar = Button(text = "Назад ", font = "Calibre 14",background='blue',command = setBack )
btn_forwar.place(x = 150 ,y = 500)

root.mainloop()