from multiprocessing import Value
from tkinter import *
from tkinter import messagebox as mb


root = Tk()
root.geometry('300x250')
root.configure(background='#00BFFF')
root.title("Норма веса")
root.resizable(0,0)

lbl_height = Label(text="Введите ваш рост", font = "Calibre 15",background='#FF8C00')
lbl_height.place(x = 10, y = 20)
ent_height = Entry(width = 5, font = "Calibri 15")
ent_height.place(x = 200, y = 20)

lbl_weight = Label(text="Введите ваш вес", font = "Calibre 15",background='#FF8C00')
lbl_weight.place(x = 10, y = 60)
ent_weight = Entry(width = 5, font = "Calibri 15")
ent_weight.place(x = 200, y = 60)

s = IntVar()

gender_husband = Radiobutton(text="Женский", value=1, variable= s,background='#FF8C00', justify=LEFT)
gender_husband.place(x = 100, y = 100 ),
gender = Radiobutton(text="Мужской",value=2,variable= s,background='#FF8C00', justify=RIGHT)
gender.place(x = 10, y = 100)

def weigh_calculation():
    try:
        x = int(ent_height.get())
        y = int(ent_weight.get())
        m = 100
        w = 110
        if s.get() == 1:
            if (y > (x - w)):
                mb.showinfo("Норма веса","Норма вашего веса: " + str(x - w) + " кг" + '\n'
                "Ваш избыточный вес: " + str(y - (x - w)) + " кг")
            elif (y < (x - w)):
                mb.showinfo("Норма веса","Норма вашего веса: " + str(x - w) + " кг" + '\n'
                "У вас недовес: " + str(y - (x - w)) + " кг")
            elif (y == (x - w)):
                mb.showinfo("Норма веса","Норма вашего веса: " + str(x - w) + " кг" + '\n' "Ваш вес в норме")

        elif s.get() == 2:
            if (y > (x - m)):
                mb.showinfo("Норма веса","Норма вашего веса: " + str(x - m) + " кг" + '\n'
                "Ваш избыточный вес: " + str(y - (x - m)) + " кг")
            elif (y < (x - m)):
                mb.showinfo("Норма веса","Норма вашего веса: " + str(x - m) + " кг" + '\n' 
                "У вас недовес: " + str(y - (x - m)) + " кг")
            elif (y == (x - m)):
                mb.showinfo("Норма веса","Норма вашего веса: " + str(x - m) + " кг" + '\n' "Ваш вес в норме")
    except ValueError:
        mb.showerror("Ошибка","Ошибка введите цифры")
   
btn_calculate = Button(text = "Рассчитать ", font = "Calibre 14",background='#FF8C00',command = weigh_calculation)
btn_calculate.place(x = 80 ,y = 160)
root.mainloop()