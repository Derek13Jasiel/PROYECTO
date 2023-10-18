from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
import menu_administrador
from enviar_correo import enviar
import validacion_profe as valid_p
import archivos as valid
from menu_principal import Menu_principal
#import validacion_profe as profe_v
#configuracion  del frame principal
sig = 0 #varible de la parte de modificacion de curso 
global otro
otro = 0

def menu():
    global raiz
   # global pantalla2

    raiz = Tk()
    raiz.title("Inicia de Ceción")
    raiz.geometry("350x400+500+150")
    raiz.resizable(0,0) #no se puede exapandir
    img= (Image.open("usac.png"))
    imagen_reducida= img.resize((320,150))#comando para modificar los valores de altura y anchura de la imagen
    nueva_imagen= ImageTk.PhotoImage(imagen_reducida)
    mostrar = Label(raiz, image= nueva_imagen)
    mostrar.pack()

    #crear mis stringvars 
    nombre = StringVar()
    contraseña = StringVar()
        

    #raiz.config(bg="blue", cursor= "circle")#color y mouse
    raiz.iconbitmap("logo.ico")

    #crear labels de la Universidad
    #texto = Label(raiz,text="UNIVERSIDAD DE SAN CARLOS")
    #texto.pack()
    #texto2 = Label(raiz,text="DE GUATEMALA")
    #texto2.pack()

    def recuperarf():
        recuperar_r = Toplevel()
        recuperar_r.geometry("350x400+500+150")
        recuperar_r.resizable(0,0)
        recuperar_r.iconbitmap("usac.ico")
        usuario_v = StringVar()
        correo_v = StringVar()
        mensaje = Label(recuperar_r,text="Ingrese Sus datos",font=("curier 18"))
        mensaje.place(x=50,y=40)
        mensaje = Label(recuperar_r,text="Usuario")
        mensaje.place(x=20,y=140)
        mensaje = Label(recuperar_r,text="correo electronico")
        mensaje.place(x=20,y=200)
        usuario = Entry(recuperar_r,textvariable=usuario_v)
        usuario.place(x=150,y=140)
        correo = Entry(recuperar_r,textvariable=correo_v)
        correo.place(x=150,y=200)
        def confirmar():
            with open("texto3.txt","r")as f:
                a = len(f.readlines())
                f.close()
                valor = 0
            with open("texto3.txt","r")as f2:    
                for x in range(a):
                    palabra = f2.readline()
                    sep = palabra.split('-')
                    if (usuario.get()==sep[4]and correo.get()==sep[5]):
                        enviar(usuario.get(),correo.get(),sep[7])
                        valor = 1
                        messagebox.showinfo("Recuperacion","Se le ha enviado su contraseña por su correo electronico")
                if(valor != 1):
                 messagebox.showerror("Hubo un Problema","El Usuario o el correo no coinciden o no estan registrados")
        confirmar_boton = Button(recuperar_r,text="confirmar",command=confirmar)
        confirmar_boton.place(x=130,y=250)


    #crear labels de ingreso de datos nombre y contraseña
    texto3 = Label(raiz,text="Nombre",font=("curier 10"), bd= 4)
    texto3.place(x = 30, y = 160)
    texto4 = Label(raiz,text="contraseña",font=("curier 10"), bd= 4)
    texto4.place(x = 30, y = 180)
    recuperar = Button(raiz,text="recuperar mi contraseña",command=recuperarf)
    recuperar.place(x=100,y=370)

    #crear entradas para nombre y contraseña
    entrada = Entry(raiz,textvariable=nombre)#nombre
    entrada.place(x = 110, y = 160)
    entrada = Entry(raiz,textvariable=contraseña,show='*')#contraseña
    entrada.place(x = 110, y = 180)


    #funciones
    #funcion validar administracion y validar usuarios
    def adminf():
        
        if nombre.get() == "admin" and  contraseña.get()== "1234": #verificacion del administrador
            administracion()
            
        else:
           if(valid.verificar(nombre.get(),contraseña.get()) == 1) :
               #llama a la funcion verificar del modulo valid 
                
               inicio(nombre.get())

           elif (valid.verificar(nombre.get(),contraseña.get()) != 1):
               messagebox.showerror("Hubo un problema","Usuario o contraseña incorrecta")
                  
           
               


    def inicio(usuario):
        raiz.destroy()#importante destruir los widgets antes de pasar a otro 
        
        Menu_principal(usuario)#llama a la funcion menu principal desde el modulo de menu principal
 
    
    #crear botones 
    cecion = Button(raiz, text = "Iniciar Ceción" , command= adminf, bg="#b5b5b5",bd = 0)
    cecion.place( x = 130 , y = 220)

    registrarse = Button(raiz, text = "registrarse", command= registrarsef , bg="#b5b5b5",bd = 0 )
    registrarse.place (x = 170, y = 280)

    maestro = Button(raiz, text = "Maestro", command= maestrof , bg="#b5b5b5",bd = 0 )
    maestro.place (x = 110, y = 280)




    raiz.mainloop()


def registrarsef(): #CREA EL MUNU DE RISGISTRO
    pantalla2 = Toplevel()
    pantalla2.geometry("400x500+300+200")
    pantalla2.title("Registrarse")
    pantalla2.resizable(0,0)
    pantalla2.iconbitmap("usac.ico")
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
    contra= Entry(pantalla2,textvariable=vcontra,show='*') 
    contra.place(x=180 , y = 280)

    contra2 = Label(pantalla2, text="Confirmar contraseña",font=("curier 10"))
    contra2.place(x=50, y= 310)
    contra2= Entry(pantalla2,textvariable=vcontra2,show='*') 
    contra2.place(x=180 , y = 310)
    def seleccionar():

            global img_tk
            pantalla2.filename = filedialog.askopenfilename(title="buscar imagenes")

            #label1 = Label(pantalla2,text=pantalla2.filename)
            #label1.pack()

            img = Image.open(pantalla2.filename)
            nueva = img.resize((100,100))
            img_tk = ImageTk.PhotoImage(nueva)

            label2 = Label(pantalla2,image = img_tk)
            label2.place(x=180,y=340)





    def validar():#metodo llama a validar el registro 
        #se verifica el usuario y si este no se repite
        valor_de_verificacion = 0
        with open("texto.txt","r")as ver:
            a = len(ver.readlines())
            ver.close()
            print(a)
        with open("texto.txt","r")as ver2: 
            for n in range(a):
                 
              palabra = ver2.readline()
              sep = palabra.split('-')

              if (usuario.get()==sep[4]):
                  valor_de_verificacion = 1
        ver2.close() 
        if(nombre.get()!= "" and apellido.get()!="" and celular.get()!="" and usuario.get()!=""and fecha.get()!= ""and contra.get()!="" and contra2.get()!=""):

            _contra_ = contra.get()       
            if(contra.get()!=contra2.get()):
                messagebox.showerror("Error ","Contraseñas no coinciden")
                valor_de_verificacion = 2
            elif(len(contra.get())<8):
                messagebox.showerror("Error ","La contraseña es de 8 caracteres")
                valor_de_verificacion = 2
            elif(_contra_.islower()==True):
                messagebox.showerror("Error ","La contraseña debe Tener Mayusculas")
                valor_de_verificacion = 2
            """ elif(_contra_.isdigit()==False):
                messagebox.showerror("Error ","La contraseña debe Tener un Digito")
                valor_de_verificacion = 2  """  

                
            if(valor_de_verificacion ==0):      
                valid.valid_registro(nombre.get(),apellido.get(),DPI.get(),celular.get(),usuario.get(),correo.get(),fecha.get(),contra.get(),contra2.get())
                print(nombre.get() + apellido.get())
            elif(valor_de_verificacion == 1):
                messagebox.showerror("Usuario No Valido","El Usuario  "+usuario.get()+"  Ya esta rigistrado")  
        else:
          messagebox.showerror("Error ","Todas las casillas deben estar completadas")        

#------------boton para seleccionar la imagen y para validar el registro-----------
    buscar = Button(pantalla2,text="Seleccione una foto",command=seleccionar)
    buscar.place(x=50, y=380)    

    
    boton = Button(pantalla2, text= "confirmar",command=validar,font=("curier 10"))
    boton.place(x= 180, y= 450)

def maestrof():
    raiz.destroy()
    valid_p.Registro()
    
sig = 0    
#------------------------Administrador---------------------------------------------------------#
def administracion():
    raiz.destroy()
    pantalla4 = Tk()
    pantalla4.geometry("400x400")
    pantalla4.title("Administracion ")
    pantalla4.iconbitmap("logo.ico")
    pantalla4.resizable(0,0)
    global va 
    va = 0
    global sig
    sig = 0
    

    entorno = LabelFrame(pantalla4,text="Opciones de Administrador",width="295",height="300", fg="black")
    entorno.place(relx=0.1,rely=0.1)

    
    
    
    def  regisMaestros():#esta parte sera para crear el entorno al registro de maestro
        pantalla4.destroy()
        pantalla5_registro = Tk()
        pantalla5_registro.geometry("300x300")
        pantalla5_registro.iconbitmap("logo.ico")
        pantalla5_registro.title("registro de Maestros")
        
        pantalla5_registro.resizable(0,0)

        nombre_v = StringVar()
        apellido_v = StringVar()
        dpi_v = StringVar()
        Contra_v = StringVar()
        contra2_v = StringVar()

        #crear las label y entradas para el registro de maestros
        nombre = Label(pantalla5_registro,text="Nombre")
        nombre.place(x= 30, y= 40)
        nombre_e = Entry(pantalla5_registro,textvariable= nombre_v)
        nombre_e.place(x= 100, y= 40)
        apellido = Label(pantalla5_registro,text="Apellido")
        apellido.place(x= 30, y= 70)
        apellido_e = Entry(pantalla5_registro,textvariable= apellido_v)
        apellido_e.place(x= 100, y= 70)
        dpi = Label(pantalla5_registro,text="DPI")
        dpi.place(x= 30, y= 100)
        dpi_e = Entry(pantalla5_registro,textvariable= dpi_v)
        dpi_e.place(x= 100, y= 100)
        contra = Label(pantalla5_registro,text="Contraseña")
        contra.place(x= 30, y= 130)
        contra_e = Entry(pantalla5_registro,textvariable= Contra_v,show='*')
        contra_e.place(x= 100, y= 130)
        contra2 = Label(pantalla5_registro,text="confirme ")
        contra2.place(x= 30, y= 160)
        contra_e = Entry(pantalla5_registro,textvariable= contra2_v,show='*')
        contra_e.place(x= 100, y= 160)
        #funcion  para registrar en el modulo valid(archivos)con el metodo registromaestro()
        def registrar_M():

            valid.RegistroMaestros(nombre_v.get(),apellido_v.get(),dpi_v.get(),Contra_v.get(),contra2_v.get())
           

        confirmar = Button(pantalla5_registro,text="Confirmar",command=registrar_M)
        confirmar.place(x= 100 , y = 180  )
#-------------------------------------------------------------------
    with open("texto4.txt","r")as f:#esto debe pasar a texto3
        a = len(f.readlines())
        f.close()
        guardar = []
        with open("texto4.txt","r")as f2:
         for n in range(a):
            linea = f2.readline()
            sep = linea.split('-')
            guardar.append(sep[0])
            guardar.append(sep[1])
            guardar.append(sep[2])
            guardar.append(sep[3])
            guardar.append(sep[4])
            guardar.append(sep[5])
            
        
#---------------------------------------------------------------
    def llamar():
        pantalla4.destroy()
        menu_administrador.new_Curso()

    def  MaestrosRegistrados():
        print("print registrar mestros")

    def  verCursos():
        hola = StringVar()
        print(hola)
    
        
                


         
    def editarcurso():
        print("modificar")
        mod = Toplevel()
        mod.geometry("450x200")
        mod.iconbitmap("logo.ico")
        mod.resizable(0,0)
        
        curso_v = StringVar()
        costo_v = StringVar()
        horario_v= StringVar()
        codigo_v = StringVar()
        cup_v = StringVar()
        catedratico_v = StringVar()
#----------apartado de entrada para ver o modificar curso--------------#
        nombre_curso = Label(mod,text="     curso                     codigo       costo      horario      cupo       catedratico")
        nombre_curso.place(x= "10",y="10")
        curso = Entry(mod,width="15",textvariable=curso_v)#curso
        curso. place(x= 10, y=50)
        costo = Entry(mod,width="5",textvariable=costo_v)#codigo
        costo. place(x= 120, y=50)
        horario = Entry(mod,width="5",textvariable=horario_v)#costo
        horario. place(x= 170, y=50)
        codigo = Entry(mod,width="12",textvariable=codigo_v)#horario
        codigo. place(x= 220, y=50)
        cupo = Entry(mod,width="5",textvariable=cup_v)#cupo
        cupo. place(x= 310, y=50)
        catedratico = Entry(mod,width="15",textvariable=catedratico_v)#catedratico
        catedratico. place(x= 350, y=50)
        
        def siguiente():
            global otro #elimina el texto en los entry 
            curso.delete(first=0,last=20)
            costo.delete(first=0,last=20)
            horario.delete(first=0,last=20)
            codigo.delete(first=0,last=20)
            cupo.delete(first=0,last=20)
            catedratico.delete(first=0,last=20)

            curso.insert(7,guardar[0+otro])#agrega los valores de los cusos 
            costo.insert(7,guardar[1+otro])
            horario.insert(7,guardar[2+otro])
            codigo.insert(7,guardar[3+otro])
            cupo.insert(7,guardar[4+otro])
            catedratico.insert(7,guardar[5+otro])
            otro = otro +6
            if (otro == 6*a):
                otro = 0
            #----------------------------------------------------------#                
        def modificarf():
            respuesta = messagebox.askyesno("Modificar", "¿Esta Seguro que desea Modificar?")
            if (respuesta == True):
                with open("texto4.txt","r")as f:
                    num = len(f.readlines())
                    f.close()
                    datosmodificados1 = []
                with open("texto4.txt","r")as f2:
                    for n in range(num):
                        word = f2.readline()
                        sep1 = word.split('-')
                        if (otro==(n+1)*6):#---------si otro es igual a  n*6  entonces agrega los valores en las entradas
                            print(str(otro)+"--vr--"+str((n+1)*6))
                            datosmodificados1.append(curso.get())
                            datosmodificados1.append(costo.get())
                            datosmodificados1.append(horario.get())
                            datosmodificados1.append(codigo.get())
                            datosmodificados1.append(cupo.get())
                            datosmodificados1.append(catedratico.get())
                        else:
                            datosmodificados1.append(sep1[0])    
                            datosmodificados1.append(sep1[1])
                            datosmodificados1.append(sep1[2])
                            datosmodificados1.append(sep1[3])
                            datosmodificados1.append(sep1[4])
                            datosmodificados1.append(sep1[5])
                        datosmodificados1.append(sep1[6])
                        datosmodificados1.append(sep1[7])
                        datosmodificados1.append(sep1[8])
                        datosmodificados1.append(sep1[9])
                        datosmodificados1.append(sep1[10])
                        datosmodificados1.append(sep1[11])
                        datosmodificados1.append(sep1[12])
                        datosmodificados1.append(sep1[13])
                        datosmodificados1.append(sep1[14])
                        

                    with open("texto4.txt","w")as f3:
                        extra = 0
                        for x in range(num):

                         f3.write(datosmodificados1[extra+0]+"-"+datosmodificados1[extra+1]+"-"+datosmodificados1[extra+2]+"-"+datosmodificados1[extra+3]+"-"+datosmodificados1[extra+4]+"-"+datosmodificados1[extra+5]+"-"+datosmodificados1[extra+6]+"-"+datosmodificados1[extra+7]+"-"+datosmodificados1[extra+8]+"-"+datosmodificados1[extra+9]+"-"+datosmodificados1[extra+10]+"-"+datosmodificados1[extra+11]+"-"+datosmodificados1[extra+12]+"-"+datosmodificados1[extra+13]+"-"+datosmodificados1[extra+14]+"-"+"v"+"\n")
                         extra = extra + 15

        def eliminar():
            respuesta2 = messagebox.askyesno("Eliminar", "¿Esta Seguro que desea Eliminar el Curso?")
            if(respuesta2 == True):
                with open("texto4.txt","r")as f:
                    num = len(f.readlines())
                    f.close()
                    datosmodificados1 = []
                with open("texto4.txt","r")as f2:
                    for n in range(num):
                        word = f2.readline()
                        sep1 = word.split('-')
                        if (otro==(n+1)*6):#---------si otro es igual a  n*6  entonces agrega los valores en las entradas
                            print(str(otro)+"--vr--"+str((n+1)*6))
                        else:
                            datosmodificados1.append(sep1[0])    
                            datosmodificados1.append(sep1[1])
                            datosmodificados1.append(sep1[2])
                            datosmodificados1.append(sep1[3])
                            datosmodificados1.append(sep1[4])
                            datosmodificados1.append(sep1[5])
                            datosmodificados1.append(sep1[6])
                            datosmodificados1.append(sep1[7])
                            datosmodificados1.append(sep1[8])
                            datosmodificados1.append(sep1[9])
                            datosmodificados1.append(sep1[10])
                            datosmodificados1.append(sep1[11])
                            datosmodificados1.append(sep1[12])
                            datosmodificados1.append(sep1[13])
                            datosmodificados1.append(sep1[14])
                        

                    with open("texto4.txt","w")as f3:
                        extra = 0
                        for x in range(num-1):

                         f3.write(datosmodificados1[extra+0]+"-"+datosmodificados1[extra+1]+"-"+datosmodificados1[extra+2]+"-"+datosmodificados1[extra+3]+"-"+datosmodificados1[extra+4]+"-"+datosmodificados1[extra+5]+"-"+datosmodificados1[extra+6]+"-"+datosmodificados1[extra+7]+"-"+datosmodificados1[extra+8]+"-"+datosmodificados1[extra+9]+"-"+datosmodificados1[extra+10]+"-"+datosmodificados1[extra+11]+"-"+datosmodificados1[extra+12]+"-"+datosmodificados1[extra+13]+"-"+datosmodificados1[extra+14]+"-"+"v"+"\n")
                         extra = extra + 15
                siguiente()         
        siguiente()             

                    

                    
  
            
  #------------------------------------------------------------------------
  
        botonmodificar = Button(mod,text="Modificar",width="10",height="2",bg="green",command=modificarf)
        botonmodificar.place(x=50,y=130)
        botoneliminar = Button(mod,text="Eliminar",width="10",height="2",bg="red",command=eliminar)
        botoneliminar.place(x=170,y=130)      
        botonsiguiente = Button(mod,text="Siguiente",width="10",height="2",bg="yellow",command=siguiente)
        botonsiguiente.place(x=300,y=130)


        
    

        
        
#--------------------creacion de botones para el modo administrador----------------------------------------#

    #boton registrar nuevo maestro
    registrar = Button(entorno,text= "Registrar Maestros",command= regisMaestros,width="32")
    registrar.place(relx=0.1, rely=0.1)    

    #boton crear nuevo curso
    crear_curso = Button(entorno, text= "crear nuevo curso", command= llamar,width="32")   
    crear_curso.place(relx=0.1 , rely=0.2)

    #boton para ver curso creados
    verC = Button(entorno, text= "Cursos creados", command= verCursos,width="32")   
    verC.place(relx=0.1 , rely=0.3)

    #boton para ver Maestros Registrados
    VerP = Button(entorno, text= "Maestros registrados", command= MaestrosRegistrados,width="32")   
    VerP.place(relx=0.1 , rely=0.4)
     #boton para modificar curso
    modificar = Button(entorno, text= "modificar curso", command= editarcurso,width="32")   
    modificar.place(relx=0.1 , rely=0.5)

    


            
    

menu() # esta empieza la funcion menu   



