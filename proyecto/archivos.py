

# modulo valid


#--------------verificar usuario----------------#text.txt
def verificar(usuario,contra):
   with open("texto.txt","r") as f:
    a = len(f.readlines())
    
   f.close()    

   f = open("texto.txt","r",encoding="utf-8")  
   valor2 = ""
   valor3 = ""
   for n in range(a):

     separa = f.readline()        
     hola = separa.split('-')
     print(hola[4]+"---"+hola[7])
     if (hola[7] == contra  and hola[4].strip() == usuario):
         print("valor2 = "+valor2+"----------valor3 = "+valor3)
         return 1
   f.close() 



   """ if hola[4] == usuario or hola[7] == contra:
         print("valor2 = "+valor2+"----------valor3 = "+valor3)
         return 1
   f.close() """



#------------------------verificacion de maestros-------------------------------#texto2.txt

def verificarPro(usuariop,contrap): #funcion para verificar a los maestro en el login para catedraticos
   
  
   f2 = open("texto2.txt","r",encoding="utf-8")
   a = len(f2.readlines())
   f2.close()
   valor2 = ""
   valor3 = ""

   f2_v = open("texto2.txt","r",encoding="utf-8")
   for n in range(a):
       
       datos = f2_v.readline()
       
       sep = datos.split('-')
       print(sep[0] + "--"+sep[3])
       print("--usuario y contraseña")


       if (sep[0]== usuariop and sep[3]== contrap)==True:
          valor2= sep[0]      
          valor3= sep[3]
          
          print("valor2 = "+valor2+"----------valor3 = "+valor3)
          f2.close()
          return 1
   f2_v.close()     
 
        

   
   #-----------------------#
 
   

#---------------------------------registros a llamar------------------------------------------------#

#----------------registros de alumnos--------------------------#texto.txt
def valid_registro(nombre,apellido,dpi,celular,usuario,correo,fecha,contra,contra2): #funcion para registrar los datos ingresados en el apartado de registro
   if(contra == contra2):
      
      with open("texto.txt","a")as f:
       f.write(nombre+"-"+apellido+"-"+dpi+"-"+celular+"-"+usuario+"-"+correo+"-"+fecha+"-"+contra+"-"+"0"+"-"+"0"+"-"+"0"+"-"+"0"+"-"+"0"+"-"+"0"+"-"+"v"+"\n")
       f.close()#cada estudiente puede ser asignadoa 6 cursos

#-----------------registro de maestros-------------------------#texto2.txt
def RegistroMaestros(nombre,apellido,dpi,contra,contra2): #funcion para registrar los datos ingresados en el apartado de registro
    if(contra == contra2):
      with open("texto2.txt","a")as f2:
       f2.write(nombre+"-"+apellido+"-"+dpi+"-"+contra+"-"+"v"+"\n")
       f2.close()

#-----------------registro de cursos----------------------------#texto3.txt

def RegistroCurso(curso,codigo,costo,horario,cupo,catedratico): #funcion para registrar los cursos desde el modulo administrador
     
      with open("texto4.txt","a")as f3:

       f3.write(curso+"-"+codigo+"-"+costo+"-"+horario+"-"+cupo+"-"+catedratico+"-"+"0"+"-"+"0"+"-"+"0"+"-"+"0"+"-"+"0"+"-"+"0"+"-"+"0"+"-"+"0"+"-"+"0"+"-"+"v"+"\n")
       f3.close()#cada curso puede tener 8 apartados diferentes y uno para especificarlos
      

