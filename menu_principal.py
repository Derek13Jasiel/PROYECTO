from tkinter import *
from clases_del_curso import nuevo_curso_
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

def Menu_Profesores(clases):
    menu2 = Tk()
    menu2.title("Apartado de profesores")
    menu2.iconbitmap("usac.ico")
    menu2.state('zoomed')#zoomed te deja centrado y pantalla completa
    print(clases)
    
    
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

    def accion():
        #curso,codigo y horario
        nuevo_curso_(clases[0],"90","10am")#llama a la funcion nuevo curso desde clases del cuso
    def accion2():
        #curso,codigo y horario
        nuevo_curso_(clases[1],"90","10am")#llama a la funcion nuevo curso desde clases del cuso
    def accion3():
        #curso,codigo y horario
        nuevo_curso_(clases[2],"90","10am")#llama a la funcion nuevo curso desde clases del cuso
    def accion4():
        #curso,codigo y horario
        nuevo_curso_(clases[3],"90","10am")#llama a la funcion nuevo curso desde clases del cuso    
                


        



    #asignarCurso= []

#-----------crear cursos automaticamente---------""
#no funcion esta parte correctamente
    a = 0
    n = 0
    """for n in range(len(clases)):
         asignarCurso.append(n)
         asignarCurso[n]= Button(centro_Cursos, text=clases[n],font=("Verdana",10),width="10",height="5",command=accion())
         asignarCurso[n].place(x=30+a,y = 30) 
         a = a + 120  
         n = n+1"""
    asignarCurso1= Button(centro_Cursos, text=clases[n],font=("Verdana",10),width="10",height="5",command=accion)
    asignarCurso1.place(x=30+a,y = 30) 
    n = n +1
    a = a + 120
    asignarCurso2= Button(centro_Cursos, text=clases[n],font=("Verdana",10),width="10",height="5",command=accion2)
    asignarCurso2.place(x=30+a,y = 30) 
    n = n +1
    a = a + 120
    asignarCurso3= Button(centro_Cursos, text=clases[n],font=("Verdana",10),width="10",height="5",command=accion3)
    asignarCurso3.place(x=30+a,y = 30) 
    n = n +1
    a = a + 120
    asignarCurso4= Button(centro_Cursos, text=clases[n],font=("Verdana",10),width="10",height="5",command=accion4)
    asignarCurso4.place(x=30+a,y = 30) 
    n = n +1
    a = a + 120   
 ################################################
    

         


    #----------botones ------------------------#
    





    menu2.mainloop()    









    


      






