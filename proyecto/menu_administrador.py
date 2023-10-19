from tkinter import *
from PIL import Image, ImageTk
from archivos import RegistroCurso


valor1 = ""
valor2 = ""
valor3 = ""
valor4 = ""
valor5 = ""
valor6 = ""

def new_Curso(): # codigo para crear un nuevo curso
        

        curso = Tk()
        curso.geometry("390x350")
        curso.title("crear nuevo curso")
        curso.resizable(0,0)
        curso.iconbitmap("C:/Users/Usuario/Desktop/proyecto/logo.ico")

        nombref = StringVar()
        codigof = StringVar()
        costof =  StringVar()
        horariof = StringVar()
        cupof = StringVar()
        profe = StringVar()

        n_curso= Label(curso, text=  "Nombre del Curso")
        n_curso.place(x = 40 , y = 60)
        n_cursoC= Label(curso, text=  "codigo del curso")
        n_cursoC.place(x = 180 , y = 60)

        n_Entrada = Entry(curso, textvariable=nombref)
        n_Entrada.place(x = 40, y = 90)
        n_EntradaC = Entry(curso, textvariable=codigof)
        n_EntradaC.place(x = 180, y = 90)

        n_costo= Label(curso, text=  "costo del curso")
        n_costo.place(x = 40 , y = 120)
        n_horario= Label(curso, text=  "horario del curso")
        n_horario.place(x = 180 , y = 120)

        n_Entradach = Entry(curso, textvariable=costof)
        n_Entradach.place(x = 40, y = 150)
        n_Entradah = Entry(curso, textvariable=horariof)
        n_Entradah.place(x = 180, y = 150)

        n_cupo= Label(curso, text=  "cupo del curso")
        n_cupo.place(x = 40 , y = 180)
        n_catedratico= Label(curso, text=  "catedratico del curso")
        n_catedratico.place(x = 180 , y = 180)

        n_Entradacc = Entry(curso, textvariable=cupof)
        n_Entradacc.place(x = 40, y = 210)
        n_Entradapc = Entry(curso, textvariable=profe)
        n_Entradapc.place(x = 180, y = 210)

        def confirmarCurso():#envia los valores al registro texto3.txt para guardar los datos del nuevo curso
                RegistroCurso(n_Entrada.get(),n_EntradaC.get(),n_Entradach.get(),n_Entradah.get(),n_Entradacc.get(),n_Entradapc.get())
                valor1 = n_Entrada  #valor del nombre del curso
                valor2 = n_EntradaC #codigo del curso
                valor3 = n_Entradach # costo del curso
                valor4 = n_Entradah # horio del curso
                valor5 = n_Entradacc #cupo del curso
                valor6 = n_Entradapc #nommbre del catedratico asignada al curso
                #nuevo_Curso(valor1,valor2,valor3,valor4,valor5,valor6)        
                

                
        confirmar = Button(curso, text= "Confirmar nuevo curso", command= confirmarCurso)
        confirmar.place(x= 100, y = 250)

"""ef  nuevo_Curso(nombre,codigo,costo,horario,cupo,catedratico):

    menu = Tk()
    menu.title(nombre)
    menu.iconbitmap("usac.ico")
    menu.state('zoomed')#zoomed te deja centrado y pantalla completa
    
    img= (Image.open("bienbenido.jpg"))
    imagen_reducida= img.resize((400,205))
    nueva_imagen= ImageTk.PhotoImage(imagen_reducida)
    mostrar = Label(menu, image= nueva_imagen)
    mostrar.pack()

    
   
    menu.mainloop()  """

        



        
        






    


    
        
        
    
    
    
    
