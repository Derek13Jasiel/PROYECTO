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
         cuadro_centrado = LabelFrame(curso_nuevo,text="Horario de "+  horario,font="30",width="950",height="450",relief=SUNKEN,bd=10)
         cuadro_centrado.place(x=200, y= 230)
   
 
         inicio = Button(curso_nuevo,text= "INICIO",background="light cyan",font="19")
         inicio.place(x= 20,y=20)
         notas = Button(curso_nuevo,text="Califiaciones",background="light cyan",font="19")
         notas.place(x=80,y= 20)
         #---saber el numero de apartados--------------#
         with open("texto4.txt","r")as f:
           a = (len(f.readlines())) 
           datosapartados = []  
           f.close()
           with open("texto4.txt","r")as leer:
            for w in range(a):
             lecutura = leer.readline()
             separador = lecutura.split('-')
             if (curso==separador[0]):
                apartados_numero = separador[6]
                datosapartados.append(separador[7])
                datosapartados.append(separador[8])


         numero_apartados = int(apartados_numero)#lee el numero de apartados y lo pasa a entero
         print(numero_apartados)

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
                  print("hola falta este apartado")

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

         if (numero_apartados != 0 and numero_apartados>0):
          apartado1 = Button(cuadro_centrado,text=datosapartados[0],font = 50 , width=10, height=5)
          apartado1.place(x= 150, y= 30)
         numero_apartados = numero_apartados-1
         if (numero_apartados != 0 and numero_apartados>0):
          apartado2 = Button(cuadro_centrado,text=datosapartados[1],font = 50 , width=10, height=5)
          apartado2.place(x= 270, y= 30)
         numero_apartados = numero_apartados-1
         
         curso_nuevo.mainloop()


      
        
        
"""with open("texto3.txt","r")as f:
    a = (len(f.readlines())) 
    datos = []
    valor = 2
    valor2 = int(valor)
    entrada ='12'
    f.close()
    conteo = 0
   #----crea una lista llamada datos y agrega todos los valores del texto eceptuando el cambio a realizar---#
with open("texto3.txt","r")as f2:
    for n in range(a):
        word = f2.readline()
        sep = word.split('-')
        datos.append(sep[0])
        datos.append(sep[1])
        datos.append(sep[2])
        datos.append(sep[3])
        datos.append(sep[4])
        datos.append(sep[5])
        if (conteo == valor2):
           datos.append(entrada)
           print("si se pudo")
        else:
           datos.append(sep[6])
           print("no se pudo")
        conteo = conteo + 1

 #----------------escribe nuevamente las lines de codigo con el valor modificado----------#       
print(datos)
with open("texto4.txt","w")as f3:
    n = 0
    for x in range(a):

     f3.write(datos[n+0]+"-"+datos[n+1]+"-"+datos[n+2]+"-"+datos[n+3]+"-"+datos[n+4]+"-"+datos[n+5]+"-"+datos[n+6]+"-"+"v"+"\n")
     n = n + 7
print(datos[20])"""






        

          
         
        
    