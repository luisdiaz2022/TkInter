from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Hola Mundo: Archivos')

# root.filename = filedialog.askopenfilename(title='Elige  una foto', filetypes=(("Archivos PNG", "*.png"), ('Todos', '*')))
# label = Label(root, text=root.filename)
# label.pack()
# img = Image.open(root.filename)
# imgTK = ImageTk.PhotoImage(img)

# label2 = Label(root, image=imgTK)
# label2.pack()

def open():
    global imgTK
    root_filename = filedialog.askopenfilename(title='Elige  una foto', filetypes=(("Archivos PNG", "*.png"), ('Todos', '*')))
    label = Label(root, text=root_filename)
    label.pack()
    img = Image.open(root_filename)
    imgTK = ImageTk.PhotoImage(img)
    
    l2 = Label(root, image=imgTK)
    l2.pack()

btn = Button(root, text='Cargar Imagen', command=open)
btn.pack()

root.mainloop()