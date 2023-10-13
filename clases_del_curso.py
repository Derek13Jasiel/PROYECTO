from tkinter import*
from win32api import GetSystemMetrics
#rom PIL import Image, ImageTk
ancho = GetSystemMetrics(0)
alto = GetSystemMetrics(1)
global valorx 
global valory
valorx = 230
valory = 260

class cursonuevo():
     
     def __init__(self,master,curso,codigo,horario):
          
         self.nombre = Frame(master)
         self.nombre.title(curso)
         self.nombre.iconbitmap("usac.ico")
         self.codigo  = codigo
         self.nombre.state('zoomed')#zoomed te deja centrado y pantalla completa
         
         #-----------------------------------------#
         label_superior = Label(self.nombre,background="deep sky blue",width=ancho,height="10")
         label_superior.place(x=0,y=0)

         nombre_delcurso = Label(self.nombre,text=curso,bg="blue",width="40",height="5",font="800")
         nombre_delcurso.place(x=(ancho)/2-170, y=60)
         #-----------apartado de framelabel------------------------#
         cuadro_centrado = LabelFrame(self.nombre,text="Horario de "+horario,font="30",width="950",height="450",relief=SUNKEN,bd=10)
         cuadro_centrado.place(x=200, y= 230)
         #---------------crear botones -----------------------#
         def nuevo_apartado(variable):
          variable = variable + 120
          print("HOLA")
          informacion2 = Button(self.nombre,text="musica" ,font = 50 , width=10, height=5)
          informacion2.place(x= variable, y= 260)#estamos haciendo pruebas
 
         inicio = Button(self.nombre,text= "INICIO",background="light cyan",font="19")
         inicio.place(x= 20,y=20)
         notas = Button(self.nombre,text="Califiaciones",background="light cyan",font="19")
         notas.place(x=80,y= 20)
         #----------------------boton para crear otro boton en el apartado de framlabel------------------#}
         hoy = 230
         crear_boton = Button(self.nombre, text="mumento",command=nuevo_apartado(hoy),background="light cyan",font="19")
         crear_boton.place(x=1200,y=20)
         
         
         #-----------botones de informacion------------#
         informacion = Button(self.nombre,text="informacion",font = 50 , width=10, height=5)
         informacion.place(x= valorx, y= valory) # x debe de ser 230  y debe de ser 260


      
        
          
root = Tk()
ventana = cursonuevo(root,"mate basica","22022","9:00 a 10:00") 
root.mainloop()






        

          
         
        
    