from tkinter import *
from clases_del_curso import nuevo_curso_
from PIL import Image, ImageTk


"""esta  modulo esta divido en dos partes
el menú principal del estudiente y el menu 
principal del Menu princpal del maestro
1) estudiante
2)profesor"""
global valor_iterraciones
valor_iterraciones = 0

global clases_asignadas
global informacion


def Menu_principal(usuario):
    menu = Tk()
    menu.title("Tablero")
    menu.iconbitmap("C:/Users/Usuario/Desktop/proyecto/usac.ico")
    menu.state('zoomed')#zoomed te deja centrado y pantalla completa

    def leer():
      with open("C:/Users/Usuario/Desktop/proyecto/texto.txt","r")as saber_iterraciones:
         valor_de_filas = len(saber_iterraciones.readlines())
         saber_iterraciones.close()
      with open("C:/Users/Usuario/Desktop/proyecto/texto.txt","r")as saber_iterraciones2:
         
         global valor_iterraciones
         global clases_asignadas
         
         clases_asignadas = []

         for m in range(valor_de_filas):
            palabra_d = saber_iterraciones2.readline()
            separador = palabra_d.split('-')

            if(usuario == separador[4]):
               #print(usuario+"     "+separador[4])
               #print(separador[8])
               valor_iterraciones = int(separador[8])
               clases_asignadas.append(separador[9])
               clases_asignadas.append(separador[10])
               clases_asignadas.append(separador[11])
               clases_asignadas.append(separador[12])
               clases_asignadas.append(separador[13])
               clases_asignadas.append(separador[14])

              # print(valor_iterraciones)
              # print(clases_asignadas)
      with open("C:/Users/Usuario/Desktop/proyecto/texto4.txt")as cl:
         cl_s =  len(cl.readlines())
         cl.close()
      global informacion   
      informacion = []   
      
      with open("C:/Users/Usuario/Desktop/proyecto/texto4.txt")as cl2:
         for n in range(cl_s):
          palabra_i = cl2.readline()
          sep3 = palabra_i.split('-')
          m = 0
          for s in range(len(clases_asignadas)):
            if(clases_asignadas[m]==sep3[0]):
               informacion.append(sep3[1])#codigo
               informacion.append(sep3[3])#horario
               informacion.append(sep3[5])#catedratico 
            m = m + 1  

      print(informacion)
      saber_iterraciones2.close()
    leer()

    
    
#----------imagen de fondo-----------#
    img2= (Image.open("C:/Users/Usuario/Desktop/proyecto/fondo1.png"))
    imagen_reducida2= img2.resize((1365,700))
    nueva_imagen2= ImageTk.PhotoImage(imagen_reducida2)
    mostrar2 = Label(menu, image= nueva_imagen2)
    mostrar2.place(x=0,y=0)
 #-------------imagen de bienbenida-----------#   
    img= (Image.open("C:/Users/Usuario/Desktop/proyecto/bienbenido2.png"))
    imagen_reducida= img.resize((380,150))
    nueva_imagen= ImageTk.PhotoImage(imagen_reducida)
    mostrar = Label(mostrar2, image= nueva_imagen)
    mostrar.place(relx=0.37,rely=0.03)
    
    centro_Cursos = LabelFrame(mostrar2,text= "Cursos Asignados",width="800",height="450",relief="sunken",font=("Verdana",24),background="LightBlue1")
    centro_Cursos.place(relx=0.2,rely=0.35)
    #----------funcion crear asignarse nuevo curso-------------#
    def asignarse():
      root = Tk()  
      root.title("Asignar Un Curso") 
      root.geometry('380x380') 
      root.iconbitmap("C:/Users/Usuario/Desktop/proyecto/usac.ico")
      root.resizable(0,0)
      with open("C:/Users/Usuario/Desktop/proyecto/texto4.txt","r")as f:
         a = len(f.readlines())
         f.close()
         clases_disponibles = []
         profesores_disponibles = []
         horarios_disponible = []
         costo_disponibles = []
         codigo_disponibles = []
      with open("C:/Users/Usuario/Desktop/proyecto/texto4.txt","r")as f2:

       for n in range(a):
        fila = f2.readline()
        sep = fila.split('-')
        clases_disponibles.append(sep[0])
        codigo_disponibles.append(sep[1])
        costo_disponibles.append(sep[2])
        horarios_disponible.append(sep[3])
        profesores_disponibles.append(sep[5])
      f2.close()
      
      seleccione = Label(root,text="Seleccione una clase")
      seleccione.place(x=30,y=40)


      valor = StringVar(root) 
      valor.set("Cursos") 

      menu_clases = OptionMenu(root, valor, *clases_disponibles) 
      menu_clases.place(x=180,y=40)

      informacion = LabelFrame(root,text="informacion del curso",width="330",height="200")
      informacion.place(x=30,y=100)
      
      
      def verinformacion(): 
         #---obtenemos la posicion de el valor.get() y buscamos hoario y profesor en sus respectivas listas
         b = clases_disponibles.index(valor.get())

         profesores_variable =  profesores_disponibles[b]
         codigo_variable = codigo_disponibles[b]
         costo_variable = costo_disponibles[b]
         horario_variable = horarios_disponible[b]

         profesores = Label(informacion,text=profesores_variable,bg="red",width="14",anchor='w')
         profesores.place(x=200,y=50)
         horario = Label(informacion,text=horario_variable,bg="red",width="14")
         horario.place(x=200,y=80)
         codigo = Label(informacion,text=codigo_variable,bg="red",width="14")
         codigo.place(x=200,y=110)
         costo = Label(informacion,text=costo_variable,bg="red",width="14")
         costo.place(x=200,y=140)
###########################################################3
         return None
      def asignarsef():
         with open("C:/Users/Usuario/Desktop/proyecto/texto.txt","r")as fila:
            c = len(fila.readlines()) #numero de filas de el apartado de registro(texto.txt)
            print(c)
            datos = []#----------esta lista se almacenaran todos los datos de texto.txt
            fila.close()#codigo es para leer los archivos y reescribirlos (texto.txt) agregando los nuevos apartados
         with open("C:/Users/Usuario/Desktop/proyecto/texto.txt","r")as fila2:

            for n in range(c):
                     
                  cadena = fila2.readline()
                  sep2 = cadena.split('-')#14
                  
                  datos.append(sep2[0])
                  datos.append(sep2[1])
                  datos.append(sep2[2])
                  datos.append(sep2[3])
                  datos.append(sep2[4])#apartado de usuario
                  datos.append(sep2[5])
                  datos.append(sep2[6])
                  datos.append(sep2[7])
                  if (usuario==sep2[4]): #sirve para localizar al uzuario y incertar la nueva
                     num = int(sep2[8])
                     datos.append(str(num+1))
                     if(num == 0):
                      datos.append(valor.get())
                     else:
                      datos.append(sep2[9])
                     if(num == 1):
                      datos.append(valor.get())
                     else:
                      datos.append(sep2[10])    
                     if(num == 2):
                      datos.append(valor.get())
                     else:
                      datos.append(sep2[11])
                     if(num == 3):
                      datos.append(valor.get())
                     else:
                      datos.append(sep2[12])
                     if(num == 4):
                      datos.append(valor.get())
                     else:
                      datos.append(sep2[13])
                     if(num == 5):
                      datos.append(valor.get())
                     else:
                      datos.append(sep2[14]) 
                  else:
                     datos.append(sep2[8])
                     datos.append(sep2[9])
                     datos.append(sep2[10])
                     datos.append(sep2[11])
                     datos.append(sep2[12])
                     datos.append(sep2[13])  
                     datos.append(sep2[14])  

         with open("C:/Users/Usuario/Desktop/proyecto/texto.txt","w")as f3:
            n = 0
            for x in range(c):

               f3.write(datos[n+0]+"-"+datos[n+1]+"-"+datos[n+2]+"-"+datos[n+3]+"-"+datos[n+4]+"-"+datos[n+5]+"-"+datos[n+6]+"-"+datos[n+7]+"-"+datos[n+8]+"-"+datos[n+9]+"-"+datos[n+10]+"-"+datos[n+11]+"-"+datos[n+12]+"-"+datos[n+13]+"-"+datos[n+14]+"-"+"v"+"\n")
               n = n + 15
         global informacion      
         informacion.clear()                 
         clases_disponibles.clear()
         #print(clases_asignadas)
         valor_iterraciones = num +1
         leer()
         iterar(valor_iterraciones)
         #print(datos)
      
###############################################################         



      asignarse = Button(root,text="Asignarse",command=asignarsef)#lla a la funcion para asignar un nuevo curso
      asignarse.place(x=150,y= 320)

      prueba = Label(informacion,textvariable=valor) 
      prueba.place(x=200,y=20)

      info = Label(informacion,text="curso:")
      info.place(x=130,y=20)
      info = Label(informacion,text="Catedratico:")
      info.place(x=130,y=50)
      info = Label(informacion,text="Horario:")
      info.place(x=130,y=80)
      info = Label(informacion,text="Codigo:")
      info.place(x=130,y=110)
      info = Label(informacion,text="Costo:")
      info.place(x=130,y=140)


      verInformacion = Button(informacion, text='ver informacion', command=verinformacion) 
      verInformacion.place(x=20,y=120)



      
      root.mainloop() 

    #----------botones ------------------------#


    asignarCurso = Button(mostrar2, text="Asignarse a un curso",font=("Verdana",10),width="20",height="2",command=asignarse)
    asignarCurso.place(relx=0.87,rely=0.01)
    def accion():
       nuevo_curso_(clases_asignadas[0],informacion[0],informacion[1],informacion[2],"E")
    def accion2():
       nuevo_curso_(clases_asignadas[1],informacion[3],informacion[4],informacion[5],"E")
    def accion3():
       nuevo_curso_(clases_asignadas[2],informacion[6],informacion[7],informacion[8],"E")
    def accion4():
       nuevo_curso_(clases_asignadas[3],informacion[9],informacion[10],informacion[11],"E")  
    def accion5():
       nuevo_curso_(clases_asignadas[4],informacion[12],informacion[13],informacion[14],"E")  
    def accion6():
       nuevo_curso_(clases_asignadas[5],informacion[15],informacion[16],informacion[17],"E")         
    
    #simula el numero de clases asignadas
    def iterar(iteraciciones):
      
      if(iteraciciones != 0 and iteraciciones >0):
         boton1 = Button(centro_Cursos,width="19",height="9",text=clases_asignadas[0],command=accion)
         boton1.place(x=100,y=50)
      iteraciciones= iteraciciones - 1 
      if(iteraciciones != 0 and iteraciciones >0):
         boton2 = Button(centro_Cursos,width="19",height="9",text=clases_asignadas[1],command=accion2)
         boton2.place(x=300,y=50)
      iteraciciones= iteraciciones - 1 
      if(iteraciciones != 0 and iteraciciones >0):   
         boton3 = Button(centro_Cursos,width="19",height="9",text=clases_asignadas[2],command=accion3)
         boton3.place(x=500,y=50)
      iteraciciones= iteraciciones - 1 
      if(iteraciciones != 0 and iteraciciones >0):   
         boton4 = Button(centro_Cursos,width="19",height="9",text=clases_asignadas[3],command=accion4)
         boton4.place(x=100,y=230)
      iteraciciones= iteraciciones - 1 
      if(iteraciciones != 0 and iteraciciones >0):   
         boton5 = Button(centro_Cursos,width="19",height="9",text=clases_asignadas[4],command=accion5)
         boton5.place(x=300,y=230)
      iteraciciones= iteraciciones - 1 
      if(iteraciciones != 0 and iteraciciones >0):   
         boton6 = Button(centro_Cursos,width="19",height="9",text=clases_asignadas[5],command=accion6)
         boton6.place(x=500,y=230)
    iterar(valor_iterraciones)
    print(valor_iterraciones)


    menu.mainloop()


#-------------------------------------------------------------------------    

def Menu_Profesores(clases,catedratico):
    numero_clases = len(clases)
    print(numero_clases)#numero de clases asignadas a un profesor
    menu2 = Tk()
    menu2.title("Apartado de profesores")
    menu2.iconbitmap("C:/Users/Usuario/Desktop/proyecto/usac.ico")
    menu2.state('zoomed')#zoomed te deja centrado y pantalla completa
    print(clases)
    valor_agregado = 10 - numero_clases
    for n in range(valor_agregado):
     clases.append("")
    
    
#----------imagen de fondo-----------#
    img2= (Image.open("C:/Users/Usuario/Desktop/proyecto/FONDO.webp"))
    imagen_reducida2= img2.resize((1365,700))
    nueva_imagen2= ImageTk.PhotoImage(imagen_reducida2)
    mostrar2 = Label(menu2, image= nueva_imagen2)
    mostrar2.place(x=0,y=0)
 #-------------imagen de bienbenida-----------#   
    img= (Image.open("C:/Users/Usuario/Desktop/proyecto/bienbenido2.png"))
    imagen_reducida= img.resize((380,150))
    nueva_imagen= ImageTk.PhotoImage(imagen_reducida)
    mostrar = Label(mostrar2, image= nueva_imagen)
    mostrar.place(relx=0.37,rely=0.03)
    
    centro_Cursos = LabelFrame(mostrar2,text= "Cursos Asignados",width="800",height="450",relief="sunken",font=("Verdana",24),background="LightBlue1")
    centro_Cursos.place(relx=0.2,rely=0.35)
#-------funciones para los apartado de clases asignadas
    def accion0():
        #curso,codigo y horario
        with open("C:/Users/Usuario/Desktop/proyecto/texto4.txt","r")as f:
           a = len(f.readlines())
           f.close()
        with open("C:/Users/Usuario/Desktop/proyecto/texto4.txt","r")as f2:
           for n in range(a):
              info = f2.readline()   
              sep0 = info.split('-')
              if ( clases[0] == sep0[0] ):
                 horario0 = sep0[3]
           f2.close()     
        nuevo_curso_(clases[0],"90",horario0,catedratico,"M")#llama a la funcion nuevo curso desde clases del cuso
    def accion1():
        #curso,codigo y horario
        with open("C:/Users/Usuario/Desktop/proyecto/texto4.txt","r")as f:
           a = len(f.readlines())
           f.close()
        with open("C:/Users/Usuario/Desktop/proyecto/texto4.txt","r")as f2:
           for n in range(a):
              info = f2.readline()   
              sep0 = info.split('-')
              if ( clases[1] == sep0[0] ):
                 horario1 = sep0[3]   
        f2.close()              
        nuevo_curso_(clases[1],"90",horario1,catedratico,"M")#llama a la funcion nuevo curso desde clases del cuso
    def accion2():
        #curso,codigo y horario
        with open("C:/Users/Usuario/Desktop/proyecto/texto4.txt","r")as f:
           a = len(f.readlines())
           f.close()
        with open("C:/Users/Usuario/Desktop/proyecto/texto4.txt","r")as f2:
           for n in range(a):
              info = f2.readline()   
              sep0 = info.split('-')
              if ( clases[2] == sep0[0] ):
                 horario2 = sep0[3]   
        f2.close() 
        nuevo_curso_(clases[2],"90",horario2,catedratico,"M")#llama a la funcion nuevo curso desde clases del cuso
    def accion3():
        #curso,codigo y horario
        with open("C:/Users/Usuario/Desktop/proyecto/texto4.txt","r")as f:
           a = len(f.readlines())
           f.close()
        with open("C:/Users/Usuario/Desktop/proyecto/texto4.txt","r")as f2:
           for n in range(a):
              info = f2.readline()   
              sep0 = info.split('-')
              if ( clases[3] == sep0[0] ):
                 horario3 = sep0[3]   
        f2.close() 
        nuevo_curso_(clases[3],"90",horario3,catedratico,"M")#llama a la funcion nuevo curso desde clases del cuso
    def accion4():
        #curso,codigo y horario
        with open("C:/Users/Usuario/Desktop/proyecto/texto4.txt","r")as f:
           a = len(f.readlines())
           f.close()
        with open("C:/Users/Usuario/Desktop/proyecto/texto4.txt","r")as f2:
           for n in range(a):
              info = f2.readline()   
              sep0 = info.split('-')
              if ( clases[4] == sep0[0] ):
                 horario4 = sep0[3]   
        f2.close() 
        nuevo_curso_(clases[4],"90",horario4,catedratico,"M")#llama a la funcion nuevo curso desde clases del cuso    
#-------------------------------------------------------                

    #asignarCurso= []

#-----------crear cursos automaticamente---------""
#no funcion esta parte correctamente
    a = 0
    n = 0
    """for n in range(len(clases)):
         asignarCurso.append(n)
         asignarCurso[n]= Button(centro_Cursos, text=clases[n],font=("Verdana",10),width="10",height="5",command=accion())
         asignarCurso[n].place(x=30+a,y = 30) 
         a = a + 120  
         n = n+1"""
    if(numero_clases != 0 and numero_clases>0):
     asignarCurso0= Button(centro_Cursos, text=clases[n],font=("Verdana",10),width="10",height="5",command=accion0)
     asignarCurso0.place(x=30+a,y = 30)

     n = n +1
     a = a + 120
    numero_clases= numero_clases - 1 
    if(numero_clases != 0 and numero_clases>0):
     asignarCurso1= Button(centro_Cursos, text=clases[n],font=("Verdana",10),width="10",height="5",command=accion1)
     asignarCurso1.place(x=30+a,y = 30)

     n = n +1
     a = a + 120
    numero_clases= numero_clases - 1 
    if(numero_clases != 0 and numero_clases>0):
     asignarCurso2= Button(centro_Cursos, text=clases[n],font=("Verdana",10),width="10",height="5",command=accion2)
     asignarCurso2.place(x=30+a,y = 30)
    
     n = n +1
     a = a + 120
    numero_clases= numero_clases - 1 
    if(numero_clases != 0 and numero_clases>0 ):
     asignarCurso3= Button(centro_Cursos, text=clases[n],font=("Verdana",10),width="10",height="5",command=accion3)
     asignarCurso3.place(x=30+a,y = 30)
      
     n = n +1
     a = a + 120
    numero_clases= numero_clases - 1  
    if(numero_clases != 0 and numero_clases>0):
     asignarCurso4= Button(centro_Cursos, text=clases[n],font=("Verdana",10),width="10",height="5",command=accion4)
     asignarCurso4.place(x=30+a,y = 30)
     print("este es el ultimo dato ")
     print(type(numero_clases))
     print(numero_clases)
     n = n +1
     a = a + 120
    numero_clases= numero_clases - 1  

 ################################################
    

         


    #----------botones ------------------------#
    





    menu2.mainloop()    









    


      






