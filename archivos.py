
# modulo valid
cantidad_estudiantes = 6
cantidad_profesores = 3
valor3 = "h"
valor4 = "h"
def verificar(usuario,contra):
    

   f = open("texto.txt","r")  
   for n in range(cantidad_estudiantes):

     separa = f.readline()        
     hola = separa.split('-')
     if hola[4] == usuario and hola[7]== contra:
        print("saber") #esta parte verifica los datos ingresados de usuario y contraseña.
        print(hola[4]) 
        print("saber")
        print(hola[7])
        print("saber")
        valor1 = hola[4]
        valor2 = hola[7]
 
   if  usuario == valor1  and contra == valor2 : # es la validacion de la base de datos,verifica usuario y contraseña
      print ("si se puedo")
      return 1

   else:

      print("valores finales")
      print(valor1)
      print(valor2)
     
      
   f.close()
   return 0


def valid_registro(nombre,apellido,dpi,celular,usuario,correo,fecha,contra,contra2): #funcion para registrar los datos ingresados en el apartado de registro
   f = open("texto.txt","a")
   f.write("\n"+nombre+"-"+apellido+"-"+dpi+"-"+celular+"-"+usuario+"-"+correo+"-"+fecha+"-"+contra+"-"+contra2)
   f.close()


def verificarPro(usuariop,contrap):
    

   f2 = open("texto2.txt","r")  
   for n in range(cantidad_profesores):

     separa2 = f2.readline()        
     hola2 = separa2.split('-')

     print(hola2[0]+hola2[1])
     

 
   if  usuariop == valor3 and contrap == valor4 : # es la validacion de la base de datos,verifica usuario y contraseña
      print ("si se puedo")
      return 1

   else:

      print("valores finales")
    
     
      
   f2.close()
   return 0   

   
"""def verificarPro(nombrep,contrap):

   f2 = open("texto2.txt","r")
   for n in range(cantidad_profesores):

     separa2 = f2.readline()        
     hola2 = separa2.split('-')
     if valor1 == hola2[0] and valor2 == hola2[1]:
         valor1 = hola2[0]
         valor2 = hola2[1]

   
   if nombrep == valor1 and contrap == valor2:
       return 1
   else:
        return 0
   f2.close() """


def RegistroMaestros(nombre,apellido,dpi,contra,contra2): #funcion para registrar los datos ingresados en el apartado de registro
      f2 = open("texto2.txt","a")
      f2.write("\n"+nombre+"-"+apellido+"-"+dpi+"-"+contra+"-"+contra2)
      f2.close()

   












     
     



   



     













    





