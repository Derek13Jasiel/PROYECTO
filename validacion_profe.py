from tkinter import *
from tkinter import messagebox
from archivos import verificarPro
from menu_principal import Menu_Profesores
global registro
#----------registro y menu de los profesores------------------#
def Registro():
    
    registro = Tk()
    registro.geometry("250x300+550+200")
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
    contra = Label(registro, text= "contraseña")
    contra.place (x=50, y = 110)
    contraE = Entry(registro,textvariable=contra_v,show='*')
    contraE.place(x= 50, y= 140)

    def  verificar():
      
       #-------------------------------------------------#
      if(verificarPro(nombreE.get(),contraE.get())==1):
        print("si se puedo")
        Menu_principal(nombreE.get(),registro.destroy())#envia el nombre al la funcion menu princiapal  y destruye la ventana de registro
        

      else:
         messagebox.showerror("hubo un problema","usuario o contraseña incorrecta")
       #-----------------------------------------------#
    
    boton = Button(registro,text="iniciar",command= verificar)
    boton.place(x= 100, y = 180)

    registro.mainloop()

#--------funcion vizualiza el apartado del menu del catedratico-----------#
     

def Menu_principal(usuario,registro):#
    #------mandamos a ver los curso y si los el catedratico esta asigna
  registro
  with open("texto3.txt","r") as f:
    a = len(f.readlines())
    
    f.close()
    with open("texto3.txt","r")as f2:
     resultado= []
     for n in range(a):
       palabra = f2.readline()
       sep = palabra.split('-')
       print(sep[0])
       print(sep[5])

       print(type(sep[0]))
       if (usuario and sep[5]):#parte a resolver
         resultado.append(sep[0])
         print(n+1)
                
    f2.close()

    
    


    Menu_Profesores(resultado)


    #------------------------#
    print(resultado)
  


  





    








   
