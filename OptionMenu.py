from tkinter import *

root = Tk()
root.title('Hola mundo: Option Menu')
root.geometry('500x500')

def enviar():
    label = Label(root, text=value.get())
    label.pack()

lista = [
    'Chanchito Feliz', 
    'Chanchito Triste', 
    'Chanchito Emocionado'
]

value = StringVar()
value.set(lista[0])

drop = OptionMenu(root, value, *lista)
drop.pack()

btn = Button(root, text='Enviar', command=enviar)
btn.pack()

root.mainloop()