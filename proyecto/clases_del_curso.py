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
         numero_apartados = "0"
         datosapartados = []  
         def leerapartados(apartados_numero):
          with open("texto4.txt","r")as f:
            a = (len(f.readlines())) 
            
            f.close()
            with open("texto4.txt","r")as leer:
               for w in range(a):
                lecutura = leer.readline()
                separador = lecutura.split('-')
                if (curso==separador[0]):
                  apartados_numero = separador[6]
                  datosapartados.append(separador[7])
                  datosapartados.append(separador[8])
                  datosapartados.append(separador[9])
                  datosapartados.append(separador[10])
                  datosapartados.append(separador[11])
                  datosapartados.append(separador[12])
                  datosapartados.append(separador[13])
                  datosapartados.append(separador[14])

          return apartados_numero    
            
         

         numero_apartados = int(leerapartados(numero_apartados))#lee el numero de apartados y lo pasa a entero
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
                 entrada = Entry(mensaje,width="30",textvariable=valor_entrada)# este es el entre para asignarle nombre a los apartados
                 entrada.place(x=80, y=20)
                 #----------funcion para poder agregar nuevo boton----------#
                 a = 0
                 
                 def apartado():
                  print("hola falta este apartado")
                  with open("texto4.txt","r")as f:
                     a = len(f.readlines()) 
                     datos = []
                     f.close()
                     def apartado_previo():
                        with open("texto4.txt","r")as f2:
                           for n in range(a):
                              word = f2.readline()
                              sep = word.split('-')
                              if(curso == sep[0]):
                                 print(sep[6])
                                 valor_de_apartado = sep[6]
                                 

                        return valor_de_apartado
                  

                           
                     
                     valor_apartado = int(apartado_previo())
                     valor_apartado = valor_apartado + 1
                     salida = str(valor_apartado)
                     print(salida)
 #--------------------------esta parte modifica el valor de los apartados sep[6]------------------------
                  with open("texto4.txt","r")as f2:
                     for n in range(a):
                        word = f2.readline()
                        sep = word.split('-')
                        datos.append(sep[0])
                        datos.append(sep[1])
                        datos.append(sep[2])
                        datos.append(sep[3])
                        datos.append(sep[4])
                        datos.append(sep[5])
                        if (curso == sep[0]):
                           datos.append(salida)
                           print("si se pudo")
                           if(valor_apartado == 1):
                              datos.append(entrada.get())    #parte donde se le asigna el nombre con el valor_entrada.get()
                           else:
                              datos.append(sep[7])
                           if(valor_apartado == 2):
                              datos.append(entrada.get())    
                           else:
                              datos.append(sep[8])
                           if(valor_apartado == 3):
                              datos.append(entrada.get())   
                           else:
                              datos.append(sep[9])
                           if(valor_apartado == 4):
                              datos.append(entrada.get())    
                           else:
                              datos.append(sep[10])
                           if(valor_apartado == 5):
                              datos.append(entrada.get())   
                           else:
                              datos.append(sep[11])
                           if(valor_apartado == 6):
                              datos.append(entrada.get())    
                           else:
                              datos.append(sep[12])
                           if(valor_apartado == 7):
                              datos.append(entrada.get())    
                           else:
                              datos.append(sep[13])
                           if(valor_apartado == 8):
                              datos.append(entrada.get())    
                           else:
                              datos.append(sep[14]) 


                        else:
                           datos.append(sep[6])
                           print("no se pudo")
                           datos.append(sep[7])
                           datos.append(sep[8])
                           datos.append(sep[9])
                           datos.append(sep[10])
                           datos.append(sep[11])
                           datos.append(sep[12])
                           datos.append(sep[13])
                           datos.append(sep[14])
                          
                                  
                            
                         

                     


                  #----------------escribe nuevamente las lines de codigo con el valor modificado----------#       
                  print(datos)
                  with open("texto4.txt","w")as f3:
                     n = 0
                     for x in range(a):

                        f3.write(datos[n+0]+"-"+datos[n+1]+"-"+datos[n+2]+"-"+datos[n+3]+"-"+datos[n+4]+"-"+datos[n+5]+"-"+datos[n+6]+"-"+datos[n+7]+"-"+datos[n+8]+"-"+datos[n+9]+"-"+datos[n+10]+"-"+datos[n+11]+"-"+datos[n+12]+"-"+datos[n+13]+"-"+datos[n+14]+"-"+"v"+"\n")
                        n = n + 15
                  print(datos[20])#por si sale mal
                  #-------prueba para eliminar los elmentes de la lista datosapartados
                  datosapartados.clear()
                  

                  #------------------------------------------------#
                  leerapartados("hola")              
                                 
#----------------------------------------------------------------------------------------------------------------------------------              
                  iterar_botones(valor_apartado)      

                 #---------crear botones de un apartado nuevo-----#
                 boton = Button(mensaje,text="confirmar nuevo apartado",command=apartado)
                 boton.place(x=100,y=60)
                 
                 #--------------------------------------------------#





                 pantalla.mainloop()
         
         crear_boton = Button(curso_nuevo, text="Nuevo apartado",background="light cyan",font="19",command=nuevo)
         crear_boton.place_forget()#x=1200,y=20   
         
         
         #-----------botones de informacion------------#
         informacion = Button(cuadro_centrado,text="informacion",font = 50 , width=10, height=5)
         informacion.place(x= 30, y= 30) # x debe de ser 230  y debe de ser 260

         def iterar_botones(numero_apartados):
          if (numero_apartados != 0 and numero_apartados>0):
            apartado1 = Button(cuadro_centrado,text=datosapartados[0],font = 50 , width=10, height=5)
            apartado1.place(x= 150, y= 30)
            numero_apartados = numero_apartados-1
          if (numero_apartados != 0 and numero_apartados>0):
            apartado2 = Button(cuadro_centrado,text=datosapartados[1],font = 50 , width=10, height=5)
            apartado2.place(x= 270, y= 30)
            numero_apartados = numero_apartados-1
          if (numero_apartados != 0 and numero_apartados>0):
            apartado3 = Button(cuadro_centrado,text=datosapartados[2],font = 50 , width=10, height=5)
            apartado3.place(x= 390, y= 30)
            numero_apartados = numero_apartados-1
          if (numero_apartados != 0 and numero_apartados>0):
            apartado4 = Button(cuadro_centrado,text=datosapartados[3],font = 50 , width=10, height=5)
            apartado4.place(x= 510, y= 30)
            numero_apartados = numero_apartados-1
          if (numero_apartados != 0 and numero_apartados>0):
            apartado5 = Button(cuadro_centrado,text=datosapartados[4],font = 50 , width=10, height=5)
            apartado5.place(x= 630, y= 30)
            numero_apartados = numero_apartados-1
          if (numero_apartados != 0 and numero_apartados>0):
            apartado6 = Button(cuadro_centrado,text=datosapartados[5],font = 50 , width=10, height=5)
            apartado6.place(x= 30, y=  200)
            numero_apartados = numero_apartados-1 
          if (numero_apartados != 0 and numero_apartados>0):
            apartado6 = Button(cuadro_centrado,text=datosapartados[6],font = 50 , width=10, height=5)
            apartado6.place(x= 150, y=  200)
            numero_apartados = numero_apartados-1
          if (numero_apartados != 0 and numero_apartados>0):
            apartado6 = Button(cuadro_centrado,text=datosapartados[7],font = 50 , width=10, height=5)
            apartado6.place(x= 270, y=  200)
            numero_apartados = numero_apartados-1                                     

         iterar_botones(numero_apartados)


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






        

          
         
        
    