from tkinter import *

root = Tk()
root.title('Hola mundo: Checkbox')

root.geometry('500x500')

var = StringVar()
var.set('si')

def mostrar():
    label = Label(root, text=var.get())
    label.pack()

checkbox = Checkbutton(root, text='Soy un checkbox', variable=var, onvalue='si', offvalue='no')
checkbox.pack()

btn = Button(root, text='Click', command=mostrar)
btn.pack()

root.mainloop()