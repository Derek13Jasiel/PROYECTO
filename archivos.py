from cryptography.fernet import Fernet

# modulo valid
cantidad_estudiantes = 6
cantidad_profesores = 2
#---------funcion para encriptar y desencriptar -----------------#
def codificacion():
#-------crear clave y convertir el mensaje a bytes    
    clave = Fernet.generate_key()
    mensaje = "hola".encode()#pasa de str a bytes para encoding
    f = Fernet(clave)#atribuir a la variable f las  propiedades del modulo Fernet#
#----------ENCRIPTAR-----------------#    
    encriptado = f.encrypt(mensaje)
    print(encriptado)
    print("hola mundo")
#-----------DESENCRIPTAR--------------#
    desencriptado = f.decrypt(encriptado)
    print(desencriptado)
    encoding = 'utf-8' #tipo de encoding
    paso = str(desencriptado, encoding)#pasa de bytes a str
    

    if paso == "hola":
        print("avanzamos")
    else:
        print("no se puedo")

#--------------verificar usuario----------------#
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
   if(contra == contra2):
  
      f = open("texto.txt","a")
      f.write(nombre+"-"+apellido+"-"+dpi+"-"+celular+"-"+usuario+"-"+correo+"-"+fecha+"-"+contra+"\n")
      f.close()






def verificarPro(usuariop,contrap): #funcion para verificar a los maestro en el login para catedraticos
   f2 = open("texto2.txt")


   for n in range(cantidad_profesores):
       datos = f2.readline()
       
       sep = datos.split('-')

       #print(sep[0])
       #print(sep[1])
       if sep[0 ]== usuariop and sep[1]== contrap:
          valor2= sep[0]      
          valor3= sep[1]
         
 
   f2.close()     
   if valor2 == usuariop and valor3 == contrap:
      return 1
   else:
      return 0
   



def RegistroMaestros(nombre,apellido,dpi,contra,contra2): #funcion para registrar los datos ingresados en el apartado de registro
      f2 = open("texto2.txt","a")
      f2.write("\n"+nombre+"-"+apellido+"-"+dpi+"-"+contra+"-"+contra2)
      f2.close()

def RegistroCurso(curso,codigo,costo,horario,cupo,catedratico): #funcion para registrar los cursos desde el modulo administrador
      f3 = open("texto3.txt","a")
      f3.write("\n"+curso+"-"+costo+"-"+horario+"-"+cupo+"-"+catedratico)
      f3.close()



   












     
     



   



     













    





