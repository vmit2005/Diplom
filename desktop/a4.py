import tkinter
from PIL import Image, ImageTk
from re import findall,match

def is_valid(newval):
    print(newval)
    return match(r"^\d{1,4},\d{0,2}",newval) is not None



FILENAME = "rebro.png"
win = tkinter.Tk()  # окно
win.geometry(f"700x500+100+100")
win.resizable(width=False,height=False)

check=(win.register(is_valid, "%P"))

c = tkinter.Canvas(win,width=800,height=450)  # поле для картинки
src_img = Image.open(FILENAME)
img = ImageTk.PhotoImage(src_img)
c.create_image(450, 200, image=img)
c.pack()
rbr={}
dd=tkinter.Entry(win, validate="key",validatecommand=check)
dd.place(x=10,y=10)


tkinter.Button(text='   Далее    ', bd=3, font=('Arial', 13)).place(x=250, y=420)

win.mainloop()

check