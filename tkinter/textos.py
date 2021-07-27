from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

texto = Label(ventana,text="Bienvenido a mi programa")
texto.config(fg="white",
            bg="black",
            padx="30",
            pady="30",
            font=("Arial",30))
texto.pack()

def pruebas(nombre,apellido,pais):
    return ("hola soy",nombre,apellido,"de",pais)

texto = Label(ventana,text=pruebas("daniel","bedoya","colombia"))
texto.config(fg="yellow",
            bg="red",
            padx="20",
            pady="20",
            font=("Arial",40),
            #width=10,
            #height=10,
            cursor="spider")
texto.pack(anchor=S)

ventana.mainloop()