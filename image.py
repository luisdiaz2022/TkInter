from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hola Mundo')

# imagen = Image.open('icon.png')
# imagen.show()

img = ImageTk.PhotoImage(Image.open('icon.png'))
l = Label(image=img)
l.pack()

root.mainloop()