from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Carrusel')

img1 = ImageTk.PhotoImage(Image.open('images/1.png'))
img2 = ImageTk.PhotoImage(Image.open('images/2.png'))
img3 = ImageTk.PhotoImage(Image.open('images/3.png'))
img4 = ImageTk.PhotoImage(Image.open('images/4.png'))

lista = [img1, img2, img3, img4]

label = Label(root, image=img1)
label.grid(row=0, column=0, columnspan=3)

def adelante(img_num):
    global label
    global btn_adelante
    global btn_atras

    label.grid_forget()
    label = Label(root, image=lista[img_num])
    btn_atras = Button(root, text='<-', command=lambda: atras(img_num - 1))
    btn_adelante = Button(root, text='->', command=lambda: adelante(img_num + 1))

    if img_num == 3:
        btn_adelante = Button(root, text='N/A', state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    btn_atras.grid(row=1, column=0)
    btn_adelante.grid(row=1, column=2)

def atras(img_num):
    global label
    global btn_adelante
    global btn_atras

    label.grid_forget()
    label = Label(root, image=lista[img_num])
    btn_atras = Button(root, text='<-', command=lambda: atras(img_num - 1))
    btn_adelante = Button(root, text='->', command=lambda: adelante(img_num + 1))

    if img_num == 0:
        btn_atras = Button(root, text='N/A', state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    btn_atras.grid(row=1, column=0)
    btn_adelante.grid(row=1, column=2)

btn_atras = Button(root, text='N/A', state=DISABLED)
btn_adelante = Button(root, text='->', command=lambda: adelante(1))

btn_atras.grid(row=1, column=0)
btn_adelante.grid(row=1, column=2)

root.mainloop()