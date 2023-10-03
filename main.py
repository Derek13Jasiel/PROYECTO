from tkinter import *
#configuracion  del frame principal

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
entrada = Entry(raiz,textvariable=contraseña)#contraseña
entrada.place(x = 110, y = 160)

#funciones
def cambiar():
    print("prueba")

#crear botones 
continuar = Button(raiz, text = "continuar" , command= cambiar, bg="#b5b5b5",bd = 0)
continuar.place( x = 175 , y = 250)
#continuar.pack(side = LEFT)
#continuar.grid( row=2 , column=1)

registrarse = Button(raiz, text = "registrarse", bg="#b5b5b5",bd = 0 )
registrarse.place (x = 95, y = 250)




raiz.mainloop()



