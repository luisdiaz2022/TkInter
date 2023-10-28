from tkinter import *

root = Tk()
root.title('Hola Mundo')

# frame = LabelFrame(root, text='Login', padx=10, pady=10, borderwidth=10)
# frame = Frame(root, padx=10, pady=10, borderwidth=10, text='Login') no permite texto y sin marco
frame = LabelFrame(root, padx=10, pady=10, borderwidth=10, text='Login')
frame.pack(padx=50, pady=50)

l = Label(frame, text='Estoy dentro de un Frame')
btn = Button(frame, text='Salir', command=root.quit)
l.pack()
btn.pack()

root.mainloop()