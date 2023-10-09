
# modulo valid


cantidad_estudiantes = 6
cantidad_profesores = 3


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
 
   if  usuario == valor1  or contra == valor1 : # es la validacion de la base de datos,verifica usuario y contraseña
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
   
   
def verificarPro(nombrep,apellidosp,contra2p):
   f2 = open("texto.txt","r")
   for n in range(cantidad_estudiantes):

     separa2 = f2.readline()        
     hola2 = separa2.split('-')
     if nombrep == hola2[0] and apellidosp ==hola2[1] and contra2p == hola2[2]:
       print("prueba")


   



     













    





