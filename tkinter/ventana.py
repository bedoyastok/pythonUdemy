from tkinter import *
import os.path

class Programa:

    def __init__(self):
        self.title = "titulo"
        self.icon = "./images/icono.ico"
        self.icon_alt = "./tkinter/images/icono.ico"
        self.size = "500x500"
        self.resizable = False

    def cargar(self):
        #crear ventana
        ventana = Tk()
        self.ventana = ventana

        #titulo ventana
        ventana.title(self.title)

        #tamaño de la ventana
        ventana.geometry(self.size)

        #bloquear tamaño(1,1)(1,0)(0,1)
        if self.resizable:
            ventana.resizable(0,0)
        else:
            ventana.resizable(1,1)

        """ #comprobar si existe un archivo
        ruta_icono = os.path.abspath("./images/icono.ico")

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        #imagen favicon en .ico
        ventana.iconbitmap(ruta_icono)

        #mostrar texto en el programa
        texto = Label(ventana, text = ruta_icono)
        texto.pack() """


    def addTexto(self,dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
        #arrancar ventana y mostrar hasta cerrarla
        self.ventana.mainloop()

#instanciar programa
programa = Programa()
programa.cargar()
programa.addTexto("hola que tal")
programa.addTexto("soy otro texto")
programa.addTexto("siiii")
programa.mostrar()