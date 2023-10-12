from tkinter import*
from win32api import GetSystemMetrics
#rom PIL import Image, ImageTk
ancho = GetSystemMetrics(0)
alto = GetSystemMetrics(1)
class cursonuevo():
     def empezar(self,nombre,codigo,horario): 
         self.nombre = nombre
         self.nombre= Tk()
         self.nombre.title(self.nombre,)
         self.nombre.iconbitmap("usac.ico")
         self.codigo  = codigo
         self.nombre.state('zoomed')#zoomed te deja centrado y pantalla completa
         
         #-----------------------------------------#
         label_superior = Label(self.nombre,background="deep sky blue",width=ancho,height="10")
         label_superior.place(x=0,y=0)

         nombre_delcurso = Label(self.nombre,text=self.nombre,bg="blue",width="40",height="5",font="800")
         nombre_delcurso.place(x=(ancho)/2-170, y=60)
         #---------------crear botones -----------------------#
         inicio = Button(self.nombre,text= "INICIO",background="light cyan",font="19")
         inicio.place(x= 20,y=20)
         notas = Button(self.nombre,text="Califiaciones",background="light cyan",font="19")
         notas.place(x=80,y= 20)
         #-----------apartado de framelabel------------------------#
         cuadro_centrado = LabelFrame(self.nombre,text="Horario de "+horario,font="30",width="950",height="450",relief=SUNKEN,bd=10)
         cuadro_centrado.place(x=200, y= 230)
         #-----------botones de informacion de la 
         informacion = Button(self.nombre,text="informacion",font = 50 , width=10, height=5)
         informacion.place(x= 230, y= 260)
        
   
         self.nombre.mainloop()

 

ventana = cursonuevo() 
ventana2 = cursonuevo()

ventana.empezar("hola","2200","9:00 a 10:00am")
ventana2.empezar("adios","2200","10:00 a12:am")


        

          
         
        
    