from tkinter import *
from tkinter import filedialog

a = 10
for n in range(10):
    a = a -1 
    print(a)
print(a)    


"""raiz = Tk()
raiz.geometry("350x400")

#--------------abre los archivos para saber los cursos disponibles(archivo:texto3.txt)-------#

with open("texto3.txt","r") as f:
    a = len(f.readlines())
    
    f.close()
    with open("texto3.txt","r")as f2:
     resultado= []
     for n in range(a):
       palabra = f2.readline()
       sep = palabra.split('-')
       resultado.append(sep[0])       
         
f2.close()
#------------------------------funcion Accion---------------

def hola():
  info1_v = Label(mostrar,textvariable=valor)
  info1_v.place(x= 50,y=15)
    



    #-------------------------------------------------
valor = StringVar()

mostrar = LabelFrame(text="Informacion del curso",height="200",width="260")
mostrar.place(x=40,y= 130)
info1 = Label(mostrar,text="clase")
info1.place(x= 15,y=15)

opcion_curso = Label(raiz,text="Seleccione un Curso")
opcion_curso.place(x=30,y=30)

menu = OptionMenu(raiz,valor, *resultado,command=hola)
menu.config(height="2",width="15")
menu.place(x=150, y=30)



raiz.mainloop()"""



 #----------esta parte si funciona ------------""#" 
"""with open("texto3.txt","r") as f:
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
       if ("Julio Alberto" == sep[5]):#parte a resolver
         resultado.append(sep[0])
         print(n+1)
         

print(resultado)         
         
    


f2.close"""


#------------para abrir un archivo
"""raiz = Tk()
def abrir():
    archivo = filedialog.askopenfilename(title="abrir",initialdir="C:/")

boton = Button(raiz,text="abrir",command=abrir) 
boton.pack()
raiz.mainloop()"""""
############-----------------------#  
"""a = "2209"
b = 0
x = 0
resultado= ["","","","",""]
f = open("texto4.txt")
variable = f.readline()
var = int(variable)

hola = "Derek-2022-mate","Derek-2022-Fisica","andrea-2209-mate2","andrea-2209-laboratorio","Derek-2022-programacion"
for n in range(var):
    palabra = hola[n]

    palabra2 = palabra.split('-')

    if palabra2[1]== a:
        
        resultado[b]= palabra2[2]
        b = b + 1

        
            
        
print(resultado)"""""

"""hola = open("texto4.txt")
for n in range(0):
    sep = hola.readline()
    sep2 = sep.split('-')
    print(sep2[0])
    print(sep2[1])
    #print(sep[2])
    
    #print(sep[3])


hola.close() """   

"""""#------------------------verificacion de maestros-------------------------------#texto2.txt

def verificarPro(usuariop,contrap): #funcion para verificar a los maestro en el login para catedraticos
   f2 = open("texto2.txt","r",encoding="utf-8")
   valor2 = ""
   valor3 = ""
   
   for n in range(cantidad_profesores):
       
       datos = f2.readline()
       
       sep = datos.split('-')
       print(sep[0] + "--"+sep[3])
       print("--usuario y contraseña")


       if "Julio Alberto"== usuariop and "uno"== contrap:
          valor2= sep[0]      
          valor3= sep[3]
          
          print("valor2 = "+valor2+"----------valor3 = "+valor3)
          return 1
       else:
          return 0
         
 
        
   if valor2 == usuariop and valor3 == contrap:
      f2.close()
      return 1
      
   else:
      f2.close()
      return 0
   
   #-----------------------#"""
#-------------por si se me arruina esta es la parte de la verificacion de el profesor ------------#
""""def verificarPro(usuariop,contrap): #funcion para verificar a los maestro en el login para catedraticos
   f2 = open("texto2.txt","r",encoding="utf-8")
   valor2 = ""
   valor3 = ""
   
   for n in range(cantidad_profesores):
       
       datos = f2.readline()
       
       sep = datos.split('-')
       print(sep[0] + "--"+sep[3])
       print("--usuario y contraseña")


       if sep[0]== usuariop and sep[3]== contrap:
          valor2= sep[0]      
          valor3= sep[3]
          
          print("valor2 = "+valor2+"----------valor3 = "+valor3)
          f2.close()
          return 1
       
         
 
        

   
   #-----------------------#"""




       


    