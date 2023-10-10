from tkinter import *
from tkinter import messagebox
import menu_administrador
import validacion_profe as valid_p
import archivos as valid
#import validacion_profe as profe_v
#configuracion  del frame principal


def menu():
   # global pantalla1
   # global pantalla2

    raiz = Tk()
    raiz.title("login")
    raiz.geometry("350x400")
    raiz.resizable(0,0) #no se puede exapandir

    #crear mis stringvars 
    nombre = StringVar()
    contraseña = StringVar()
        

    #raiz.config(bg="blue", cursor= "circle")#color y mouse
    raiz.iconbitmap("logo.ico")

    #crear labels de la Universidad
    texto = Label(raiz,text="UNIVERSIDAD DE SAN CARLOS")
    texto.pack()
    texto2 = Label(raiz,text="DE GUATEMALA")
    texto2.pack()

    #crear labels de ingreso de datos nombre y contraseña
    texto3 = Label(raiz,text="Nombre",font=("curier 10"), bd= 4)
    texto3.place(x = 30, y = 140)
    texto4 = Label(raiz,text="contraseña",font=("curier 10"), bd= 4)
    texto4.place(x = 30, y = 160)

    #crear entradas para nombre y contraseña
    entrada = Entry(raiz,textvariable=nombre)#nombre
    entrada.place(x = 110, y = 140)
    entrada = Entry(raiz,textvariable=contraseña,show='*')#contraseña
    entrada.place(x = 110, y = 160)


    #funciones
    #funcion validar administracion y validar usuarios
    def adminf():
    
        if nombre.get() == "admin" and  contraseña.get()== "1234": #verificacion del administrador
            administracion()
            raiz.quit
        else:
           if(valid.verificar(nombre.get(),contraseña.get()) == 1) :
               #llama a la funcion verificar del modulo valid 
                
               inicio()
           elif (valid.verificar(nombre.get(),contraseña.get()) == 0):
               messagebox.showerror("hubo un problema","usuario o contraseña incorrecta")
                  
           
               


    def inicio():
        
        administracion()
 
        
    
    #crear botones 
    cecion = Button(raiz, text = "Iniciar Ceción" , command= adminf, bg="#b5b5b5",bd = 0)
    cecion.place( x = 130 , y = 200)

    registrarse = Button(raiz, text = "registrarse", command= registrarsef , bg="#b5b5b5",bd = 0 )
    registrarse.place (x = 170, y = 280)

    maestro = Button(raiz, text = "Maestro", command= maestrof , bg="#b5b5b5",bd = 0 )
    maestro.place (x = 110, y = 280)




    raiz.mainloop()


def registrarsef(): #CREA EL MUNU DE RISGISTRO
    pantalla2 = Toplevel()
    pantalla2.geometry("400x400")
    pantalla2.title("Registrarse")
    pantalla2.resizable(0,0)
    #string vars para la entrada en registro
    vnombre = StringVar()
    vapellido = StringVar()
    vdpi = StringVar()
    vcelular = StringVar()
    vusuario = StringVar()
    vcorreo = StringVar()
    vfecha = StringVar()
    vcontra= StringVar()
    vcontra2 = StringVar()

    #crear las label de ingreso de datos 
    info = Label(pantalla2, text="INGRESE SUS DATOS",font=("curier 14"))
    info.pack()

    nombre = Label(pantalla2, text="Nombre ",font=("curier 10"))
    nombre.place(x=50, y= 60)
    nombre = Entry(pantalla2,textvariable= vnombre) 
    nombre.place(x=110 , y = 60)

    apellido = Label(pantalla2, text="Apellido ",font=("curier 10"))
    apellido.place(x=50, y= 90)
    apellido = Entry(pantalla2,textvariable=vapellido) 
    apellido.place(x=110 , y = 90)

    DPI = Label(pantalla2, text="DPI ",font=("curier 10"))
    DPI.place(x=50, y= 120)
    DPI = Entry(pantalla2) 
    DPI.place(x=110 , y = 120)

    celular = Label(pantalla2, text="Teléfono ",font=("curier 10"))
    celular.place(x=50, y= 150)
    celular= Entry(pantalla2,textvariable=vcelular) 
    celular.place(x=110 , y = 150)

    usuario = Label(pantalla2, text="Nombre de Usuario ",font=("curier 10"))
    usuario.place(x=50, y= 190)
    usuario= Entry(pantalla2,textvariable=vusuario) 
    usuario.place(x=180 , y = 190)

    correo = Label(pantalla2, text="Correo electronico",font=("curier 10"))
    correo.place(x=50, y= 220)
    correo= Entry(pantalla2,textvariable=vcorreo) 
    correo.place(x=180 , y = 220)

    fecha = Label(pantalla2, text="Fecha de Nacimiento ",font=("curier 10"))
    fecha.place(x=50, y= 250)
    fecha= Entry(pantalla2,textvariable=vfecha) 
    fecha.place(x=180 , y = 250)
    #codigo para la contraseña y para confirmarla
    contra = Label(pantalla2, text="Contraseña ",font=("curier 10"))
    contra.place(x=50, y= 280)
    contra= Entry(pantalla2,textvariable=vcontra) 
    contra.place(x=180 , y = 280)

    contra2 = Label(pantalla2, text="Confirmar contraseña",font=("curier 10"))
    contra2.place(x=50, y= 310)
    contra2= Entry(pantalla2,textvariable=vcontra2) 
    contra2.place(x=180 , y = 310)

    def validar():#metodo llama a validar el registro 
        valid.valid_registro(nombre.get(),apellido.get(),DPI.get(),celular.get(),usuario.get(),correo.get(),fecha.get(),contra.get(),contra2.get())
        print(nombre.get() + apellido.get())

    
    boton = Button(pantalla2, text= "confirmar",command=validar,font=("curier 10"))
    boton.place(x= 180, y= 350)

def maestrof():
    valid_p.Registro()
    

def administracion():
    pantalla4 = Toplevel()
    pantalla4.geometry("400x400")
    pantalla4.title("Administracion ")
    
    def  regisMaestros():#esta parte sera para crear el entorno al registro de maestro
        pantalla4_registro = Toplevel()
        pantalla4_registro.geometry("300x300")
        pantalla4_registro.title("registro de Maestros")
        pantalla4_registro.resizable(0,0)

        nombre_v = StringVar()
        apellido_v = StringVar()
        dpi_v = StringVar()
        Contra_v = StringVar()
        contra2_v = StringVar()

        #crear las label y entradas para el registro de maestros
        nombre = Label(pantalla4_registro,text="Nombre")
        nombre.place(x= 30, y= 40)
        nombre_e = Entry(pantalla4_registro,textvariable= nombre_v)
        nombre_e.place(x= 100, y= 40)
        apellido = Label(pantalla4_registro,text="Apellido")
        apellido.place(x= 30, y= 70)
        apellido_e = Entry(pantalla4_registro,textvariable= apellido_v)
        apellido_e.place(x= 100, y= 70)
        dpi = Label(pantalla4_registro,text="DPI")
        dpi.place(x= 30, y= 100)
        dpi_e = Entry(pantalla4_registro,textvariable= dpi_v)
        dpi_e.place(x= 100, y= 100)
        contra = Label(pantalla4_registro,text="Contraseña")
        contra.place(x= 30, y= 130)
        contra_e = Entry(pantalla4_registro,textvariable= Contra_v,show='*')
        contra_e.place(x= 100, y= 130)
        contra2 = Label(pantalla4_registro,text="confirme ")
        contra2.place(x= 30, y= 160)
        contra_e = Entry(pantalla4_registro,textvariable= contra2_v,show='*')
        contra_e.place(x= 100, y= 160)
        #funcion  para registrar en el modulo valid(archivos)con el metodo registromaestro()
        def registrar_M():

            valid.RegistroMaestros(nombre_v.get(),apellido_v.get(),dpi_v.get(),Contra_v.get(),contra2_v.get())

        confirmar = Button(pantalla4_registro,text="Confirmar",command=registrar_M)
        confirmar.place(x= 100 , y = 180  )

    def llamar():
        menu_administrador.new_Curso("hola")
        pantalla4.iconify


    #boton registrar nuevo maestro
    registrar = Button(pantalla4,text= "Registrar Mestros",command= regisMaestros)
    registrar.place(x=180, y= 40)    

    #boton crear nuevo curso
    crear_curso = Button(pantalla4, text= "crear nuevo curso", command= llamar)   
    crear_curso.place(x = 30 , y = 40)
    


            
    

       

menu() # esta empieza la funcion menu   



