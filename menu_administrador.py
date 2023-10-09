from tkinter import *


def new_Curso(hola ): # codigo para crear un nuevo curso
        nombref = StringVar()
        codigof = StringVar()
        curso = Tk()
        curso.geometry("400x400")
        curso.title(hola)
        curso.iconbitmap("logo.ico")

        n_curso= Label(curso, text=  "Nombre del Curso")
        n_curso.place(x = 40 , y = 60)
        n_cursoC= Label(curso, text=  "codigo del curso")
        n_cursoC.place(x = 180 , y = 60)

        n_Entrada = Entry(curso, textvariable=nombref)
        n_Entrada.place(x = 40, y = 90)
        n_EntradaC = Entry(curso, textvariable=codigof)
        n_EntradaC.place(x = 180, y = 90)

        






    


    
        
        
    
    
    
    
