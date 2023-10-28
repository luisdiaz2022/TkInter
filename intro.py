from tkinter import *

root = Tk()
root.title('Hola mundo')
root.geometry('400x400')

label = Label(root, text='Hola Mundo! mi primera etiqueta')
# Label(root, text='Hola Mundo! mi primera etiqueta').pack

label.pack()

root.mainloop()