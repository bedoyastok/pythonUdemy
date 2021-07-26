from io import open
import pathlib
import shutil

#abrir archivo
ruta =str(pathlib.Path().absolute())+'/fichero_texto.txt'
archivo = open(ruta,'a+')

""" #escribir en el archivo
archivo.write('*/*/*/hola desde python/*/*/*/\n') """

#cerrar archivo
archivo.close()

#abrir archivo
ruta =str(pathlib.Path().absolute())+'/fichero_texto.txt'
archivo_lectura = open(ruta,'r')#permiso de lectura

""" #leer contenido de archivo
contenido = archivo_lectura.read()
print(contenido) """

#leer contenido y guardar en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

""" for cadafrase in lista:
    print('+  ',cadafrase.upper().islower()) """


#copiar datos de un archivo en otro con shutil
ruta_original = str(pathlib.Path().absolute())+'/fichero_texto.txt'
ruta_nueva =str(pathlib.Path().absolute())+'/fichero_copiado.txt'
shutil.copyfile(ruta_original,ruta_nueva)