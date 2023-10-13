from tkinter import *
from archivos import verificarPro
from menu_principal import Menu_Profesores
global registro
#----------registro y menu de los profesores------------------#
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
         print("No se puedo")
       #-----------------------------------------------#
    
    boton = Button(registro,text="iniciar",command= verificar)
    boton.place(x= 100, y = 180)

    registro.mainloop()

#--------funcion vizualiza el apartado del menu del catedratico-----------#
     

def Menu_principal(usuario,registro):#
    #------mandamos a ver los curso y si los el catedratico esta asigna
    resultado = ["","","","","","","","","","","","","","","","","","","","","",""]   
    #verCurso(dpi)
    #print(usuario)

    
    f2 = open("texto3.txt","r",encoding='utf-8')#obtener las clases
    
    b = 0
    
      
    for n in range(4):
     lector = f2.readline()

     sep = lector.split('-')

     if sep[5]== usuario:
        print(sep[5])
        print(sep[0])
        
        resultado[b]= sep[0]
        b = b + 1
    f2.close()


    Menu_Profesores()


    #------------------------#
    print(resultado)
  


  





    








   
