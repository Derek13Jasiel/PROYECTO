from tkinter import *

from PIL import Image, ImageTk




def Menu_principal():
    menu = Tk()
    menu.title("Tablero")
    menu.iconbitmap("usac.ico")
    menu.state('zoomed')#zoomed te deja centrado y pantalla completa
    
    
#----------imagen de fondo-----------#
    img2= (Image.open("fondo1.png"))
    imagen_reducida2= img2.resize((1365,700))
    nueva_imagen2= ImageTk.PhotoImage(imagen_reducida2)
    mostrar2 = Label(menu, image= nueva_imagen2)
    mostrar2.place(x=0,y=0)
 #-------------imagen de bienbenida-----------#   
    img= (Image.open("bienbenido2.png"))
    imagen_reducida= img.resize((380,150))
    nueva_imagen= ImageTk.PhotoImage(imagen_reducida)
    mostrar = Label(mostrar2, image= nueva_imagen)
    mostrar.place(relx=0.37,rely=0.03)
    
    centro_Cursos = LabelFrame(mostrar2,text= "Cursos Asignados",width="800",height="450",relief="sunken",font=("Verdana",24),background="LightBlue1")
    centro_Cursos.place(relx=0.2,rely=0.35)
    #----------funcion crear asignarse nuevo curso-------------#
    def asignarse():
        ventanAsignacion = Toplevel()
        ventanAsignacion.iconbitmap("usac.ico")
        ventanAsignacion.geometry("300x300+910+80")
        ventanAsignacion.resizable(0,0)
        ventanAsignacion.title("Asignarse un curso")
        barra= Menu(ventanAsignacion)
        archivo = Menu(barra)
        archivo.add_command(label= "abrir")
        archivo.add_command(label= "cerrar")
        archivo.add_command(label= "cancelar")
        archivo.add_separator()
        archivo.add_command(label= "salir")
        barra.add_cascade(label= "archivo",menu=archivo)
        ventanAsignacion.config(menu=barra)

    #----------botones ------------------------#

    asignarCurso = Button(mostrar2, text="Asignarse a un curso",font=("Verdana",10),width="20",height="2",command=asignarse)
    asignarCurso.place(relx=0.87,rely=0.01)
    




    menu.mainloop()

def Menu_Profesores():
    menu2 = Tk()
    menu2.title("Apartado de profesores")
    menu2.iconbitmap("usac.ico")
    menu2.state('zoomed')#zoomed te deja centrado y pantalla completa
    
    
#----------imagen de fondo-----------#
    img2= (Image.open("FONDO.webp"))
    imagen_reducida2= img2.resize((1365,700))
    nueva_imagen2= ImageTk.PhotoImage(imagen_reducida2)
    mostrar2 = Label(menu2, image= nueva_imagen2)
    mostrar2.place(x=0,y=0)
 #-------------imagen de bienbenida-----------#   
    img= (Image.open("bienbenido2.png"))
    imagen_reducida= img.resize((380,150))
    nueva_imagen= ImageTk.PhotoImage(imagen_reducida)
    mostrar = Label(mostrar2, image= nueva_imagen)
    mostrar.place(relx=0.37,rely=0.03)
    
    centro_Cursos = LabelFrame(mostrar2,text= "Cursos Asignados",width="800",height="450",relief="sunken",font=("Verdana",24),background="LightBlue1")
    centro_Cursos.place(relx=0.2,rely=0.35)
 


    #----------botones ------------------------#

    asignarCurso = Button(mostrar2, text="Asignarse a un curso",font=("Verdana",10),width="20",height="2")
    asignarCurso.place(relx=0.87,rely=0.01)
    




    menu2.mainloop()    









    


      






