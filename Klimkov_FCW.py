from tkinter import *


w = Tk()
w.title('Конвектор криптовалют.')
display_width = w.winfo_screenwidth()
display_height = w.winfo_screenheight()
w_width = 600
w_height = 400
w.geometry(f'{w_width}x{w_height}+{display_width//2 - w_width//2}+{display_height//2 - w_height//2}')

w.mainloop()