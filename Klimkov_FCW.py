from tkinter import *  # Библиотека для создания графического интерфейса программы с виджетами.


w = Tk()  # Создаём окно интерфейса программы.
w.title('Конвектор криптовалют.')  # Даём окну название.
display_width = w.winfo_screenwidth()  # Запрашиваем размер монитора по оси икс в пикселях.
display_height = w.winfo_screenheight()  # Запрашиваем размер монитора по оси игрек в пикселях.
w_width = 600  # Переменная, в которой хранится заданная ширнина окна в пикселях.
w_height = 400  # Переменная, в которой хранится заданная высота окна в пикселях.
w.geometry(f'{w_width}x{w_height}+{display_width//2 - w_width//2}+{display_height//2 - w_height//2}')  # Устанавливаем
# размер окна и размещаем окно программы по центру монитора.

w.mainloop()  # Запускаем основной цикла событий GUI.