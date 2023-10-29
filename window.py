from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Hola Mundo')

# def open(): Solucion 1
#     img = ImageTk.PhotoImage(Image.open('Icon.png'))
#     top = Toplevel()
#     top.title('Hola mundo, nueva ventana')
#     l = Label(top, text='Soy un texto en una segunda ventana')
#     l2 = Label(top, image=img)
#     l.pack()
#     l2.pack()
#     top.mainloop()

# def open(): Solucion 2
#     global img
#     img = ImageTk.PhotoImage(Image.open('Icon.png'))
#     top = Toplevel()
#     top.title('Hola mundo, nueva ventana')
#     l = Label(top, text='Soy un texto en una segunda ventana')
#     l2 = Label(top, image=img)
#     l.pack()
#     l2.pack()

def open(img):
    top = Toplevel()
    top.title('Hola mundo, nueva ventana')
    l = Label(top, text='Soy un texto en una segunda ventana')
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()

img = ImageTk.PhotoImage(Image.open('Icon.png'))
    
btn = Button(root, text='Click', command=lambda: open(img)).pack()

root.mainloop()