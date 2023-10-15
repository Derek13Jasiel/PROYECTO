from tkinter import*
from win32api import GetSystemMetrics
#rom PIL import Image, ImageTk
ancho = GetSystemMetrics(0)
alto = GetSystemMetrics(1)
global valorx 
global valory
valorx = 230
valory = 260
a = 0

     
def nuevo_curso_(curso,codigo,horario):
         
         curso_nuevo = Tk() 
         curso_nuevo.title(curso)
         curso_nuevo.iconbitmap("usac.ico")
         curso_nuevo.state('zoomed')#zoomed te deja centrado y pantalla completa
         
         #-----------------------------------------#
         label_superior = Label(curso_nuevo,background="deep sky blue",width=ancho,height="10")
         label_superior.place(x=0,y=0)

         nombre_delcurso = Label(curso_nuevo,text=curso,bg="white",width="30",height="3",font="Helvetica 30")
         nombre_delcurso.place(x= 330, y=50)
         #-----------apartado de framelabel------------------------#
         cuadro_centrado = LabelFrame(curso_nuevo,text="Horario de "+horario,font="30",width="950",height="450",relief=SUNKEN,bd=10)
         cuadro_centrado.place(x=200, y= 230)
   
 
         inicio = Button(curso_nuevo,text= "INICIO",background="light cyan",font="19")
         inicio.place(x= 20,y=20)
         notas = Button(curso_nuevo,text="Califiaciones",background="light cyan",font="19")
         notas.place(x=80,y= 20)
         #----------------------boton para crear otro boton en el apartado de framlabel------------------#}
         def nuevo():
                 
                 pantalla = Tk()
                 valor_entrada = StringVar()
                 pantalla.geometry("360x370+600+200")
                 pantalla.title("Nuevo Apartado")
                 pantalla.resizable(0,0)
                 pantalla.iconbitmap("usac.ico")
                 
                 mensaje = LabelFrame(pantalla,text="Opciones de nuevo apartado",height="300",width="300")
                 mensaje.place(x=30,y=30)
                 mensaje2 = Label(mensaje,text="Nombre: ")
                 mensaje2.place(x=10,y=20)
                 entrada = Entry(mensaje,width="30",textvariable=valor_entrada)
                 entrada.place(x=80, y=20)
                 #----------funcion para poder agregar nuevo boton----------#
                 a = 0
                 
                 def apartado():
                         boton = Button(cuadro_centrado,text=entrada.get(),font = 50 , width=10, height=5)
                         boton.place(x=150+a,y=30)
                         a = a + 120
                 #---------crear botones de un apartado nuevo-----#
                 boton = Button(mensaje,text="confirmar nuevo apartado",command=apartado)
                 boton.place(x=100,y=60)
                 #--------------------------------------------------#





                 pantalla.mainloop()
         
         crear_boton = Button(curso_nuevo, text="Nuevo apartado",background="light cyan",font="19",command=nuevo)
         crear_boton.place(x=1200,y=20)
         
         
         #-----------botones de informacion------------#
         informacion = Button(cuadro_centrado,text="informacion",font = 50 , width=10, height=5)
         informacion.place(x= 30, y= 30) # x debe de ser 230  y debe de ser 260
         curso_nuevo.mainloop()


      
        
        







        

          
         
        
    