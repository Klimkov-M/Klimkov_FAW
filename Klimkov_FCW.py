from tkinter import *  # Библиотека для создания графического интерфейса программы с виджетами.
from tkinter import ttk



def theme():  # Функция визуализации интерфейса окна программы.
    height_f00 = 40  # Высота фрейма f_0 в пикселях.
    F = 'Courier 16'
    f = 'Courier 12'

    fg_tf = '#ffff00'  # Цвет текста во фреймах.
    fg_cb = '#242B8C'  # Цвет шрифта комбобоксов.
    bg_f0 = '#4f19a8'  # Цвет фона шапки.
    bg_ww = '#370588'  # Цвет фона окна.
    bg_cb = '#D9D9D9'  # Цвет фона комбобоксов.

    f_0.config(bg=bg_f0, height=height_f00)
    f_1.config(bg=bg_ww, height=w_height - height_f00)

    label_title.config(font=F, bg=bg_f0, fg=fg_tf)
    button_exit.config(font=f, bg=bg_f0, fg=fg_tf, width=3, bd=2, relief="ridge", highlightthickness=1)

    w.option_add("*TCombobox*Listbox.font", f)  # Меняем шрифт в выпадающем списке комбобоксов
    styleComboboxT = ttk.Style()  # Вытаскиваем класс для управления базой данных стилей в модуле tkinter.ttk.
    styleComboboxT.theme_use('classic')  # Вытаскиваем классическую тему из класса управления базой данных стилей.
    styleComboboxT.configure('TCombobox',  # Меняем стандартные параметры на свои.
                             fieldbackground=bg_cb,  # Цвет фона.
                             background=bg_cb,  # Цвет стрелки.
                             foreground=fg_cb,  # Цвет шрифта.
                             selectforeground=fg_cb)  # Цвет шрифта при выборе.
    # Ниже определяем форматы меток, комбобоксов, поля ввода.
    normal_currency.config(font=f, width=24, height=12, justify=CENTER, state='readonly')
    crypto_currency.config(font=f, width=24, height=12, justify=CENTER, state='readonly')
    label_norm_curr.config(font=F, bg=bg_ww, fg=fg_tf)
    label_crip_curr.config(font=F, bg=bg_ww, fg=fg_tf)


currencies = {# Журнал с данными для работы с комбобоксами, запросами из интернета и отображения на метках в интерфейсе.
    'Российский рубль     RUB': ['RUB', 'одного российского рубля'],
    'Кувейтский динар     KWD': ['KWD', 'одного кувейтского динара'],
    'Доллар США           USD': ['USD', 'одного доллара США'],
    'Евро                 EUR': ['EUR', 'одного евро'],
    'Японская йена        JPY': ['JPY', 'одной японской йены'],
    'Британский фунт      GBP': ['GBP', 'одного британского фунта'],
    'Австралийский доллар AUD': ['AUD', 'одного австралийского доллара'],
    'Канадский доллар     CAD': ['CAD', 'одного канадского доллара'],
    'Швейцарский франк    CHF': ['CHF', 'одного швейцарского франка'],
    'Китайский юань       CNY': ['CNY', 'одного китайского юаня'],
    'Казахстанский тенге  KZT': ['KZT', 'одного казахстанского тенге'],
    'Узбекский сум        UZS': ['UZS', 'одного узбекского сума']}



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

f_0 = Frame(w);f_0.pack(fill=BOTH)  # Фрейм заголовка.
f_1 = Frame(w);f_1.pack(fill=BOTH, expand = True)  # Фрейм основного окна.

label_title = Label(f_0,text=f'{chr(128202)}{chr(128200)} Конвертер криптовалют')
button_exit = Button(f_0, text=chr(10005), command=w.destroy)
label_title.place(relx=.29, rely=.5, anchor='center')
button_exit.place(relx=.96, rely=.5, anchor='center')

label_norm_curr = Label(f_1, text='ОБЫЧНАЯ ВАЛЮТА')
label_crip_curr = Label(f_1, text=' КРИПТОВАЛЮТА ')
normal_currency = ttk.Combobox(f_1, values=list(currencies.keys()))  # Комбобокс с целевой валютой.
crypto_currency = ttk.Combobox(f_1, values=list(currencies.keys()))  # Комбобокс с первой базовой валютой.
label_norm_curr.grid(row=0, column = 0, padx = 19, pady = (20,5))
label_crip_curr.grid(row=0, column = 1, padx = 19, pady = (20,5))
normal_currency.grid(row=1, column = 0, padx = 19)
crypto_currency.grid(row=1, column = 1, padx = 19)



theme()



w.mainloop()  # Запускаем основной цикла событий GUI.