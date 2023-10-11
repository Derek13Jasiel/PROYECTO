from tkinter import *
from PIL import Image, ImageTk



def Menu_principal():
    menu = Tk()
    menu.title("Tablero")
    menu.iconbitmap("usac.ico")
    menu.state('zoomed')#zoomed te deja centrado y pantalla completa
    
    img= (Image.open("bienbenido.jpg"))
    imagen_reducida= img.resize((400,205))
    nueva_imagen= ImageTk.PhotoImage(imagen_reducida)
    mostrar = Label(menu, image= nueva_imagen)
    mostrar.pack()
   
    menu.mainloop()








