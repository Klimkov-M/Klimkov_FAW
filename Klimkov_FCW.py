from tkinter import *  # Библиотека для создания графического интерфейса программы с виджетами.
from tkinter import ttk

from PIL.ImageOps import expand


def theme():
    height_f00 = 40
    F = 'Courier 16'
    f = 'Courier 11'

    bgW = '#370588'  # Цвет фона окна.
    bgC = '#4f19a8'  # Цвет фона шапки.
    fgT = '#ffff00'  # Цвет текста.

    f_00.config(bg=bgC, height=height_f00)
    f_01.config(bg=bgW, height=w_height - height_f00)

    label_title.config(font=F, bg=bgC, fg=fgT)
    button_exit.config(font=f, bg=bgC, fg=fgT, width=3, bd=2, relief="ridge", highlightthickness=1)



w = Tk()  # Создаём окно интерфейса программы.
w.overrideredirect(True) # Скрываем шапку с кнопками управления и стандартной иконкой, также делаем окно статичным и
# исключаем возможность растянуть окно.
w.title('Конвектор криптовалют.')  # Даём окну название.
display_width = w.winfo_screenwidth()  # Запрашиваем размер монитора по оси икс в пикселях.
display_height = w.winfo_screenheight()  # Запрашиваем размер монитора по оси игрек в пикселях.
w_width = 600  # Переменная, в которой хранится заданная ширнина окна в пикселях.
w_height = 400  # Переменная, в которой хранится заданная высота окна в пикселях.
w.geometry(f'{w_width}x{w_height}+{display_width//2 - w_width//2}+{display_height//2 - w_height//2}')  # Устанавливаем
# размер окна и размещаем окно программы по центру монитора.

f_00 = Frame(w);f_00.pack(fill=X, expand=True)  # Фрейм заголовка.
f_01 = Frame(w);f_01.pack(fill=X, expand=True)  # Фрейм основного окна.
label_title = Label(f_00,text=f'{chr(128202)}{chr(128200)} Конвертер криптовалют')
button_exit = Button(f_00, text=chr(10005), command=w.destroy)
label_title.place(relx=.29, rely=.5, anchor='center')
button_exit.place(relx=.96, rely=.5, anchor='center')

theme()



w.mainloop()  # Запускаем основной цикла событий GUI.