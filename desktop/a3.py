import tkinter
from PIL import Image, ImageTk
from re import findall
rbr={'proba':5}

def validator(s):
    def tupount(str):
        str1=""
        for i in str:
            if i==",":
                str1+="."
            else:
                str1+=i
        return str1
    try:
        rez=int(tupount(''.join(findall(r'[\d,.]',s))))
        return rez
    except:
        return  None

def view_new_rebro():
    FILENAME = "rebro.png"
    win = tkinter.Tk()  # окно
    win.title("Ребро")
    win.geometry(f"700x500+100+100")
    win.resizable(width=False,height=False)
    c = tkinter.Canvas(win,width=800,height=450)  # поле для картинки
    src_img = Image.open(FILENAME)
    img = ImageTk.PhotoImage(src_img)
    c.create_image(450, 200, image=img)
    c.pack()



    def add_digit():

        rbr1={"Обозначение":str(ename.b.get()),
            "A":validator(ea.b.get()),
            "B":validator(eb.b.get()),
            "C":validator(ec.b.get()),
            "D":validator(ed.b.get()),
            "E":validator(ee.b.get()),
            "S":validator(es.b.get())
             }
        win.destroy()
        global  rbr
        rbr=rbr1

    class E:  # текстовая метка и окно ввода


        def __init__(self, e_text, x, y, vert=False):
            self.a = tkinter.Label(win, text=e_text)
            self.a.place(x=x, y=y)

            if vert == True:
                self.b = tkinter.Entry(win, justify=tkinter.RIGHT, font=('Arial', 15), width=16)
                self.b.place(x=x, y=y + 30)
            else:
                self.b = tkinter.Entry(win, justify=tkinter.RIGHT, font=('Arial', 15), width=10)
                self.b.place(x=x + 55, y=y)




    ename = E("Обозначение", 40, 10, True)
    ea = E("A", 50,90)
    eb = E("B", 50, 140)
    ec = E("C", 50, 180)
    ed = E("D", 50, 230)
    ee = E("E", 50, 280)
    es = E("S", 50, 330)


    tkinter.Button(text='   Далее    ', bd=3, font=('Arial', 13), command=add_digit).place(x=250, y=420)

    win.mainloop()
    return rbr
def main():
    print (view_new_rebro())

if __name__ == '__main__':
    main()
