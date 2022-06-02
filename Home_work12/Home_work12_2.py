from tkinter import *
import winsound 
from tkinter import messagebox as mb


root = Tk()
root.geometry('300x250')
root.configure(background= '#FFB6C1')
root.title("Ксилофон")
root.resizable(0,0)

def sound_1():
    freq = 500          
    dur = 1000       
    winsound.Beep(freq, dur)

def sound_2():
    freq = 200          
    dur = 1000       
    winsound.Beep(freq, dur)

def sound_3():
    freq = 800          
    dur = 1000       
    winsound.Beep(freq, dur)

def sound_4():
    freq = 1800          
    dur = 1000       
    winsound.Beep(freq, dur)

def sound_5():
    freq = 1100          
    dur = 1000       
    winsound.Beep(freq, dur)

def personal_data(event):
    mb.showinfo("Приложение сделал","Имя: Алексей\nФамилия: Насретдинов")


lbl_sound = Label(text="Выберите звук", font = "Calibre 20",background= '#FFB6C1')
lbl_sound.place(x = 50, y = 30)




btn_calculate = Button(text = "звук 1", font = "Calibre 14",background='#FF8C00',command = sound_1)
btn_calculate.place(x = 10 ,y = 100)

btn_calculate = Button(text = "звук 2 ", font = "Calibre 14",background='#7FFF00', command = sound_2)
btn_calculate.place(x = 110 ,y = 100)

btn_calculate = Button(text = "звук 3", font = "Calibre 14",background='#00FFFF', command = sound_3)
btn_calculate.place(x = 210,y = 100)

btn_calculate = Button(text = "звук 4 ", font = "Calibre 14",background='#FFFF00', command = sound_4)
btn_calculate.place(x = 10 ,y = 150)

btn_calculate = Button(text = "звук 5", font = "Calibre 14",background='#4B0082', command = sound_5)
btn_calculate.place(x = 110 ,y = 150)

root.bind("<F1>",personal_data)

root.mainloop()