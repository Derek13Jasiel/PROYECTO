from tkinter import *
from archivos import verificarPro


def Registro():
    
    registro = Tk()
    registro.geometry("250x300")
    registro.title("Inicio de secion para catedraticos ")
    registro.resizable(0,0)
    registro.iconbitmap("usac.ico")
    #crear los label y botones de ingreso de datos
    nombre_v = StringVar()
    contra_v = StringVar()
    nombre = Label(registro, text= "Usuario")
    nombre.place (x=50, y = 50)
    nombreE = Entry(registro,textvariable=nombre_v)
    nombreE.place(x= 50, y= 80)
    nombre = Label(registro, text= "contraseña")
    nombre.place (x=50, y = 110)
    contraE = Entry(registro,textvariable=contra_v,show='*')
    contraE.place(x= 50, y= 140)

    def  verificar():
      

      if(verificarPro(nombreE.get(),contraE.get())==1):
        print("si se puedo")
      else:
         print("no se puedo")


    boton = Button(registro,text="iniciar",command=verificar)   
    boton.place(x=90, y= 180) 

    registro.mainloop()
    
    








   
