import tkinter as tk
from PIL import Image, ImageTk

def add_digit(digit):
    value = calc.get()+str(digit)
    calc.delete(0,tk.END)
    calc.insert(0,value)

win = tk.Tk()
win.geometry(f"240x350+100+200")
win['bg']='#888888'
win.title('Калькулятор')
calc=tk.Entry(win, justify=tk.RIGHT, font=('Arial',15),width=15)
calc.grid(row=0,column=0,columnspan=3)
tk.Button(text='1',bd=3, font=('Arial',13), command=lambda :add_digit(1)).grid(row=1, column=0,stick='wens',padx=5,pady=5)
tk.Button(text='2',bd=3, font=('Arial',13), command=lambda :add_digit(2)).grid(row=1, column=1,stick='wens',padx=5,pady=5)
tk.Button(text='3',bd=3, font=('Arial',13), command=lambda :add_digit(3)).grid(row=1, column=2,stick='wens',padx=5,pady=5)
tk.Button(text='4',bd=3, font=('Arial',13), command=lambda :add_digit(4)).grid(row=2, column=0,stick='wens',padx=5,pady=5)
tk.Button(text='5',bd=3, font=('Arial',13), command=lambda :add_digit(5)).grid(row=2, column=1,stick='wens',padx=5,pady=5)
tk.Button(text='6',bd=3, font=('Arial',13), command=lambda :add_digit(6)).grid(row=2, column=2,stick='wens',padx=5,pady=5)
tk.Button(text='7',bd=3, font=('Arial',13), command=lambda :add_digit(7)).grid(row=3, column=0,stick='wens',padx=5,pady=5)
tk.Button(text='8',bd=3, font=('Arial',13), command=lambda :add_digit(8)).grid(row=3, column=1,stick='wens',padx=5,pady=5)
tk.Button(text='9',bd=3, font=('Arial',13), command=lambda :add_digit(9)).grid(row=3, column=2,stick='wens',padx=5,pady=5)
tk.Button(text='0',bd=3, font=('Arial',13), command=lambda :add_digit(0)).grid(row=4, column=0,stick='wens',padx=5,pady=5)
tk.Checkbutton(win,text="Привет").grid(row=5,column=0)
FILENAME="rebro.png"
# src_img=Image.open(FILENAME)
# t=tk.Tk
# c=tk.Canvas(t,width=213,height=200)

win.grid_columnconfigure(0,minsize=60)
win.grid_columnconfigure(1,minsize=60)
win.grid_columnconfigure(2,minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)
win.mainloop()